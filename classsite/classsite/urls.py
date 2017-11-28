"""classsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import DetailView
from classpage.models import News
from classpage.views import index, course_view, Announce_view, file_view, file_view_math, file_view_language, file_view_others
from classpage.views import uploads_file_view, uploads_success_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^news/(?P<pk>\d+)$', DetailView.as_view(
        model = News,
        template_name = "newspage.html",
    )),
    url(r'^course/$', course_view),
    url(r'^announce/$', Announce_view),
    url(r'^file/$', file_view),
    url(r'^file/math/$', file_view_math),
    url(r'^file/language/$', file_view_language),
    url(r'^file/others/$', file_view_others),
    url(r'^uploads/$', uploads_file_view),
    url(r'^uploads/success$', uploads_success_view)
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
