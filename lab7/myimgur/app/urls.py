from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:image_id>', views.detail, name="detail"),
    path('<int:image_id>/comment', views.submit_comment, name="submit_comment"),
    path('comment/<int:comment_id>/approve', views.approve_comment, name="approve_comment"),
]