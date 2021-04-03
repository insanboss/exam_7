from django import forms

from survey_app.models import Poll, AnswerOption


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class AnswerOptionForm(forms.ModelForm):
    class Meta:
        model = AnswerOption
        fields = ['option_text']
