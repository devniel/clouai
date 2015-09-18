from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models


# Account model manager 
class UserManager(BaseUserManager):
	def create_user(self, email, password=None, **kwargs):

		from repositories.models import Repository

		# create user

		if not email:
			raise ValueError('Users must have a valid email address.')

		if not kwargs.get('username'):
			raise ValueError('Users must have a valid username.')

		user = self.model(
			email=self.normalize_email(email), username=kwargs.get('username')
		)

		user.set_password(password)
		user.save()

		# Create repository
		repository = Repository(owner=user, name=user.username)
		repository.save()

		return user

	def create_superuser(self, email, password, **kwargs):
		user = self.create_user(email, password, **kwargs)
		user.is_admin = True
		user.save()
		return user

# Account model
class User(AbstractBaseUser):
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=40, unique=True)
	is_admin = models.BooleanField(default=False)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	def get_full_name(self):
		return self.username

	def get_short_name(self):
		return self.username
	
	def is_superuser(self):
		return self.is_admin

	def is_staff(self):
		return self.is_admin

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return self.is_admin

	def __unicode__(self):
		return self.email

	def get_username(self):
		return self.username

	def get_email(self):
		return self.email
