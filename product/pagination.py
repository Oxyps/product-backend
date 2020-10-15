from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
	page_size = 10
	page_query_param= 'page'

	def get_next_link(self):
		if not self.page.has_next():
			return None
		return self.page.next_page_number()

	def get_previous_link(self):
		if not self.page.has_previous():
			return None
		return self.page.previous_page_number()

	def get_paginated_response(self, data):
		return Response({
			'next_page': self.get_next_link(),
			'prev_page': self.get_previous_link(),
			'page_size': self.page_size,
			'count_results': self.page.paginator.count,
			'results': data
		})