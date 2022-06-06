from rest_framework import permissions



class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.owner #the one who created the expense is the one only to access it