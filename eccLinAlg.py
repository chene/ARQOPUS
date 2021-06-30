# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 19:32:28 2021

@author: Elvis C.S. Chen
chene@robarts.ca
"""


import numpy as np
import numpy.matlib
import math

def rotx3x3(angle):
    """
    
    Parameters
    ----------
    angle : 
        angle in radian

    Returns
    -------
    a 3x3 rotation matrix about x-axis by an amount "angle"

    """
    ca = math.cos(angle)
    sa = math.sin(angle)
    m = np.array([[1,0,0],[0, ca, -sa], [0, sa, ca]])
    return m

def rotx4x4(angle):
    """
    

    Parameters
    ----------
    angle : 
        angle in radian

    Returns
    -------
     a 4x4 rotation matrix about x-axis by an amount "angle"

    """
    m = np.identity(4);
    m[0:3,0:3]=rotx3x3(angle)
    return m

def roty3x3(angle):
    """
    
    Parameters
    ----------
    angle : 
        angle in radian

    Returns
    -------
    a 3x3 rotation matrix about y-axis by an amount "angle"

    """
    ca = math.cos(angle)
    sa = math.sin(angle)
    m = np.array([[ca,0,sa],[0,1,0],[-sa,0,ca]])
    return m

def roty4x4(angle):
    """

    Parameters
    ----------
    angle : 
        angle in radian.

    Returns
    -------
    a 4x4 rotation matrix about y-axis by an amount "angle"

    """
    m = np.identity(4)
    m[0:3,0:3] = roty3x3(angle)
    return m

def rotz3x3(angle):
    """

    Parameters
    ----------
    angle : 
        angle in radian

    Returns
    -------
    a 3x3 rotation matrix about z-axis by an amoung "angle"

    """
    ca = math.cos(angle)
    sa = math.sin(angle)
    m = np.array([[ca, -sa, 0], [sa, ca, 0], [ 0, 0, 1]])
    return m

def rotz4x4(angle):
    """

    Parameters
    ----------
    angle : 
        angle in radian

    Returns
    -------
    a 4x4 rotation matrix about z-axis by an amoung "angle"

    """
    m = np.identity(4)
    m[0:3,0:3] = rotz3x3(angle)
    return m


def qnorm( qin ):
    """

    Parameters
    ----------
    qin : 
        4x1 input quaternion

    Returns
    -------
    TYPE
        4x1 normalized quaternion

    """
    return qin/np.linalg.norm(qin)

def q2m3x3( qin ):
    """
    
    Parameters
    ----------
    qin : 
        4x1 quaternion ([x,y,z,w])

    Returns
    -------
    3x3 rotation matrix

    """
    q = qnorm( qin )
    m = np.identity(3)
    xx = q[0]*q[0]
    yy = q[1]*q[1]
    zz = q[2]*q[2]

    xy = q[0]*q[1]
    xz = q[0]*q[2]
    
    yz = q[1]*q[2]
    
    wx = q[3]*q[0]
    wy = q[3]*q[1]
    wz = q[3]*q[2]
    
    m[0,0] = 1 - 2 * (yy + zz);
    m[0,1] = 2 * (xy - wz);
    m[0,2] = 2 * (xz + wy);
    
    m[1,0] = 2 * (xy + wz);
    m[1,1] = 1 - 2 * (xx + zz);
    m[1,2] = 2 * (yz - wx);
    
    m[2,0] = 2 * (xz - wy);
    m[2,1] = 2 * (yz + wx);
    m[2,2] = 1 - 2 * (xx + yy);
    return m
    
def m3x32q(m):
    """

    Parameters
    ----------
    m : 
        a 3x3 matrix

    Returns
    -------
    a quaternion of 4x1 that represents the same rotation as the input 3x3

    """
    T = 1.0 + m[0,0] + m[1,1] + m[2,2]
    
    if T > 0.000000001:
        S = math.sqrt(T)*2
        X = ( m[2,1] - m[1,2] )/ S
        Y = ( m[0,2] - m[2,0] )/ S
        Z = ( m[1,0] - m[0,1] )/ S
        W = .25 * S
    else:
        if ( m[0,0] > m[1,1] and m[0,0] > m[2,2] ):
            S = math.sqrt( 1.0 + m[0,0] - m[1,1] - m[2,2]) * 2
            X = 0.25 * S
            Y = ( m[1,0] + m[0,1] ) / S
            Z = ( m[0,2] + m[2,0] ) / S
            W = ( m[2,1] - m[1,2] ) / S
        elif ( m[1,1] > m[2,2] ):
            S = math.sqrt( 1 + m[1,1] - m[0,0] - m[2,2] ) * 2
            X = ( m[1,0] + m[0,1] ) / S
            Y = 0.25 * S
            Z = ( m[2,1] + m[1,2] ) / S
            W = ( m[0,2] - m[2,0] ) / S
        else:
            S = math.sqrt( 1 + m[2,2] - m[0,0] - m[1,2] ) * 2
            X = ( m[0,2] + m[2,0] ) / S
            Y = ( m[2,1] + m[1,2] ) / S
            Z = .25 * S
            W = ( m[1,0] - m[0,1] ) / S
    return np.array([[X],[Y],[Z],[W]])
