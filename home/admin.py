from django.contrib import admin
from home.models import Blog, Contact

class BlogAdmin(admin.ModelAdmin):
    class Media:  # inner class
        # what to add
        css = {  # Dictionary
            "all": ("css/main.css",)
        }

        js = ("js/blog.js",)  # Tuple


# Register your models here.
admin.site.register(Contact)
admin.site.register(Blog, BlogAdmin)