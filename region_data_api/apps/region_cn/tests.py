# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import Region


class RegionModelTest(TestCase):
    def setUp(self):
        self.parent = Region.objects.create(code="110000", name="省")

    def test_create_method(self):
        region = Region.objects.create(code="110101", name="市", parent_id=1)
        self.assertEqual(region.parent.id, 1)
        self.assertEqual(region.parent.code, "110000")
        self.assertEqual(region.parent.name, "省")
        self.assertEqual(region.id, 2)
        self.assertEqual(region.name, "市")
        self.assertEqual(region.code, "110101")
