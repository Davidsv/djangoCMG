from django.contrib import admin
from django.forms import forms
from screen.models import *

class messageInline(admin.TabularInline):
    model = message
    extra = 1
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.attname == 'text':
            kwargs['widget'] = forms.Textarea(attrs= { 'rows': 1, 'cols': 30 } )
        if db_field.attname == 'headline':
            kwargs['widget'] = forms.TextInput(attrs={ 'size': 15 })
        return super(messageInline, self).formfield_for_dbfield(db_field, **kwargs)

class infochannelAdmin(admin.ModelAdmin):
    inlines = [messageInline]

admin.site.register(main_area)
admin.site.register(format)
admin.site.register(infochannel, infochannelAdmin)
#admin.site.register(message)