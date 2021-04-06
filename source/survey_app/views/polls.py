from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from survey_app.forms import PollForm
from survey_app.models import Poll


class IndexPolls(ListView):
    template_name = 'polls/index_polls.html'
    context_object_name = 'polls'
    model = Poll
    ordering = 'created_at'

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
