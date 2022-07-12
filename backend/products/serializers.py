from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    client_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:

        model = Product
        fields = [
                'title',
                'content',
                'price',
                'sale_price',
                'client_discount',
            ]

    def get_client_discount(self, obj):
        try:
            return obj.get_discount()
        except Exception as e:
            print(e)
            return None
