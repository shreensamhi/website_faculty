from django.urls import path
from . import views

urlpatterns =[
    path('',views.chooseproject,name='chooseproject'),
    path('homepage1',views.homepage1,name='homepage1'),
    path('activestudent',views.activestudent,name='activestudent'),
    path('homepage',views.homepage,name='homepage'),
    path('page1',views.page1,name='page1'),
    path('page2',views.page2, name='page2'),
    path('page3',views.page3,name='page3'),
    path('page4',views.page4, name='page4'),
    path('page5',views.page5,name='page5'),
    path('cs',views.cs,name='cs'),
    path('cscourse',views.cscourse,name='cscourse'),
    path('ds',views.ds,name='ds'),
    path('dscourse',views.dscourse, name='dscourse'),
    path('generalcourse',views.generalcourse,name='generalcourse'),
    path('IS',views.IS, name='is'),
    path('iscourse',views.iscourse,name='iscourse'),
    path('it',views.it, name='it'),
    path('itcourse',views.itcourse,name='itcourse'),
    path('delete/<int:id>',views.delete, name ='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),


]