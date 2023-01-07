
from django.contrib import admin
from django.urls import path, include
from App import views


urlpatterns = [
    # Native path to access the Django admin
    path('admin/', admin.site.urls),
    # Path to access the frontend page
    path('', views.frontend, name='frontend'),

    # Path to login / logout
    path('login/', include('django.contrib.auth.urls')),

    # ----------BACKEND SECTION--------------|

    # Path to access the backend page
    path('backend/', views.backend, name='backend'),

    # Path to add client
    path('add_patient', views.add_patient, name='add_patient'),

    # Path to access client individually
    path('patient/<str:patient_id>', views.patient, name='patient'),

    # Path to edit client
    path('edit_patient', views.edit_patient, name='edit_patient'),

    # Path to delete a  client
    path('delete_patient/<str:patient_id>',
         views.delete_patient, name='delete_patient'),



]
