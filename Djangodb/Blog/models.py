from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
import enum

# Create your models here.

class BookOrCourse(models.Model) :
    # fields

    RECOMMENDED_TYPES = (
        ('COURSE' , 'Course'),
        ('BOOK' , 'Book'),
    )

    Level_Types = (
        ('ADVANCED' , 'Advanced'),
        ('INTERMEDIATE' , 'Intermediate'),
        ('INCIPIANTE' , 'Incipiante'),
    )
    title = models.CharField(max_length=255 , null=True , blank = True)#
    producername = models.CharField(max_length=255 , null=True , blank = True)#
    level = models.CharField(max_length = 50, null = True,choices=Level_Types )#
    rec_type = models.CharField(max_length = 50 ,null = True,choices=RECOMMENDED_TYPES)#
    estimatedtimetocomplete = models.CharField(max_length=255 , null=True , blank = True)









