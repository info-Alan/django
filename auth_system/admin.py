from django.contrib import admin

# Register your models here.
from .models import Department, Cource, Purpose,Material,Person

admin.site.register(Department)
admin.site.register(Cource)
admin.site.register(Purpose)
admin.site.register(Material)
admin.site.register(Person)