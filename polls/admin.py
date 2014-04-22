from django.contrib import admin
from polls.models import Choice, Question

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {"fields": ["question_text"]}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    #Choice objects are edited on the Question admin page
    inlines = [ChoiceInline]

    #display individual fields
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    #an improvement to the Question change list page: Filters
    list_filter = ["pub_date"]

    #search capability
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
