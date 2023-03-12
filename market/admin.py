from django.contrib import admin
from django.contrib.auth.models import Group
from django.db.models import QuerySet
from market import models


admin.site.register(models.Product)
admin.site.register(models.Contact)
admin.site.register(models.BusinessUnit)
admin.site.unregister(Group)


@admin.register(models.BaseModel)
class CustomAdmin(admin.ModelAdmin):
    list_filter = ('contacts__city', )
    actions = ['set_duty']

    @admin.action(description='Обновление задолженности поставщику')
    def set_duty(self, request, qs: QuerySet):
        qs.update(duty=models.BaseModel.duty == 0)
