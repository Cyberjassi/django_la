from django.shortcuts import render
from django.views.generic import TemplateView,FormView,CreateView,ListView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
from classroom.form import f1
from classroom.models import Stu
# Create your views here.
class homepage(TemplateView):
    template_name = 'classroom/home.html'

class Thankyouview(TemplateView):
    template_name = 'classroom/thanks.html'

class formview(FormView):
    form_class = f1
    template_name = 'classroom/form.html'
    success_url = '/thanks/'
    def form_valid(self, form):
        return super().form_valid(form)
    
class StuCreateView(CreateView):
    model = Stu
    fields = '__all__'
    success_url = '/thanks/'

class StuListView(ListView):
    model = Stu
    context_object_name = 'Student'
    queryset = Stu.objects.all()

class StuDetailVies(DetailView):
    model = Stu

class StuUpdateView(UpdateView):
    model = Stu
    fields = '__all__'
    success_url = '/list_stu/'

class StuDeleteView(DeleteView):
    model = Stu
    success_url = '/list_stu/'

    
