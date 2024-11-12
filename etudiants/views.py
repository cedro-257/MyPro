from django.shortcuts import render

# Create your views here.
def add_show(request):
    
    # context = {
    #     'message': 'Bienvenue sur la page Add and Show'
    # }
    return render(request, 'etudiants/addandshow.html')