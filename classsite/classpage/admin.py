from django.contrib import admin
from classpage.models import News
from classpage.models import Announcement
from classpage.models import File_language, File_math, File_others

# Register your models here.


admin.site.register(News)
admin.site.register(Announcement)


admin.site.register(File_language)
admin.site.register(File_math)
admin.site.register(File_others)