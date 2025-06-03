from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from marketplace.models import Posts


# Create your views here.
def dashboard_home(request):
    posts = Posts.objects.all().order_by('-published_at')
    return render(request, 'dashboard/index.html', {'posts': posts})