from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey
import mptt

from mysite import settings


class Category(MPTTModel):
    name = models.CharField(max_length=150, verbose_name="Category")
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name=u'Parrent class')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name_plural = "Category"
        verbose_name = "Category"
        ordering = ('tree_id', 'level')

    class MPTTMeta:
        order_insertion_by = ['name']


mptt.register(Category, order_insertion_by=['name'])


class Keywords(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Теги')

    class Meta():
        db_table = 'keywords'


    def __str__(self):
        return self.name


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
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
    category = TreeForeignKey(Category, blank=True, null=True, related_name='cat')
    keywords = models.ManyToManyField(Keywords, related_name="keywords", related_query_name="keyword", verbose_name='Теги')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comments(models.Model):
    comments_text = models.TextField()
    comments_article_id = models.ForeignKey(Post)
    comments_date = models.DateTimeField(u'date', auto_now=True, null=True)
    comments_author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)

    class Meta():
        db_table = 'comments'




