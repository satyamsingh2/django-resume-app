from django.shortcuts import render
from .models import Resume ,Post
from django.views.generic import ListView
from .forms import ContactMe

#from django.http import HttpResponse

# Create your views here.


"""def home(request):
    return HttpResponse('<h1>HOME PAGE<h1/>')"""
    
def home(request):
    return render(request, 'resume/home.html')


def about(request):
    resume=Resume.objects.get(pk=1)#to fetch our data from database
    return render(request, 'resume/about.html', {'resume': resume})

def blog(request):
    post_objects= Post.objects.all().order_by("-date")
    item_name=request.GET.get('item_name')
    if item_name != '' and item_name is not None :
        post_objects=post_objects.filter(title__icontains=item_name)
    return render(request, 'resume/blog.html', {'post_objects': post_objects})


"""class PostListView(ListView):
    model=Post
    template_name='resume/blog.html'
    context_object_name='posts'
    ordering=['-date']"""
    
def form(request):
    form=ContactMe
    return render(request, 'resume/form.html', {'form': form})