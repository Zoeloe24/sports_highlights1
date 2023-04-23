from django.contrib import admin

# Register your models here.
from .models import Videos, About, Articles

class VideosAdmin(admin.ModelAdmin):
    list_display = ('title','created', 'status' )
    list_display_links = ('title', 'created')
    list_filter = ('title',)
    list_editable = ('status',)
    search_fields = ('title', 'status',)
    list_per_page = 25

admin.site.register(Videos, VideosAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'role', )
    list_display_links = ('name', 'email')
    list_filter = ('name',)
    list_editable = ('phone',)
    search_fields = ('name', 'email',)
    list_per_page = 25

admin.site.register(About, AboutAdmin)


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', )
    list_display_links = ('title', 'author')
    list_filter = ('title',)
    list_editable = ('is_published',)
    search_fields = ('title', 'author',)
    list_per_page = 25

admin.site.register(Articles, ArticlesAdmin)