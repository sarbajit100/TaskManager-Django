from django.db import models

# Create your models here.

class Department(models.Model):
    department=models.CharField(max_length=100)

    def __str__(self):
        return self.department
    
class Task(models.Model):
    task_created=models.DateField()
    name=models.CharField(max_length=50)
    dep=models.ForeignKey(Department,on_delete=models.CASCADE)
    task=models.TextField(max_length=500)
    status=models.CharField(max_length=100)

    def __str__(self):
        return self.name