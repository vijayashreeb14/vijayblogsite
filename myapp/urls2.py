from django.urls import path
from . import views

urlpatterns = [
    # Existing URLs
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/save/', views.save_post, name='save_post'),
]