from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('<slug:post_slug>/', views.post, name='post_details'),
    path('categorys/<slug:category_slug>', views.category, name='category'),
]
