from django.db import models
from django.conf import settings

class Recipe(models.Model):
  user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
  title = models.CharField(max_length=255)
  time_minutes = models.IntegerField()
  price = models.DecimalField(max_digits=5, decimal_places=2)
  link = models.CharField(max_length=255, blank=True, null=True)
  ingredients = models.ManyToManyField('Ingredient', related_name='ingredient')
  tags = models.ManyToManyField('Tag', related_name='tag')

  def __str__(self):
      return self.title
