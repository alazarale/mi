from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.home , name='home'),
    url(r'^home/$', views.home , name='home'),
    url(r'^product/$', views.product, name='product'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^service/$', views.service, name='service'),
    url(r'^news/$', views.news, name='news'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.detail, name='detail'),
    url(r'^(?P<month>\d{2})/(?P<day>\d{2})/(?P<name>[-\w]+)/$', views.description, name='description')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)