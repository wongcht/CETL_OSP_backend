from django.db import models
import json
# Create your models here.

class Survey(models.Model):
    title = models.TextField()
    token = models.CharField(max_length=5, unique=True, editable=False)
    def __str__(self):
        return f'{self.title} (Token: {self.token}, ID: {self.pk})'

class Question(models.Model):
    survey = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE)
    prompt = models.TextField()
    INPUT_TYPE_CHOICES = (
        ('t', 'Text Box'),
        ('m', 'Multiple Choice'),
    )    
    input_type = models.CharField(max_length=1, choices=INPUT_TYPE_CHOICES)
    input_spec = models.TextField(blank=True, help_text="* One Row One Option<br>* Option Character and Option Text are separated by single comma only, no space<br>* Example:<br><span style='color:blue;'>A,Apple<br>B,Boy<br>C,Cat</span>")
    @property
    def mc_choices(self):
        rows = self.input_spec.splitlines()
        choices = []
        for row in rows:
            row_split = row.split(",", 1)
            choices.append(row_split)
        print(choices)
        return choices
        "Returns the person's full name."
        # return '%s %s' % (self.first_name, self.last_name)
    def __str__(self):
        return f'{self.survey} | {self.prompt}'

class Response(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    content = models.TextField()
    @property
    def answer(self):
        json.loads(content)