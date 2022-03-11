from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import PostCreateForm
from .models import Post

# Create your views here.
class BlogListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        context = {
            "posts":posts
        }
        return render(request, "blog_list.html", context)

class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        form = PostCreateForm()
        context = {
            "form":form
        }
        return render(request, "blog_create.html", context)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = PostCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get("title")
                content = form.cleaned_data.get("content")
                date = form.cleaned_data.get("date")

                post, created = Post.objects.get_or_create(title=title, content=content, date=date)
                post.save()

                return redirect("blog:home")

class BlogEditView(View):
    def get(self, request, *args, **kwargs):
        post = Post.objects.get(id=kwargs["id"])
        context = {
            "post":post
        }
        return render(request, "blog_edit.html", context)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = PostCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get("title")
                content = form.cleaned_data.get("content")
                date = form.cleaned_data.get("date")

                post = Post.objects.get(id=kwargs["id"])
                post.title=title
                post.content=content
                post.date=date
                post.save()

                return redirect("blog:home")

class BlogDeleteView(View):
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            post = Post.objects.get(id=kwargs["id"])
            post.delete()

        return redirect("blog:home")
