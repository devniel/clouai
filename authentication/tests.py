from django.test import TestCase

# Create your tests here.

class RepositoryCreationTestCase(TestCase):
	def setUp(self):

		self.password = "xxx";
		self.user = User.objects.create_user(username="xxx", password=self.password, email="xxx@gmail.com")
		self.user.save()