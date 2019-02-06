from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
from django.core.validators import RegexValidator


class UserProfile(models.Model):
	alphanumeric = RegexValidator(r'^[0-9A-Z]*$', 'Only alphanumeric characters are allowed.')
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	USN = models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric], unique=True)
	year = models.IntegerField()
	sem = models.IntegerField()
	phone = models.IntegerField()

	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)


class Books(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	book_name = models.CharField(max_length=100)
	price = models.IntegerField()
	negotiable = models.BooleanField(default=False)
	description = models.TextField(max_length=50)
	date_posted = models.DateTimeField(auto_now=True)
	date_updated = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'books'
		unique_together = (("user", "book_name"),)                             # checks that user does not post ad for same book multiple times .



	
	#image = models.ImageField(upload_to='profile_image',blank = True)

