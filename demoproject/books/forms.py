from django import forms
from . import models


class EditBook(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['language'].choices = [('', '-- Kies een taal --')] + list(self.fields['language'].choices)[1:]


    class Meta:
        model = models.Book
        fields =  '__all__' 

        error_messages = {
              'title': {
                'required': 'Vul een titel in.',
                'max_length': 'De titel mag niet langer zijn dan 500 tekens.',
            },
            'author': {
                'required': 'Vul de naam van de auteur in.',
                'max_length': 'De naam van de auteur mag niet langer zijn dan 200 tekens.',
            },
            'language': {
                'required': 'Selecteer een taal uit de lijst.',
                'invalid_choice': 'De geselecteerde taal is niet geldig.',
            },
            'first_pub_year': {
                'required': 'Vul het oorspronkelijke jaar van uitgave in.',
                'invalid': 'Vul een geldig getal in voor het jaartal.',
                'min_value': 'Het jaartal mag niet vóór 1100 liggen.',
                'max_value': 'Het jaartal mag niet in de toekomst liggen.',
            },
        }
