from django.urls import path
from api.views import ListCreateWords, GetDailyQuiz, GetRandomQuiz

urlpatterns = [
    path("words/", ListCreateWords.as_view(), name="list-create-words"),
    path("daily/", GetDailyQuiz.as_view(), name="get-daily-quiz"),
    path("random-quiz/", GetRandomQuiz.as_view(), name="get-random-quiz"),
]
