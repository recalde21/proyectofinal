from django.urls import path
from perfiles.views import profile, editprofile

urlpatterns = [
    path('', profile, name="profile"),
    path('editprofile', editprofile, name="editprofile"),
]