from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from profiles.views import login_view,\
    logout_view,\
    register_view, user_account, other_account, verify_user, style_list, product_delete


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', user_account, name='profile'),
    path('delete/<int:id>/', product_delete, name='product_delete'),
    path('user/<int:account_id>/', other_account, name='other_account'),
    path('verify_user/', verify_user, name='verify_user'),
    path('register/', register_view, name='register'),
    path('imagemakers/', style_list, name='style_list'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
