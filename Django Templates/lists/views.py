from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from django.http import HttpResponse
from django.shortcuts import render

from .models import Item


class HomeView(View):

	def get(self, request, *args, **kwargs):
		return render(request, 'index.html', {
			'tasks': Item.objects.all()
		})

	def post(self, request, *args, **kwargs):
		return render(request, 'home.html', {
			'new_task': request.POST.get('item_text')
		})


class TaskDetailView(View):

	def get(self, request, *args, **kwargs):
		return render(request, 'detail.html', {
			'task': Item.objects.get(id=self.kwargs.get('id'))
		})


class TaskListView(ListView):
	model = None 


class TaskCreateView(CreateView):
	template_name_suffix = '_create_form'


def home_page(request):
	if request.method == 'POST':
		return render(request, 'home.html', {
			'new_task': request.POST.get('item_text')
		})
	return render(request, 'home.html')