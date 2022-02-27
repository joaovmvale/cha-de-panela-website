from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "name",
            "section",
            "price",
            "suggested_link",
            "status",
            "image",
            "qr_code",
            "bought",
            "reserved",
            "purchase_limit",
        )