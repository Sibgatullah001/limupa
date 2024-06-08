from django.urls import path
from limupapp.views import AboutUs, BlogDetailsLeftSidebar, Error, Index

urlpatterns = [
    path('',Index.as_view(), name='index'),
    path('error/',Error.as_view(), name='error'),
    path('about-us/',AboutUs.as_view(), name='about-us'),
    path('blog-details-left-sidebar/',BlogDetailsLeftSidebar.as_view(), name='blog-details-left-sidebar'),
    path('blog-details-left-sidebar/',BlogDetailsLeftSidebar.as_view(), name='blog-details-left-sidebar'),
]
