from django.contrib import admin

from website.models import Menu, MainBanner, Category, AddCategoryItem, Explore, ExploreProducts, SocialMediaSection, \
    SocialMediaItem, Subscriber, AboutUsMainSection, AboutUsTeamSection, AboutUsServiceSection

# Register your models here.

admin.site.register(Menu),
admin.site.register(MainBanner),
admin.site.register(Category),
admin.site.register(AddCategoryItem),
admin.site.register(Explore),
admin.site.register(ExploreProducts),
admin.site.register(SocialMediaSection),
admin.site.register(SocialMediaItem),
admin.site.register(Subscriber),
admin.site.register(AboutUsMainSection),
admin.site.register(AboutUsTeamSection),
admin.site.register(AboutUsServiceSection),
