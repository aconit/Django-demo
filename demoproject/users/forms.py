from django import forms
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import AuthenticationForm


class CustomLoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'De ingevoerde gebruikersnaam of het wachtwoord is onjuist. Let op: wachtwoorden zijn hoofdlettergevoelig.',
        'inactive': 'Dit account is niet actief.',
    }
     
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].label = 'Gebruikersnaam'
        self.fields['username'].error_messages.update({
            'required': 'Gebruikersnaam is verplicht.'
        })        
        
        self.fields['password'].label = 'Wachtwoord'
        self.fields['password'].error_messages.update({
            'required': 'Wachtwoord is verplicht.'
        })

       

class EditUser(forms.ModelForm):

    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=True,
        empty_label="-- Kies een group --",
        error_messages={
            'required': 'Vul de groep in.',
        }
    )
      
    class Meta:
        model = User
        fields =  ['username', 'password', 'group']

        labels = {
            'username': 'Gebruikersnaam',
            'password': 'Wachtwoord',
            'group': 'Groep',
        }

        error_messages = {
            'username': {
                'required': 'Vul de gebruikersnaam in.',
            },
            'password': {
                'required': 'Vul het wachtwoord in.',
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if self.instance and self.instance.pk:
            current_group = self.instance.groups.first()
            print(current_group)
            if current_group:
                self.fields['group'].initial = current_group.pk



    def save(self, commit=True):
        user = super().save(commit=False)
        
        raw_password = self.cleaned_data.get('password')
        if raw_password:
            user.set_password(raw_password)
           
        if commit:
            user.save()
            selected_group = self.cleaned_data.get('group')
            user.groups.clear()
            if selected_group:
                user.groups.add(selected_group)
        return user