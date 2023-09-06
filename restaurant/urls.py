from django.urls import path, include
from rest_framework import routers

from .views import homeRestaurant, SingleMenuItemView
from .views import BookingViewSet, UserViewSet, MenuItemsViewSet

router = routers.DefaultRouter() # Defining the DefaultRouter

router.register(r'booking', BookingViewSet)
router.register(r'menu-items', MenuItemsViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('home', homeRestaurant, name="homeRestaurant"),

    path('restaurant/', include(router.urls)), # Routers

    # path('menu', MenuItemsView.as_view(), name='menu-items'),
    # path('menu/<int:pk>', SingleMenuItemView.as_view(), name='single-item'),
    # path('booking', BookingView.as_view(), name='bookings'),
    # path('booking/<int:pk>', BookingSingleView.as_view(), name='bookings-single'),
]


