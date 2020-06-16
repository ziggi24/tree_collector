from django.forms import ModelForm
from .models import Tree

class Tree_Form(ModelForm):
  class Meta:
    model = Tree
    fields = ['name', 'age', 'height', 'species']

