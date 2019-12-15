from rest_framework import serializers
from app1.models import Flats


class FlatSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model=Flats
        fields=('id','hname','city','area','rate')