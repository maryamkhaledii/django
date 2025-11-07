from django.forms import ModelForm, Form, CharField, ImageField, ModelMultipleChoiceField
from students.models import Student, Course, Profile


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["fullname"]


class CourseForm(ModelForm):
    class Meta:
        model = Course
        exclude = ["students", ]


# class ProfileForm(ModelForm):
#     class Meta:
#         model = Profile
#         fields = ["bio", "avatar", "student"]


class ProfileForm(Form):
    bio = CharField()
    avatar = ImageField()
    student = ModelMultipleChoiceField(queryset=Student.objects.all())