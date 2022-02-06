from django.db import models


class Word(models.Model):
    correct_spelling = models.CharField(max_length=100)
    wrong_spelling = models.CharField(max_length=100)
    upload_date = models.DateTimeField(auto_now_add=True)
    last_use_date = models.DateField(blank=True, null=True)
    # "use" means usage in a quiz

    class Meta:
        ordering = ["-upload_date"]

    def __str__(self) -> str:
        return self.correct_spelling


class Quiz(models.Model):
    display_date = models.DateField(null=True)
    words = models.ManyToManyField(Word)

    def __str__(self) -> str:
        return f"({self.display_date or '???'}) " + "/".join(
            [w.correct_spelling for w in self.words.all()]
        )
