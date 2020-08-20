from django.db import models
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, NumberAttribute, UnicodeSetAttribute, UTCDateTimeAttribute
)


class Search(Model):
    class Meta:
        table_name = 'Search'
        # Specifies the region
        region = 'us-west-1'
        # Optional: Specify the hostname only if it needs to be changed from the default AWS setting
        host = 'http://localhost:8000'
        # Specifies the write capacity
        write_capacity_units = 10
        # Specifies the read capacity
        read_capacity_units = 10

    search_id = NumberAttribute(hash_key=True)
    search_query = UnicodeAttribute(range_key=True)
    searched_at = UnicodeAttribute(default='')
    

if not Search.exists():
    Search.create_table(wait=True)