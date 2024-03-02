from django.urls import path

from .views import (
    home,
    country_detail_view,
    state_detail_view,
    municipality_detail_view,
    stats,
    pie_chart_varones_hembras,
    bar_char_cuadro_honor,
)


urlpatterns = [
    path("home/", home, name="home"),
    path("stats", stats, name="stats"),
    path("api/countries/<int:country_id>/", country_detail_view, name="country_detail"),
    path("api/states/<int:state_id>/", state_detail_view, name="state_detail"),
    path(
        "api/municipalities/<int:municipality_id>/",
        municipality_detail_view,
        name="municipality_detail",
    ),
    path(
        "stats/pie_chart_data/",
        pie_chart_varones_hembras,
        name="pie_chart_varones_hembras",
    ),
    path("stats/bar_chart_data/", bar_char_cuadro_honor, name="cuadro-honor"),
]
