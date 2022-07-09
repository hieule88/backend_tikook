from rest_framework import serializers
from api.models import TikiNgonItem

class TikiNgonItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TikiNgonItem
        fields = ('ItemID','Name', 'Price', 'Discount', 'Stars', 'NumStarts', 'ImageItem', 'NumBuys', 'InStock', 'Provider', 'Amount', 'Description') 