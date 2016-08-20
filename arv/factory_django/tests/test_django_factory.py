# -*- coding: utf-8 -*-

# $Id:$


from django.test import TestCase
# import pytest
from arv.factory.api import Gen
from arv.factory.api import lazy

from ..django_model_factory import DjangoFactory
# When using relative model imports I get: Conflicting models in
# application
from tests.models import PersonModel
from tests.models import PetModel


class TestDjangoFactory(TestCase):

    def setUp(self):
        class PetFactory(DjangoFactory):
            defaults = {
                "name": lazy(Gen, ["rocky", "tobby", "bailey", "max"]),
            }
            constructor = PetModel

        class PersonFactory(DjangoFactory):
            defaults = {
                "name": lazy(Gen, ["bob", "alice", "ann"]),
                "pet": PetFactory,
            }
            constructor = PersonModel

        self.PetFactory = PetFactory
        self.PersonFactory = PersonFactory
        self.pet_factory = PetFactory()
        self.person_factory = PersonFactory()

    def test_object_gets_persisted(self):
        self.assertFalse(PetModel.objects.exists())
        pet = self.pet_factory.make()
        self.assertEqual(PetModel.objects.count(), 1)
        new_pet = PetModel.objects.all()[0]
        self.assertEqual(pet.id, new_pet.id)
        self.assertEqual(pet.name, new_pet.name)

    def test_subobject_gets_persisted(self):
        self.assertFalse(PersonModel.objects.exists())
        self.assertFalse(PetModel.objects.exists())

        person = self.person_factory.make()

        self.assertEqual(PersonModel.objects.count(), 1)
        new_person = PersonModel.objects.all()[0]
        self.assertEqual(person.id, new_person.id)
        self.assertEqual(person.name, new_person.name)

        self.assertEqual(PetModel.objects.count(), 1)
        new_pet = PetModel.objects.all()[0]
        self.assertEqual(person.pet.id, new_pet.id)
        self.assertEqual(person.pet.name, new_pet.name)
