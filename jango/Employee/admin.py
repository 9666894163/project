from django.contrib import admin
from .models import Employee

# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):

        list_display = ['empname','empno','empsalary','salEvalution','bonus']
    

        def salEvalution(self,name):
            if name.empsalary > 70000:
                return 'High'
            else:
                return 'Low'    

        def bonus(self, obj):
            return obj.empsalary/10        


admin.site.register(Employee,EmployeeAdmin)