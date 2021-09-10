from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate as auth, login
from django.views.decorators.csrf import csrf_protect
from django.views.generic import DetailView
from django.forms.utils import ErrorList
from django.contrib.auth.models import User
from .forms import LoginForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

from .forms import ProfileForm, form_validation_error
from .models import Profile

@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileView(View):
    profile = None

    def dispatch(self, request, *args, **kwargs):
        self.profile, __ = Profile.objects.get_or_create(user=request.user)
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = {'profile': self.profile, 'segment': 'profile'}
        return render(request, 'user/profile.html', context)

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=self.profile)

        if form.is_valid():
            profile = form.save()
            profile.user.first_name = form.cleaned_data.get('first_name')
            profile.user.last_name = form.cleaned_data.get('last_name')
            profile.user.email = form.cleaned_data.get('email')
            profile.user.save()

            messages.success(request, 'Profile saved successfully')
            return redirect('profile')
        else:
            messages.error(request, form_validation_error(form))
            return redirect('profile')

class ProfileDetailView(DetailView):
    model = User
    template_name = 'user/settings.html'
    context_object_name = 'us'

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = auth(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "user/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = auth(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            return redirect('login')

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "user/register.html", {"form": form, "msg": msg, "success": success})

def ui_modals(request):
    return render(request, "user/ui-modals.html")