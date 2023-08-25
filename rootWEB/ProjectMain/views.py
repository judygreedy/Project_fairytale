from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def funcMain(request):
    print("check_ProjectMain_funcMain")
    return render(request, 'ProjectMain/index.html')