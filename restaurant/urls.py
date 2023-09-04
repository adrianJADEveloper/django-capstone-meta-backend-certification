from django.urls import path, include
from rest_framework import routers

from .views import homeRestaurant, MenuItemsView, SingleMenuItemView
from .views import BookingViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'booking', BookingViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', homeRestaurant, name="homeRestaurant"),
    path('menu', MenuItemsView.as_view(), name='menu-items'),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name='single-item'),
    # path('booking', BookingView.as_view(), name='bookings'),
    # path('booking/<int:pk>', BookingSingleView.as_view(), name='bookings-single'),

    path('restaurant/', include(router.urls)), # Routers
]

