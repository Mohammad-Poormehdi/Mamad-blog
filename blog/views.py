from django.shortcuts import render
from .models import Post, Category, PostComment
from .forms import AddComment
# Create your views here.

def index(request):
    posts = Post.objects.all()
    categorys = Category.objects.all()
    return render(request, 'blog/index.html', {
        'blog_posts':posts,
        'post_categorys':categorys,
    })

def post(request, post_slug):
        comment_form = AddComment()
        selected_post = Post.objects.get(slug=post_slug)
        post_comment = PostComment.objects.value('comment')
        return render(request, 'blog/post.html',{
            'post':selected_post,
            'post_found':True,
            'comment_form':comment_form,
            'post_comment': post_comment,
        })
            

def category(request, category_slug):
    selected_category = Category.objects.get(slug=category_slug,)
    selected_posts = Post.objects.filter(category=selected_category.id)
    return render(request, 'blog/categorys.html', {
        'post_category':selected_posts,
    })
