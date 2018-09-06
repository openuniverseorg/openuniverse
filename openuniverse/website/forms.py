from django import forms

class FindProjectForm(forms.Form):
    project = forms.CharField(label='Your name', max_length=100)
    