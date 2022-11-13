from django.urls import path
from ..views.Note import Note

urlpatterns = [
    #####################################################################################
    path("Note/NoteSELECT", Note.NoteSELECT, name="NoteSELECT"),
    path("Note/NoteINSERT", Note.NoteINSERT, name="NoteINSERT"),
    # path("Note/NoteDELETE", Note.NoteDELETE, name="NoteDELETE"),
]
