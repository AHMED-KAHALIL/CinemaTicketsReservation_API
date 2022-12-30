from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Guest,Movie,Reservations
from rest_framework.decorators import api_view
from .serializers import GuestSerializer, MovieSerializer, ReservationSerializer
from rest_framework import serializers,status,filters ,mixins,generics,viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Function based views
@api_view(['GET','POST'])
def FBV_list(request):
    #GET
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializers= GuestSerializer(guests,many=True)
        return Response(serializers.data)
    #POST
    elif request.method =='POST':
        serializer=GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        return Response(serializer.data,status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def fbv_pk(request,pk):
    try:
        guest= Guest.objects.get(pk=pk)
    except Guest.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =='GET':
        serializers = GuestSerializer(guest)
        return Response(serializers.data)
    elif request.method =='PUT':
        serializers= GuestSerializer(guest,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)            

# Class Based View 
# GET & POST
class Cbv(APIView):
    # get & post 
    def get(self,request):
        guests= Guest.objects.all()
        serializers= GuestSerializer(guests,many=True)
        return Response(serializers.data)
    def post(self,request):
        serializers=GuestSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.data,status=status.HTTP_400_BAD_REQUEST)
# GET & PUT # DELETE 
class Cbv_pk(APIView):
    def get_object(self,pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            raise Http404 
    def get(self,requset,pk):
        guest=self.get_object(pk)
        serializers=GuestSerializer(guest)
        return Response(serializers.data)
    def put(self,requset,pk):
        guest=self.get_object(pk)
        serializers=GuestSerializer(guest,data=requset.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.data,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        guest=self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  

#Misins
# GET & POST
class mixins_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Guest.objects.all()
    serializer_class= GuestSerializer
    def get(self,request):
        return self.list(request)
    def post(self , request):
        return self.create(request)
# GET & PUT # DELETE 
class mixins_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Guest.objects.all()
    serializer_class= GuestSerializer
    def get(self,request,pk):
        return self.retrieve(request)
    def put(self , request,pk):
        return self.update(request)
    def delete(self , request,pk):
        return self.destroy(request)    

#Generics
# GET & POST
class genericslist(generics.ListCreateAPIView):
    queryset=Guest.objects.all()
    serializer_class= GuestSerializer
    authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

# GET & PUT # DELETE 
class generics_pk(generics.RetrieveUpdateDestroyAPIView):
       queryset=Guest.objects.all()
       serializer_class= GuestSerializer
       authentication_classes=[TokenAuthentication]
       permission_classes=[IsAuthenticated]
      
class viewsets_guest(viewsets.ModelViewSet):
     queryset=Guest.objects.all()
     serializer_class= GuestSerializer

class viewsets_movie(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    filter_backends=[filters.SearchFilter]
    search_fields=['movie']

class viewsets_reservations(viewsets.ModelViewSet):
    queryset=Reservations.objects.all()
    serializer_class=ReservationSerializer

#search_movies
@api_view(['GET'])
def search(request):
    movies=Movie.objects.filter(movie=request.data['movie'])
    serializer= MovieSerializer(movies,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def new_reservations(request):
       movie=Movie.objects.get(movie=request.data['movie'])
       guest=Guest()
       guest.name=request.data['name']
       guest.mobile=request.data['mobile']
       guest.save()
       reservations=Reservations()
       reservations.guest=guest
       reservations.movie=movie
       reservations.save()  

