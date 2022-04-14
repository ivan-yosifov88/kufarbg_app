from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from kufarbg_app.main_app.models import Destinations, Likes


@login_required
def like_destination(request, pk):
    destination = Destinations.objects.get(pk=pk)
    if request.user.is_authenticated:
        like = Likes.objects.filter(user_id=request.user.id).filter(trip_id=pk)
        if like:
            like.delete()
        else:
            Likes.objects.create(user_id=request.user.id, trip_id=destination.id)

    return redirect('dashboard')
