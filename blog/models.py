from django.db import models
# Create your models here.


class Blog(models.Model):

    article_title = models.CharField(max_length=50, verbose_name='заголовок статьи')
    article_body = models.TextField(verbose_name='содержимое статьи')
    article_image = models.ImageField(upload_to='media', blank=True, null=True, verbose_name='изображение статьи')
    publicated_date = models.DateTimeField(verbose_name='дата публикации')
    count_views = models.PositiveIntegerField(verbose_name='количество просмотров')
    is_published = models.BooleanField(default=True, verbose_name="опубликовано")

    def __str__(self):

        return self.article_title

    class Meta:

        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
