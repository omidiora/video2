from django.shortcuts import render
from django.views.generic import ListView
from .models import Membership


# Create your views here.

class MembershipSelectView(ListView):
    model=Membership
