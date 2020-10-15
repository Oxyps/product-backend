from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_query_param= 'page'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'prev': self.get_previous_link()
            },
            'total': self.page.paginator.count,
            'page_size': self.page_size,
            'results': data
        })