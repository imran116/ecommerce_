from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.core.paginator import Paginator

from website import forms
from website.models import Menu, MainBanner, Category, AddCategoryItem, Explore, ExploreProducts, SocialMediaSection, \
    SocialMediaItem, AboutUsServiceSection, AboutUsTeamSection, AboutUsMainSection, Cart, CartItem


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menus'] = Menu.objects.filter(is_menu=True, is_active=True)
        context['mainBanners'] = MainBanner.objects.all()
        context['categoryLists'] = Category.objects.filter(is_active=True)
        context['explores'] = Explore.objects.get()
        context['exploresProducts'] = ExploreProducts.objects.get()
        context['socialMediaSections'] = SocialMediaSection.objects.get()
        context['socialMediaItems'] = SocialMediaItem.objects.filter(is_active=True)

        return context


def get_women_product(request):
    menus = Menu.objects.filter(is_menu=True, is_active=True)
    category_name = Category.objects.get(category_name='Women')
    women_item = AddCategoryItem.objects.filter(category=category_name)
    paginator = Paginator(women_item, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'itemObjects': page_obj,
        'menus': menus

    }
    return render(request, 'products.html', context)


# def get_women_product(request):
#     menus = Menu.objects.filter(is_menu=True, is_active=True)
#     category_name = Category.objects.get(category_name='Women')
#     women_item = AddCategoryItem.objects.filter(category=category_name)
#     context = {
#         'itemObjects': women_item,
#         'menus': menus
#
#     }
#     return render(request, 'products.html', context)


def get_men_product(request):
    menus = Menu.objects.filter(is_menu=True, is_active=True)
    category_name = Category.objects.get(category_name='Men')
    men_item = AddCategoryItem.objects.filter(category=category_name)
    paginator = Paginator(men_item, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'itemObjects': page_obj,
        'menus': menus

    }
    return render(request, 'products.html', context)


def get_kid_product(request):
    menus = Menu.objects.filter(is_menu=True, is_active=True)
    category_name = Category.objects.get(category_name='Kid')
    kid_item = AddCategoryItem.objects.filter(category=category_name)
    paginator = Paginator(kid_item, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'itemObjects': page_obj,
        'menus': menus

    }
    return render(request, 'products.html', context)


def get_accessories_product(request):
    menus = Menu.objects.filter(is_menu=True, is_active=True)
    category_name = Category.objects.get(category_name='Accessories')
    accesories_item = AddCategoryItem.objects.filter(category=category_name)
    paginator = Paginator(accesories_item, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'itemObjects': page_obj,
        'menus': menus

    }
    return render(request, 'products.html', context)


def get_all_products(request):
    menus = Menu.objects.filter(is_menu=True, is_active=True)
    all_category_product = AddCategoryItem.objects.all()
    context = {
        'itemObjects': all_category_product,
        'menus': menus
    }
    return render(request, 'products.html', context)


# Product Details Section Start
class ProductsDetails(View):
    def get(self, request, product_id):
        product = AddCategoryItem.objects.get(id=product_id)
        context = {
            'product': product,
            'menus': Menu.objects.filter(is_menu=True, is_active=True)
        }
        return render(request, 'single-product.html', context=context)


# Product Details Section End
class BuyProducts(View):
    def post(self, request, product_id):
        product = AddCategoryItem.objects.get(id=product_id)
        quantity = request.POST.get('quantity')

        total_price = product.price * int(quantity)
        context = {
            'quantity': quantity,
            'total_price': total_price,
            'product': product,
            'menus': Menu.objects.filter(is_menu=True, is_active=True)
        }
        return render(request, 'buy-product.html', context=context)



# Product

class SubscriberView(View):
    def post(self, request):
        form = forms.SubscriberForms(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Subscribe Successful. Thank you")
        else:
            messages.error(request, "Invalid Email Use different one!")

        return redirect('/')


def get_aboutus_section(request):
    menus = Menu.objects.filter(is_menu=True, is_active=True)

    context = {
        'menus': menus,
        'aboutUsMainSection': AboutUsMainSection.objects.get(),
        'aboutUsTeamSection': AboutUsTeamSection.objects.all(),
        'aboutUsServiceSections': AboutUsServiceSection.objects.all(),
    }
    return render(request, 'about.html', context)


# Login and Signup Section Start here

class get_register_view(View):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        form = forms.RegisterForm(data=request.POST)

        password = form.data['password']
        confirm_password = form.data['confirm_password']
        if password == confirm_password:
            if form.is_valid():
                password = form.data['password']
                user = form.save()
                user.set_password(password)
                user.save()
                messages.success(request, "SignUp Successful.")
                return redirect('login')
            else:
                messages.error(request, "Invalid Credentials")
                return render(request, 'register.html' , {'form':form})
        else:
            messages.error(request, "Confirm Password Wrong")
            return render(request, 'register.html', {'form': form})

        return render(request, 'register.html', {'form': form})


class get_login_view(View):
    def get(self,request):
        return render(request, 'login.html')

    def post(self,request):

        form = forms.LoginForm(data=request.POST)
        if form.is_valid():
            username = form.data['username']
            password = form.data['password']

            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    login(request,user)
                    return redirect('home')
                else:
                    messages.error(request, "Password Not match!")
                    return render(request, 'login.html', {'form': form})
            except ObjectDoesNotExist:
                messages.error(request, "User Not Found!")
                return render(request, 'login.html', {'form': form})
        else:
            messages.error(request, "User Not Found!")
            return render(request, 'login.html', {'form': form})

# Login and Signup Section End here


def add_to_cart(request, product_id):
    product = AddCategoryItem.objects.get(pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('home')

def cart_view(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cartitem_set.all()
    return render(request, 'cart.html', {'cart_items': cart_items})

def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(CartItem, id=cart_id, cart__user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_view')
