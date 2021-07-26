#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Head and Tails random app

"""

__author__ = 'GM'

import random

toss = random.randint(1, 2)
if toss == "1":
  print("Heads")
else:
  print("Tails")

