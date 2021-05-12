from django.urls import path
from .views import (
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView
)
from . import views

urlpatterns = [
    path('', ProjectListView.as_view(), name='git-home'),
    #path('', views.home, name='git-home'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/new/', ProjectCreateView.as_view(), name='project-create'),

]

