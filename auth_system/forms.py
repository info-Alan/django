from django import forms

from auth_system.models import Person, Cource


class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cource'].queryset = Cource.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['cource'].queryset = Cource.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass 
        elif self.instance.pk:
            self.fields['cource'].queryset = self.instance.department.cource.order_by('name')