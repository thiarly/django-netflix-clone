from django.apps import AppConfig


class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'
    
    def ready(self):
        from .models import Usuario
        import os
        
        email = os.getenv("EMAIL-ADMIN")
        senha = os.getenv("SENHA-ADMIN")
        
        usuarios = Usuario.objects.filter(email=email)
        if not usuarios:
            Usuario.objects.create_superuser(username='admin', email=email, password=senha, is_active=True, is_staff=True)
        
    
    
