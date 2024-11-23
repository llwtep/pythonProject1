from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .forms import CustomUserRegistrationForm, CustomUserLoginForm, CustomUserUpdateForm, CustomProfileUpdateForm
from .models import CustomUser
from main.models import Post


def registration(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')

    form = CustomUserRegistrationForm()

    return render(request, 'register_page.html', {'form':form})


def CustomLogin(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('main')
            else:
                messages.error(request,'Invalid credentials')
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})


class UserPostListView(ListView):
    model = Post
    template_name = 'post/user-posts.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.filter(author=self.kwargs['pk']).order_by('-created_at')


def profileView(request, pk):
    if request.method == 'POST':
        u_form = CustomUserUpdateForm(request.POST, instance=request.user)
        p_form = CustomProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        print('Files in request.FILES:', request.FILES)
        print('Image field data:', request.FILES.get('image'))
        if u_form.is_valid() and p_form.is_valid():
            print('Image to save:', p_form.instance.image)
            u_form.save()
            p_form.save()
            return redirect('profile',pk=request.user.pk)
        else:
            print('Form errors:', p_form.errors)
    else:
        u_form = CustomUserUpdateForm(instance=request.user)
        p_form = CustomProfileUpdateForm(instance=request.user.profile)


    author = get_object_or_404(CustomUser, id=pk)
    is_owner = request.user == author

    posts_list_view = UserPostListView.as_view()

    response = posts_list_view(request, pk=pk)
    posts = response.context_data['posts']

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'author': author,
        'is_owner': is_owner,
        'posts': posts
    }
    return render(request, 'profile.html', context)
