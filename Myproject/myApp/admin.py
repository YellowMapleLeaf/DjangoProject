from django.contrib import admin
from .models import Friends,Text

# Register your models here.

# admin.site.register(Friends)
# class rFriends(admin.TabularInline):
#     model = rFriends
#     extra = 3

@admin.register(Friends)
class friendsShow(admin.ModelAdmin):
    # inlines = [rFriends]
    def sex(self):
        if self.fSex:
            return "男"
        else:
            return "女"
    def single(self):
        if self.fSingle:
            return "单身"
        else:
            return "已婚"
    list_display = ["fName",sex,"fAge",single]
    list_per_page = 10
    list_filter = ["fName"]

admin.site.register(Text)

# admin.site.register(Friends,friendsShow)