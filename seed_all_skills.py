import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from portfolio.models import Skill

def seed_all_skills():
    """
    Seed all skills with their appropriate Font Awesome or Devicon classes.
    This will create skills if they don't exist, or update icon_class if they do.
    """
    
    skills_data = [
        # Frontend
        {'name': 'HTML', 'icon_class': 'fab fa-html5'},
        {'name': 'CSS', 'icon_class': 'fab fa-css3-alt'},
        {'name': 'Bootstrap', 'icon_class': 'fab fa-bootstrap'},
        {'name': 'TailwindCSS', 'icon_class': 'fas fa-wind'},  # No official icon, using wind
        {'name': 'JavaScript', 'icon_class': 'fab fa-js'},
        {'name': 'ReactJS', 'icon_class': 'fab fa-react'},
        {'name': 'Angular', 'icon_class': 'fab fa-angular'},
        
        # Backend
        {'name': 'PHP', 'icon_class': 'fab fa-php'},
        {'name': 'Python', 'icon_class': 'fab fa-python'},
        {'name': 'FastAPI', 'icon_class': 'fas fa-bolt'},  # No official icon
        {'name': 'Laravel', 'icon_class': 'fab fa-laravel'},
        {'name': 'Java', 'icon_class': 'fab fa-java'},
        {'name': 'JEE', 'icon_class': 'fas fa-server'},
        {'name': 'Spring', 'icon_class': 'fas fa-leaf'},
        {'name': 'Spring Boot', 'icon_class': 'fas fa-leaf'},
        {'name': 'Spring AI', 'icon_class': 'fas fa-brain'},
        {'name': 'Spring Security', 'icon_class': 'fas fa-shield-alt'},
        
        # Databases
        {'name': 'SQL', 'icon_class': 'fas fa-database'},
        {'name': 'MySQL', 'icon_class': 'fas fa-database'},
        {'name': 'PostgreSQL', 'icon_class': 'fas fa-database'},
        {'name': 'H2', 'icon_class': 'fas fa-database'},
        {'name': 'MongoDB', 'icon_class': 'fas fa-database'},
        
        # DevOps & Tools
        {'name': 'CI/CD', 'icon_class': 'fas fa-sync-alt'},
        {'name': 'GitHub Actions', 'icon_class': 'fab fa-github'},
        {'name': 'Docker', 'icon_class': 'fab fa-docker'},
        {'name': 'Git', 'icon_class': 'fab fa-git-alt'},
        {'name': 'GitHub', 'icon_class': 'fab fa-github'},
        {'name': 'GitLab', 'icon_class': 'fab fa-gitlab'},
        
        # API & Testing
        {'name': 'Postman', 'icon_class': 'fas fa-paper-plane'},
        {'name': 'Swagger', 'icon_class': 'fas fa-file-code'},
        
        # Project Management
        {'name': 'Jira', 'icon_class': 'fab fa-jira'},
        {'name': 'Trello', 'icon_class': 'fab fa-trello'},
        {'name': 'Agile Methodologies', 'icon_class': 'fas fa-tasks'},
        
        # Design
        {'name': 'Figma', 'icon_class': 'fab fa-figma'},
        {'name': 'StarUML', 'icon_class': 'fas fa-project-diagram'},
    ]
    
    created_count = 0
    updated_count = 0
    
    print("=" * 60)
    print("SEEDING SKILLS")
    print("=" * 60)
    
    for skill_data in skills_data:
        skill, created = Skill.objects.get_or_create(
            name=skill_data['name'],
            defaults={'icon_class': skill_data['icon_class']}
        )
        
        if created:
            print(f"✅ Created: {skill.name} ({skill.icon_class})")
            created_count += 1
        else:
            # Update icon_class if it's different
            if skill.icon_class != skill_data['icon_class']:
                skill.icon_class = skill_data['icon_class']
                skill.save()
                print(f"🔄 Updated: {skill.name} ({skill.icon_class})")
                updated_count += 1
            else:
                print(f"⏭️  Skipped: {skill.name} (already exists)")
    
    print("=" * 60)
    print(f"✅ Created: {created_count} skills")
    print(f"🔄 Updated: {updated_count} skills")
    print(f"📊 Total skills in database: {Skill.objects.count()}")
    print("=" * 60)

if __name__ == '__main__':
    seed_all_skills()