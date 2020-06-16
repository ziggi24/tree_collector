from django.forms import ModelForm
from .models import Tree, Watering

class Tree_Form(ModelForm):
  class Meta:
    model = Tree
    fields = ['name', 'age', 'height', 'species']

class Watering_Form(ModelForm):
  class Meta:
    model = Watering
    fields = ['date', 'fertilizer']
