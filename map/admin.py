from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from .models import *

admin.site.site_header = '后台管理系统'
admin.site.index_title = '首页'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'category')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

    list_display_links = ('name',)

    actions = ['make_copy']
    print(super.__dict__)

    def make_copy(self, request, queryset):
        # 点击触发它
        # queryset：选中的数据
        # request 请求对象
        print(queryset)

    # # # 在list页面显示头像
    # @admin.display(
    #     boolean=True,
    #     ordering='id',
    #     description='Is Published?',
    # )
    # def img(self, obj):
    #     # 在custom.js里面实现了show_pic函数，onclick进行调用
    #     # div = f"""<img id='icon_{obj.id}' src='{obj.icon.url}'
    #     # width='32px' οnclick='show_pic("{obj.icon.url})"' />"""
    #     div = """ console.log("{obj.id}")"""
    #     print(obj)
    #     return mark_safe(div)

    # # 挂载自定义的js，css也可以挂，可以挂载本地文件，也可以挂载网络文件
    class Media:
        js = (
            'admin/js/custom.js',
            'admin/js/adminfix.js',
            #   也可以挂载cdn文件，这里仅示例
            #  'https://cdn.bootcdn.net/ajax/libs/jquery/3.6.0/jquery.js',
        )

    @admin.display()
    def get_media(self):
        # Tried "super(ContentAdmin, self).get_media()"
        ## » Says method doesn't exists
        # Tried "super(ContentAdmin, self).media"
        ## » Exactly the same thing as "self.media" below
        media = self.media
        print("#### MEDIA IS {}".format(media.__dict__))
        return media


# admin.site.register(Category)
#
# admin.site.register(Address)

admin.site.register(Category, CategoryAdmin)
# admin.site.register(Address, AddressAdmin)
admin.site.register(Address, AddressAdmin)
