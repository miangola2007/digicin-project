from django.shortcuts import render, get_object_or_404, redirect
from core.models import CIN, CINStatus

def dashboard(request):
    pending_cins = CIN.objects.filter(status=CINStatus.PENDING)
    return render(request, 'controller/dashboard.html', {
        'cins': pending_cins,
        'pending_count': pending_cins.count()
    })

def examine(request, pk):
    cin = get_object_or_404(CIN, pk=pk)
    if request.method == 'POST':
        # Logique de validation ici
        pass
    return render(request, 'controller/examine.html', {'cin': cin})