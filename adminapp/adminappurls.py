from django.urls import path
from . import views
urlpatterns=[
    path('adminhome/',views.adminhome,name='adminhome'),
    path('viewenquiry/',views.viewenquiry,name='viewenquiry'),
    path('viewclass.html/',views.viewclass,name='viewclass'),
    path('addclass.html/',views.addclass,name='addclass'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
    path('addsubject/',views.addsubject,name='addsubject'),
    path('viewsubject/',views.viewsubject,name='viewsubject'),
    path('delenq/<id>',views.delenq,name='delenq'),
    path('delclass/<id>',views.delclass,name='delclass'),
    path('delsubject/<id>',views.delsubject,name='delsubject'),
    path('editclass/<id>',views.editclass,name='editclass'),
    path('editsub/<id>',views.editsub,name='editsub'),
    path('addteacher/',views.addteacher,name='addteacher'),
    path('viewteacher/',views.viewteacher,name='viewteacher'),
    path('delteacher/<id>',views.delteacher,name='delteacher'),
    path('addstudent/',views.addstudent,name='addstudent'),
    path('viewstudent/',views.viewstudent,name='viewstudent'),
    path('addnoti/',views.addnoti,name='addnoti'),
    path('viewnoti/',views.viewnoti,name='viewnoti'),
]