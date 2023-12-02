from django.http import HttpResponse
from django.shortcuts import redirect, render
from pet.forms import PetSaleForm
from django.contrib.auth.decorators import login_required
from pet.models import Pet

@login_required
def Catalog(request):

    pets = Pet.objects.all()  # Obtener todas las mascotas
   

    return render(request, 'catalog.html', {'pets': pets} )
    
def add_petsale(request):
    if request.method == 'POST':
        form = PetSaleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/catalog')  
    else:
        form = PetSaleForm()
    return render(request, 'add_petsale.html', {'form': form})