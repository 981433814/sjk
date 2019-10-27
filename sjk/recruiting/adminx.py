import xadmin
from .models import Hr, Applicant, Detail, Record

from xadmin import views


class BaseSetting:
    enable_themes = True  # 开启主题功能
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings:
    """
    后台修改
    """
    site_title = '涛声依旧'
    site_footer = '涛声依旧'
    menu_style = 'accordion'  # 开启分组折叠


xadmin.site.register(views.CommAdminView, GlobalSettings)


class HrAdmin(object):
    list_display = ['name', 'username', 'password']
    search_fields = ['name', 'username', 'password']
    list_filter = ['name', 'username', 'password']
    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(status='p')

    make_published.allowed_permissions = ('publish',)


xadmin.site.register(Hr, HrAdmin)


class DetailAdmin(object):
    list_display = ['title', 'hr', 'post', 'salary', 'statue']
    search_fields = ['title', 'statue']
    list_filter = ['title', 'statue']


xadmin.site.register(Detail, DetailAdmin)


class ApplicantAdmin(object):
    list_display = ['name', 'sex', 'telephone', 'salary', 'province', 'city', 'station', 'school', 'specialty']
    search_fields = ['name', 'sex', 'telephone', 'salary', 'province', 'city', 'station', 'school', 'specialty']
    list_filter = ['name', 'sex', 'telephone', 'salary', 'province', 'city', 'station', 'school', 'specialty']


xadmin.site.register(Applicant, ApplicantAdmin)


class RecordAdmin(object):
    list_display = ['hr', 'detail', 'applicant']
    search_fields = ['detail', 'applicant', 'hr']
    list_filter = ['detail', 'applicant', 'hr']


xadmin.site.register(Record, RecordAdmin)
