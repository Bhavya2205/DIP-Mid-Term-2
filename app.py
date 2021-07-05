# -*- coding: utf-8 -*-
"""APP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bYctHNtzbRgU5BCaKEQnydltnYShb_0j
"""

import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import tensorflow as tf
#from keras.preprocessing import image
import os
from werkzeug.utils import secure_filename
st.set_option('deprecation.showfileUploaderEncoding', False)
#from keras.models import load_model

html_temp = """
   <div class="" style="background-color:blue;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Poornima Institute of Engineering & Technology</p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">Digital Image Processing Lab</p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">Mid Term 2 Practical</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)
  
st.title("""
        Mathematical Operations on the Images
         """
         )
file= st.file_uploader("Please upload image", type=("jpg", "png"))
Operation = ' ' #@param ["+", "-", "*", "/"] {allow-input: true}

import cv2
from  PIL import Image, ImageOps
if file is None:
  st.text("Please upload an Image file")
else:
  if Operation=='+':
    print("Added Image")
    img=img1+img2
  if Operation=='-':
    print("Subtracted Image")
    img=img1-img2
  if Operation=='*':
    print("Multipled Image")
    img=img1*img2
  if Operation=='/':
    print("Divided Image")
    img=img1/img2
  cv2_imshow(img)
  
if st.button("About"):
  st.header(" Bhavya Maheshwari")
  st.subheader("PIETCS036")
html_temp = """
   <div class="" style="background-color:orange;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:20px;color:white;margin-top:10px;">Digital Image Processing Practical</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)
