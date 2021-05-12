from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
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
    fields = ['name', 'description', 'git_repository'] #description should be optional

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['name', 'description', 'git_repository']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.owner:
            return True
        return False

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/'

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.owner:
            return True
        return False
