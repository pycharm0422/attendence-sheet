from django.contrib import admin
from . models import Student, Teacher, Class, Count, Feedback


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Count)
admin.site.register(Feedback)
