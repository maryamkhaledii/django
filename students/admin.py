from django.contrib import admin
from students.models import Student, Course, Profile,Teacher

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Profile)
