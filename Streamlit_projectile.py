#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 10:42:20 2022

@author: namnguyen
"""

import numpy as np
import math
import streamlit as st
from math import pi, cos, sin
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
import pandas as pd
import os

path= os.getcwd()



st.write(
    """
# 📊 Projectile Motion
Very simple and applicable problem.
"""
)



## The question

st.subheader("Introduction:")

st.write("Considering no air resistance, what is the trajectory followed by a projectile thrown with initial velocity $v_0$ at an angle $\\theta$?")



## The short answer

st.write("The trajectory followed by a projectile thrown with initial velocity $v_0$ at an angle $\\theta$, without air resistance, is:  ")



st.latex(" x(t) = v_0 \\cos(\\theta)t \\\\\\\\")
st.latex("y(t) = v_0 \\sin(\\theta)t - \\frac{1}{2} g t^{2}")



st.subheader("Quizz time!")

st.write("Following the equation above, answer the following question")

st.write("What is the trajectory of a projectile without considering air resistance?")
st.write("- A straight line")
st.write("+ A parabola")
st.write("- A circle")
st.write("- A hyperbola ")       
 
        

st.write("At what angle is obtained the maximal distance?")
st.write("- 15")
st.write("+ 30")
st.write("- 45")
st.write("- 60 ")  
               




#with st.expander("Adjust test parameters"):
st.markdown("### Parameters")


c1, c2 = st.columns([3,1])
dv0 = 1
v0 = c1.slider("Initial Velocity [meters/second]", 
                        min_value=dv0, max_value=100*dv0, 
                        value=50, step=dv0, help="Initial velocity for the projectile")
dtheta = 1
theta_deg = c2.slider("Initial Angle [degrees]", 
                        min_value=5, max_value=90, 
                        value=60, step=5, help="Initial velocity for the projectile")    
    

import Projectile as pj

var1=pj.myDict(v0,theta_deg)
var2=pj.nA(v0,theta_deg)
var3=pj.dF(v0,theta_deg)

#figureStream=pj.myPlots(var=var3,color='red', path='figureStream.gif',  name=r'$v_0=$'+str(v0)+str(', ' ) +r'$\theta=$'+str(theta_deg)+r'$^0$')
figureStream=pj.myPlots(var=var3,color='red',   name=r'$v_0=$'+str(v0)+str(', ' ) +r'$\theta=$'+str(theta_deg)+r'$^0$')
st.set_option('deprecation.showPyplotGlobalUse', False)

st.pyplot(figureStream)
#
st.markdown("### Current Data: "+ r'$v_0=$'+str(v0)+str(', ' ) +r'$\theta=$'+str(theta_deg)+r'$^0$')
my_current_data=st.dataframe(var3)




st.markdown("### Current Data:")

def save_file(fileStr):
    with open (os.path.join("dirctory", fileStr.name),"wb")as f:
        f.write(fileStr.getbuffer())
    return st.success("Saved file: {}in directory.format(fileStr.name)")

savefigure = st.radio(
     "Do you want to save this figure?",
     options=["Yes", "No"],
     help="Mark your option.",
     )
if savefigure == "No":
    st.warning('figure will NOT be saved')
     
if savefigure=="Yes":
   st.warning("Your figure is SAVED")
  #figureStream.save("figure.png")
  
 
 


savedata = st.radio(
     "Do you want to save this data under CSV or Excel file?",
     options=["Yes", "No"],
     help="Mark your option.",
     )
if savedata == "No":
    st.warning('data will NOT be saved')
   
if savedata=="Yes":
   st.warning("Your data will be saved under Excel and CSV")  
   
   var3.to_csv('MyData.csv')
   var3.to_excel('MyData.xlsx')    








