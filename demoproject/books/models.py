import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class LanguageChoices(models.IntegerChoices):
        ENG=1, "Engels"
        NED=2, "Nederlands"
        FRA=3, "Frans",
        DEU=4, "Duits",
        ESP=5, "Spaans",
        ITA=6, "Italiaans",
        RUS=7, "Russisch"


def current_year():
    return datetime.date.today().year

class Book (models.Model):
        title=models.CharField( max_length=500,verbose_name="Titel")
        description = models.TextField(null=True, blank=True, verbose_name="Omschrijving")
        author = models.CharField(max_length=200, verbose_name="Auteur")
        language =models.IntegerField(choices=LanguageChoices.choices, verbose_name="Taal")
        first_pub_year = models.IntegerField(validators=[
            MinValueValidator(1100), 
            MaxValueValidator(current_year)
        ], verbose_name="Oorspronkelijk uitgegeven")

