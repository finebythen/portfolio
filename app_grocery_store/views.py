from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app_grocery_store/index.html')
