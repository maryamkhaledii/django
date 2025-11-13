from django.views import View
from students.models import *
from students.forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin

class AllStudentsView(LoginRequiredMixin, View):
    html_file = "student/all_student.html"
    form = StudentForm()

    def get(self, request):
        all_students = Student.objects.all()
        context = {"students": all_students, "form": self.form}
        return render(request, self.html_file, context)

    def post(self, request):
        st_form = StudentForm(request.POST)
        if st_form.is_valid():
            try:
                Student.objects.get(username=request.POST["username"])
            except ObjectDoesNotExist:
                saved_obj = st_form.save()
                if saved_obj:
                    return redirect("todo:home")
            except:
                pass
        return render(request, self.html_file, {"form": self.form, "message": "نام کاربری تکراری است"})


class AddCourseView(View):
    html = "student/add_course.html"

    def get(self, request):
        if request.user.is_authenticated:
            form = CourseForm()
            return render(request, self.html, {"form": form})
        else:
            return redirect("account:user-login")

    def post(self, request):
        form_data = CourseForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect("todo:home")
        return render(request, self.html, {"form": CourseForm()})


class AddProfileView(View):
    html = "student/add_profile.html"

    def get(self, request):
        form = ProfileForm()
        return render(request, self.html, {"form": form})

    def post(self, request):
        form_data = ProfileForm(request.POST, request.FILES)
        # if form_data.is_valid():
        data = form_data.cleaned_data
        avatar = data["avatar"]
        bio = data["bio"]
        student = data["student"]
        Profile.objects.create(
            avatar=avatar, bio=bio, student=student
        )
        # form_data.save()
        return redirect("todo:home")
        # return render(request, self.html, {"form": ProfileForm()})


class AllTeachersView(View):
    html = "student/teachers.html"
    def get(self, request):
        teachers = Teacher.objects.all()
        return render(request, self.html, {"teachers": teachers})


class AllCoursesView(LoginRequiredMixin, View):
    html_file = "student/courses.html"

    def get(self, request):
        all_courses = Course.objects.all()
        return render(request, self.html_file, {"courses": all_courses})
    

class EnrollCourseView(LoginRequiredMixin, View):

    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        course.students.add(request.user.profile.student)
        return redirect("student:all-courses")