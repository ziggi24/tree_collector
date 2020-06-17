from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tree, Worker
from .forms import Tree_Form, Watering_Form

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
  available_workers = Worker.objects.exclude(id__in=tree.workers.all().values_list('id'))
  watering_form = Watering_Form()
  context = {'tree': tree, 'watering_form': watering_form, 'workers': available_workers}
  return render(request, 'trees/show.html', context)

def trees_edit(request, tree_id):
  tree = Tree.objects.get(id=tree_id)
  if request.method == 'POST':
    tree_form = Tree_Form(request.POST, instance = tree)
    if tree_form.is_valid():
      tree_form.save()
      return redirect('detail', tree_id=tree_id)
  else:
    tree_form = Tree_Form(instance=tree)
  context = {'tree': tree, 'tree_form': tree_form}
  return render(request, 'trees/edit.html', context)

def trees_delete(request, tree_id):
  Tree.objects.get(id=tree_id).delete()
  return redirect('index')

def add_watering(request, tree_id):
  watering_form = Watering_Form(request.POST)
  if watering_form.is_valid():
    new_watering = watering_form.save(commit=False)
    new_watering.tree_id = tree_id
    new_watering.save()
  return redirect('detail', tree_id=tree_id)

def assoc_worker(request, tree_id, worker_id):
  Tree.objects.get(id=tree_id).workers.add(worker_id)
  return redirect('detail', tree_id=tree_id)

def deassoc_worker(request, tree_id, worker_id):
  Tree.objects.get(id=tree_id).workers.remove(worker_id)
  return redirect('detail', tree_id=tree_id)


