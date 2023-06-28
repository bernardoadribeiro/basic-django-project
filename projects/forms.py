from django import forms


class ProjectForm(forms.Form):
    """ Form to create a new project"""

    title = forms.CharField(label='Title', max_length=128)
    description = forms.CharField(label='Description', widget=forms.Textarea)
    technology = forms.CharField(label='Technology', max_length=20)
    image = forms.CharField(label='Image link', max_length=500)
