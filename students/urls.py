from django.urls import path, include
from students.views import student_view, courses_view
from students.class_views import *
from students.api import *
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, CourseViewSet, TeacherViewSet, profile_detail

app_name = "student"

router = DefaultRouter()

router.register("all-courses", CourseViewset, basename="all-courses")

urlpatterns = [
    path("all-courses/", AllCoursesView.as_view(), name="all-courses"),
    path("all_students/", AllStudentsView.as_view(), name="student_list_new"),
    path("add-course/", AddCourseView.as_view(), name="add_course"),
    path("add-profile/", AddProfileView.as_view(), name="add_profile"),
    path("all-teachers/", AllTeachersView.as_view(), name="teachers"),
    path("enroll-course/<int:pk>/", EnrollCourseView.as_view(), name="enroll"),
    #-----------------------------------------------------------------------------------------
    # api urls
    path("api/all-students/", AllStudentApiView.as_view()),
    path("api/all-students/<int:pk>/", AllStudentApiView.as_view()),
    path("api/courses/enroll/", EnrollApiView.as_view()),
    path("api/", include(router.urls)),
    path('api/profiles/<int:pk>/', profile_detail),

    # path("api/all-courses/", CourseViewset.as_view())
]