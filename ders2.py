#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 08:35:30 2025

@author: velibilir
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#verileri yükleme
veriler=pd.read_csv("eksikveriler.txt")
  
print(veriler)

#veri işleme
boy=veriler[['boy']]
print(boy)

boykilo=veriler[['boy','kilo']]
print(boykilo)