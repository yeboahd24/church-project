from django.contrib.auth.backends import ModelBackend
from staff.models import Staff


class AuthenticateStaff(ModelBackend):
    # Staff Authentication (email, password)
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = Staff.objects.get(email=email)
            if user.check_password(password):
                return user
        except Staff.DoesNotExist:
            return None