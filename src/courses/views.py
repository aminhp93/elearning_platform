from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Course

class CourseListView(ListView):
	model = Course

class CourseDetailView(DetailView):
	model = Course

class CourseCreateView(CreateView):
	model = Course

class CourseUpdateView(UpdateView):
	model = Course

class CourseDeleteView(DeleteView):
	model = Course

	
