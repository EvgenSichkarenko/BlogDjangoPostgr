from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug')


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug')


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Posts
        fields = '__all__'


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug', 'views', 'created_at', 'category', 'get_photo')
    readonly_fields = ('views',)
    save_on_top = True
    save_as = True
    list_filter = ('category', 'tags')
    list_display_links = ('title', 'slug')

    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" width=150>')


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')


@admin.register(EmailSubs)
class EmailSubscribers(admin.ModelAdmin):
    list_display = ('email', 'created_at')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('username', 'context', 'created_at', 'category')
