from typing import Iterable

from django.db.models.manager import BaseManager
from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from .models import Product, Comment, Category
from .forms import CommentForm


def get_all_products(category) -> Iterable[Product]:
    if category:
        return Product.objects.filter(category_id=category)
    return Product.objects.all()


def get_all_categories() -> BaseManager:
    return Category.objects.all()


def get_product_by_id(pk: int) -> Product:
    product = get_object_or_404(Product, pk=pk)

    return product


def get_form_and_create_comment(request: HttpRequest, product: Product) -> CommentForm:
    if request.method == "POST" and request.user.is_authenticated:
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.product = product
            comment.save()
            form = CommentForm()

    else:
        form = CommentForm()

    return form


def get_product_comments(product: Product, since=None) -> Iterable[Comment]:
    comments = Comment.objects.filter(product=product)
    if since is not None:
        comments = comments.filter(id__gt=since)
    return comments
