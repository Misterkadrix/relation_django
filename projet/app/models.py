from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.



class President(models.Model):
    class Genre(models.TextChoices):
        homme = "homme"    
        femme = "femme"    
        other = "autre"        
    nom = models.fields.CharField(max_length=30)
    age = models.fields.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(101)])
    genre = models.fields.CharField(choices=Genre.choices,max_length=5)
    image = models.ImageField(upload_to='image_president')
    
    def __str__(self):
        return f'{self.nom}'

class Continent(models.Model):
    nom = models.fields.CharField(max_length=30)
    def __str__(self):
        return f'{self.nom}'

class Pays(models.Model):
    nom = models.fields.CharField(max_length=30)
    population = models.fields.BigIntegerField()
    president = models.OneToOneField(President,on_delete=models.CASCADE, related_name="pays")
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE, related_name="pays",blank=True)
    
    