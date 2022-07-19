from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def prtform_create(self, serializer):
        print(serializer.validate_data)
        title = serializer.validate_data.get('title')
        content = serializer.validate_data.get('content')
        # or None
        if content is None:
            content = title
        serializer.save(content=content)


product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_list_view = ProductListAPIView.as_view()

@api_view(['GET','POST'])
def product_alt_view(request, *args, **kwargs):
    method = request.method

    if method == "GET":
        pass
        queryset=Product.objects.all()
        data=ProductSerializer(queryset,many=True).data
        return Response(data)

    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid (raise_exception=True):
            print(serializer.data)
            return Response(serializer.data)
    return Response({"invalid" : "invalid error"}, status=400)
