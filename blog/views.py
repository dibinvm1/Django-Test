from django.shortcuts import render, redirect
from blog.models import Post,Comment
from blog.forms import CommentForm
# Create your views here.

def blogPostsIndex(request):
    '''Method for rendering the Index page of blog Posts '''
    posts = Post.objects.all().order_by('-createdOn')
    context = {  'posts' : posts }
    return render(request, 'blogPostsIndex.html', context)

def blogPostsCategory(request, category):
    '''Method for rendering the index page with blog Posts by a category '''
    posts = Post.objects.filter(categories__name__contains=category).order_by('-createdOn')
    context = {'category' : category, 'posts' : posts }
    return render(request, "blogPostsIndex.html",context)

def blogPostDetails(request, pk):
    '''Method for rendering the page of blog Posts in detail '''
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(author=form.cleaned_data['author'],
            body=form.cleaned_data['body'],
            post=post)
            comment.save()
            return redirect('blogPostDetails',pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {'comments' : comments, 'post' : post, 'form':form, }
    return render(request, "blogPostDetails.html",context)


