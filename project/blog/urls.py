from django.urls import path, re_path

from blog.views import blog_view, blog_info, PostView

urlpatterns = [
    path('', PostView.as_view()),
    re_path('(?P<pk>\d+)/', blog_view),
    path('info/', blog_info),
]
