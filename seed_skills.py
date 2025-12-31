import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from portfolio.models import Skill

def seed_skills():
    # Clear existing skills to avoid duplicates/mess
    Skill.objects.all().delete()
    
    skills_map = [
        # Frontend
        {'name': 'HTML', 'icon_class': 'fab fa-html5'},
        {'name': 'CSS', 'icon_class': 'fab fa-css3-alt'},
        {'name': 'JavaScript', 'icon_class': 'fab fa-js'},
        {'name': 'Bootstrap', 'icon_class': 'fab fa-bootstrap'},
        {'name': 'TailwindCSS', 'icon_class': 'fas fa-wind'}, # Approximate
        {'name': 'Angular', 'icon_class': 'fab fa-angular'},
        
        # Backend
        {'name': 'PHP', 'icon_class': 'fab fa-php'},
        {'name': 'POO', 'icon_class': 'fas fa-cubes'},
        {'name': 'Laravel', 'icon_class': 'fab fa-laravel'},
        {'name': 'Java', 'icon_class': 'fab fa-java'},
        {'name': 'Java EE', 'icon_class': 'fas fa-server'},
        {'name': 'Spring Boot', 'icon_class': 'fas fa-leaf'},
        {'name': 'Python', 'icon_class': 'fab fa-python'},
        {'name': 'FastAPI', 'icon_class': 'fas fa-bolt'},
        {'name': 'C', 'icon_class': 'fas fa-copyright'}, # Approximate

        # Databases
        {'name': 'SQL', 'icon_class': 'fas fa-database'},
        {'name': 'MySQL', 'icon_class': 'fas fa-database'},
        {'name': 'H2', 'icon_class': 'fas fa-hdd'},
        {'name': 'PostgreSQL', 'icon_class': 'fas fa-database'},

        # Analysis & Design
        {'name': 'Figma', 'icon_class': 'fab fa-figma'},
        {'name': 'StarUML', 'icon_class': 'fas fa-project-diagram'},

        # Project Management
        {'name': 'Trello', 'icon_class': 'fab fa-trello'},
        {'name': 'Jira', 'icon_class': 'fab fa-jira'},
        {'name': 'Agile', 'icon_class': 'fas fa-users-cog'},

        # Collaboration
        {'name': 'Git', 'icon_class': 'fab fa-git-alt'},
        {'name': 'GitHub', 'icon_class': 'fab fa-github'},
        {'name': 'GitLab', 'icon_class': 'fab fa-gitlab'},
        {'name': 'Docker', 'icon_class': 'fab fa-docker'},
    ]

    for skill_data in skills_map:
        Skill.objects.create(name=skill_data['name'], icon_class=skill_data['icon_class'])
    
    print(f"Successfully seeded {len(skills_map)} skills with icons.")

if __name__ == '__main__':
    seed_skills()
