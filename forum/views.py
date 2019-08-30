from django.shortcuts import render
from .models import Forum, Comment
from .form import ForumForm
from django.urls import reverse

# Create your views here.
def index(request):
    if request.method = 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            f = form.save()
            forum_id = f.pk
            return HttpResponseRedirect(reverse("forum", args=forum_id))

    form = ForumForm()
    context = {
        "forums": Forum.object.all(),
        "form": form
    }
    return render(request, "forum/index.html", context)

def forum(request, forum_id):
    try:
        forum = Forum.objects.get(pk=forum_id)
    except: Forum.DoesNotExist:
        raise Http404("Forum does not exist")
    context = {
    "forum": forum,
    }
    return render(request, "forum/forum.html", context)

def comment(request, forum_id):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    comment_text = request.POST["comment"]
    f = Forum.object.get(pk=forum_id)
    c = Comment(forum=f, desc=comment_text)
    c.save()
    return HttpResponseRedirect(reverse("forum", args=(forum_id)))
