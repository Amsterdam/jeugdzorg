from django.contrib import admin
from .models import *
from .forms import *
from adminsortable.admin import SortableAdmin
from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline


class VoorwaardeInline(SortableStackedInline):
    model = Voorwaarde
    extra = 1


class RegelingenTagsInline(SortableStackedInline):
    model = RegelingTag
    extra = 1


class ContactNaarRegelingInline(admin.TabularInline):
    model = ContactNaarRegeling
    extra = 1


class ContactNaarThemaInline(admin.TabularInline):
    model = ContactNaarThema
    extra = 1


class ContactNaarOrganisatieInline(admin.TabularInline):
    model = ContactNaarOrganisatie
    extra = 1


@admin.register(Regeling)
class RegelingAdmin(SortableAdmin):
    list_display = ['titel', 'bron_veranderd']
    #raw_id_fields = ['contact', ]

    inlines = [
        VoorwaardeInline,
        ContactNaarRegelingInline,
    ]
    #filter_horizontal = ('contact',)  #


@admin.register(Voorwaarde)
class VoorwaardeAdmin(SortableAdmin):
    pass


@admin.register(Organisatie)
class OrganisatieAdmin(SortableAdmin):
    pass


# @admin.register(RegelingTag)
# class RegelingTagAdmin(SortableAdmin):
#     pass


@admin.register(Thema)
class DoelAdmin(SortableAdmin):
    prepopulated_fields = {'slug': ('titel',), }
    inlines = [
        ContactNaarThemaInline,
    ]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [
        ContactNaarOrganisatieInline,
    ]


@admin.register(EventItem)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'value', 'timestamp', 'url', ]
    list_filter = ['url', 'name', ]


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     form = UserChangeForm
#     add_form = UserCreationForm
