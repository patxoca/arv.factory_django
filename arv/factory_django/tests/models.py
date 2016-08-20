# -*- coding: utf-8 -*-

# $Id:$

from django.db import models


class PetModel(models.Model):

    name = models.CharField(
        max_length=10,
        null=False,
        blank=False,
    )

    class Meta:
        app_label = "tests"


class PersonModel(models.Model):
    """ParentModel
    """

    name = models.CharField(
        max_length=10,
        null=False,
        blank=False,
    )

    pet = models.ForeignKey(
        PetModel,
        null=False,
        blank=False,
    )

    class Meta:
        app_label = "tests"
