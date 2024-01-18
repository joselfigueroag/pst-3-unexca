from django.urls import path

from .views import home, country_detail_view, state_detail_view, municipality_detail_view


urlpatterns = [
    path("home/", home, name="home"),
    path("api/countries/<int:country_id>/", country_detail_view, name="country_detail"),
    path("api/states/<int:state_id>/", state_detail_view, name="state_detail"),
    path("api/municipalities/<int:municipality_id>/", municipality_detail_view, name="municipality_detail"),
]
