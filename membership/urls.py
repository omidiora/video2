from django.urls import path,include
from .views import MembershipSelectView

app_name='membership'
urlpatterns = [
    path('',MembershipSelectView.as_view(), name='select'),
]

