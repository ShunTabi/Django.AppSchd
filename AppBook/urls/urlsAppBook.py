from django.urls import path
from ..views.MyBook import MyBook

urlpatterns = [
    #####################################################################################
    path("MyBook/MyBookSEARCH", MyBook.MyBookSEARCH, name="MyBookSEARCH"),
    path("MyBook/MyBookINSERT", MyBook.MyBookINSERT, name="MyBookINSERT"),
    path("MyBook/MyBookDELETE", MyBook.MyBookDELETE, name="MyBookDELETE"),
]
