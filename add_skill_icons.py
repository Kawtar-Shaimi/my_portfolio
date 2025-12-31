import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from portfolio.models import Skill

# Dictionary mapping skill names to their DevIcons or FontAwesome classes
skill_icons = {
    # Frontend
    'HTML': 'fab fa-html5',
    'CSS': 'fab fa-css3-alt',
    'JavaScript': 'fab fa-js',
    'React': 'fab fa-react',
    'Angular': 'fab fa-angular',
    'TailwindCSS': 'fas fa-wind',
    'Bootstrap': 'fab fa-bootstrap',
    
    # Backend & Languages
    'Python': 'fab fa-python',
    'Java': 'fab fa-java',
    'PHP': 'fab fa-php',
    'Spring': 'fas fa-leaf',
    'Spring Boot': 'fas fa-leaf',
    'Spring Security': 'fas fa-shield-alt',
    'Spring Data JPA': 'fas fa-database',
    'Laravel': 'fab fa-laravel',
    'Django': 'fas fa-code',
    'FastAPI': 'fas fa-bolt',
    'Jakarta EE': 'fas fa-server',
    
    # Databases
    'PostgreSQL': 'fas fa-database',
    'MySQL': 'fas fa-database',
    'MongoDB': 'fas fa-database',
    'H2': 'fas fa-database',
    'Hibernate': 'fas fa-database',
    
    # DevOps & Tools
    'Docker': 'fab fa-docker',
    'Git': 'fab fa-git-alt',
    'GitHub': 'fab fa-github',
    'GitLab': 'fab fa-gitlab',
    'VS Code': 'fas fa-code',
    'IntelliJ IDEA': 'fas fa-laptop-code',
    'Postman': 'fas fa-paper-plane',
    'Swagger': 'fas fa-book',
    
    # Testing & Quality
    'JUnit 5': 'fas fa-vial',
    'Mockito': 'fas fa-flask',
    'Liquibase': 'fas fa-stream',
    
    # Project Management
    'Trello': 'fab fa-trello',
    'Jira': 'fab fa-jira',
    'Figma': 'fab fa-figma',
    'StarUML': 'fas fa-project-diagram',
    
    # Collaboration
    'Agile': 'fas fa-sync-alt',
}

# Update skills with icons
updated_count = 0
for skill in Skill.objects.all():
    if skill.name in skill_icons:
        skill.icon_class = skill_icons[skill.name]
        skill.save()
        updated_count += 1
        print(f"✓ Updated {skill.name} with icon: {skill_icons[skill.name]}")
    else:
        print(f"⚠ No icon found for: {skill.name}")

print(f"\n✅ Successfully updated {updated_count} skills with icons!")
print(f"Total skills: {Skill.objects.count()}")
