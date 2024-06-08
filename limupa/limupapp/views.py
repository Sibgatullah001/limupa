from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

# ------------------------- index ______
class Index(TemplateView):
    template_name = 'limupapp/index.html'

# ------------------------- 404 ______
class Error(TemplateView):
    template_name = 'limupapp/404.html'

# ------------------------- about-us ______
class AboutUs(TemplateView):
    template_name = 'limupapp/about-us.html'

# ------------------------- blog-details-left-sidebar ______
class BlogDetailsLeftSidebar(TemplateView):
    template_name = 'limupapp/blog-details-left-sidebar.html'

# ------------------------- blog-left-sidebar ______
class BlogLeftSidebar(TemplateView):
    template_name = 'limupapp/blog-left-sidebar.html'

# ------------------------- cart ______
class Cart(TemplateView):
    template_name = 'limupapp/cart.html'

# ------------------------- checkout ______
class Checkout(TemplateView):
    template_name = 'limupapp/checkout.html'

# ------------------------- compare ______
class Compare(TemplateView):
    template_name = 'limupapp/compare.html'

# ------------------------- contact ______
class Contact(TemplateView):
    template_name = 'limupapp/contact.html'

# ------------------------- faq ______
class Faq(TemplateView):
    template_name = 'limupapp/faq.html'

# ------------------------- login-register ______
class loginRegister(TemplateView):
    template_name = 'limupapp/login-register.html'

# ------------------------- shop-left-sidebar ______
class ShopLeftSidebar(TemplateView):
    template_name = 'limupapp/shop-left-sidebar.html'

# ------------------------- single-product ______
class SingleProduct(TemplateView):
    template_name = 'limupapp/single-product.html'

# ------------------------- Wishlist ______
class Wishlist(TemplateView):
    template_name = 'limupapp/wishlist.html'