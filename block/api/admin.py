from django.contrib import admin

from .models import Views, Content


class ContentAdmin(admin.ModelAdmin):
    list_display = ('views_count', 'author', 'text', 'video', 'pub_date')
    search_fields = ('text',)
    list_filter = ('pub_date', )

    @admin.display(description='count')
    def views_count(self, obj):
        return Views.objects.filter(views=obj.id).count()


admin.site.register(Content, ContentAdmin)
