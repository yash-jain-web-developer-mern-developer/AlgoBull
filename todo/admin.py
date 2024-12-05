from django.contrib import admin
from .models import Todo, Tag

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'timestamp', 'due_date')
    list_filter = ('status', 'timestamp', 'due_date')
    search_fields = ('title', 'description')
    filter_horizontal = ('tags',)
    readonly_fields = ('timestamp',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
