from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Nuevos modelos importados con sus nombres actualizados
from .models import Club, Deportista, Torneo, ParticipacionClub

# Registro en el admin con soporte para import/export
admin.site.register(Club, ImportExportModelAdmin)
admin.site.register(Deportista, ImportExportModelAdmin)
admin.site.register(Torneo, ImportExportModelAdmin)
admin.site.register(ParticipacionClub, ImportExportModelAdmin)
