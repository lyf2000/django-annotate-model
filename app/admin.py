from django.contrib import admin

# Register your models here.

from app.models import (
    Course,
    AcademicGroup,
    Tariff,
)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    pass


@admin.register(AcademicGroup)
class AcademicGroupAdmin(admin.ModelAdmin):
    pass
