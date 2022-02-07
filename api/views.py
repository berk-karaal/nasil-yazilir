from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status, permissions

from django.utils import timezone

from api import custom_permissions
from api.serializers import WordSerializer, QuizSerializer
from api.models import Word, Quiz

import random


class APIRoot(APIView):
    def get(self, request):
        return Response(
            {
                "words": reverse("list-create-words", request=request),
                "daily-quiz": reverse("get-daily-quiz", request=request),
                "random-quiz": reverse("get-random-quiz", request=request),
            }
        )


class ListCreateWords(APIView):

    permission_classes = [permissions.IsAdminUser | custom_permissions.IsSafeMethod]

    def get(self, request):
        words = Word.objects.all()
        serializer = WordSerializer(instance=words, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


PREFERRED_QUIZ_LENGTH = 5


class GetDailyQuiz(APIView):
    def get(self, request):
        try:
            quiz = Quiz.objects.get(display_date=timezone.now().date())

        except Quiz.DoesNotExist:
            # Today's quiz wasn't created. So, create!
            quiz = Quiz.objects.create(display_date=timezone.now().date())

            # First, use newly added words(their last_use_date is None)
            for word in Word.objects.order_by("upload_date").filter(last_use_date=None)[
                :PREFERRED_QUIZ_LENGTH
            ]:
                quiz.words.add(word)
                word.last_use_date = timezone.now().date()
                word.save()

            if quiz.words.all().count() < PREFERRED_QUIZ_LENGTH:
                # If newly added words aren't enough, use "oldest used words" to fill rest of the quiz
                # Choose randomly in order to prevent making same quizes
                used_ids = [obj.id for obj in quiz.words.all()]
                randomly_selected_words = random.sample(
                    list(
                        Word.objects.exclude(id__in=used_ids).order_by("last_use_date")[
                            : PREFERRED_QUIZ_LENGTH * 3
                        ]
                    ),
                    k=PREFERRED_QUIZ_LENGTH - quiz.words.all().count(),
                )
                for word in randomly_selected_words:
                    quiz.words.add(word)
                    word.last_use_date = timezone.now().date()
                    word.save()

        serializer = QuizSerializer(instance=quiz)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetRandomQuiz(APIView):
    def get(self, request):
        words = random.sample(list(Word.objects.all()), k=PREFERRED_QUIZ_LENGTH)
        quiz = Quiz.objects.create(display_date=None)
        for word in words:
            quiz.words.add(word)

        response = Response(QuizSerializer(quiz).data, status=status.HTTP_200_OK)
        quiz.delete()  # I saved this temporary object to the db because of many to many realtionship

        return response
