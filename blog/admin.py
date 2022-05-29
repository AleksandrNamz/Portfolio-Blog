from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


from .models import *


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    """Создание и редактирование повесток на администраторском сайте"""
    list_display = ['id', 'title', 'category', 'get_photo', 'author',  'created_at', 'views']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'content', 'category', 'tags']
    list_filter = ['tags', 'category']
    fields = ('title', 'slug', 'category', 'tags', 'content', 'photo', 'get_photo', 'author',  'created_at', 'views')
    readonly_fields = ('views', 'get_photo', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    form = PostAdminForm
    save_as = True
    save_on_top = True

    def get_photo(self, picture):
        if picture.photo:
            return mark_safe(f'<img src={picture.photo.url} width="75">')
        return 'нет фото'

    get_photo.short_description = 'изображение'


class CategoryAdmin(admin.ModelAdmin):
    """Отображает категории на администраторском сайте"""
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    """Отображает ярлыки на администраторском сайте"""
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)

admin.site.site_title = 'Управление весточками'
admin.site.site_header = 'Управление весточками'