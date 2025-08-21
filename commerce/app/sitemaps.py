from django.contrib.sitemaps import Sitemap
from .models import Product, Categories

FRONTEND_DOMAIN = "https://namits.shop"  # 👈 your real frontend


# ✅ 1. React Frontend Static Pages
class StaticReactSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return [
            "", "products", "categories", "about", "contact",
            "cart", "wishlist", "profile", "edit-profile",
            "order/history", "help", "login", "signup"
        ]

    def location(self, item):
        return f"{FRONTEND_DOMAIN}/{item}" if item else FRONTEND_DOMAIN



# ✅ 2. Products Sitemap (from DB)
class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Product.objects.all()

    def location(self, obj):
        return f"{FRONTEND_DOMAIN}/products/{obj.id}/"


# ✅ 3. Categories Sitemap (from DB)
class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Categories.objects.all()

    def location(self, obj):
        return f"{FRONTEND_DOMAIN}/categories/{obj.id}/"
