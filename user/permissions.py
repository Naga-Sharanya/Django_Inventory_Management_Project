# users/permissions.py
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class HasModulePermission(permissions.BasePermission):
    """
    Custom permission to check if the user has permission for a specific module.
    """
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_staff:
            return True
        elif user and user.roles.filter(role='customer').exists():
            return view.module_name == 'orders'
        elif user and user.roles.filter(role='seller').exists():
            return view.module_name in ['products', 'orders', 'inventory']
        return False

def has_object_permission(self, request, view, obj):
    """
    Additional check for object-level permissions (e.g., PUT, PATCH, DELETE).
    """
    user = request.user
    if not user or not user.roles.exists():
        return False

    user_roles = user.roles.values_list('role', flat=True)
    module_name = view.module_name

    if 'customer' in user_roles and module_name == 'orders':
        # Allow customers to modify objects only in the 'orders' module
        return True
    elif 'seller' in user_roles and module_name in ['products', 'orders', 'inventory']:
        # Allow sellers to modify objects in specified modules
        return True

    # Deny permissions for other cases
    raise PermissionDenied("Sorry, you are not allowed to modify objects in this module.")

