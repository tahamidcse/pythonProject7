from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import User,Submissions
from .serializers import UserSerializer,SubmissionSerializer
from .utils import create_code_file
import subprocess
# Create your views here.
def hello_world(request):
    return HttpResponse("Welcome to online ide")
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SubmissionsViewSet(ModelViewSet):
    queryset = Submissions.objects.all()
    serializer_class = SubmissionSerializer

    def create(self, request, *args, **kwargs):
        request.data["status"] = "P"
        file_name = create_code_file(request.data.get("code"),
                                     request.data.get("language"))
        output = execute_file(file_name,request.data.get("language"))
        request.data["output"] = output
        return super().create(request,args,kwargs)
def execute_file(file_name, language):

    if language == "cpp":
        # g++ xyz.cpp
        result = subprocess.run(["g++", "code/" + file_name], stdout=subprocess.PIPE)
        if result.returncode != 0:
            # Compile time error
            return
        result = subprocess.run(["a.exe"], stdout=subprocess.PIPE)
        if result.returncode != 0:
            #runtime
            return
        return result.stdout.decode("utf-8")