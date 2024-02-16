from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from .forms import RegisterForm


class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid (self, form:User):
        user = form.save()
        if user :
            login(self.request, user=user)
        
        return super(RegisterView, self).form_valid(form)

class MyLoginView(LoginView):
    template_name = 'users/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('tasks')
    
    def form_invalid(self, form: AuthenticationForm) -> HttpResponse:
        messages.error(self.request, 'Invalid username or password')
        return super().render_to_response(self.get_context_data(form=form))
