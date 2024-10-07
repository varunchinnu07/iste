from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('payment/<int:team_id>/', views.payment, name='payment'),
    path('success/', views.payment_success, name='payment_success'),
]
# urlpatterns = [
#     # your existing URL patterns
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)