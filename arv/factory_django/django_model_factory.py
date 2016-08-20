# -*- coding: utf-8 -*-

from arv.factory.api import Factory
from arv.factory.persistance import PersistanceMixin
from django.db.models import Model


class DjangoFactory(PersistanceMixin, Factory):
    """Factory for creating django models.
    """

    def _get_fields(self, obj):
        for f in obj._meta.get_fields():
            try:
                # ignore internal fields like ManyToOneRel
                yield f.name, getattr(obj, f.name)
            except AttributeError:
                pass

    def _is_persistable(self, obj):
        return isinstance(obj, Model)

    def _link_to_parent(self, parent, name, child):
        setattr(parent, name + "_id", child.pk)

    def _save(self, obj):
        obj.save()
        return obj
