"""Project common utils."""
from django.db import connection


def queries_count(func):
    """Check DB connections count during function execution."""

    def wrapper(*args, **kwargs):
        queries_count_before = len(connection.queries)
        result = func(*args, **kwargs)
        queries_count_after = len(connection.queries)

        print(f'{func.__name__} executed total of {queries_count_after - queries_count_before} queries')

        return result

    return wrapper
