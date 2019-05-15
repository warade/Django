from django.conf.urls import url, include
from django.contrib import admin
from .views import home, redirect_somewhere
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^redirect/$', redirect_somewhere, name='redirect_somewhere'),
    url(r'^blog/', include('blog.urls', namespace = 'blog')),
]
