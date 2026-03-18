from django.contrib import admin
from .models import post, category,comment

admin.site.registrer(post)
admin.site.registrer(category)
admin.site.registrer(comment)
# Register your models here.
