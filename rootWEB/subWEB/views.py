from django.shortcuts import render

# Create your views here.

# browser : http://127.0.0.1:8000/[내가임의로설정한경로1]/[내가임의로설정한경로2]

def testfuc(request):
    print('client request url : http://127.0.0.1:8000/main/test , testfuc() call')
    return render(request, 'subWEB/html1.html')