from audioop import reverse
from django.views import generic

from .models import BlogApp, Post

class PostList(generic.ListView):
    model = Post

class PostCreate(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDetail(generic.DetailView):
    model = Post

class PostUpdate(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDelete(generic.DeleteView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    