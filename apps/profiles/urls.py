from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import HomeView, ProfileView

urlpatterns = [
    path('home', login_required(HomeView.as_view()), name='home'),
    path('profile', login_required(ProfileView.as_view()), name='profile'),
]