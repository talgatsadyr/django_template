from django.urls import path, include
from django.views.generic import TemplateView

from django.conf import settings
from users.views import register, user_login, password_reset, password_reset_confirm, password_reset_invalid, \
    password_reset_complete

urlpatterns = [
    path('register/', register, name='register'),
    path('', user_login, name='user_login'),
    path('password_reset/', password_reset, name='password_reset'),
    path('password_reset_confirm/', password_reset_confirm, name='password_reset_confirm'),
    path('password_reset_invalid/', password_reset_invalid, name='password_reset_invalid'),
    path('password_reset_complete/', password_reset_complete, name='password_reset_complete'),

]

if settings.DEBUG:
    import os
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)