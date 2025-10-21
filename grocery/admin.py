from django.contrib import admin
from .models import grocery_item

@admin.register(grocery_item)
class GroceryAdmin(admin.ModelAdmin):
	list_display = ('name', 'quantity', 'section', 'user', 'date_added')
	list_filter = ('section', 'user', 'date_added')
	search_fields = ('name',)
