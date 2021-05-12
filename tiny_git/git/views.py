from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from .models import Project

#function based view
def home(request):
    return render(request, 'git/home.html')


class ProjectListView(ListView):
    model = Project
    template_name = 'git/home.html' # <app>/<model>_<viewtype>.html
                                    # by default it expects this: git/project_list.html
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['name', 'description', 'git_repository']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
