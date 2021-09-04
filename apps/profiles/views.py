from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from .forms import ProfileForm
from .models import Information, Skills
from django.contrib.auth.models import User
from django.db.models import Avg

# Create your views here.

class HomeView(View):

    form_class = ProfileForm
    initial = {}
    template_name = 'web/home.html'

    def get(self, request, *args, **kwargs):
        all_skills = Skills.objects.aggregate(
            Avg('python_xp'), 
            Avg('javascript_xp'),
            Avg('sql_xp'),
            Avg('java_xp'),
            Avg('spark_xp'),
            Avg('html_xp'),
            Avg('others_xp'),
        )
        user_skills = Skills.objects.filter(user = request.user).values()[0]
        context = {
            'all_skills': all_skills,
            'user_skills': user_skills
        }
        return render(request, self.template_name, context)

    
class ProfileView(View):

    form_class = ProfileForm
    initial = {}
    template_name = 'web/profile.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(
            initial={
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
            }
        )
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username = request.user)
        form = self.form_class(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('profiles:home')