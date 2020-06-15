from django.shortcuts import render
from django.http import HttpResponse
from .models import Tree

# Create your views here.



def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def trees_index(request):
  trees = Tree.objects.all()
  context = {'trees': trees}
  return render(request, 'trees/index.html', context)

def trees_detail(request, tree_id):
  tree = Tree.objects.get(id=tree_id)
  context = {'tree': tree}
  return render(request, 'trees/show.html', context)

