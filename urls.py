from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
import os

admin.autodiscover()

from rest_framework_nested import routers
from authentication.views import UserViewSet
from authentication.views import LoginView, LogoutView

from index import index
from repositories.views import RecordViewSet, RepositoryViewSet, PropertyViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'repositories', RepositoryViewSet)
router.register(r'properties', PropertyViewSet)

repositories_router = routers.NestedSimpleRouter(router, r'repositories', lookup='repositories')
repositories_router.register(r'records', RecordViewSet)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin', include(admin.site.urls)),

    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/', include(repositories_router.urls)),

    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),

    url(r'^(?P<repository_name>[a-z]+)/oai/', include('oai.urls')),
    url(r'^(?P<repository_name>[a-z]+)/oai', include('oai.urls')),

    url(r'^oai/', include('oai.urls')),
    url(r'^oai', include('oai.urls')),
    url('^.*$', index, name='index'),
)
