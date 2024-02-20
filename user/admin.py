# from django.contrib import admin
# from .models import CustomUser
# from .models import Module
# from .serializers import ModuleAdminSerializer

# admin.site.register(CustomUser)
# admin.site.register(Module, ModuleAdmin)

from django.contrib import admin
from .models import CustomUser, CustomUserModule, CustomUserPermission, CustomUserRole

# class CustomUserModuleAdmin(admin.ModelAdmin):
#     model = CustomUserModule
    
admin.site.register(CustomUser)
admin.site.register(CustomUserModule)
admin.site.register(CustomUserPermission)
admin.site.register(CustomUserRole)
