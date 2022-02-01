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

  PYTHON = 'PY'
  JAVASCRIPT = 'JS'
  TYPESCRIPT = 'TS'
  C_SHARP = 'C#'
  LANGUAGE_CHOICES = [
    (PYTHON, 'Python'),
    (JAVASCRIPT, 'JavaScript'),
    (TYPESCRIPT, 'TypeScript'),
    (C_SHARP, 'C#')
  ]
  
  name = models.CharField(max_length=255)
  task = models.CharField(max_length=3, choices=TASK_CHOICES, default=TWO_NUMBER_SUM)
  language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default=PYTHON)
  solution = models.TextField()
