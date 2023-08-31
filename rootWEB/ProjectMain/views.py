from django.shortcuts import redirect,render
from django.http import HttpResponse
# from .models import Student2

# Create your views here.
def funcMain(request):
    print("check_ProjectMain_funcMain")
    return render(request, 'ProjectMain/index2.html')
