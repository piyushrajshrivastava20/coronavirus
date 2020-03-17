from django.shortcuts import render
from django.http import HttpResponse

from .models import India

# Create your views here.
def home_view(request):
	obj = India.objects.get(id=1)

	context={
		'object':obj,
	}

	return render(request , "home.html",context)
