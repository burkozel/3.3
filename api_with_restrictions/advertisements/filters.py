from django_filters import rest_framework as filters
from advertisements.models import Advertisement
from api_with_restrictions.advertisements.models import AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    status = filters.ChoiceFilter(choices=AdvertisementStatusChoices.choices)
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ("status", "created at")
