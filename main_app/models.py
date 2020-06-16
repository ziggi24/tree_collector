from django.db import models

# Create your models here.

class Tree(models.Model):
  name = models.CharField(max_length=100)
  age = models.CharField(max_length=100)
  height = models.CharField(max_length=100)
  species = models.CharField(max_length=100)

  def __str__(self):
    return f"{self.name} the {self.species}"

FERTILIZERS = (
  ('N', 'Nitrogen'),
  ('P', 'Phosphorus'),
  ('K', 'Potassium')
)

class Watering(models.Model):
  date = models.DateField('Watering Date')
  fertilizer = models.CharField(max_length=1, choices=FERTILIZERS, default=FERTILIZERS[0][0])
  tree = models.ForeignKey(Tree, on_delete=models.CASCADE, related_name='waterings')

  def __str__(self):
    return f"{self.get_fertilizer_display()} added to {self.tree} on {self.date}"
  
  class Meta:
    ordering = ['-date', 'fertilizer']