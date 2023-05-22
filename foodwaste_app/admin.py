from django.contrib import admin
from foodwaste_app.models import Data_Model_table, Employee_Model, Food_Model, Rubbishbin_Model, Waste_Model

class EmployeeModelAdmin(admin.ModelAdmin):
    tab_display = ('emp_id','firstname','lastname','username','email')

# Register your models here.
auditModel =[Data_Model_table, Employee_Model, Food_Model, Rubbishbin_Model, Waste_Model]
admin.site.register(auditModel, EmployeeModelAdmin)
# admin.site.register(EmployeeModelAdmin)
