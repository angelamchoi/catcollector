from django.db import models
from django.urls import reverse

# A tuple of of 2-tuples
MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

# Cat Model
class Cat(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

# Feeding Model
class Feeding(models.Model):
  date = models.DateField()
  meal = models.CharField(
    max_length=1,
      choices= MEALS,
      default=MEALS[0][0] # setting default value for meal to be 'B'
  )

# Foreign Key
cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
# 1st arg = model, 2nd arg = what do we do if we delete the ref model 

def __str__(self):
  # Nice method for obtaining the friendly value of a Field.choice
  return f"{self.get_meal_display()} on {self.date}" # this is called metadata

def get_absolute_url(self):
  return reverse('detail', kwargs={'cat_id': self.id})



### NOTES ###
# on_delete=models.CASCADE -> if we delete a cat, we will need to go through the table and delete any feeding ref the cat
