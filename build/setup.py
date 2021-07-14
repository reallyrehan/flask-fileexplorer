# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:17:01 2019

@author: rehan.ahmed
"""

from cx_Freeze import setup, Executable 
  

includefiles = [ ]
includes = ['jinja2.ext']  # add jinja2.ext here
excludes = []

setup(
name = 'WiFile',
version = '1',
description = 'File explorer over wifi',
author = 'Rehan Ahmed',
author_email = 'rhnahdshk@gmail.com',
# Add includes to the options
options = {'build_exe':   {'excludes':excludes,'include_files':includefiles, 'includes':includes}},   
executables = [Executable('setupWin.py')]
)