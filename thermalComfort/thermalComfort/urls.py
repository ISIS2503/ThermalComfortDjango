from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', admin.site.urls),
    url(r'^sql/', include('dashboard.urls')),
    url(r'^nosql/', include('dashboard_nosql.urls')),
]
