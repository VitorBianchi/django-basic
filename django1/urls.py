from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from core.views import error404, error500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'))
]


handler404 = error404
handler500 = error500