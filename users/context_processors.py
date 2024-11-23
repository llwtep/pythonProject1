from .models import CustomUser

def user_context_processor(request):
    users = CustomUser.objects.all()
    return {'users': users}