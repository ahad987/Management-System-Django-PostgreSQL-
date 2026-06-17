from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AuthenticationApp.urls')),
    path('employee/', include('EmployeeApp.urls')),
    path('std/', include('StudentApp.urls')),
    path('prd/', include('ProductApp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)