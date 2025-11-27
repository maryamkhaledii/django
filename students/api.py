# from rest_framework.views import APIView
# from students.models import Student
# from rest_framework.response import Response

# class AllStudentApiView(APIView):
#     def get(self, request):
#         student_ids = Student.objects.all().values_list("fullname", flat=True)
#         students_dict = {"names": student_ids}
#         print(students_dict)
#         return Response(students_dict)
    
#     def post(self, request):
#         Student.objects.create(

#         )
#         return Response({"message": "ok"})
    
#     def put(self, request, pk):
#         print(pk)
#         print(request.data)
#         return Response({"message": "ok"})



from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from students.models import *
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from students.serializers import StudentSerializer, CourseSerializer
from rest_framework.decorators import action

class AllStudentApiView(APIView):
    def get(self, request, pk=None):
        if pk:
            student = Student.objects.get(id=pk)
            return Response({
                "name": student.fullname,
                "score": student.score
            })
        else:
            student_names = Student.objects.all().values_list("fullname", flat=True)
            students_dict = {"names": student_names}
            print(students_dict)
            return Response(students_dict)
    
    def post(self, request):
        data = request.data
        srz_data = StudentSerializer(data=data)
        if srz_data.is_valid():
            Student.objects.create(
                fullname=data["fullname"],
                score=data["score"]
            )
            return Response({"message": "ok"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "validation error"}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        print(pk)
        print(request.data)
        return Response({"message": "ok"})

    
class EnrollApiView(APIView):

    def post(self, request):
        data = request.data
        st_id = data["student_id"]
        cr_id = data["course_id"]
        try:
            student = Student.objects.get(id=st_id) 
            course = Course.objects.get(id=cr_id)
            if student in course.students.all():
                return Response({"message": "this student has exists"}, status=status.HTTP_400_BAD_REQUEST)
            student.courses.add(course)
        except ObjectDoesNotExist:
            return Response({"message": "error does not exists"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({"message": "course added"}, status=status.HTTP_200_OK)


class CourseViewset(ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # def retrieve(self, request, pk):
    #     srz_data = self.serializer_class(instance=self.queryset.get(id=pk))
    #     data = srz_data.data
    #     teacher = Teacher.objects.get(id=data["teacher"])
    #     data["teacher"] = {"fullname": teacher.fullname, "score": teacher.score}
    #     return Response(data)

    # def list(self, request):
    #     srz_data = CourseSerializer(instance=self.queryset, many=True)
    #     return Response(srz_data.data)

    # def create(self, request):
    #     srz_data = CourseSerializer(data=request.data)
    #     if srz_data.is_valid():
    #         srz_data.save()
    #         return Response("ok", status=status.HTTP_201_CREATED)
    #     return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False)
    def is_active_list(self, request):
        q = Course.objects.filter(is_active=True)
        srz_data = self.serializer_class(instance=q, many=True)
        return Response(srz_data.data)
