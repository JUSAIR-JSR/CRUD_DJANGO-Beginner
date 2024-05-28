from django.contrib import admin

from . models import MovieInfo,Director,censorInfo,Actor
# Register your models here.


admin.site.register(MovieInfo)
admin.site.register(Director)
admin.site.register(censorInfo)
admin.site.register(Actor),

