from django.contrib import admin
from django.urls import path,include
from tickets import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
router=DefaultRouter()
router.register('guests',views.viewsets_guest)
router.register('movies',views.viewsets_movie)
router.register('reservations',views.viewsets_reservations)

urlpatterns = [
    path('admin/', admin.site.urls),
    # GET & POST Fome Rest Framwork Function Based View @api_view 
    path('fbvlist/',views.FBV_list),
    #GET & PUT & DELETE Fome Rest Framwork Function Based View VIEW @api_view 
    path('fbv_pk/<int:pk>',views.fbv_pk),
    #GET & Post From Rest Framwork Class Based View @API_VIEW 
    path('cbv/',views.Cbv.as_view()),
    #GET & PUT & DELETE From Rest Framwork Class Based View @API_VIEW
    path('cbv_pk/<int:pk>',views.Cbv_pk.as_view()),
    #GET & Post From Rest Framwork Class Based View mixins
    path('misins/',views.mixins_list.as_view()),
    #GET & PUT & DELETE From Rest Framwork Class Based View mixins
    path('misins_pk/<int:pk>',views.mixins_pk.as_view()),
    #GET & Post From Rest Framwork Class Based View generics
    path('generics/',views.genericslist.as_view()),
    #GET & PUT & DELETE From Rest Framwork Class Based View generics
    path('generics_pk/<int:pk>',views.generics_pk.as_view()),
    #GET & Post From Rest Framwork Class Based View viewsets
    path('viewsets/',include(router.urls)),
    #GET & PUT & DELETE From Rest Framwork Class Based View viewsets
    #search
    path('search/',views.search),
    #new reservations
    path('newresvations',views.new_reservations),
    path('api-auth',include('rest_framework.urls')),
    #token
    path('token-auth',obtain_auth_token),


]
