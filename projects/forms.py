from dataclasses import field
from tkinter import Widget
from django.forms import ModelForm
from .models import Project
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description',
                  'demo_link', 'source_link', 'tags']
        # fields = '__all__'
        widgets = {
            'tags':forms.CheckboxSelectMultiple()
        }
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, filed in self.fields.items():
            filed.widget.attrs.update({'class':'input'})
        # self.fields['title'].widget.attrs.update({
        #     'class':'input',
        #     'placeholder':'Add Title'
        #     })

        # self.fields['description'].widget.attrs.update({
        #     'class':'input',
        #     'placeholder':'Add Description'
        #     })