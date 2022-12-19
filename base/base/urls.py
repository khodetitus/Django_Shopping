from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Watch Store Admin"
admin.site.site_title = "Watch Store Admin Portal"
admin.site.index_title = "Welcome to Watch Store Admin Portal"

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('products.urls', namespace='products')),
                  path('customers/', include('customers.urls', namespace='customers')),
                  path('orders/', include('orders.urls', namespace='orders')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
