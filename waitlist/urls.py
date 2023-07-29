from django.urls import include, path, re_path
from .views import WaitlistAPI
from .routers import router

urlpatterns = [
    re_path(r'^', include(router.urls)),
    path('public', WaitlistAPI.as_view(), name='public')
]
