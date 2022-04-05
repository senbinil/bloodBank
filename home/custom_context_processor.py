from location.models import District


def district_render(request):
    return{'kl_district':District.objects.all(),}