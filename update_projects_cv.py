import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from portfolio.models import Project

def update_projects():
    # Clear existing sample projects
    Project.objects.all().delete()
    
    # Add real projects from CV
    Project.objects.create(
        title="Delivery Tour Optimizer",
        description="An optimization application for delivery tours integrating pagination, history, and artificial intelligence (Ollama). Developed with Spring Boot, Java EE, LiquidBase, and PostgreSQL.",
        tech_stack="Spring Boot, Java EE, Ollama, LiquidBase, PostgreSQL",
        github_link="https://github.com/Kawtar-Shaimi",
        demo_link=""
    )
    
    Project.objects.create(
        title="Blood Donation Management",
        description="A web application allowing donor and receiver management, blood compatibility identification, and dynamic status availability sorting using Java EE, TailwindCSS, JavaScript, MVC, and PostgreSQL.",
        tech_stack="Java EE, TailwindCSS, JavaScript, MVC, PostgreSQL",
        github_link="https://github.com/Kawtar-Shaimi",
        demo_link=""
    )
    
    Project.objects.create(
        title="ERP Documentation Site",
        description="Development and architecture of a comprehensive documentation website for ERP BUSINESS SUITE using Laravel, GitHub, and StarUML.",
        tech_stack="Laravel, GitHub, StarUML, PHP",
        github_link="https://github.com/Kawtar-Shaimi",
        demo_link=""
    )
    
    print("Successfully updated projects with CV data!")
    print(f"Total projects: {Project.objects.count()}")

if __name__ == '__main__':
    update_projects()
