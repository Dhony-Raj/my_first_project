from django.shortcuts import render,HttpResponse

def flat(request):
    return render(request, './flat.html')
# Create your views here.
