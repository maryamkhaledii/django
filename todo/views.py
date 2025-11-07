from django.shortcuts import render
from django.http import HttpResponse
from todo.models import Task
from students.models import Student, Course
from django.views import View


def len2(text):
    return len(text)


def home_view(request):
    list_tasks = Task.objects.all()
    titles = []
    for obj in list_tasks:
        length = len2(obj.title)
        titles.append(str(length))
    new = ", ".join(titles)
    return HttpResponse(new)


def home_view2(request):
    context = {"student": ["Ali", "hosein"]}
    return render(request, 'todo/new.html', context)


def task_view(request):
    if request.method == "GET":
        tasks = list(Task.objects.all())
        context = {"list_tasks": tasks}
        return render(request, 'todo/start.html', context)


def task_view2(request):
    tasks = Task.objects.all()
    titles = []
    for obj in tasks:
        titles.append(obj.title)
    context = {"tasks_titles": titles}
    return render(request, 'todo/start.html', context)


def task_student(request, st_id):

    student_obj = Student.objects.get(id=st_id)
    if student_obj.fullname == "mohamad":
        student_obj.fullname = "ali"
    elif student_obj.fullname == "ali":
        student_obj.fullname == "mohamad"

    Task.objects.create(
        title="new task",
        done=False,
        category="sport",
        description="desc new task",
        student=student_obj
    )

    Task.objects.bulk_create(tasks)

    course = Course.objects.get(code=1)
    course.students.add(student_obj)

    tasks_student = Task.objects.filter(student_id=st_id)
    context = {"tasks": tasks_student}
    return render(request, "todo/list_student_1.html", context)
