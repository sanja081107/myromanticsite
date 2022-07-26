from django.db import models
from django.urls import reverse


class Question(models.Model):
    title = models.CharField(max_length=50, verbose_name='Имя')
    photo = models.ManyToManyField('Photo', related_name='photo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Question'
        ordering = ['pk']

    # def get_absolute_url(self):
    #     return reverse('people_detail', kwargs={'people_slug': self.slug})


class Photo(models.Model):
    title = models.CharField(max_length=50, verbose_name='Имя')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
        ordering = ['title']
