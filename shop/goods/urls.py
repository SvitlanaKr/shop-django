from typing import List

from django.urls import path
from django.urls.resolvers import RoutePattern
from django.contrib.staticfiles.urls import static
from django.conf import settings

from .views import product_list, single_product

urlpatterns: List[RoutePattern] = [
    path("list/", product_list, name="all_products"),
    path("<int:pk>/", single_product, name="product_details"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
