from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from core.models import CIN, CINStatus

def dashboard(request):
    """Affiche la liste des dossiers à valider."""
    dossiers = CIN.objects.filter(status=CINStatus.PENDING).order_by('created_at')
    return render(request, 'controller/dashboard.html', {'dossiers': dossiers})

def examine_cin(request, pk):
    """Vue détaillée pour comparer les scans et les données."""
    cin = get_object_or_404(CIN, id=pk)
    return render(request, 'controller/examine.html', {'cin': cin})

def action_validate(request, pk):
    """Action de validation finale."""
    if request.method == 'POST':
        cin = get_object_or_404(CIN, id=pk)
        cin.status = CINStatus.VALIDATED
        cin.validated_at = timezone.now()
        cin.save()
        return redirect('controller:dashboard')