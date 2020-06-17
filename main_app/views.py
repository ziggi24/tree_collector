from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Tree, Worker
from .forms import Tree_Form, Watering_Form

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def trees_index(request):
  if request.method == 'POST':
    tree_form = Tree_Form(request.POST)
    if tree_form.is_valid:
      new_tree = tree_form.save(commit=False)
      new_tree.user = request.user
      new_tree.save()
      return redirect('index')
  else:
    tree_form = Tree_Form()
  trees = Tree.objects.filter(user=request.user)
  context = {'trees': trees, 'tree_form': tree_form}
  return render(request, 'trees/index.html', context)

@login_required
def trees_detail(request, tree_id):
  tree = Tree.objects.get(id=tree_id)
  if tree.user != request.user:
    return render(request, 'trees/notyourtree.html')
  available_workers = Worker.objects.exclude(id__in=tree.workers.all().values_list('id'))
  watering_form = Watering_Form()
  context = {'tree': tree, 'watering_form': watering_form, 'workers': available_workers}
  return render(request, 'trees/show.html', context)

@login_required
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

@login_required
def trees_delete(request, tree_id):
  Tree.objects.get(id=tree_id).delete()
  return redirect('index')

@login_required
def add_watering(request, tree_id):
  watering_form = Watering_Form(request.POST)
  if watering_form.is_valid():
    new_watering = watering_form.save(commit=False)
    new_watering.tree_id = tree_id
    new_watering.save()
  return redirect('detail', tree_id=tree_id)

@login_required
def assoc_worker(request, tree_id, worker_id):
  Tree.objects.get(id=tree_id).workers.add(worker_id)
  return redirect('detail', tree_id=tree_id)

@login_required
def deassoc_worker(request, tree_id, worker_id):
  Tree.objects.get(id=tree_id).workers.remove(worker_id)
  return redirect('detail', tree_id=tree_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else: 
      error_message = 'Invalid signup please try again'
  else:
    form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
