from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, Skill, Message, Experience

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('message')
        
        if name and email and content:
            Message.objects.create(name=name, email=email, message=content)
            
            try:
                send_mail(
                    subject=f'New Contact Message from {name}',
                    message=f'You have received a new message from your portfolio contact form.\n\n'
                            f'Name: {name}\n'
                            f'Email: {email}\n\n'
                            f'Message:\n{content}\n\n'
                            f'---\n'
                            f'This message was sent from your portfolio website.',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.RECIPIENT_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully!')
            except Exception as e:
                print(f"Email error: {e}")
                messages.success(request, 'Your message has been saved! We will get back to you soon.')
            
            return redirect('index')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    projects = Project.objects.all().order_by('-created_at')
    
    # Split comma-separated tech stacks into lists
    for project in projects:
        project.frontend_list = [tech.strip() for tech in project.frontend.split(',') if tech.strip()] if project.frontend else []
        project.backend_list = [tech.strip() for tech in project.backend.split(',') if tech.strip()] if project.backend else []
        project.database_list = [tech.strip() for tech in project.database.split(',') if tech.strip()] if project.database else []
        project.security_list = [tech.strip() for tech in project.security.split(',') if tech.strip()] if project.security else []
        project.architecture_list = [tech.strip() for tech in project.architecture.split(',') if tech.strip()] if project.architecture else []
        project.tools_list = [tech.strip() for tech in project.tools.split(',') if tech.strip()] if project.tools else []
    
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    
    context = {
        'projects': projects,
        'skills': skills,
        'experiences': experiences,
    }
    return render(request, 'portfolio/index.html', context)