from django.contrib import admin
from .models import *


class C1_admin(admin.ModelAdmin):
    pass


admin.site.register(C1, C1_admin)
