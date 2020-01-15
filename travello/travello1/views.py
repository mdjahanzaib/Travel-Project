from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
  # dest1= Destination()
  # dest1.name='Hunza'
  # dest1.price=1200
  # dest1.desc='Beauty of Pakistan'
  # dest1.img='destination_6.jpg'
  # dest1.offer= False


  # dest2= Destination()
  # dest2.name='Gilgit'
  # dest2.price=1500
  # dest2.desc='Beauty of Pakistan'
  # dest2.img='destination_5.jpg'
  # dest2.offer= False


  # dest3= Destination()
  # dest3.name='Skardu'
  # dest3.price=1600
  # dest3.desc='Beauty of Pakistan'
  # dest3.img='destination_4.jpg'
  # dest3.offer= True


  # dest4= Destination()
  # dest4.name='Sawat'
  # dest4.price=2000
  # dest4.desc='Beauty of Pakistan'
  # dest4.img='destination_3.jpg'
  # dest4.offer= False

  # dest5= Destination()
  # dest5.name='Neelum Valley'
  # dest5.price=2200
  # dest5.desc='Beauty of Pakistan'
  # dest5.img='destination_2.jpg'
  # dest5.offer= True


  # dest6= Destination()
  # dest6.name='Khunjarab'
  # dest6.price=2500
  # dest6.desc='Beauty of Pakistan'
  # dest6.img='destination_1.jpg'
  # dest6.offer= False

  # Dests=[dest1,dest2,dest3,dest4,dest5,dest6]
  Dests=Destination.objects.all()


  return render(request, 'index.html',{'Dests':Dests})
