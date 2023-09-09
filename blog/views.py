from django.shortcuts import render, get_object_or_404
from .models import Post

def all_posts(request):
    """
    Shows all blogs
    """
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }
    return render(request, 'blog/all_posts.html', context)


def post_detail(request, pk):
    """
    Shows the blogs details
    """
    post = get_object_or_404(Post, pk=pk)
    
    context = {
        'post': post,
    }
    
    return render(request, 'blog/post_detail.html', context)


#def post_list(request):
  #  posts = Post.objects.all()
  #  return render(request, 'blog/blog.html', {'posts': posts})

#def post_detail(request, pk):
 #   post = get_object_or_404(Post, pk=pk)
  #  return render(request, 'blog/post_detail.html', {'post': post})
