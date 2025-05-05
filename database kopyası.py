#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 16:33:15 2025

@author: velibilir
"""
import sqlite3

# Veritabanına bağlantı kur
conn = sqlite3.connect('malzeme_takip.db')
cursor = conn.cursor()

# Veritabanı bağlantısı başarılıysa, tabloyu oluşturabiliriz


