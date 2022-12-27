from encroachment_app.models import Encroachment_table
from rest_framework import serializers

class EncroachmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Encroachment_table
        fields = ['encrt_id', 'status', 'region','subregion','encrt_size','dist_coa','criticality']