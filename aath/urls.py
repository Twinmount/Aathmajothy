from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index,name="index"),
    path("index",views.index,name="index"),
    path("about",views.about,name="about"),
    path("service_psychiatric_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore",views.service_psychiatric_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore,name="service_psychiatric_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore"),
    path("contact",views.contact,name="contact"),
    path("family_therappy_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore",views.family_therappy_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore,name="family_therappy_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore"),
    path("child_guidance_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore",views.child_guidance_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore,name="child_guidance_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore"),
    path("anxiety_depression_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore",views.anxiety_depression_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore,name="anxiety_depression_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore"),
    path("phobia_treatment_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore",views.phobia_treatment_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore,name="phobia_treatment_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore"),
    path("depression_treatment_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore",views.depression_treatment_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore,name="depression_treatment_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore"),
    path("couple_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore",views.couple_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore,name="couple_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore"),
    path("marriage_therappy_post_marriage_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore",views.marriage_therappy_post_marriage_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore,name="marriage_therappy_post_marriage_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore"),
    path("individual_personal_face_to_face_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore",views.individual_personal_face_to_face_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore,name="individual_personal_face_to_face_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore"),


]
