from rest_framework.views import APIView
from students.models import Student
from rest_framework.response import Response

class AllStudentApiView(APIView):
    def get(self, request):
        student_ids = Student.objects.all().values_list("fullname", flat=True)
        students_dict = {"names": student_ids}
        print(students_dict)
        return Response(students_dict)
    
    def post(self, request):
        Student.objects.create(

        )
        return Response({"message": "ok"})
    
    def put(self, request, pk):
        print(pk)
        print(request.data)
        return Response({"message": "ok"})

