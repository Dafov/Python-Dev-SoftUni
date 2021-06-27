from notes.note.models import Note
from notes.profiles.models import Profile

def get_profile():
    profile = Profile.objects.first()
    if profile:
        notes = Note.objects.all()
        profile.all_notes = len(notes)
    return profile