from django.db import models
from django.db.models import Q

class Pet(models.Model):

    class Category(models.TextChoices):
        DOG = 'DOG', 'Perro'
        CAT = 'CAT', 'Gato'

    class Breed(models.TextChoices):
        LABRADOR = 'LAB', 'Labrador'
        PUG = 'PUG', 'Carlino'
        BEAGLE = 'BGL', 'Beagle'
        BULLDOG = 'BLD', 'Bulldog'
        PERSIAN = 'PERS', 'Persa'
        SIAMESE = 'SMS', 'Siamés'
        MAINE_COON = 'MCO', 'Maine Coon'
        RAGDOLL = 'RGL', 'Ragdoll'
    #Campos:
    name = models.CharField(max_length=200,null=True)
    age= models.PositiveIntegerField(default=0,null=False)
    vaccunes=models.CharField(max_length=1000,null=True)
    category = models.CharField(max_length=4, choices=Category.choices, null=False,default=Category.DOG)
    breed = models.CharField(max_length=4, choices=Breed.choices, null=False,default=Breed.BULLDOG)
    image = models.ImageField(upload_to='static/images',null=True,default='kora')
    #ToDo:  URL de la imagen
    price = models.DecimalField(max_digits=5, decimal_places=2, help_text='Precio de la venta.')
    discount = models.DecimalField(max_digits=5, decimal_places=2, help_text='Porcentaje de descuento de la venta.')
    description = models.TextField(help_text='Descripción de la venta.',null=True)
    enabled = models.BooleanField(default=True, help_text='Indica si la venta está habilitada o no.')
    


    #Métodos
    def __str__(self):
        return self.name
    
    def get_all_pets():
        return Pet.objects.all()
    
    def get_pet_by_name(name):
        return Pet.objects.filter(name=name)
    
    
    def get_pets_by_search(search_text):
        search_items=search_text.lower().split()
        if(len(search_items)==3):
            pets=Pet.objects.filter(category=search_items[0], breed=search_items[1],name=search_items[2])

        else:
            pets=Pet.get_all_pets()
        
        return pets
        

        
    
