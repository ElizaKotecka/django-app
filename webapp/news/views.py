from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView

from .models import Posts
from .forms import PostsForm

# Create your views here.

def marketplace_home(request):
    news = Posts.objects.all().order_by('-published_at')
    return render(request, 'news/index.html', {'news': news})

def marketplace_create(request):
    error = ''

    if request.method == 'POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Submitted form contain errors'

    form = PostsForm()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'news/create.html', data)

class NewsDetailView(DetailView):
    model = Posts
    template_name = 'news/show.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Posts
    template_name = 'news/update.html'
    form_class = PostsForm

class NewsDeleteView(DeleteView):
    model = Posts
    template_name = 'news/delete.html'
    success_url = '/news/'