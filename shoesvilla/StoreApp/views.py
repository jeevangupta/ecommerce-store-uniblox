from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    user = request.user

    #return HttpResponse("Hello World !")
    return render(request, "./home.html")


