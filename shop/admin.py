from django.contrib import admin
from parler.admin import TranslatableAdmin

# Register your models here.
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'slug']

    # prepopulated_fields = {'slug': ('name',)}  prepopulated_fields используется для того, чтобы указывать поля, значение которых устанавливается автоматически с использованием значения других полей

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}


'''
Атрибут list_editable в классе ProductAdmin используется для того, чтобы
задать поля, которые можно редактировать, находясь на странице отображения списка на сайте администрирования. Такой подход позволит редактировать несколько строк одновременно. Любое поле в list_editable также
должно быть указано в атрибуте list_display, поскольку редактировать можно только отображаемые поля.
'''


@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']

    # prepopulated_fields = {'slug': ('name',)}
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}
