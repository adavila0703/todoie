from django.contrib import admin
from .models import Todo
from simple_history.admin import SimpleHistoryAdmin

# class TodoAdmin(admin.ModelAdmin):
#

class Todohistory(SimpleHistoryAdmin):
    history_list_display = {'field1', 'field2', 'some_user_defined',}
    readonly_fields = ('created',)


admin.site.register(Todo, Todohistory)
