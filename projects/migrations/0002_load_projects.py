from django.db import migrations
import json
import os


def load_projects(apps, schema_editor):
    Project = apps.get_model('projects', 'Project')
    migrations_dir = os.path.dirname(__file__)
    fixtures_path = os.path.normpath(os.path.join(migrations_dir, '..', 'fixtures', 'projects.json'))
    if not os.path.exists(fixtures_path):
        return
    with open(fixtures_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for item in data:
        fields = item.get('fields', {})
        title = fields.get('title')
        if not title:
            continue
        Project.objects.update_or_create(
            title=title,
            defaults={
                'description': fields.get('description', ''),
                'technology': fields.get('technology', ''),
                'github_link': fields.get('github_link', ''),
            }
        )


def unload_projects(apps, schema_editor):
    Project = apps.get_model('projects', 'Project')
    # No-op reverse: do not delete projects on rollback
    return


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_projects, reverse_code=unload_projects),
    ]
