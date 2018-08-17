# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from arv.factory.api import gen
from arv.factory.api import Factory
from arv.factory.persistance import PersistanceMixin
from django.db import models


class DjangoFactory(PersistanceMixin, Factory):
    """Factory for creating django models.
    """

    def _get_fields(self, obj):
        for f in obj._meta.get_fields():
            if isinstance(f, models.ForeignKey):
                yield f.name, getattr(obj, f.name)

    def _is_persistable(self, obj):
        return isinstance(obj, models.Model)

    def _link_to_parent(self, parent, name, child):
        setattr(parent, name + "_id", child.pk)

    def _save(self, obj):
        obj.save()
        return obj


def fk_factory(factory_class, **kwargs):
    """Factory for creating valid foreign keys.

    This factory function returns a value generator that creates
    models and returns it's primary key. In order to ensure that the
    models get a primary key they are persisted.

    This function will create a factory for the models from
    ``factory_class`` and ``kwargs`` each time it's called. In order
    to use it safely en metafactory definitions (avoiding factory
    sharing among factories) it must be wrapped in a ``lazy`` object.

    """
    if not issubclass(factory_class, DjangoFactory):
        raise TypeError("expected DjangoFactory subclass")

    factory = factory_class(**kwargs)

    def wrapper():
        while True:
            # in order to get a pk we need to persist the object
            model = factory.make()
            yield model.pk
    return gen.Gen(wrapper())
