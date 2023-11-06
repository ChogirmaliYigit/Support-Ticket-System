from django.contrib import admin
from django.db.models import Count
from django.contrib.admin import SimpleListFilter

from users.models import User, Company, Member


class HasCompanyFilter(SimpleListFilter):
    title = 'Has Company'
    parameter_name = 'has_company'

    def lookups(self, request, model_admin):
        return (
            ("true", True),
            ("false", False),
        )

    def queryset(self, request, queryset):
        if self.value() == "true":
            return queryset.annotate(count_companies=Count('companies')).filter(count_companies__gt=0)
        if self.value() == "false":
            return queryset.annotate(count_companies=Count('companies')).filter(count_companies=0)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "has_company", "is_active", "date_joined", )
    list_filter = ("language", "is_active", "date_joined", HasCompanyFilter)
    fields = ("first_name", "last_name", "email", "profile_image", "language", "is_active", "is_staff", )


admin.site.register(Company)
admin.site.register(Member)
