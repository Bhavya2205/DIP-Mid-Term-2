# -- coding: utf-8 --

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
   <div class="" style="background-color:orange;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Poornima Institute of Engineering & Technology</p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">Mid Term 2 Practical</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)
  
st.title("""
        Mathematical Operations
         """
         )
file1= st.file_uploader("Please upload image", type=("jpg", "png"))
file2= st.file_uploader("Please upload image", type=("jpg", "png"))
Operation = st.selectbox("Operations: ",
                     ['+', '-', '*','/'])

import cv2
from  PIL import Image, ImageOps
def apply_transform(img1_data, img2_data):
  #img = image.load_img(image_data, target_size=(224, 224))
  #image = image.img_to_array(img)
  #img_reshap= np.expand_dims(image, axis=0)
  #img_reshap = preprocess_input(img_reshap)
   
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
  st.image(img, use_column_width=True)
  return 0
if file is None:
  st.text("Please upload an Image file")
else:
  file_bytes1 = np.asarray(bytearray(file1.read()), dtype=np.uint8)
  img1 = cv2.imdecode(file_bytes1, 1)
  st.image(file,caption='Uploaded Image.', use_column_width=True)

  file_bytes2 = np.asarray(bytearray(file2.read()), dtype=np.uint8)
  img2 = cv2.imdecode(file_bytes2, 1)
  st.image(file,caption='Uploaded Image.', use_column_width=True)
    
if st.button("Apply Transformation"):
  result=apply_transform(img1, img2)
  
if st.button("About"):
  st.header("Bhavya Maheshwari")
  st.subheader("PIET18CS036")
html_temp = """
   <div class="" style="background-color:orange;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:20px;color:white;margin-top:10px;">DIP Midterm 2</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)
