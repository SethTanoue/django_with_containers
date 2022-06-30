from django.views import generic
from django.urls import reverse_lazy
from .models import Robot

class IndexView(generic.ListView):
    template_name = 'robots/index.html'
    context_object_name = 'robot_list'

    def get_queryset(self):
        """Return the all robots."""
        return Robot.objects.all()

class CreateView(generic.edit.CreateView):
    template_name = 'robots/create.html'
    model = Robot
    fields = ['message']
    success_url = reverse_lazy('robots:index') # more robust than hardcoding to /robots/; directs user to index view after creating a robot

class UpdateView(generic.edit.UpdateView):
    template_name = 'robots/update.html'
    model = Robot
    fields = ['message']
    success_url = reverse_lazy('robots:index')

class DeleteView(generic.edit.DeleteView):
    template_name = 'robots/delete.html' # override default of robots/robot_confirm_delete.html
    model = Robot
    success_url = reverse_lazy('robots:index')

class New_Page(generic.edit.CreateView):
    template_name = 'robots/newPage.html'
    model = Robot
    fields = ['message']
    success_url = reverse_lazy('robots:index')