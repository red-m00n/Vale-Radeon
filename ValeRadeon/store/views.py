from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from store.models import Cart, Order, Product

# Create your views here.

def index(request):
    products = Product.objects.all()

    return render(request , 'store/index.html', context={"products": products} )

def product_details(request,slug):
    product = get_object_or_404(Product,slug=slug)
    return render(request , 'store/product_details.html',context={"product": product} )

def add_to_cart(request,slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)

    order, created = Order.objects.get_or_create(user=user, product=product)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.qte += 1 
        order.save()

    return redirect(reverse("product", kwargs={"slug": slug}))

def cart(request):
    orders = Order.objects.filter(user=request.user)
    
    # Calculate the total price
    total_price = sum(order.product.price * order.qte for order in orders)
    
    context = {
        'orders': orders,
        'total_price': total_price,
    }
    
    cart = get_object_or_404(Cart, user=request.user)
    context["orders"] = cart.orders.all()  # Add this line to update the orders in the context
    return render(request, 'store/cart.html', context)

def delete_cart(request):
    if cart := request.user.cart:
        cart.orders.all().delete()
        cart.delete()

    return redirect(reverse('index'))

def checkout(request):
    return render(request, 'store/checkout.html')

def confirmation(request):
    return render(request, 'store/shippingpage.html')