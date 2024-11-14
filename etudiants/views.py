from django.shortcuts import render, HttpResponseRedirect 
from .forms import StudentRegistration
from .models import User
# Create your views here.
#cettee fonction permet d'ajouter et d'afficher les iformations
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['pawword']
            reg =User(name =nm, email =em, password =pw)
            reg.save()
            fm = StudentRegistration()
                
    else:
        fm = StudentRegistration(request.POST )  
        stud = User.objects.all()
    return render(request, 'etudiants/addandshow.html', {'form': fm, 'stu': stud})

#une methode qui permet de modifier les informations
def update_data(request):
    if request.method == 'POST':
        pi =User.objects.get(pk=id) 
        fm = StudentRegistration(request.POST, instance=pi) 
        if fm.is_valid():
            fm.save()
    else:
        
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance = 1  )
    return render(request, 'etudiant/updatestudent.html',{'form':fm})

#cette fonction permet de supprimer les donnees 

def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
        
    
    # context = {
    #     'message': 'Bienvenue sur la page Add and Show'
    # }
    