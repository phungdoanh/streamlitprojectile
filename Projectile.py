#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 13:06:47 2022

@author: namnguyen
"""

#%%
import numpy as np
import math
import streamlit as st
from math import pi, cos, sin
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
import pandas as pd
import os



 #%%
def myDict(u,theta):
     g = 9.8
     theta = np.deg2rad(theta)
     t_flight = 2*u*math.sin(theta)/g
     
     T=[]
     X=[]
     Y=[]
     N=101
     for i in range(N):
         t=(t_flight/(N-1))*i 
         T.append(t)
         x = u*math.cos(theta)*t
         X.append(x)
         y = u*math.sin(theta)*t - 0.5*g*t**2
         Y.append(y)
      
     xdict= {'t':T, 'x': X, 'y': Y} 
     return xdict
 

    
#%%  
def nA(u, theta):
    g = 9.8
    theta = np.deg2rad(theta)
    t_flight = 2*u*np.sin(theta)/g
    t = np.linspace(0, t_flight, 100)
    x = u*np.cos(theta)*t
    y = u*np.sin(theta)*t - 0.5*g*t**2
    
    my_array=np.array([t,x,y])
       
    return my_array


#%%  
def dF(u, theta):
    g = 9.8
    theta = np.deg2rad(theta)
    t_flight = 2*u*np.sin(theta)/g
    t = np.linspace(0, t_flight, 100)
    x = u*np.cos(theta)*t
    y = u*np.sin(theta)*t - 0.5*g*t**2
    
    df=pd.DataFrame({'t': t, 'x': x, 'y': y})
    df.set_index('t')
    df.style.highlight_max(color = 'red', axis = 0)
    def highlight_max(s):
        is_max = s == s.max()
        return ['color: red' if cell else '' for cell in is_max]
  
    final_df=df

    return final_df




#%%
 
#def myPlots(var, color='red',path= 'projectile.gif', name='abc'):
def myPlots(var, color='red', name='abc'):    
    ## transform the var ( container) into list for plotting
    if type(var)== np.ndarray:
        #print('To be developed!')
        #pass
        t=var[0]
        x=var[1]
        y=var[2]
    elif type(var)==dict:
        t=var['t']
        x=var['x']
        y=var['y']
    elif type(var)==pd.DataFrame:
        t=var['t']
        x=var['x']
        y=var['y']
    else:
        print('Out of range')        
        
  
   
    ## Plotting 
    fig, ax = plt.subplots()
    line, = ax.plot(x, y, color=color, label=name)
    circle = plt.Circle((0.1, 0.1), radius=np.sqrt(0.01))
    ax.add_patch(circle)
    time_text=ax.text(0.65,0.95,'',fontsize=15,transform=ax.transAxes, bbox=dict(facecolor='white',edgecolor='black'))

    def update(time, x, y, line, circle):
        line.set_data(x[:time], y[:time])
        circle.center = x[time],y[time]
        line.axes.axis([0, max(np.append(x,y)), 0, max(np.append(x,y))])
        
        return line,circle
    plt.plot(x,y, color=color, label=name)   
    plt.xlabel('Distance [m]')
    plt.ylabel('Height [m]')
    plt.legend()
   

    #ani = animation.FuncAnimation(fig,     update, len(x), fargs=[x, y, line, circle],
     #                             interval=25, blit=True)
  
    #ani.save(path,writer='pillow', fps=100,dpi=200)

    plt.show()
    

#%%    
#myPlots(var=myDict(20, 40),color='blue')


#myPlots(var=nA(49, 60),color='green')


#myPlots(var=dF(20, 40),color='purple')





 
 








    