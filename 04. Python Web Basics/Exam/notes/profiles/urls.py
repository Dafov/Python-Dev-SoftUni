from notes.profiles.views import create_profile, delete_profile, profile_details
from django.urls.conf import path


urlpatterns = (
    path('profile/', profile_details, name='profile details'),
    path('create/', create_profile, name='create profile'),
    path('', delete_profile, name='delete profile'),
)
