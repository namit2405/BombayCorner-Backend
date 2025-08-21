from django.contrib.sitemaps import Sitemap
from .models import Product, Categories


# ✅ 1. React Frontend Static Pages
class StaticReactSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        # Add all your React frontend routes here
        return [
            "/",                # Home
            "/products",        # Products listing
            "/categories",      # Categories page
            "/about",           # About page
            "/contact",         # Contact page
            "/cart",            # Cart page
            "/wishlist",        # Wishlist
            "/profile",         # User Profile
            "/edit-profile",    # Edit Profile
            "/order/history",   # Order history
            "/help",            # Customer Service chatbot/FAQ
            "/login",           # Login
            "/signup",          # Signup
        ]

    def location(self, item):
        return item


# ✅ 2. Products Sitemap (from DB)
class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Product.objects.all()

    def location(self, obj):
        return f"/products/{obj.id}/"   # React frontend product detail page


# ✅ 3. Categories Sitemap (from DB)
class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Categories.objects.all()

    def location(self, obj):
        return f"/categories/{obj.id}/"
