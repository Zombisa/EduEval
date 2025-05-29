from mozilla_django_oidc.auth import OIDCAuthenticationBackend
from django.contrib.auth.models import Group

class KeycloakOIDCBackend(OIDCAuthenticationBackend):
    def filter_users_by_claims(self, claims):
        username = claims.get("preferred_username") or claims.get("sub")
        return self.UserModel.objects.filter(username=username)

    def create_user(self, claims):
        user, created = self.UserModel.objects.get_or_create(
            username=claims.get('preferred_username'),
            defaults={
                'email': claims.get('email', ''),
                'first_name': claims.get('given_name', ''),
                'last_name': claims.get('family_name', ''),
            }
        )
        self._assign_roles(user, claims)
        return user



    def update_user(self, user, claims):
        user = super().update_user(user, claims)
        self._assign_roles(user, claims)
        return user

    def _assign_roles(self, user, claims):
        roles = claims.get("realm_access", {}).get("roles", [])
        mapping = {
            "profesor": "profesor",
            "coordinador": "profesor",
            "evaluador": "evaluador"
        }
        user.groups.clear()
        for role in roles:
            group_name = mapping.get(role)
            if group_name:
                group, _ = Group.objects.get_or_create(name=group_name)
                user.groups.add(group)
