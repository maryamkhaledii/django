from django.urls import path
from students.views import student_view, courses_view
from students.class_views import *

app_name = "student"

urlpatterns = [
    path("all_students/", student_view, name="student_list"),
    path("courses/", courses_view),
    path("all_students_new/", AllStudentsView.as_view(), name="student_list_new"),
    path("add-course/", AddCourseView.as_view(), name="add_course"),
    path("add-profile/", AddProfileView.as_view(), name="add_profile"),
    path("all-teachers/", AllTeachersView.as_view(), name="teachers")

]