from django import forms

from .models import Employee

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ('emp_code', 'fullname',  'mobile', 'position')
        labels = {
            'emp_code':'Employee Code',
            'fullname':'Full Name',
            'mobile':'Mobile Number',
            'position':'Position',
        }
    
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
         
        self.fields['position'].empty_label='Select'