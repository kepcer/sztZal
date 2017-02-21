"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib import admin
from testin import views as testin_views
from lep import views as lep_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', lep_views.index, name='index'),
    url(r'^index/$', lep_views.index, name='index'),
    url(r'^warmachine_players/', lep_views.warmachine_players, name='warmachine_players'),
    url(r'^available_games/', lep_views.available_games, name='available_games'),
    url(r'^news/', lep_views.news, name='news'),
    url(r'^members/', lep_views.members, name='members'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^account/', lep_views.account, name='account'),
    url(r'^add_game/', lep_views.add_game, name='add_game'),
    url(r'^add_photo/', lep_views.add_photo, name='add_photo'),
    url(r'^photos/', lep_views.photos, name='photos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)