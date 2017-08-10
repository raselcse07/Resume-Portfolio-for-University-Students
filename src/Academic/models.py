import datetime
from django.db import models
from .utils import year_dropdown






class Department(models.Model):

    dept_name       =models.CharField(max_length=250,primary_key=True,unique=True)
    dept_name_short =models.CharField(max_length=250,unique=True)


    class Meta:

        ordering=["dept_name"]
        verbose_name="Department"
        verbose_name_plural="Departments"

    def __str__(self):

        return str(self.dept_name_short)
