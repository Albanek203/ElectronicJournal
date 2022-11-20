from django.contrib import admin
from .models import *

admin.site.register(Student)
admin.site.register(Journal)
admin.site.register(Topic)
admin.site.register(Mark)
admin.site.register(StudentJournal)