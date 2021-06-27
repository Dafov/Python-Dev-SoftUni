from django.http.response import HttpResponseRedirect
from notes.note.models import Note
from notes.profiles.forms import CreateProfileForm
from core.profile_util import get_profile
from django.shortcuts import render, redirect

def profile_details(request):
    profile = get_profile()
    
    context = {
        'profile': profile,
    }

    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)

def delete_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        profile.delete()
        Note.objects.all().delete()
        return redirect('home')

