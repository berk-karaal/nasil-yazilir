from django.contrib import admin
from django.contrib.auth.models import Group
from api.models import Word, Quiz


@admin.action(description="Make selected words newly added")
def make_newly_added(modelAdmin, request, queryset):
    for obj in queryset:
        obj.last_use_date = None
        obj.save()


@admin.register(Word)
class WordAdminModel(admin.ModelAdmin):
    list_display = (
        "correct_spelling",
        "wrong_spelling",
        "upload_date",
        "last_use_date",
    )  # fields to list in objects listing page

    readonly_fields = ("upload_date",)  # declare read_only fields
    fields = (
        "correct_spelling",
        "wrong_spelling",
        "upload_date",
        "last_use_date",
    )  # fields to show in object detail page

    actions = [
        make_newly_added,
    ]  # declare custom actions


admin.site.unregister(Group)
admin.site.register(Quiz)
