import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from .forms import PostCreateForm
from .models import Post, LikesOfThePost
from django.views.generic.list import ListView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
import requests
from django.contrib import messages
def weatherPageView(request):
    API = '05404a89baafe78fce493e958535794c'
    city_name = 'Tashkent'
    description = ''
    temp = ''
    humidity = ''
    speed = ''

    try:
        if request.method == 'POST':
            city_name = request.POST.get('city_name_input').strip().capitalize()
        data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API}&units=metric')
        weather = json.loads(data.text)
        description = str(weather['weather'][0]['description'])
        temp = str(round(weather['main']['temp'],1))
        humidity = str(weather['main']['humidity'])
        speed = str(weather['wind']['speed'])
    except Exception:
        messages.add_message(request, messages.ERROR, 'Error please enter city name correctly')

    context = {
        'description':description,
        'temp':temp,
        'speed':speed,
        'humidity':humidity,
        'city_name':city_name,
    }
    return render(request, 'main/weather-page.html', context)


class PostListView(ListView):
    model = Post
    ordering = ['-created_at']
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

@login_required
def PostCreationView(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('main')
    else:
        form = PostCreateForm()
    return render(request, 'posts/post-create.html', {'form': form})



class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('main')
    template_name = 'posts/post_confirm_delete.html'
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

@login_required
def LikePostView(request):
    post_id = request.GET.get('post_id')
    user = request.user
    like_filter = LikesOfThePost.objects.filter(post=post_id,user=user).first()
    post = get_object_or_404(Post, id=post_id)
    if like_filter is None:
        new_like = LikesOfThePost.objects.create(post=post_id, user=user)
        new_like.save()
        post.count_of_likes=post.count_of_likes+1
        post.save()
    else:
        post.count_of_likes=post.count_of_likes-1
        post.save()
        like_filter.delete()

    return redirect(request.META.get('HTTP_REFERER', '/'))


