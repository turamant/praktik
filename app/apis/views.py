from rest_framework.generics import ListAPIView

from apis.serializers import NewSerializer
from web_admin.models import New


class GetListAllNew(ListAPIView):
    serializer_class = NewSerializer

    def get_queryset(self):
        return New.objects.all()
