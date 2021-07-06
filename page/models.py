from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.db.models.fields import CharField, TextField
from django.utils import timezone

class Movie(models.Model):
    originalName = models.CharField(max_length=100, placeholder="Nombre original de la pelicula")
    nameInSpain = models.CharField(max_length=100, blank=True, null=True, placeholder="Nombre de la pelicula en España")
    year = models.PositiveSmallIntegerField(validators=[MinValueValidator(1895)], default=2021)
    director = models.CharField(max_length=50)
    duration = models.PositiveSmallIntegerField(placeholder="Minutos")
    sinopsis = models.TextField(placeholder="Breve resumen de la trama")
    genres = models.CharField(max_length=100, placeholder="Separados con coma")
    
    RATE_CHOICES = (
        (0, "0"),
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    )
    
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, default=0)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.originalName + " - " + str(int(round(self.year)))

