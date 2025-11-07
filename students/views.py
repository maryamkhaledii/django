from django.shortcuts import render, redirect
from students.models import Student, Course
from students.forms import StudentForm


def student_view(request):
    form = StudentForm()
    html_file = "student/all_student.html"
    if request.method == "GET":
        all_students = Student.objects.all()
        context = {"students": all_students, "form": form}
        return render(request, html_file, context)
    elif request.method == "POST":
        d = StudentForm(request.POST)
        if d.is_valid():
            saved_obj = d.save()
        # data = request.POST
        # fullname1 = data["fullname"]
        # username1 = data["username"]
        # phone1 = data["phone_number"]
        # student_object = Student.objects.create(fullname=fullname1, username=username1, phone_number=phone1, score=0)
            if saved_obj:
                return redirect("todo:home")
        return render(request, html_file, {"form": form})


def courses_view(request):
    all_courses = Course.objects.all()
    context = {"courses": all_courses}
    return render(request, "student/courses.html", context)