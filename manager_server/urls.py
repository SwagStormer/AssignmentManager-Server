"""manager_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from rest_framework import routers
from rest_framework.authtoken import views
from assignment.views import CourseViewSet, TaskViewSet, MyUserViewSet, VersionViewSet
from bell.views import ScheduleViewSet, PeriodViewSet, DateViewSet
from schoolpage.views import AnnouncementViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'users', MyUserViewSet)
router.register(r'version', VersionViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'periods', PeriodViewSet)
router.register(r'announcements', AnnouncementViewSet)
router.register(r'dates', DateViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'api/', include(router.urls))
]

