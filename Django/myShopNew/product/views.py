from django.shortcuts import render

from .models import *

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request

from django.template.loader import render_to_string


# Create your views here.


def product_detail(request, id, slug):
    query = request.GET.get('q')

    category = Categorie.objects.all()

    product = Product.objects.get(pk=id)
    related_products = Product.objects.filter(
        category=product.category).exclude(pk=id)

    images = Image.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id, status='True')

    context = {'product': product, 'category': category,
               'images': images, 'comments': comments,
               'related_products': related_products,
               }

    if product.variant_type != "None":  # Product have variants
        if request.method == 'POST':  # if we select color
            variant_id = request.POST.get('variantid')
            # selected product by click color radio
            variant = Variant.objects.get(id=variant_id)
            colors = Variant.objects.filter(
                product_id=id, size_id=variant.size_id)
            sizes = Variant.objects.raw(
                'SELECT * FROM product_variant WHERE product_id=%s GROUP BY size_id', [id])
            query += variant.title+' Size:' + \
                str(variant.size) + ' Color:' + str(variant.color)
        else:
            variants = Variant.objects.filter(product_id=id)
            colors = Variant.objects.filter(
                product_id=id, size_id=variants[0].size_id)
            # colors = Color.objects.filter(id=variant_colors)
            print("ghg", colors)
            sizes = Variant.objects.raw(
                'SELECT * FROM product_variant WHERE product_id=%s GROUP BY size_id', [id])
            variant = Variant.objects.get(id=variants[0].id)

        context.update({'sizes': sizes, 'colors': colors,
                        'variant': variant, 'query': query
                        })

    return render(request, 'product_detail.html', context)


def ajaxcolor(request):
    data = {}
    if request.POST.get('action') == 'post':
        size_id = request.POST.get('size')
        productid = request.POST.get('productid')
        colors = Variant.objects.filter(product_id=productid, size_id=size_id)
        context = {
            'size_id': size_id,
            'productid': productid,
            'colors': colors,
        }
        data = {'rendered_table': render_to_string(
            'color_list.html', context=context)}
        return JsonResponse(data)
    return JsonResponse(data)
