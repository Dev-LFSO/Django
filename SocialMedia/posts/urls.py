from django.urls import path
from .views import all_posts, like_post

app_name = 'posts'

urlpatterns = [
    path('', all_posts, name='all_posts'),
    path('<int:post_id>/', like_post, name='like_post')
]