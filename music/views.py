from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .forms import DeleteNewForm

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'music/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'music/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'music/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'music/post_edit.html', {'form': form})

# def delete_Form(request, instance):
#     #+some code to check if this object belongs to the logged in user
#     logged_user = get_logged_user_from_request(request)
#     if logged_user:
#         form = PostForm(request.GET, instance=Post.objects.get(pk=instance).delete())
#         if form.is_valid():
#             form.delete()
#             return HttpResponseRedirect('/champs') # wherever to go after deleting
#         else:
#             form = DeleteNewForm(instance=Post.objects.get(pk=instance))
#             return render(request, 'polls/delete_.html', {'form': form})
#     else:
#         form = DeleteNewForm(instance=Post.objects.get(pk=instance))
#         form.delete()

#         return render(request, 'polls/delete_form.html', {'form': form})