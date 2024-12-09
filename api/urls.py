from django.urls import path

from api import views

urlpatterns = [
    path('', views.getData),

    path('user', views.getAllUsers),
    path('user/<int:id>', views.getSingleUser),
    path('user/add', views.addUser),
    path('user/update/<int:id>', views.updateUser),
    path('user/delete/<int:id>', views.deleteUser),

    # Idea CRUD URLs
    path('idea', views.getAllIdeas),
    path('idea/<int:id>', views.getSingleIdea),
    path('idea/add', views.addIdea),
    path('idea/update/<int:id>', views.updateIdea),
    path('idea/delete/<int:id>', views.deleteIdea),

    path('category', views.categoryHandle),
    path('category/<int:id>', views.categoryHandle),


]
