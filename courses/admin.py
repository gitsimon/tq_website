from django.contrib import admin

# Register your models here.
from courses.models import *

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CourseInline(admin.TabularInline):
    model=Course
    fields = ('name','type','period',"position",)
    # define the sortable
    sortable_field_name = "position"
    extra=0

class OfferingAdmin(admin.ModelAdmin):
    list_display = ('name', 'period','display','active')
    inlines = (CourseInline,)
    
class TeachInlineForCourse(admin.TabularInline):
    model = Teach
    extra = 2
    fk_name = 'course'
    
    # define the raw_id_fields (grappelli feature)
    raw_id_fields = ('teacher',)
    # define the autocomplete_lookup_fields (grappelli feature)
    autocomplete_lookup_fields = {
        'fk': ['teacher'],
    }
          
class SubscribeInlineForCourse(admin.TabularInline):
    model = Subscribe
    extra = 1
    fk_name = 'course'
    
    # define the raw_id_fields (grappelli feature)
    raw_id_fields = ('user','partner')
    # define the autocomplete_lookup_fields (grappelli feature)
    autocomplete_lookup_fields = {
        'fk': ['user','partner'],
    }
    
class SubscribeInlineForUser(admin.TabularInline):
    model = Subscribe
    extra = 1
    fk_name = 'user'
    
    # define the raw_id_fields (grappelli feature)
    raw_id_fields = ('course','partner')
    # define the autocomplete_lookup_fields (grappelli feature)
    autocomplete_lookup_fields = {
        'fk': ['course'],
        'fk': ['partner'],
    }
    
class CourseCancellationInline(admin.TabularInline):
    model = CourseCancellation
    extra = 1
    
class CourseTimeInline(admin.TabularInline):
    model = CourseTime
    extra = 1
    
class PeriodCancellationInline(admin.TabularInline):
    model = PeriodCancellation
    extra = 2
    
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'type','offering','period','format_times','room','format_prices','format_teachers')
    list_filter = ('offering', 'type', 'room')
    inlines = (CourseCancellationInline,CourseTimeInline,TeachInlineForCourse,SubscribeInlineForCourse,)
    
    model = Course
    fieldsets = [
        ('What?', {
                     'classes': ("grp-collapse grp-open",),
                     'fields': ['name','type','min_subscribers','max_subscribers']}),
        ('When?', {
                   'classes': ("grp-collapse grp-open",),
                   'fields': ['offering','period',]}),
        ("CourseCancellation Inlines", {"classes": ("placeholder cancellations-group",), "fields" : ()}),
        ("CourseTime Inlines", {"classes": ("placeholder times-group",), "fields" : ()}),
        ('Where?', {
                    'classes': ("grp-collapse grp-open",),
                    'fields': ['room']}),
        ('Billing', {
                     'classes': ("grp-collapse grp-closed",),
                     'fields': ['price_with_legi','price_without_legi']}),
        ('Etc', {
                 'classes': ("grp-collapse grp-closed",),
                 'fields': ['comment'],}),
    ]
    
class CourseTypeAdmin(admin.ModelAdmin):  
    list_display = ('name', 'format_styles', 'level', 'couple_course',)
    list_filter = ('level', 'couple_course')
  
    model = CourseType
    
    # define the raw_id_fields (grappelli feature)
    raw_id_fields = ('styles',)
    # define the autocomplete_lookup_fields (grappelli feature)
    autocomplete_lookup_fields = {
        'm2m': ['styles'],
    }
    
class PeriodAdmin(admin.ModelAdmin):
    inlines = (PeriodCancellationInline,)
    
class TeachAdmin(admin.ModelAdmin):
    # define the raw_id_fields (grappelli feature)
    raw_id_fields = ('teacher',)
    # define the autocomplete_lookup_fields (grappelli feature)
    autocomplete_lookup_fields = {
        'fk': ['teacher'],
    }
    
class StyleAdmin(admin.ModelAdmin):
    list_display = ('name', 'url_info', 'url_video', )

admin.site.register(Offering, OfferingAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseType, CourseTypeAdmin)
admin.site.register(Room)
admin.site.register(Period, PeriodAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Teach, TeachAdmin)

class UserInfoInline(admin.StackedInline):
    model = UserInfo
    can_delete = False

# Define a new User admin
class MyUserAdmin(UserAdmin):
    inlines = (UserInfoInline, SubscribeInlineForUser)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)

