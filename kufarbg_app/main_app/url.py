from django.urls import path

from kufarbg_app.main_app.views.generic import ShowHomeView, ShowContactView
from kufarbg_app.main_app.views.users import CreateDestinationView, DestinationsView, DestinationDetailsView, \
    MyDestinationDetailsView, DestinationCommentView

urlpatterns = (
    path('', ShowHomeView.as_view(), name='show home'),
    path('contacts/', ShowContactView.as_view(), name='contacts'),
    path('create_destination/', CreateDestinationView.as_view(), name='create destination'),
    path('dashboard/', DestinationsView.as_view(), name='dashboard'),
    path('<int:pk>/trip_details/', DestinationDetailsView.as_view(), name='destination details'),
    path('my_destinations/', MyDestinationDetailsView.as_view(), name='my destinations'),
    path('<int:pk>/comment_destination/', DestinationCommentView.as_view(), name='comment destination'),
)
