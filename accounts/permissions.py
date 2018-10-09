from rest_framework import permissions


class AnonCreateAndUpdateOwnerOnly(permissions.BasePermission):
	"""
	Custom permission:
		- allow anonymous POST
		- allow authenticated GET and PUT on *own* record
		- allow all actions for staff
	"""

	def has_permission(self, request, view):
		return view.action == 'create' or request.user and request.user.is_authenticated

	def has_object_permission(self, request, view, obj):
		allowed_actions = ['retrieve', 'update', 'partial_update']
		return view.action in allowed_actions and obj.id == request.user.id or request.user.is_staff


class ListAdminOnly(permissions.BasePermission):
	"""
	Custom permission to only allow access to lists for admins
	"""

	def has_permission(self, request, view):
		return view.action != 'list' or request.user and request.user.is_staff


class AnonReadCreateAndUpdateAdminOnly(permissions.BasePermission):
	"""
	Custom permission to allow anonymous read. Create and Update can only be done by admins.
	"""

	def has_permission(self, request, view):
		if view.action == 'list' or view.action == 'retrieve':
			return True
		else:
			if request.user and request.user.is_authenticated and request.user.is_admin:
				return True
			else:
				return False