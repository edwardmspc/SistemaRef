from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):

	def _create_user(self, username, email, password, is_staff,
			is_superuser, **extra_fields):
		if not username:
			raise ValueError('El usuario debe ser obligado')
		if not email:
			raise ValueError('El email debe ser obligado')
		email = self.normalize_email(email)
		user = self.model(username=username, email=email, is_active=True,
				is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
		user.set_password(password)
		user.save(using = self._db)
		return user

	def create_user(self, username, email, password=None, **extra_fields):
		return self._create_user(username, email, password, False, False,**extra_fields)

	def create_superuser(self, username, email, password, **extra_fields):
		return self._create_user(username, email, password, True, True, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(max_length=50, unique=True)
	email = models.EmailField(max_length=50, unique=True)
	
	#middle_name = models.CharField(max_length=50, blank=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	inviter = models.CharField(max_length=50,blank=True)
	#date_birthday = models.DateField(null=True)
	
	date_joined = models.DateTimeField(default=timezone.now)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	
	objects = CustomUserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def get_short_name(self):
		return self.username