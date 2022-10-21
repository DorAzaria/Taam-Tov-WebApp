from django.forms import ModelForm, fields, models
from .models import Recipe, Comment, RecipeIngredient, RecipeMethod
from django import forms

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'intro', 'tags', 'description', 'featured_image', ]
        labels = {
            'title': 'שם המתכון',
            'tags': 'סגנון',
            'intro': 'תקציר מתכון',
            'description': 'כתבו מתכון',
            'featured_image': 'הוסף תמונה',
        }
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
        # self.fields['title'].widget.attrs.update({'class':'input', 'placeholder': 'הוסף שם מתכון'})

        # self.fields['description'].widget.attrs.update({'class':'input', 'placeholder': 'כתוב את המתכון'})

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['value', 'body']

        labels = {
            'value': 'לייק',
            'body': 'הוסיפו תגובה ללייק שלכם'
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['name', 'quanity', 'unit']

        labels = {
            'name': 'שם',
            'quanity': 'כמות',
            'unit': 'יחידת מידה'
        }

        def __init__(self, *args, **kwargs):
            super(RecipeIngredientForm, self).__init__(*args, **kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class': 'input'})

class RecipeMethodForm(forms.ModelForm):
    class Meta:
        model = RecipeMethod
        fields = ['description']

        labels = {
            'description': 'תיאור'
        }


        def __init__(self, *args, **kwargs):
            super(RecipeMethodForm, self).__init__(*args, **kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class': 'input'})