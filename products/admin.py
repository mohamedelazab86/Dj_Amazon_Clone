from django.contrib import admin
from .models import ProdImage,Product,Brand,Review
from django_summernote.admin import SummernoteModelAdmin


# customize in line
class Productimageunline(admin.TabularInline):
    model =ProdImage

# customize data

class Productadmin(SummernoteModelAdmin):
    list_display=['name','flag','sku','price']
    list_filter=['price','name']
    search_fields=['name']
    summernote_fields = ('subtitle','description')
    inlines=[Productimageunline]



# Register your models here.
admin.site.register(Product,Productadmin)
admin.site.register(ProdImage)
admin.site.register(Brand)
admin.site.register(Review)