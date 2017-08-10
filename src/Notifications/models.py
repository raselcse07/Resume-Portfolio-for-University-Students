import random
import string
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify




def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):

    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


class AdminMessage(models.Model):

    title       =models.CharField(max_length=200)
    slug        =models.SlugField(unique=True,blank=True)
    message     =models.TextField()
    publish     =models.DateField(auto_now=False, auto_now_add=False)
    updated     =models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp   =models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.title



    class Meta:
        ordering = ["-timestamp", "-updated"]


def create_slug(instance, new_slug=None):

    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = AdminMessage.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug



def pre_save_post_receiver(sender, instance, *args, **kwargs):

    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_post_receiver, sender=AdminMessage)
