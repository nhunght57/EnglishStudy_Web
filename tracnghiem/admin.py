from django.contrib import admin

# Register your models here.

from django.contrib import admin
from tracnghiem.models import Choice, Question

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {"fields": ["question_text"]}),
    ]

    #Choice objects are edited on the Question admin page
    inlines = [ChoiceInline]

    #display individual fields
    list_display = ('question_text',)

    #an improvement to the Question change list page: Filters
    # list_filter = ["pub_date"]

    #search capability
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)