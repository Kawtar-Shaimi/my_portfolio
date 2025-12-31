from django.contrib import admin
from .models import Skill, Project, Message, Experience

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'image', 'github_link', 'demo_link')
        }),
        ('Tech Stack', {
            'fields': ('frontend', 'backend', 'database', 'security', 'architecture', 'tools'),
            'description': 'Enter comma-separated technologies for each category'
        }),
    )

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'start_date', 'end_date', 'order')
    list_editable = ('order',)
    ordering = ('order', '-created_at')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('created_at',)