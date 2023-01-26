from django.contrib import admin
from .models import Post, Category, Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title',)
    list_filter = ('category',)
    prepopulated_fields = {'slug':('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Comment)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
