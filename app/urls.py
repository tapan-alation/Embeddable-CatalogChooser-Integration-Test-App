from django.conf.urls import url
from views import catalog_chooser
from views import register
from views import alation_object_receiver


urlpatterns = [
    url(r'^register_opener/', register.RegisterOpenerView.as_view()),
    url(r'^alation_object_receiver/', alation_object_receiver.endpoint),
    url(r'^catalog_chooser/', catalog_chooser.CatalogChooserView.as_view())
]
