import uuid

from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)


class CharFieldExample(models.Model):
    name = models.CharField(max_length=100)


class IntegerFieldExample(models.Model):
    age = models.IntegerField()


class FloatFieldExample(models.Model):
    score = models.FloatField()


class DecimalFieldExample(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)


class BooleanFieldExample(models.Model):
    is_active = models.BooleanField()


class DateFieldExample(models.Model):
    dob = models.DateField()


class TimeFieldExample(models.Model):
    wakeup_time = models.TimeField()


class DateTimeFieldExample(models.Model):
    created_at = models.DateTimeField()


class DurationFieldExample(models.Model):
    task_duration = models.DurationField()


class EmailFieldExample(models.Model):
    email = models.EmailField()


class RegexFieldExample(models.Model):
    code = models.CharField(max_length=10)



class URLFieldExample(models.Model):
    website = models.URLField()


class ChoiceFieldExample(models.Model):
    status = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('pub', 'Published')])


class MultiChoiceFieldExample(models.Model):
    tags = models.JSONField(default=list)


class ListFieldExample(models.Model):
    items = models.JSONField(default=list)


class DictFieldExample(models.Model):
    config = models.JSONField(default=dict)


class SlugFieldExample(models.Model):
    slug = models.SlugField()


class UUIDFieldExample(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)


class FilePathFieldExample(models.Model):
    file_path = models.FilePathField(path="/tmp")


class IPAddressFieldExample(models.Model):
    ip_address = models.GenericIPAddressField()


class JSONFieldExample(models.Model):
    json_data = models.JSONField()


class FileFieldExample(models.Model):
    file = models.FileField(upload_to='files/')


class ImageFieldExample(models.Model):
    image = models.ImageField(upload_to='images/')


class HiddenFieldExample(models.Model):
    modified = models.DateTimeField()
    comment = models.TextField()


class ReadWriteExample(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class MethodFieldExample(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
