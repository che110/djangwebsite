from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    intime =models.DateField(auto_now_add=True,null=True)
    sex = models.IntegerField(null=True)
    class Meta:
        db_table='student'


class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    class Meta:
        db_table='teacher'

    def __unicode__(self):
        return self.name


