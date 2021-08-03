from django.contrib import admin
from .models import BookOrCourse
from Blog.forms import ContactForm , NewUserForm

# Register your models here.

admin.site.register(BookOrCourse)
admin.site.register(ContactForm)
admin.site.register(NewUserForm)
