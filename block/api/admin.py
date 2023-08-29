from django.contrib import admin

from .models import Views, Content, BlockContents


class ContentAdmin(admin.ModelAdmin):
    list_display = ('views_count', 'slug', 'video', 'pub_date')
    search_fields = ('slug',)
    list_filter = ('pub_date', )

    @admin.display(description='count')
    def views_count(self, obj):
        return Views.objects.filter(views=obj.id).count()


admin.site.register(Content, ContentAdmin)
admin.site.register(BlockContents)
