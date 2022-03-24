import math

from rest_framework import pagination
from rest_framework.response import Response


class PageNumberPagination(pagination.PageNumberPagination):
    page_size = 20

    def paginate_queryset(self, queryset, request, view=None):
        self.page_size = int(request.GET.get('objectCount', self.page_size))
        return super(PageNumberPagination, self).paginate_queryset(queryset, request, view=view)

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'page_count': math.ceil(self.page.paginator.count / self.page_size),
            'results': data
        })


class WorkExamplesPagination(PageNumberPagination):
    page_size = 3
