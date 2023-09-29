from all_import.all_import import *

# Create your views here.
def delete_tahseel(request):
    tahseel.objects.all().delete()
    return redirect('account:dashboard')