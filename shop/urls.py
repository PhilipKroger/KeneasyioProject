from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('product_create/', views.product_create, name='product_create'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/<int:id>/', views.ProductDetailView, name='product_detail'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
