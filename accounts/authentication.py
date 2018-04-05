from accounts.models import User, Token


class PasswordlessAuthenticationBackend(object):
    """Passwordless Authentication Backend."""

    def authenticate(self, uid):
        """Authenticate."""
        try:
            token = Token.objects.get(uid=uid)
            return User.objects.get(email=token.email)
        except User.DoesNotExist:
            return User.objects.create(email=token.email)
        except Token.DoesNotExist:
            return None
