# from django.shortcuts import render, redirect
# from students.models import Student, Course
# from students.forms import StudentForm


# def student_view(request):
#     form = StudentForm()
#     html_file = "student/all_student.html"
#     if request.method == "GET":
#         all_students = Student.objects.all()
#         context = {"students": all_students, "form": form}
#         return render(request, html_file, context)
#     elif request.method == "POST":
#         d = StudentForm(request.POST)
#         if d.is_valid():
#             saved_obj = d.save()
#         # data = request.POST
#         # fullname1 = data["fullname"]
#         # username1 = data["username"]
#         # phone1 = data["phone_number"]
#         # student_object = Student.objects.create(fullname=fullname1, username=username1, phone_number=phone1, score=0)
#             if saved_obj:
#                 return redirect("todo:home")
#         return render(request, html_file, {"form": form})


# def courses_view(request):
#     all_courses = Course.objects.all()
#     context = {"courses": all_courses}
#     return render(request, "student/courses.html", context)

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import Student, Course, Profile
from .serializers import (
    StudentSerializer, CourseSerializer, TeacherSerializer,
    CreateStudentSerializer, CreateTeacherSerializer, ProfileSerializer
)


# Students
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateStudentSerializer
        return StudentSerializer


# Courses
class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# Teachers (User with is_staff=True)
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff=True)

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateTeacherSerializer
        return TeacherSerializer


# Profile detail
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)
