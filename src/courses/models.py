from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User


class Course(models.Model):
	DJANGO = "Django"
	MEAN = 'MEAN'
	IOS ='iOS'
	SERVER = 'Server'

	CATEGORIES = (
		(DJANGO, 'Django'),
		(MEAN, 'MEAN'),
		(IOS, 'iOS'),
		(SERVER, 'Server'),
	)

	user 		= models.ForeignKey(User, related_name="courses_created")
	category 	=  models.CharField(
		max_length=15,
		choices=CATEGORIES,
		default=DJANGO,
	)
	title 		= models.CharField(max_length=200)
	slug 		= models.SlugField(max_length=200, unique=True)
	overview 	= models.TextField()
	created 	= models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return self.title

class Module(models.Model):
	course 		= models.ForeignKey(Course, related_name="modules")
	title 		= models.CharField(max_length=200)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.title

class Content(models.Model):
	module 		= models.ForeignKey(Module, related_name="contents")
	content_type= models.ForeignKey(ContentType, 
									limit_choices_to={"model__in": ("text", "video", "image", "file")})
	object_id 	= models.PositiveIntegerField()
	item 		= GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.title

class ItemBase(models.Model):
	user 		= models.ForeignKey(User, related_name="%(class)s_related")
	title 		= models.CharField(max_length=200)
	created 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)

	class Meta:
		abstract=True

	def __str__(self):
		return self.title

class Text(ItemBase):
	content 	= models.TextField()

class File(ItemBase):
	file 		= models.FileField(upload_to="files")

class Image(ItemBase):
	image 		= models.ImageField(upload_to="images")

class Video(ItemBase):
	url 		= models.URLField()