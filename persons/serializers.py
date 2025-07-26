from django.utils import timezone

from rest_framework import serializers

from persons.models import *


class CharFieldExampleSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=3, max_length=10, allow_blank=True)

    class Meta: 
        model = CharFieldExample
        fields = '__all__'


class IntegerFieldExampleSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(min_value=18, max_value=100)

    class Meta: 
        model = IntegerFieldExample
        fields = '__all__'


class FloatFieldExampleSerializer(serializers.ModelSerializer):
    score = serializers.FloatField(min_value=0, max_value=100)

    class Meta: 
        model = FloatFieldExample
        fields = '__all__'


class DecimalFieldExampleSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(max_digits=4, decimal_places=2, min_value=0, max_value=100)

    class Meta: 
        model = DecimalFieldExample
        fields = '__all__'


class BooleanFieldExampleSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField()

    class Meta: 
        model = BooleanFieldExample
        fields = '__all__'


class DateFieldExampleSerializer(serializers.ModelSerializer):
    dob = serializers.DateField()

    class Meta: 
        model = DateFieldExample
        fields = '__all__'


class TimeFieldExampleSerializer(serializers.ModelSerializer):
    wakeup_time = serializers.TimeField()

    class Meta: 
        model = TimeFieldExample
        fields = '__all__'


class DateTimeFieldExampleSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField()

    class Meta: 
        model = DateTimeFieldExample
        fields = '__all__'


class DurationFieldExampleSerializer(serializers.ModelSerializer):
    task_duration = serializers.DurationField()

    class Meta: 
        model = DurationFieldExample
        fields = '__all__'


class EmailFieldExampleSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta: 
        model = EmailFieldExample
        fields = '__all__'


class RegexFieldExampleSerializer(serializers.ModelSerializer):
    code = serializers.RegexField(regex=r'^\d{4}[A-Z]{2}$')

    class Meta:
        model = RegexFieldExample
        fields = '__all__'


class URLFieldExampleSerializer(serializers.ModelSerializer):
    website = serializers.URLField()

    class Meta: 
        model = URLFieldExample
        fields = '__all__'


class ChoiceFieldExampleSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(
        choices=[('draft', 'Draft'), ('pub', 'Published')],
        allow_blank=True
    )

    class Meta: 
        model = ChoiceFieldExample
        fields = '__all__'


class MultiChoiceFieldExampleSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(
        child=serializers.ChoiceField(choices=['news', 'tech', 'sports'])
    )

    class Meta: 
        model = MultiChoiceFieldExample
        fields = '__all__'


class ListFieldExampleSerializer(serializers.ModelSerializer):
    items = serializers.ListField(child=serializers.CharField(allow_blank=True))

    class Meta: 
        model = ListFieldExample
        fields = '__all__'


class DictFieldExampleSerializer(serializers.ModelSerializer):
    config = serializers.DictField()

    class Meta: 
        model = DictFieldExample
        fields = '__all__'


class SlugFieldExampleSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField()

    class Meta: 
        model = SlugFieldExample
        fields = '__all__'


class UUIDFieldExampleSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField()

    class Meta: 
        model = UUIDFieldExample
        fields = '__all__'


class FilePathFieldExampleSerializer(serializers.ModelSerializer):
    file_path = serializers.FilePathField(path="/tmp")

    class Meta:
        model = FilePathFieldExample
        fields = '__all__'


class IPAddressFieldExampleSerializer(serializers.ModelSerializer):
    ip_address = serializers.IPAddressField()

    class Meta:
        model = IPAddressFieldExample
        fields = '__all__'


class JSONFieldExampleSerializer(serializers.ModelSerializer):
    json_data = serializers.JSONField()

    class Meta: 
        model = JSONFieldExample
        fields = '__all__'


class FileFieldExampleSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta: 
        model = FileFieldExample
        fields = '__all__'


class ImageFieldExampleSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta: 
        model = ImageFieldExample
        fields = '__all__'


class HiddenFieldExampleSerializer(serializers.ModelSerializer):
    modified = serializers.HiddenField(default=timezone.now)

    class Meta: 
        model = HiddenFieldExample
        fields = '__all__'


class ReadWriteExampleSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField()
    password = serializers.CharField(write_only=True)

    class Meta: 
        model = ReadWriteExample
        fields = '__all__'


class MethodFieldExampleSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta: 
        model = MethodFieldExample
        fields = ['id', 'first_name', 'last_name', 'full_name']

    def get_full_name(self, obj): 
        return f"{obj.first_name} {obj.last_name}"
