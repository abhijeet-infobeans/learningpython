from django.shortcuts import render
from django.views import View
from faker import Faker
from .models import Profile
from django.http import HttpResponseRedirect

# Create your views here.
class IndexView(View):
    
    def get(self, request, *args, **kwargs):
        return render(request, 'fakeprofile/index.html')
    
    def post(self, request, *args, **kwargs):
        submit_id = int(request.POST['save_fake_data'])
        profile = Profile()
        faker_obj = Faker()
        profile.name = faker_obj.name()
        profile.address = faker_obj.address()
        profile.country = faker_obj.country()
        profile.email = faker_obj.email()
        profile.save()
        return HttpResponseRedirect('/')
        
    