from django.contrib import admin
from .models import articles,posts,delhi,bangalore,chennai,mumbai,ques

# Register your models here.
admin.register(articles)(admin.ModelAdmin)
admin.register(posts)(admin.ModelAdmin)
admin.register(delhi)(admin.ModelAdmin)
admin.register(bangalore)(admin.ModelAdmin)
admin.register(chennai)(admin.ModelAdmin)
admin.register(mumbai)(admin.ModelAdmin)
admin.register(ques)(admin.ModelAdmin)
