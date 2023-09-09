from django.contrib import admin
from .models import Apartment, Town, Type, ApartmentImages, Booking, Feature, ApartmentFeature

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'square', 'occupants',)
    search_fields = ('name', 'description', 'square', 'occupants',)

@admin.register(ApartmentFeature)
class ApartmentFeatureAdmin(admin.ModelAdmin):
    list_filter = ('apartment', 'feature',)
    search_fields = ('apartment__name', 'feature__name',)

@admin.register(Town)
class TownAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(ApartmentImages)
class ApartmentImagesAdmin(admin.ModelAdmin):
    list_display = ('apartment', 'image',)
    list_filter = ('apartment',)
    search_fields = ('apartment__name',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('apartment', 'check_in_date', 'check_out_date',)
    list_filter = ('apartment', 'check_in_date', 'check_out_date',)
