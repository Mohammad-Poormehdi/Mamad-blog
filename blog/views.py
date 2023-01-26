from django.shortcuts import render
from .models import Post, Category
from .forms import CommentForm

# Create your views here.

def index(request):
    posts = Post.objects.all()
    categorys = Category.objects.all()
    return render(request, 'blog/index.html', {
        'blog_posts':posts,
        'post_categorys':categorys,
    })

def post(request, post_slug):
    comment_form = CommentForm
    selected_post = Post.objects.get(slug=post_slug)
    comments = selected_post.comment.all().order_by('-id')
    if request.method == "GET":
        return render(request, 'blog/post.html', {
            "selected_post":selected_post,
            "comment_form":comment_form,
            "comments":comments,
        })
    else:
        comment_request = CommentForm(request.POST)
        post_comment = comment_request.save()
        selected_post.comment.add(post_comment)
        return render(request, 'blog/post.html', {
            "selected_post":selected_post,
            "comment_form":comment_form,
            "comments":comments,
        })

def category(request, category_slug):
    selected_category = Category.objects.get(slug=category_slug,)
    selected_posts = Post.objects.filter(category=selected_category.id)
    return render(request, 'blog/categorys.html', {
        'post_category':selected_posts,
    })
