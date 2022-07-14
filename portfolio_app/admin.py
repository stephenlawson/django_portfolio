from django.contrib import admin

# Register your models here.

from .models import Photo, Category, Contact, ContactPhoto, Project, Tag, PhotoIndex, PortfolioIndex

admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Contact)
admin.site.register(ContactPhoto)
admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(PhotoIndex)
admin.site.register(PortfolioIndex)