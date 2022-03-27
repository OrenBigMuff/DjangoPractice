from django.views.generic import ListView, DetailView
from blog.models import Post


class PostList(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"


# DetailViewを継承したクラスで記述する中身はListViewと変わらない
class PostDetail(DetailView):
    model = Post
    context_object_name = "post"
