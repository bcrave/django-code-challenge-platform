from django.db import models

class Challenge(models.Model):
  TWO_NUMBER_SUM = '2NS'
  THREE_NUMBER_SUM = '3NS'
  FOUR_NUMBER_SUM = '4NS'

  TASK_CHOICES = [
    (TWO_NUMBER_SUM, 'Two Number Sum'),
    (THREE_NUMBER_SUM, 'Three Number Sum'),
    (FOUR_NUMBER_SUM, 'Four Number Sum')
  ]
  
  name = models.CharField(max_length=255)
  task = models.CharField(max_length=3, choices=TASK_CHOICES)
  solution = models.TextField()
