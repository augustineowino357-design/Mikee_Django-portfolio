from django.contrib import admin
from projects.models import Project  # Imports your Project model

# Customizes how the projects look inside the admin dashboard
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology')  # Columns shown in the list view
    search_fields = ('title', 'description') # Adds a search bar for easy finding

# Registers the model with the customized settings
admin.site.register(Project, ProjectAdmin)