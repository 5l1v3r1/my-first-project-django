from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify as django_slugify
from django.db.models.signals import pre_save

# Create your models here.
alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


def slugify(s):
    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('admin_category_article_list_url', kwargs={'category_slug': self.slug})


def pre_save_category_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(instance.name)
        instance.slug = slug


def pre_save_article_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(instance.name)
        instance.slug = slug


class Tag(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(blank=True)
    prev_img = models.ImageField(blank=True)
    prev_text = models.TextField(blank=True)
    detail_img = models.ImageField(blank=True)
    detail_text = models.TextField(blank=True)
    category = models.CharField(max_length=150)

    def __str__(self):
        return self.name


pre_save.connect(pre_save_article_slug, sender=Article)

pre_save.connect(pre_save_category_slug, sender=Category)


# Понимаю что это очень большой костыль, но я учусь)
class Contacts(models.Model):
    head = models.CharField(max_length=150)
    coordin_map = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone1 = models.CharField(max_length=100)
    phone2 = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.head


class PoliticsAndСonfidentiality(models.Model):
    head = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.head


class Reviews(models.Model):
    name = models.CharField(max_length=150, blank=True)
    email = models.CharField(max_length=150)
    text = models.TextField()
    anonym = models.BooleanField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class MainSlider(models.Model):
    name = models.CharField(max_length=250, blank=True)
    img = models.ImageField()
    href = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name

class MainPage(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

