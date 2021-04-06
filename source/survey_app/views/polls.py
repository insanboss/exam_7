from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from survey_app.forms import PollForm
from survey_app.models import Poll


class IndexPolls(ListView):
    template_name = 'polls/index_polls.html'
    context_object_name = 'polls'
    model = Poll
    queryset = Poll.objects.order_by('-created_at')

    paginate_by = 5
    paginate_orphans = 3


class PollView(DetailView):
    template_name = 'polls/poll_view.html'
    model = Poll
    context_object_name = 'poll'


class PollCreate(CreateView):
    template_name = 'polls/poll_create.html'
    model = Poll
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollUpdate(UpdateView):
    template_name = 'polls/poll_update.html'
    model = Poll
    form_class = PollForm
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollDelete(DeleteView):
    template_name = 'polls/poll_delete.html'
    model = Poll
    context_object_name = 'poll'
    success_url = reverse_lazy('index_polls')
