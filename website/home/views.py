from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    
    return render(request, 'index.html')
    #return HttpResponse("This is Homepage")

def about(request):
    return render(request, 'about.html',)
    #return HttpResponse("This is About page")

def services(request):
    return render(request, 'services.html',)
    #return HttpResponse("This is services page")

def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse("This is Contact page")

def pricing(request):
    return render(request, 'pricing.html')
    #return HttpResponse("This is Pricing page")
