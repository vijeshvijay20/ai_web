from django.contrib import admin
from django.urls import path, include
from web_page import routing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web_page.urls')),  # Include web_page app's URLs
    path('ws/', include(routing.websocket_urlpatterns)),
]
