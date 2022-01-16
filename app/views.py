from django.shortcuts import render

from app.models import Counter

# Create your views here.


def index(request):
    objs = Counter.objects.all()

    return render(request, 'app/index.html', {'objs': objs})
