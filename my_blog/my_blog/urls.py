from allauth.account.views import confirm_email
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # blog app urls
    path('', include('blog.urls')),

    # blog_api app urls
    url(r'^', include('blog_api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # all-auth urls
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$',
         confirm_email, name='account_confirm_email')
]
