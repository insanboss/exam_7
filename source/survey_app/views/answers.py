from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View, TemplateView

from survey_app.forms import AnswerOptionForm
from survey_app.models import AnswerOption, Poll, AnswerPoll


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


class DeleteAnswer(DeleteView):
    template_name = 'answers/delete_answer.html'
    model = AnswerOption
    context_object_name = 'answer'
    success_url = reverse_lazy('index_polls')


class AnswerCollect(TemplateView):
    template_name = 'answers_collect.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        poll = get_object_or_404(Poll, pk=kwargs['pk'])
        context['poll'] = poll
        context['answers'] = poll.answers.all()
        return context

    def post(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=kwargs['pk'])
        answer_id = request.POST.get('answer')
        print(answer_id)
        AnswerPoll.objects.create(poll=poll, answer=AnswerOption.objects.get(pk=answer_id))
        return redirect('index_polls')





