from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.URLField(blank=True, null=True, help_text="URL to icon image")
    icon_class = models.CharField(max_length=50, blank=True, null=True, help_text="FontAwesome class e.g., 'fab fa-python'")
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField(help_text="URL to project image")  # Changed from ImageField
    github_link = models.URLField(blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)
    
    # Categorized tech stack fields
    frontend = models.CharField(max_length=200, blank=True, help_text="Ex: HTML5, CSS3, JavaScript")
    backend = models.CharField(max_length=200, blank=True, help_text="Ex: Django, FastAPI, Laravel")
    database = models.CharField(max_length=200, blank=True, help_text="Ex: PostgreSQL, MySQL, MongoDB")
    security = models.CharField(max_length=200, blank=True, help_text="Ex: JWT, bcrypt, CSRF protection")
    architecture = models.CharField(max_length=200, blank=True, help_text="Ex: MVC, REST API, Microservices")
    tools = models.CharField(max_length=200, blank=True, help_text="Ex: Git, Docker, GitHub Actions")
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.CharField(max_length=50, help_text="e.g., 'June 2025'")
    end_date = models.CharField(max_length=50, help_text="e.g., 'July 2025' or 'Present'")
    description = models.TextField()
    location = models.CharField(max_length=100, blank=True, null=True)
    order = models.IntegerField(default=0, help_text="Lower numbers appear first")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', '-created_at']
        verbose_name_plural = "Experiences"
    
    def __str__(self):
        return f"{self.position} at {self.company}"

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.name}"