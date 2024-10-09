from django.urls import path
from main.views import show_main, show_xml, create_orenji_entry, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user
from main.views import edit_orenji_entry, delete_orenji_entry
from main.views import add_orenji_entry_ajax
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
    path('edit-orenji-entry/<str:id>/', edit_orenji_entry, name='edit_orenji_entry'),
    path('delete-orenji-entry/<str:id>/', delete_orenji_entry, name='delete_orenji_entry'),
    path('create-orenji-entry-ajax', add_orenji_entry_ajax, name='add_orenji_entry_ajax'),
]


