from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .services import (
    get_all_products,
    get_product_by_id,
    get_form_and_create_comment,
    get_product_comments,
)


def product_list(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "products.html",
        {
            "products": get_all_products(request.GET.get('category')),
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
