# core/models.py
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
    
    # Stockage des scans (Base64 pour le test ou ImageField en prod)
    photo = models.TextField()
    recto_scan = models.TextField()
    verso_scan = models.TextField()

    status = models.CharField(
        max_length=20, 
        choices=CINStatus.choices, 
        default=CINStatus.PENDING
    )
    revision_note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cin_number} - {self.last_name}"