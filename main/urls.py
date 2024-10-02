from django.urls import path
from main.views import show_main, show_xml, create_orenji_entry, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('create_orenji_entry/', create_orenji_entry, name='create_orenji_entry'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]


