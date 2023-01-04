from rest_framework.views import APIView
from rest_framework.response import Response
from customers.models import Profile
from products.models import Product, Category
from .serializers import ProfileSerializer, ProfileEditSerializer, ProductListSerializer, CategoryListSerializer, \
    ProductDetailSerializer
from rest_framework import status
from rest_framework import generics


# customers app api views
class ProfileApiView(APIView):
    def get(self, request, user_id):
        user = Profile.objects.get(id=user_id)
        serializer = ProfileSerializer(instance=user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileEditApiView(APIView):
    def put(self, request, user_id):
        user = Profile.objects.get(id=user_id)
        serializer = ProfileEditSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# products app api views

class ProductListApiView(generics.ListAPIView):
    queryset = Product.objects.filter(is_available=True)
    serializer_class = ProductListSerializer


class CategoryListApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class ProductDetailApiView(APIView):
    def get(self, request, product_id, slug_product):
        product = Product.objects.get(id=product_id, slug=slug_product)
        serializer = ProductDetailSerializer(instance=product)
        return Response(serializer.data, status=status.HTTP_200_OK)

# orders app api views
