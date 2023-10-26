from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Bags, Category


class BagsAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Bags
        fields = '__all__'


class BagsAdmin(admin.ModelAdmin):
    form = BagsAdminForm
    list_display = ('id', 'title', 'category', 'added_at', 'updated_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    fields = ('title', 'category', 'description','photo', 'get_photo','is_published','views', 'added_at', 'updated_at')
    readonly_fields = ('get_photo', 'views', 'added_at', 'updated_at')
    save_on_top = True

    def get_photo(self,obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=40>')

    get_photo.short_description= 'Фото'
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Bags, BagsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.site_header='Керування LIMA LIMA'