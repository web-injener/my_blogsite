from django.shortcuts import render,redirect
from .models import Post
from .forms import CommentForm
# Create your views here.
def home(request):
    post = Post.objects.all()

    form = CommentForm(request.POST or None)
    if request.method == 'POST'and form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'post': post,
        'form': form
    }
    return render(request,'index.html',context)