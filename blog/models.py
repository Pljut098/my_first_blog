from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey


class Catgory(MPTTModel):
    name = models.CharField(max_length=150, verbose_name = "Category")
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    class Meta:
        db_table = 'category'
        verbose_name_plural = "Category"
        verbose_name = "Category"
    def __unicode__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']




# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="image/",
         verbose_name="image")
    category = TreeForeignKey(Catgory, blank=True, null=True, related_name = "cat")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comments(models.Model):

    comments_text = models.TextField()
    comments_article_id = models.ForeignKey(Post)
    comments_date = models.DateTimeField(u'date',auto_now=True, null=True)
    comments_author = models.ForeignKey('auth.User', null=True)

    class Meta():
        db_table = 'comments'