from .models import Application


def get_appications():
    return Application.objects.all()


def generate_admission_number():
    request_count = Application.objects.all().count()

    return f"{(request_count+1):04}"
