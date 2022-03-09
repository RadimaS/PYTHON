from rest_framework import serializers, viewsets


class DualSerializerViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
