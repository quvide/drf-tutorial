from django.conf.urls import url, include

urlpatterns = [
    url(r"^", include("snippets.urls")),
    url(r"^api-auth/", include("rest_framework.urls"))
]
