from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.db.models.fields import CharField, TextField

class movie(models.Model):
    original_name = models.CharField(max_length=100)
    name_in_spain = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField(validators=[MinValueValidator(1895)], default=2021)
    director = models.CharField(max_length=50, default='John Doe')
    duration = models.PositiveSmallIntegerField()
    sinopsis = models.TextField(default='Lorem ipsum dolor sit amet')
    genres = models.CharField(max_length=100)
    
    RATE_CHOICES = (
        (0, "0"),
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    )
    
    rate = models.SmallIntegerField(validators=[MaxValueValidator(5)],
                                                choices=RATE_CHOICES,
                                                default=0)


