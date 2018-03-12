from django.contrib import admin
from IACS_CSMS.models import Asset,Application,Zone,Conduit,Risk,CounterMeasure
from django import forms
import csv


class ExportCsvMixin:
	def export_as_csv(self, request, queryset):
		meta = self.model._meta
		field_names = [field.name for field in meta.fields]

		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
		writer = csv.writer(response)

		writer.writerow(field_names)
		for obj in queryset:
		    row = writer.writerow([getattr(obj, field) for field in field_names])

		return response
	export_as_csv.short_description = "Export Selected"


class ApplicationAdminForm(forms.ModelForm):
	Description = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 5}))
	class Meta:
		model = Application
		fields = '__all__' 

class ApplicationAdmin(admin.ModelAdmin,ExportCsvMixin):
	form = ApplicationAdminForm
	list_display = ('Application_Name','Description','Version','Type')
	search_fields = ('Application_Name',)
	list_filter = ('Type','Version')
	fieldsets = (
	      ('Application Information', {
	          'fields': ('Application_Name','Description','Type','Version','Application_Provider','Storage_Location','License',)
	      }),
	      ('Registration Information', {
	          'fields': ('DeclaredUser','Installed_User','Reviewed_User','RegisteredDate','RevisedDate')
	      }),
	   )
	actions = ["export_as_csv"]

class AssetAdmin(admin.ModelAdmin):
	list_display = ('Asset_Name','Operating_Sytem','Asset_Type','RegisteredDate','Zone')
	search_fields = ('Asset_Name','ResponsibleUser')
	list_filter = ('Operating_Sytem','Asset_Type','RegisteredDate')
class ZoneAdmin(admin.ModelAdmin):
	list_display = ('Zone_Name','Zone_Type','RegisteredDate','ResponsibleUser')

class ConduitAdmin(admin.ModelAdmin):
	list_display = ('Name','From_Zone','To_Zone','ConnectionType','ConnectionPort')



class RiskAdminForm(forms.ModelForm):
	Description = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 5}))
	class Meta:
		model = Risk
		fields = '__all__' 

class CounterMeasureInline(admin.TabularInline):
    model = CounterMeasure

class RiskAdmin(admin.ModelAdmin,ExportCsvMixin):
	form = RiskAdminForm
	
	def Risk_Level(self,obj):
		if obj.Consequence == 'CAT':
			if obj.Likelihood == 'FREQ' or obj.Likelihood == 'PRO' or obj.Likelihood == 'OCC':
				return 'Class I: Unacceptable' 
			elif obj.Likelihood == 'REM':
				return 'Class II: Undesirable' 
			elif obj.Likelihood == 'IMP':
				return 'Class III: Tolerable'
			else:
				return 'Class IV: Acceptable'
		elif obj.Consequence =='CRI':
			if obj.Likelihood == 'FREQ' or obj.Likelihood == 'PRO': 
				return 'Class I: Unacceptable' 
			elif obj.Likelihood =='OCC':
				return 'Class II: Undesirable' 
			elif obj.Likelihood == 'REM':
				return 'Class III: Tolerable'
			elif obj.Likelihood == 'IMP':
				return 'Class III: Tolerable'
			else:
				return 'Class IV: Acceptable'
		elif obj.Consequence =='MAR':
			if obj.Likelihood == 'FREQ':
				return 'Class I: Unacceptable' 
			elif obj.Likelihood == 'PRO': 
				return 'Class II: Undesirable' 
			elif obj.Likelihood =='OCC':
				return 'Class III: Tolerable'
			elif obj.Likelihood == 'REM':
				return 'Class III: Tolerable'
			elif obj.Likelihood == 'IMP':
				return 'Class IV: Acceptable'
			else:
				return 'Class IV: Acceptable'
		else:
			if obj.Likelihood == 'FREQ':
				return 'Class II: Undesirable' 
			elif obj.Likelihood == 'PRO' or obj.Likelihood == 'OCC':
				return 'Class III: Tolerable'
			else:
				return 'Class IV: Acceptable'


	list_display = ('Risk_Name','Description','Threat_Name','Asset','Risk_Level')
	list_filter = ('Threat_Name','Zone',)
	search_fields = ('Risk_Name',)
	actions = ["export_as_csv"]
	fieldsets = (
	      ('Risk Identification', {
	          'fields': ('Risk_Name','Description','Threat_Name','Zone','Asset','Responsible_Person','Date_of_risk_assessment','Reviewed_date')
	      }),
	      ('Risk Evaluation', {
	          'fields': ('Likelihood','Consequence')
	      }),
	   )
	inlines = [ CounterMeasureInline,]
	
	
	  	


admin.site.register(Application,ApplicationAdmin)
admin.site.register(Asset,AssetAdmin)
admin.site.register(Zone,ZoneAdmin)
admin.site.register(Conduit,ConduitAdmin)
admin.site.register(Risk,RiskAdmin)

