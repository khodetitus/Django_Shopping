from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Titus_store API",
        default_version='v1.0.0',
        description="this is watch store api",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="masoudpro2@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
admin.site.site_header = "Watch Store Admin"
admin.site.site_title = "Watch Store Admin Portal"
admin.site.index_title = "Welcome to Watch Store Admin Portal"

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('products.urls', namespace='products')),
                  path('customers/', include('customers.urls', namespace='customers')),
                  path('orders/', include('orders.urls', namespace='orders')),
                  path('api/auth/', include('djoser.urls')),
                  path('api/auth/', include('djoser.urls.authtoken')),
                  path('api/v1/', include('API.urls', namespace='API')),
                  re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
                          name='schema-json'),
                  re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
