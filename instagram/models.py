from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Image(models.Model):
  image = models.ImageField(upload_to='instaimages/')
  name = models.CharField(max_length=60)
  caption = models.TextField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def save_image(self):
     self.save()

  @classmethod
  def display_images(cls):
    images = cls.objects.all()
    return images

  @property
  def all_comments(self):
    return self.comments.all()

  @property
  def all_likes(self):
    return self.imagelikes.count()

  @classmethod
  def search_images(cls, search_term):
    images = cls.objects.filter(name__icontains=search_term).all()
    return images

  def delete_post(self):
    self.delete()

  def __str__(self):
    return "%s image" % self.name

