from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home,name="slide-home" ),
    path('/mark_post_as_seen',views.mark_posts_as_seen,name="mark-post" ),
    path('profiles/<slug>/',views.profile,name="profile" ),
    path('<slug>/<id>/',views.detailedpost,name="detailed-post" ),
    ]