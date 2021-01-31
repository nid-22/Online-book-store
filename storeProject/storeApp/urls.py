from . import views as v
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.home, name='home' ),
    path('getgenre/<int:id>/', v.get_by_genre ,name='get_by_genre'),
    path('search', v.search_product ,name='search'),
    path('register',v.addUser,name='register'),
    path('login',v.login_view,name='login'),
    path('logout',v.logout_view,name='logout'),
    path('addcart/<int:id>/',v.add_cart,name='addCart'),
    path('order',v.my_order,name='morder'),
    path('cart',v.cart_list,name='crlist'),
    
]
