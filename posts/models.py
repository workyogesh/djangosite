from django.db import models
from django.utils import timezone

class Category(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	category = models.ForeignKey('Category',on_delete=models.CASCADE)
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	thumbnail=models.ImageField(upload_to='img/',null=True)
	largePhoto=models.ImageField(upload_to='img/',null=True)
	create_date = models.DateTimeField(timezone.now())
	published_date = models.DateTimeField(blank=True,null=True)

	def published(self):
		self.published_date= timezone.now()
		self.save()

	def __str__(self):
		return self.title
		
class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	text = models.TextField()
	def __str__(self):
		return self.name

	
class Forum(models.Model):
	title = models.CharField(max_length=200)
	category = models.ForeignKey('Category',on_delete=models.CASCADE)
	text = models.TextField()
	def __str__(self):
		return self.title

class Comment(models.Model):
	name = models.CharField(max_length=200)
	forumid = models.ForeignKey('Forum',on_delete=models.CASCADE)
	comment = models.TextField()
	def __str__(self):
		return self.name
	
