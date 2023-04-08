from rest_framework.views import APIView
from rest_framework import permissions, status
from kollabhunt.models.projects import Project
from .serializers import ProjectSerializer
from rest_framework.response import Response

class ProjectAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        pk = request.GET.get('project')
        model = Project.objects.get(id=pk)
        serializer = ProjectSerializer(model)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


