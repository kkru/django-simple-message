from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET"])
def getMessage(request):
    print("GET request")
    return Response({"message" : "Django says : hello!"}, status=status.HTTP_200_OK)