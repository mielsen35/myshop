from django.contrib import admin

# Register your models here.
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)} # prepopulated_fields используется для того, чтобы указывать поля, значение которых устанавливается автоматически с использованием значения других полей

'''
Атрибут list_editable в классе ProductAdmin используется для того, чтобы
задать поля, которые можно редактировать, находясь на странице отображения списка на сайте администрирования. Такой подход позволит редактировать несколько строк одновременно. Любое поле в list_editable также
должно быть указано в атрибуте list_display, поскольку редактировать можно только отображаемые поля.
'''

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
