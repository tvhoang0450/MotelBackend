from .models import User

class EmailAuthBackend():
    def authenticate(self, request,username, password):
        try:
            user = User.objects.get( email=username )
            password = user.check_password(password)
            if access:
                return user
        
        except User.DoesNotExist:
            pass
        return None