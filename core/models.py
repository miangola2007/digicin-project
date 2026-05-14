from django.db import models
import uuid

class CINStatus(models.TextChoices):
    PENDING = 'PENDING', 'En attente'
    VALIDATED = 'VALIDATED', 'Validé'
    REVISION = 'REVISION', 'À modifier'

class CIN(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cin_number = models.CharField(max_length=12, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    
    # Données et Scans
    recto_scan = models.TextField() # Stockage Base64
    verso_scan = models.TextField()
    
    # État du dossier
    status = models.CharField(max_length=20, choices=CINStatus.choices, default=CINStatus.PENDING)
    revision_notes = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    validated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.cin_number} - {self.last_name}"