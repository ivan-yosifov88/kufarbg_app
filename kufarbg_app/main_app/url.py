from django.urls import path

from kufarbg_app.main_app.views.comments import DestinationCommentView, AllDestinationComments
from kufarbg_app.main_app.views.generic import ShowHomeView, ShowContactView, ShowAboutView
from kufarbg_app.main_app.views.destinations import CreateDestinationView, DestinationsView, DestinationDetailsView, \
    MyDestinationDetailsView, EditDestinationView, \
    DeleteDestinationView
from kufarbg_app.main_app.views.likes import like_destination

urlpatterns = (
    path('create_destination/', CreateDestinationView.as_view(), name='create destination'),
    path('<int:pk>/edit_destination/', EditDestinationView.as_view(), name='edit destination'),
    path('<int:pk>/delete_destination/', DeleteDestinationView.as_view(), name='delete destination'),
    path('dashboard/', DestinationsView.as_view(), name='dashboard'),
    path('<int:pk>/trip_details/', DestinationDetailsView.as_view(), name='destination details'),
    path('my_destinations/', MyDestinationDetailsView.as_view(), name='my destinations'),
    path('<int:pk>/comment_destination/', DestinationCommentView.as_view(), name='comment destination'),
    path('<int:pk>/like_destination/', like_destination, name='like destination'),
    path('<int:pk>/all_comments/', AllDestinationComments.as_view(), name='all destination comments'),
    path('', ShowHomeView.as_view(), name='show home'),
    path('contacts/', ShowContactView.as_view(), name='contacts'),
    path('about/', ShowAboutView.as_view(), name='about us')
)
