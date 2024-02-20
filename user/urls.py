from django.urls import path
from user.views import (
    CustomUserRegistrationView, 
    CustomUserModuleListView,
    CustomUserPermissionList,
    CustomUserRoleView,
    CustomUserLoginView,
    ModuleListView
)

urlpatterns = [
    path('register/', CustomUserRegistrationView.as_view(), name='signup'),
    path('login/', CustomUserLoginView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', CustomUserLoginView.as_view(), name='refresh'),
    path('modules/', CustomUserModuleListView.as_view(), name='module-list'),
    path('modules/<int:pk>/', CustomUserModuleListView.as_view(), name='module-detail'),
    path('permissions/', CustomUserPermissionList.as_view(), name='permissions-list'),
    path('custom_user_roles/', CustomUserRoleView.as_view(), name='custom_user_roles_list'),
    path('custom_user_roles/<int:pk>/', CustomUserRoleView.as_view(), name='custom_user_roles_detail'),
    path('module-list/', ModuleListView.as_view(), name='module-list'),
    path('module-list/<int:pk>/', ModuleListView.as_view(), name='module-detail'),
]
