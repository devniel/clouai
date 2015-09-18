from django.contrib import admin
from repositories.models import *


# Register your models here.
admin.site.register(Repository)
admin.site.register(Record)
admin.site.register(RecordProperty)
admin.site.register(RecordSet)
admin.site.register(Property)
admin.site.register(Set)
