from django.views.generic import ListView, DetailView

from survey_app.models import Poll


class IndexPolls(ListView):
    template_name = 'polls/index_polls.html'
    context_object_name = 'polls'
    model = Poll
    ordering = 'created_at'

    paginate_by = 5
    paginate_orphans = 3


class ProjectView(DetailView):
    template_name = 'polls/poll_view.html'
    model = Poll
    context_object_name = 'poll'
