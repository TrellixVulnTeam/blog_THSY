from django.contrib import admin
from .models import Abone

# Register your models hasdere.
def make_published(modeladmin, request, queryset):
    queryset.update(status='True')
make_published.short_description = "Mail gönder"


class AboneAdmin(admin.ModelAdmin):

    list_display = ['mail','status']
    list_filter = ['mail','status']
    search_fields =['mail']
    actions = [make_published]
    #list_editable = ['baslik']
    class Meta:
        model = Abone



admin.site.register(Abone, AboneAdmin)