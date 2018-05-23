from django.contrib import admin
#引入自定义的模型类
from .models import Grades,Students
# Register your models here.
class StudentsInfo(admin.TabularInline): #admin.StackedInline
    model = Students
    extra = 2
    

class GradesAdmin(admin.ModelAdmin):

    inlines = [StudentsInfo]
    #列表页属性
    list_display  = ['pk','gname','gdate','ggirlnum','gboynum','isDelete']#显示字段
    list_filter   = ['gname']#过滤器
    search_fields = ['gname']#搜索框
    list_per_page = 5 #分页

    #添加/修改页属性
    #fields    = ['ggirlnum', 'gboynum', 'gname', 'gdate', 'isDelete']#规定属性的先后顺序
    fieldsets = [
        ("num",  {"fields": ['ggirlnum','gboynum']}),
        ("base", {"fields": ['gname', 'gdate', 'isDelete']}),
    ]#给属性分组

admin.site.register(Grades, GradesAdmin)

#装饰注册类,替代先写类,再admin.site.register的方法
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):

    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    #设置页面类的名称
    gender.short_description = "性别"

    list_display  = ['pk', 'sname', 'sage', gender, 'scontend', 'sgrade', 'isDelete']
    list_per_page = 5

    #执行动作的位置
    actions_on_top = False
    actions_on_bottom = True

#admin.site.register(Students,StudentsAdmin)