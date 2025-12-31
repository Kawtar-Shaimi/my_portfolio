import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from portfolio.models import Skill

# List of new skills to add
new_skills = [
    'Postman',
    'Spring Security',
    'Spring',
    'Git',
    'GitHub',
    'Hibernate',
    'Spring Data JPA',
    'VS Code',
    'Python',
    'Laravel',
    'Jakarta EE',
    'IntelliJ IDEA',
    'JUnit 5',
    'Mockito',
    'Liquibase',
    'Swagger'
]

# Add skills if they don't already exist
added_count = 0
for skill_name in new_skills:
    skill, created = Skill.objects.get_or_create(name=skill_name)
    if created:
        added_count += 1
        print(f"✓ Added: {skill_name}")
    else:
        print(f"- Already exists: {skill_name}")

print(f"\n✅ Successfully added {added_count} new skills!")
print(f"Total skills in database: {Skill.objects.count()}")
