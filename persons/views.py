from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from persons.models import *
from persons.serializers import *


class CharFieldExampleView(CreateAPIView, ListAPIView, RetrieveAPIView): 
    queryset = CharFieldExample.objects.all()
    serializer_class = CharFieldExampleSerializer


class IntegerFieldExampleView(CreateAPIView, ListAPIView, RetrieveAPIView): 
    queryset = IntegerFieldExample.objects.all()
    serializer_class = IntegerFieldExampleSerializer


class FloatFieldExampleView(CreateAPIView, ListAPIView, RetrieveAPIView): 
    queryset = FloatFieldExample.objects.all()
    serializer_class = FloatFieldExampleSerializer


class DecimalFieldExampleView(CreateAPIView, ListAPIView, RetrieveAPIView): 
    queryset = DecimalFieldExample.objects.all()
    serializer_class = DecimalFieldExampleSerializer


class BooleanFieldExampleView(CreateAPIView, ListAPIView, RetrieveAPIView): 
    queryset = BooleanFieldExample.objects.all()
    serializer_class = BooleanFieldExampleSerializer


class DateFieldExampleView(CreateAPIView, ListAPIView, RetrieveAPIView): 
    queryset = DateFieldExample.objects.all()
    serializer_class = DateFieldExampleSerializer


class TimeFieldExampleView(CreateAPIView, ListAPIView, RetrieveAPIView): 
    queryset = TimeFieldExample.objects.all()
    serializer_class = TimeFieldExampleSerializer


class DateTimeFieldExampleView(CreateAPIView, ListAPIView, RetrieveAPIView): 
    queryset = DateTimeFieldExample.objects.all()
    serializer_class = DateTimeFieldExampleSerializer


class DurationFieldExampleView(CreateAPIView, ListAPIView, RetrieveAPIView):
    queryset = DurationFieldExample.objects.all()
    serializer_class = DurationFieldExampleSerializer


class EmailFieldExampleView(CreateAPIView, ListAPIView, RetrieveAPIView): 
    queryset = EmailFieldExample.objects.all()
    serializer_class = EmailFieldExampleSerializer


class RegexFieldExampleView(CreateAPIView, ListAPIView, RetrieveAPIView):
    queryset = RegexFieldExample.objects.all()
    serializer_class = RegexFieldExampleSerializer


class URLFieldExampleView(CreateAPIView, ListAPIView, RetrieveAPIView): 
    queryset = URLFieldExample.objects.all()
    serializer_class = URLFieldExampleSerializer


class ChoiceFieldExampleView(CreateAPIView, ListAPIView, RetrieveAPIView): 
    queryset = ChoiceFieldExample.objects.all()
    serializer_class = ChoiceFieldExampleSerializer


class MultiChoiceFieldExampleView(CreateAPIView, ListAPIView, RetrieveAPIView): 
    queryset = MultiChoiceFieldExample.objects.all()
    serializer_class = MultiChoiceFieldExampleSerializer


class ListFieldExampleView(CreateAPIView, ListAPIView, RetrieveAPIView): 
    queryset = ListFieldExample.objects.all()
    serializer_class = ListFieldExampleSerializer


class DictFieldExampleView(CreateAPIView, ListAPIView, RetrieveAPIView): 
    queryset = DictFieldExample.objects.all()
    serializer_class = DictFieldExampleSerializer


class SlugFieldExampleView(CreateAPIView, ListAPIView, RetrieveAPIView): 
    queryset = SlugFieldExample.objects.all()
    serializer_class = SlugFieldExampleSerializer


class UUIDFieldExampleView(CreateAPIView, ListAPIView, RetrieveAPIView): 
    queryset = UUIDFieldExample.objects.all()
    serializer_class = UUIDFieldExampleSerializer


class FilePathFieldExampleView(CreateAPIView, ListAPIView, RetrieveAPIView):
    queryset = FilePathFieldExample.objects.all()
    serializer_class = FilePathFieldExampleSerializer


class IPAddressFieldExampleView(CreateAPIView, ListAPIView, RetrieveAPIView):
    queryset = IPAddressFieldExample.objects.all()
    serializer_class = IPAddressFieldExampleSerializer


class JSONFieldExampleView(CreateAPIView, ListAPIView, RetrieveAPIView): 
    queryset = JSONFieldExample.objects.all()
    serializer_class = JSONFieldExampleSerializer


class FileFieldExampleView(CreateAPIView, ListAPIView, RetrieveAPIView): 
    queryset = FileFieldExample.objects.all()
    serializer_class = FileFieldExampleSerializer


class ImageFieldExampleView(CreateAPIView, ListAPIView, RetrieveAPIView): 
    queryset = ImageFieldExample.objects.all()
    serializer_class = ImageFieldExampleSerializer


class HiddenFieldExampleView(CreateAPIView, ListAPIView, RetrieveAPIView): 
    queryset = HiddenFieldExample.objects.all()
    serializer_class = HiddenFieldExampleSerializer


class ReadWriteExampleView(CreateAPIView, ListAPIView, RetrieveAPIView): 
    queryset = ReadWriteExample.objects.all()
    serializer_class = ReadWriteExampleSerializer


class MethodFieldExampleView(CreateAPIView, ListAPIView, RetrieveAPIView): 
    queryset = MethodFieldExample.objects.all()
    serializer_class = MethodFieldExampleSerializer
