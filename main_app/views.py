from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tree
from .forms import Tree_Form

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def trees_index(request):
  if request.method == 'POST':
    tree_form = Tree_Form(request.POST)
    if tree_form.is_valid:
      tree_form.save()
      return redirect('index')
  else:
    tree_form = Tree_Form()
  trees = Tree.objects.all()
  context = {'trees': trees, 'tree_form': tree_form}
  return render(request, 'trees/index.html', context)

def trees_detail(request, tree_id):
  tree = Tree.objects.get(id=tree_id)
  context = {'tree': tree}
  return render(request, 'trees/show.html', context)

