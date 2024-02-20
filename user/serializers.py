from rest_framework import serializers
from .models import CustomUser, CustomUserModule, CustomUserPermission, CustomUserRole
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=120, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'confirm_password', 'contact_number', 'address']

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            contact_number=validated_data['contact_number'],
            address=validated_data['address'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        if len(attrs['password']) < 8:
            raise serializers.ValidationError({"password": "Password must be at least 8 characters long."})

        return attrs

class CustomUserLoginSerializer(TokenObtainPairSerializer):
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if not username or not password or not confirm_password:
            raise serializers.ValidationError("All fields are required")
        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match")
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Wrong username or password")

        return super().validate(attrs)



class CustomUserModuleSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()

    class Meta:
        model = CustomUserModule
        fields = ['id', 'name', 'is_active', 'created_at', 'updated_at', 'created_by']
        read_only_fields = ['created_at', 'updated_at']

    def get_created_by(self, obj):
        return obj.created_by.username if obj.created_by else None
    
    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name cannot be empty.")
        return value
    
    def create(self, validated_data):
        # Set the created_by field with the currently authenticated user
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['created_by'] = request.user
        return super().create(validated_data)


class CustomUserPermissionSerializer(serializers.ModelSerializer):
    modules = serializers.SerializerMethodField()
    roles = serializers.SerializerMethodField()

    class Meta:
        model = CustomUserPermission
        fields = ['id', 'modules', 'roles']
        
    def get_modules(self, obj):
        return [module.name for module in obj.modules.all()]

    def get_roles(self, obj):
        return [role.role for role in obj.roles.all()]


    
class CustomUserRoleSerializer(serializers.ModelSerializer):
    user_names = serializers.SerializerMethodField()
    class Meta:
        model = CustomUserRole
        fields=['id', 'role', 'user_names']


    def get_user_names(self, obj):
        return [user.username for user in obj.users.all()] if obj.users.exists() else []