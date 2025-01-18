from django.contrib import admin

from music.models import Album, Artist

# Register your models here.
#@admin.register(Album)
#class AlbumAdmin(admin.ModelAdmin):
#    exclude = ('artist',)

admin.site.register(Album)
admin.site.register(Artist)
