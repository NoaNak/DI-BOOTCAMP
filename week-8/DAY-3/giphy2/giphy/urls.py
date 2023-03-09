from django.contrib import admin
from django.urls import path
from gif_app.views import homepage, category, categories

urlpatterns = [
    path("admin/", admin.site.urls),
    path("homepage/", homepage, name="homepage"),
    path("category/<int:id>", category, name="category"),
    path("categories/", categories)
]

