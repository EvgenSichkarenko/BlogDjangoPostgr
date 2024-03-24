from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=100, verbose_name='Слаг', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tags(models.Model):
    title = models.CharField(max_length=150, verbose_name='Тег')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tags', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']


class Posts(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=150, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField()
    views = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='image')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']


class Quote(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитати'