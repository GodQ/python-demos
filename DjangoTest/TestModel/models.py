from django.db import models

# Create your models here.

from mongoengine import *


# Create your models here.
class Poem(Document):
    # poem
    meta = {
        'collection': 'poem_data'
    }
    poem_id = SequenceField(required=True, primary_key=True)
    author = StringField()
    title = StringField()

    @queryset_manager
    def show_newest(doc_cls, queryset):
        return queryset.order_by('-poem_id')

