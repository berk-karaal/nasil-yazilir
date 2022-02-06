from rest_framework import serializers
from api.models import Word, Quiz


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ["correct_spelling", "wrong_spelling"]


class QuizSerializer(serializers.ModelSerializer):
    words = WordSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ["display_date", "words"]
