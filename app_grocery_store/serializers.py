from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import Einkaufsliste


class EinkaufslisteSerializer_GET(ModelSerializer):
    class Meta:
        model = Einkaufsliste
        fields = '__all__'


class EinkaufslisteSerializer_POST(ModelSerializer):
    class Meta:
        model = Einkaufsliste
        fields = [
            'beschreibung',
        ]


class EinkaufslisteSerializer_Anzahl_PUT(ModelSerializer):
    class Meta:
        model = Einkaufsliste
        fields = [
            'anzahl',
        ]


class EinkaufslisteSerializer_Erledigt_PUT(ModelSerializer):
    class Meta:
        model = Einkaufsliste
        fields = [
            'erledigt',
        ]
