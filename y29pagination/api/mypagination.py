from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import CursorPagination

# for scratch create class for pagination
class MyPageNumberPagination(PageNumberPagination):
    # give size in one page how many api there 
    page_size=5
    # to change page instead of other txt in link
    page_query_param = 'p'

    page_size_query_param='records'

class MyLimitOffsetPagination(LimitOffsetPagination):
    # it tell default page limit
    default_limit = 5
    # limit_query_param = 'limitm'


class MyCursorPagination(CursorPagination):
    page_size = 4
    # api ordering according to field
    ordering = 'name'