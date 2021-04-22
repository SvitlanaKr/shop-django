from typing import List

from django.urls import path
from django.urls.resolvers import RoutePattern

from goods.views import goods

urlpatterns: List[RoutePattern] = [
    path("goods", goods, name="Goods"),
]
