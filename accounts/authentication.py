from accounts.models import User, Token


class PasswordlessAuthenticationBackend(object):
    """Passwordless Authentication Backend."""
    def authenticate(self, uid):
        """Authenticate."""
        token = Token.objects.get(uid=uid)
        return User.objects.get(email=token.email)
