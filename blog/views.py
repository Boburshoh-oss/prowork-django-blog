from django.http.response import HttpResponseRedirect,HttpResponse
from django.shortcuts import redirect, render,reverse
from .models import Post,Tag
from django.views.generic import View
from .mixins import ObjectListView
from django.db.models import Count
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

class PostList(ObjectListView,View):
    model=Post
    template='index.html'
    queryset=Post.objects.all()
def index(request):
    posts=Post.objects.all()
    return render(request,"index.html",context={"posts":posts})


def post_detail_view(request,slug):
    post=Post.objects.get(slug__iexact=slug)
    return render(request,"post_detail.html",context={"post":post})


def get_tags(request):
    tags=Tag.objects.annotate(posts_count=Count('posts'))
    return render(request,"tags.html",context={"tags":tags})
# class GetTagsViews(ObjectListView,View):
#     model=Tag
#     template='tags.html'
#     queryset=Tag.objects.annotate(posts_count=Count('posts'))

def tag_detail_view(request,slug):
    tag=Tag.objects.get(slug__iexact=slug)
    return render(request,'tag_detail.html',context={'tag':tag})

#create post list
@login_required(login_url='/admin/')
def post_create_view(request):
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=Post.objects.create(**form.cleaned_data)
            return redirect('post_detail', slug=post.slug)
    form=PostForm()
    return render(request,'create_post.html',context={'form':form})

def delete_post(request,pk):
    print(request.method,"metod kelishi kerak")
    post=get_object_or_404(Post,pk=pk).delete()
    print(post,"post keldimi")
    return redirect("index")