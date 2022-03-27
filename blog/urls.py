from django.urls import path
from blog.views import PostList, PostDetail

urlpatterns = [
    path("", PostList.as_view(), name="post_list"),
    path(
        "Post/<int:pk>/",
        PostDetail.as_view(),
        name="post_detail",
    ),
]
