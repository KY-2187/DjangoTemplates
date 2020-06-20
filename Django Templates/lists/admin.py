from django.contrib import admin

from .models import Item, Tag


#class TagInLineAdmin(admin.TabularInline)
class TagInlineAdmin(admin.StackedInline):
	model = Tag


class ItemAdmin(admin.ModelAdmin):
	model = Item
	list_display = ('text', 'created_on', 'modified_on', 'tags')
	fieldsets = (
		(
			'Basic Information', { 'fields': ('text',) }
		),
	)

	inLines = [TagInlineAdmin, ]



admin.site.register(Item, ItemAdmin)