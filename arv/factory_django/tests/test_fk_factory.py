# -*- coding: utf-8 -*-

# $Id:$

from __future__ import unicode_literals

from django.test import TestCase
from arv.factory.api import Factory
from arv.factory.api import gen

from ..django_model_factory import DjangoFactory
from ..django_model_factory import fk_factory
from tests.models import PetModel


class TestFkFactory(TestCase):

    def setUp(self):
        class PetFactory(DjangoFactory):
            defaults = {
                "name": gen.lazy(gen.Gen, ["rocky", "tobby", "bailey", "max"]),
            }
            constructor = PetModel
        self.PetFactory = PetFactory

    def assertPetModel(self, pk, name):
        if not PetModel.objects.filter(pk=pk).exists():
            self.fail("Model '%s' does not exists." % pk)
        model = PetModel.objects.get(pk=pk)
        self.assertEqual(model.name, name)

    def assertPetModelExists(self, pk):
        if not PetModel.objects.filter(pk=pk).exists():
            self.fail("Model '%s' does not exists." % pk)

    def test_returns_something_that_looks_like_a_primary_key(self):
        pkf = fk_factory(self.PetFactory)
        p_1 = next(pkf)
        self.assertIsNotNone(p_1)
        self.assertPetModelExists(p_1)
        p_2 = next(pkf)
        self.assertIsNotNone(p_2)
        self.assertPetModelExists(p_2)
        self.assertNotEqual(p_1, p_2)

    def test_uses_factory_class(self):
        pkf = fk_factory(self.PetFactory)
        self.assertPetModel(next(pkf), "rocky")
        self.assertPetModel(next(pkf), "tobby")

    def test_raisesValueError_if_not_a_DjangoFactory(self):
        class MyFactory(Factory):
            pass

        with self.assertRaisesRegexp(TypeError, ""):
            fk_factory(MyFactory)

    def test_each_fk_factory_has_its_own_surrogate_factory(self):
        pkf_1 = fk_factory(self.PetFactory)
        pkf_2 = fk_factory(self.PetFactory)
        p = next(pkf_1)
        self.assertPetModel(p, "rocky")
        p = next(pkf_2)
        self.assertPetModel(p, "rocky")

    def test_is_not_safe_in_metafactories(self):
        class MyFactory(Factory):
            defaults = {
                "pet": fk_factory(self.PetFactory)
            }
        factory_1 = MyFactory()
        factory_2 = MyFactory()
        v_1 = factory_1()
        v_2 = factory_2()
        self.assertPetModel(v_1["pet"], "rocky")
        self.assertPetModel(v_2["pet"], "tobby")

    def test_works_with_lazy(self):
        class MyFactory(Factory):
            defaults = {
                "pet": gen.lazy(fk_factory, self.PetFactory)
            }
        factory_1 = MyFactory()
        factory_2 = MyFactory()
        v_1 = factory_1()
        v_2 = factory_2()
        self.assertPetModel(v_1["pet"], "rocky")
        self.assertPetModel(v_2["pet"], "rocky")
