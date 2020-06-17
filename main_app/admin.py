from django.contrib import admin
from .models import Tree, Watering, Worker

# Register your models here.
admin.site.register(Tree)
admin.site.register(Watering)
admin.site.register(Worker)