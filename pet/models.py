from django.db import models

class Pet(models.Model):
    #Campos:
    name = models.CharField(max_length=200,null=False)
    age= models.PositiveIntegerField(default=0,null=False)
    vaccunes=models.CharField(max_length=1000,null=True)
    #ToDo: añadir categoria,raza e URL de la imagen
    


    #Métodos
    def __str__(self):
        return self.name
    
    def get_all_pets():
        return Pet.objects.all()
    
    def get_pet_by_name(name):
        return Pet.objects.filter(name=name).first()
        
    
