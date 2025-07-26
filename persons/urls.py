from django.urls import path

from persons.views import *


urlpatterns = [
    path('char/', CharFieldExampleView.as_view()),
    path('int/', IntegerFieldExampleView.as_view()),
    path('float/', FloatFieldExampleView.as_view()),
    path('decimal/', DecimalFieldExampleView.as_view()),
    path('bool/', BooleanFieldExampleView.as_view()),
    path('date/', DateFieldExampleView.as_view()),
    path('time/', TimeFieldExampleView.as_view()),
    path('datetime/', DateTimeFieldExampleView.as_view()),
    path('duration/', DurationFieldExampleView.as_view()),
    path('email/', EmailFieldExampleView.as_view()),
    path('regex/', RegexFieldExampleView.as_view()),
    path('url/', URLFieldExampleView.as_view()),
    path('choice/', ChoiceFieldExampleView.as_view()),
    path('multi/', MultiChoiceFieldExampleView.as_view()),
    path('list/', ListFieldExampleView.as_view()),
    path('dict/', DictFieldExampleView.as_view()),
    path('slug/', SlugFieldExampleView.as_view()),
    path('uuid/', UUIDFieldExampleView.as_view()),
    path('filepath/', FilePathFieldExampleView.as_view()),
    path('ip/', IPAddressFieldExampleView.as_view()),
    path('json/', JSONFieldExampleView.as_view()),
    path('file/', FileFieldExampleView.as_view()),
    path('image/', ImageFieldExampleView.as_view()),
    path('hidden/', HiddenFieldExampleView.as_view()),
    path('readwrite/', ReadWriteExampleView.as_view()),
    path('method/', MethodFieldExampleView.as_view()),
]
