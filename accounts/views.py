from django.shortcuts import render

def accounts(request):
    return render(request,'accounts/index.html')