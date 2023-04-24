from django.http import HttpResponse
from .models import Teachers


# Если не использовать html
def generate_teachers(request):
    teachers = Teachers.objects.all()
    teachers_str = " | ".join(
        [
            f"{teacher.first_name} {teacher.last_name}, subject: {teacher.subject}"
            for teacher in teachers
        ]
    )
    return HttpResponse(teachers_str)
