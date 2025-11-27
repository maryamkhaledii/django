from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student, Course, Profile

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'student_id', 'email']


class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'is_active', 'teacher']


class ProfileSerializer(serializers.ModelSerializer):
    user = TeacherSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'phone_number']


class CreateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'student_id', 'email']


class CreateTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data, is_staff=True)
        return user
