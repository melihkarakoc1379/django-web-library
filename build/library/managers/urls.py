from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'add/book/$', ImageUploadView, name='add-book'),

]
