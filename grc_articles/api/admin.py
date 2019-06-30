from django.contrib import admin
from api.models import Articles,Category,Type
# Register your models here.
admin.site.register(Articles)
admin.site.register(Category)
admin.site.register(Type)