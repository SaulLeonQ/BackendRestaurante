##from django.shortcuts import get_object_or_404
##from Aplication.models import Restaurant
##
##class TenantMiddlewaremodels:
##    def __init__(self, get_response):
##        self.get_response = get_response
##
##    def __call__(self, request):
##        restaurant_id = request.GET.get('restaurant_id')
##        request.restaurant = get_object_or_404(Restaurant, id=restaurant_id)
##
##        return self.get_response(request)
