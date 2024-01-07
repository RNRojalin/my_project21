from django.shortcuts import render

# Create your views here.
def htmlforms(request):
    return render(request,'htmlforms.html')

def htmlforms2(request):
    return render(request,'htmlforms2.html')