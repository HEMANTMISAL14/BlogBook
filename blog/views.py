from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post, Category
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def home(request):
    # Load all the post from db(10)
    posts = Post.objects.all()[:11]
    # print(post)

    cats = Category.objects.all()

    data = {
        'posts': posts,
        'cats': cats
    }
    return render(request, 'home.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    # print(post)
    return render(request, 'posts.html', {'post': post, 'cats': cats})


def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "category.html", {'cat': cat, 'posts': posts})


class addpost(CreateView):
    model = Post
    template_name = 'add_post.html'
    success_url = reverse_lazy('home')
    fields = '__all__'


class updatepost(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = '__all__'
    success_url = reverse_lazy('home')


class deletepost(DetailView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class addcategory(CreateView):
    model = Category
    template_name = 'add_cat.html'
    fields = '__all__'
    success_url = reverse_lazy('home')
