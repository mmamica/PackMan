from django.contrib.auth import login, logout
from django.urls import reverse_lazy
# from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render

from . import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
