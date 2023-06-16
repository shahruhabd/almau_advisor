from django.contrib.auth.models import AbstractUser

class LDAPUser(AbstractUser):
    class Meta:
        swappable = 'AUTH_USER_MODEL'