import os
import django
from django.core.files.base import ContentFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from portfolio.models import Project, Skill

def seed():
    # Skills
    skills_data = ['Python', 'Django', 'JavaScript', 'HTML/CSS', 'PostgreSQL', 'Git']
    for skill_name in skills_data:
        Skill.objects.get_or_create(name=skill_name)
    print(f"Seeded {len(skills_data)} skills.")

    # Projects
    if not Project.objects.exists():
        Project.objects.create(
            title="E-Commerce Platform",
            description="A fully featured e-commerce site with cart, checkout, and payments.",
            tech_stack="Django, Stripe, Redis",
            github_link="https://github.com/example/ecommerce",
            demo_link="https://example.com"
        )
        Project.objects.create(
            title="Task Manager Platform",
            description="A productivity tool to manage tasks and teams efficiently.",
            tech_stack="Django, React, PostgreSQL",
            github_link="https://github.com/example/taskmanager",
            demo_link="https://example.com"
        )
        print("Seeded 2 projects.")
    else:
        print("Projects already exist.")

if __name__ == '__main__':
    seed()
