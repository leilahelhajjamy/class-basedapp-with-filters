from django.shortcuts import render
from django.views.generic import View ,DeleteView , UpdateView, ListView , DetailView , CreateView
from django.http import HttpResponse
from .models import Student
from django.urls import reverse_lazy
# Create your views here.


class GreetingView(View):
    greetingMessage = '<b>Hello from the other side</b>'
    def get(self, request):
        return HttpResponse(self.greetingMessage)


class StudentListView(ListView):
    model = Student
    #default context_object_name is student_list
    #default temlate is student_list.html


class StudentDetailView(DetailView):
    model = Student



class StudentCreateView(CreateView):
    model = Student
    fields = ('firstName','lastName', 'testScore')
    #student_form.html is the default template


class StudentUpdateView(UpdateView):
    model = Student
    fields = ('testScore',)

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students')