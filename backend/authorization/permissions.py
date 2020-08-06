from rest_framework.permissions import BasePermission

class HasVaultTokenInHeaderUnChecked(BasePermission):
    """
    This only checks to see if vault token is present, this is un safe as it stands
    """
    def has_permission(self, request, view):
        return request.headers.get("X-Vault-Token") is not None
