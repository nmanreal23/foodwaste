from django import forms
from .models import Employee_Model, Food_Model, Waste_Model, Rubbishbin_Model

"""
PROJECT 2 Commence here
Below is the class for User Rego
"""
#Django ModelForms
class EmployeeRego(forms.ModelForm):
    class Meta:
        model = Employee_Model
        # fields = '__all__'
        fields = ['emp_id','firstname','lastname','username','email']
        labels = {
            'emp_id': 'Employee ID',
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'username': 'Username',
            'email': 'Email'
        }

        # exclude = []

class FoodRego(forms.ModelForm):
    class Meta:
        model = Food_Model

        fields = ['food_id','food_name','food_category','food_type','food_measurement']
        # exclude = []

class WasteRego(forms.ModelForm):
    class Meta:
        model = Waste_Model
        fields = ['waste_id','waste_quantity','waste_date','waste_reason','waste_location','waste_disposal_method','dollar_amount',
                  'total_amount','food','employeeid']

class BinRego(forms.ModelForm):
    class Meta:
        model = Rubbishbin_Model
        fields = ['bin_id','bin_name','bin_capacity','bin_status','bin_location']