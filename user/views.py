from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUserModule , CustomUserPermission, CustomUserRole
from .serializers import CustomUserModuleSerializer,CustomUserRegistrationSerializer, CustomUserPermissionSerializer, CustomUserRoleSerializer, CustomUserLoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from .permissions import HasModulePermission



class CustomUserRegistrationView(APIView):
    def post(self, request):
        serializer = CustomUserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    
   
class CustomUserLoginView(TokenObtainPairView):
    serializer_class = CustomUserLoginSerializer
    
class ModuleListView(APIView):
    def get(self, request):
        modules = CustomUserModule.objects.all()
        serializer = CustomUserModuleSerializer(modules, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class CustomUserModuleListView(APIView):
    permission_classes = [IsAuthenticated, HasModulePermission]
    def get(self, request, pk=None):
        if pk:
            module = get_object_or_404(CustomUserModule, pk=pk)
            serializer = CustomUserModuleSerializer(module)
            return Response(serializer.data)
        else:
            modules = CustomUserModule.objects.all()
            serializer = CustomUserModuleSerializer(modules, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        module = get_object_or_404(CustomUserModule, pk=pk)
        serializer = CustomUserModuleSerializer(module, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        module = get_object_or_404(CustomUserModule, pk=pk)
        module.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CustomUserPermissionList(APIView):
    permission_classes = [IsAuthenticated, HasModulePermission]
    def get(self, request):
        permissions = CustomUserPermission.objects.all()
        serializer = CustomUserPermissionSerializer(permissions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserPermissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CustomUserRoleView(APIView):
    permission_classes = [IsAuthenticated, HasModulePermission]
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            try:
                role = CustomUserRole.objects.get(pk=pk)
                serializer = CustomUserRoleSerializer(role)
                return Response(serializer.data)
            except CustomUserRole.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            roles = CustomUserRole.objects.all()
            serializer = CustomUserRoleSerializer(roles, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CustomUserRoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, *args, **kwargs):
        try:
            role = CustomUserRole.objects.get(pk=pk)
            serializer = CustomUserRoleSerializer(role, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CustomUserRole.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, *args, **kwargs):
        try:
            role = CustomUserRole.objects.get(pk=pk)
            role.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CustomUserRole.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)