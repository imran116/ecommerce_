from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Menu(models.Model):
    menu_name = models.CharField(max_length=30)
    html_page = models.CharField(max_length=100, default=False, blank=True,
                                 help_text="Enter the HTML page name without extension (e.g.,'/about' for 'about.html')")

    is_active = models.BooleanField(default=True)
    is_menu = models.BooleanField(default=True)

    def __str__(self):
        return self.menu_name


class MainBanner(models.Model):
    banner_category_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='mainBanners/')
    title = models.CharField(max_length=20)
    short_desc = models.CharField(max_length=100)
    html_page = models.CharField(max_length=100,
                                 help_text="Enter the HTML page name without extension (e.g.,'/about' for 'about.html')")

    def __str__(self):
        return self.banner_category_name


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_short_desc = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name

    @property
    def get_addCategoryItems(self):
        return self.addcategoryitem_set.filter(is_display=True)  # show only display true value in Add-category section


class AddCategoryItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='categoryProducts/')
    title = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, default=0.00, decimal_places=2)
    is_display = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.category.category_name}---{self.title}"


class Explore(models.Model):
    title = models.CharField(max_length=150)
    paragraph_one = models.TextField()
    paragraph_two = models.TextField()
    paragraph_three = models.TextField()
    quote = models.TextField()

    def __str__(self):
        return self.title


class ExploreProducts(models.Model):
    first_product_title = models.CharField(max_length=100)
    first_product_subtitle = models.CharField(max_length=100)
    first_product_image = models.ImageField(upload_to='explore-products/')

    second_product_title = models.CharField(max_length=100)
    second_product_subtitle = models.CharField(max_length=100)
    second_product_image = models.ImageField(upload_to='explore-products/')

    def __str__(self):
        return self.first_product_title


class SocialMediaSection(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.TextField()

    def __str__(self):
        return self.title


class SocialMediaItem(models.Model):
    title = models.CharField(max_length=50)
    instagram_link = models.CharField(max_length=250)
    image = models.ImageField(upload_to='social-media-products/')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Subscriber(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)

    def __str__(self):
        return self.email


# About-us Section start
class AboutUsMainSection(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='about-us/')
    paragraph_one = models.TextField()
    paragraph_two = models.TextField()
    quote = models.TextField()

    def __str__(self):
        return self.title


class AboutUsTeamSection(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='about-us-teamMember/')
    facebook_link = models.CharField(max_length=150)
    twitter_link = models.CharField(max_length=150)
    linkedin_link = models.CharField(max_length=150)
    behance_link = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class AboutUsServiceSection(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='about-us-service/')

    def __str__(self):
        return self.title
# About-us Section End here

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(AddCategoryItem, through='CartItem')


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(AddCategoryItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)