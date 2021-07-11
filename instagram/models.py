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

class Like(models.Model):
  like = models.BooleanField()
  image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='imagelikes')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userlikes')

  def __str__(self):
    return "%s like" % self.image
# class for comments 
class Comment(models.Model):
  comment = models.TextField()
  image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

  @classmethod
  def display_comments_by_imageId(cls, image_id):
    comments = cls.objects.filter(image_id=image_id)
    return comments

  def __str__(self):
    return "%s comment" % self.image
