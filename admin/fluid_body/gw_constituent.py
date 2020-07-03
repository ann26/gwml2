from django.contrib import admin
from gwml2.models.fluid_body.gw_constituent import *


class GWConstituentRelationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'gw_constituent_relation_type', 'gw_constitution_relation_mechanism')


class GWConstituentAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'gw_concentration', 'gw_state', 'gw_constituent_relation',
        'gw_material_constituent', 'gw_chemical_constituent', 'gw_biologic_constituent')

    filter_horizontal = ('gw_constituent_relation',)


# Terms
admin.site.register(StateType)
admin.site.register(ConstituentRelationType)
admin.site.register(MechanismType)
admin.site.register(MaterialType)
admin.site.register(ChemicalType)
admin.site.register(OrganismType)

admin.site.register(GWConstituentRelation, GWConstituentRelationAdmin)
admin.site.register(GWMaterialConstituent)
admin.site.register(GWChemicalConstituent)
admin.site.register(GWBiologicConstituent)
admin.site.register(GWConstituent, GWConstituentAdmin)