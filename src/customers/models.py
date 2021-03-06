# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tenant_schemas.models import TenantMixin

class Client(TenantMixin):
    name = models.CharField(max_length=100)
    
    auto_create_schema = True