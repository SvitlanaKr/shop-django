from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .services import (
    get_all_products,
    get_product_by_id,
    get_product_comments,
    get_all_categories,
    get_form_and_create_comment
)


def product_list(request: HttpRequest) -> HttpResponse:
    category = request.GET.get('category')
    return render(
        request,
        "products.html",
        {
            "products": get_all_products(category),
            "categories": get_all_categories(),
            "selected_category": category
        }
    )


def single_product(request: HttpRequest, pk: int) -> HttpResponse:
    product = get_product_by_id(pk=pk)
    form = get_form_and_create_comment(request, product)
    comments = get_product_comments(product)
    return render(
        request,
        "single_product.html",
        context={
            "product": product,
            "form": form,
            "comments": comments,
        }
    )
