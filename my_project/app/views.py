from django.http import HttpResponse
from my_project.app.models import PortComponent


def index(request):
    ports = PortComponent.objects.all()
    response = []
    for port in ports:
        users_text = ', '.join(user.name for user in port.user_set.all())
        response.append(f'<strong>{port.location}</strong>: {users_text or "-"}')

    return HttpResponse('<br>'.join(response))
