from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True, blank=True, default='')

    class Meta():
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:category_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название', help_text='max length - 255', unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    tag = models.ManyToManyField(Tag)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name="Изображение", blank=True, null=True, upload_to='product')
    price = models.FloatField()
    discount = models.FloatField(verbose_name='Скидка', validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
                                 default=0, blank=True, )
    bonus = models.PositiveIntegerField(verbose_name="Бонус", blank=True, null=True,
                                        validators=[MaxValueValidator(100)])
    in_stock = models.BooleanField(verbose_name="В наличии", default=True)
    created_dt = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    update_dt = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-pk', ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:product_detail', kwargs={'slug_category': self.category.slug, 'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
