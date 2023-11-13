from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=31)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=127, verbose_name="Заголовок")
    subtitle = models.TextField(verbose_name="Подзаголовок")
    photo = models.ImageField(upload_to='images', verbose_name="Фото")
    article = models.TextField(verbose_name="Текст статьи")
    author = models.CharField(max_length=63, verbose_name="Автор")
    data = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, verbose_name="Категория")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовать?")

    def __str__(self):
        return self.title
