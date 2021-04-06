from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from survey_app.forms import AnswerOptionForm
from survey_app.models import AnswerOption, Poll


class AddAnswer(CreateView):
    template_name = 'answers/add_answer.html'
    model = AnswerOption
    form_class = AnswerOptionForm

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        answer = form.save(commit=False)
        answer.poll = poll
        answer.save()
        return redirect('poll_view', pk=poll.pk)


class UpdateAnswer(UpdateView):
    template_name = 'answers/update_answer.html'
    model = AnswerOption
    form_class = AnswerOptionForm
    context_object_name = 'answer'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})




