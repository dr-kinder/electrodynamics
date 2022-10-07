# -----------------------------------------------------------------------------
# VectorCalculus.py
# ----------------------------------------------------------------------------- 
# Python functions for working with Maxwell's equations.
# Assume a cubic, Cartesian grid throughout.
# Vector derivatives calculated using np.diff.
# Integrals computed by Reimann summation.

import numpy as np
from Electrodynamics import draw_vector_field

# Define Cartesian unit vectors.
eX = np.array([1,0,0])
eY = np.array([0,1,0])
eZ = np.array([0,0,1])


# Gradient
def grad(f,ds):
    """
    f is a numpy array representing a scalar function in 3 dimensions.
    ds is the grid spacing.
    Returns the gradient of f, as a 3D vector field.
    """
    df = [0,0,0]
    # df[0] = np.diff(f,axis=0,append=0) / ds
    # df[1] = np.diff(f,axis=1,append=0) / ds
    # df[2] = np.diff(f,axis=2,append=0) / ds
    df[0] = np.diff(f,axis=0,append=0) / ds
    df[0] += np.diff(f,axis=0,prepend=0) / ds
    df[1] = np.diff(f,axis=1,append=0) / ds
    df[1] += np.diff(f,axis=1,prepend=0) / ds
    df[2] = np.diff(f,axis=2,append=0) / ds
    df[2] += np.diff(f,axis=2,prepend=0) / ds
    return np.array(df) / 2


# Divergence
def div(A,ds):
    """
    A is a numpy array representing a vector field in 3 dimensions.
    ds is the grid spacing.
    Returns the divergence of A, as a 3D scalar field.
    """
    dA = np.zeros_like(A[0])

    # Average forward and backward difference.
    dA += np.diff(A[0],axis=0,append=0) / ds
    dA += np.diff(A[1],axis=1,append=0) / ds
    dA += np.diff(A[2],axis=2,append=0) / ds

    dA += np.diff(A[0],axis=0,prepend=0) / ds
    dA += np.diff(A[1],axis=1,prepend=0) / ds
    dA += np.diff(A[2],axis=2,prepend=0) / ds

    dA *= 0.5

    return dA


# Curl
def curl(A,ds):
    """
    A is a numpy array representing a vector field in 3 dimensions.
    ds is the grid spacing.
    Returns the curl of A, as a 3D vector field.
    """
    dAx = grad(A[0],ds) # gradient of x-component
    dAy = grad(A[1],ds) # gradient of y-component
    dAz = grad(A[2],ds) # gradient of z-component
    
    dxA = np.zeros_like(A)  # empty array to store the curl
    dxA[0] = dAz[1] - dAy[2] # x-component of curl
    dxA[1] = dAx[2] - dAz[0] # y-component of curl
    dxA[0] = dAy[0] - dAx[1] # z-component of curl
    return dxA


# Laplacian
def laplacian(f,ds):
    # Check for scalar vs vector.
    if len(f.shape) == 3:
        ddf = div(grad(f,ds),ds)
    elif len(f.shape) == 4:
        ddf = np.zeros_like(f)
        ddf[0] = div(grad(f[0],ds),ds)
        ddf[1] = div(grad(f[1],ds),ds)
        ddf[2] = div(grad(f[2],ds),ds)
    return ddf


# Helper function to map input points to the grid being used.
def find_nearest(x0,y0,z0, X,Y,Z):
    """
    Takes a target point (x0,y0,z0) and returns the indices of
    the nearest grid point in (X,Y,Z).
    """
    x = X[:,0,0]
    y = Y[0,:,0]
    z = Z[0,0,:]
    
    xI = np.argmin(np.abs(x-x0))
    yI = np.argmin(np.abs(y-y0))
    zI = np.argmin(np.abs(z-z0))
    
    return xI, yI, zI

# Volume integral.
def volume_integral(f, P1, P2, X, Y, Z, ds):
    """
    Compute volume integral of scalar function.
    f = 3D scalar function
    P1 = coordinates of "bottom back left" corner of rectangle
    P2 = coordinates of "top right front" corner of rectangle
    ds = grid spacing
    """

    xI, yI, zI = find_nearest(*P1, X,Y,Z)
    xJ, yJ, zJ = find_nearest(*P2, X,Y,Z)

    return np.sum(f[xI:xJ, yI:yJ, zI:zJ]) * ds**3


# Surface integral.
def surface_integral(A, P1, P2, X, Y, Z, ds):
    """
    Compute the flux through a rectangular surface.
    A = 3D vector field
    P1 = coordinates of "lower left" corner of rectangle
    P2 = coordinates of "upper right" corner of rectangle
    X,Y,Z = grid of points
    ds = grid spacing

    Only works for surfaces parallel to xy, xz, or yz planes.
    """

    xI, yI, zI = find_nearest(*P1, X,Y,Z)
    xJ, yJ, zJ = find_nearest(*P2, X,Y,Z)

    if xI == xJ:
        xJ = xI+1
        return np.sum(A[0,xI:xJ,yI:yJ,zI:zJ]) * ds**2
    elif yI == yJ:
        yJ = yI+1
        return np.sum(A[1,xI:xJ,yI:yJ,zI:zJ]) * ds**2
    elif zI == zJ:
        zJ = zI+1
        return np.sum(A[2,xI:xJ,yI:yJ,zI:zJ]) * ds**2
    else:
        raise Exception("Can only do surfaces parallel xy, xz, or yz planes.")


# Line integral
def line_integral(A, P1, P2, X, Y, Z, ds):
    """
    Compute the flux through a rectangular surface.
    A = 3D vector field
    P1 = coordinates of starting point
    P2 = coordinates of ending point
    X,Y,Z = grid of points
    ds = grid spacing

    Only works for contours parallel to x, y, or z axes.
    """
    xI, yI, zI = find_nearest(*P1, X,Y,Z)
    xJ, yJ, zJ = find_nearest(*P2, X,Y,Z)

    if (xI != xJ) and (yI == yJ) and (zI == zJ):
        yJ = yI + 1
        zJ = zI + 1
        if xJ > xI:
            return np.sum(A[0,xI:xJ,yI:yJ,zI:zJ]) * ds
        else:
            return -np.sum(A[0,xJ:xI,yI:yJ,zI:zJ]) * ds
    elif (xI == xJ) and (yI != yJ) and (zI == zJ):
        xJ = xI + 1
        zJ = zI + 1
        if yJ > yI:
            return np.sum(A[1,xI:xJ,yI:yJ,zI:zJ]) * ds
        else:
            return -np.sum(A[1,xI:xJ,yJ:yI,zI:zJ]) * ds
    elif (xI == xJ) and (yI == yJ) and (zI != zJ):
        xJ = xI + 1
        yJ = yI + 1
        if zJ > zI:
            return np.sum(A[2,xI:xJ,yI:yJ,zI:zJ]) * ds
        else:
            return -np.sum(A[2,xI:xJ,yI:yJ,zJ:zI]) * ds
    else:
        raise Exception("Can only do surfaces parallel xy, xz, or yz planes.")
    


# Compute line integral along a path.
def path_integral(A, points, X, Y, Z, ds):
    """
    Compute the path_integral of a vector field along a contour through points.

    A = 3D vector field
    points = list of vertices along the path
    X,Y,Z = grid of points
    ds = grid spacing

    Only works for rectangular contours with edges parallel to x, y, or z axes.
    """
    num_points = len(points)
    gamma = 0

    for i in range(num_points-1):
        gamma += line_integral(A, points[i], points[i+1], X, Y, Z, ds)

    return gamma


# Flux through a closed surface.
def flux(A, corner, dX, dY, dZ, X, Y, Z, ds):
    """
    Compute the flux through a closed rectangular surface.

    A = 3D vector field
    corner = coordinates of lower left front corner of box
    dX, dY, dZ = length of box along x, y, and z directions
    X,Y,Z = grid of points
    ds = grid spacing
    """

    x0, y0, z0 = corner
    x1 = x0 + dX
    y1 = y0 + dY
    z1 = z0 + dZ

    args = (X, Y, Z, ds)

    Phi = 0

    # Add up flux over six faces of box.
    # Front
    pA = (x0,y0,z0)
    pB = (x1, y0, z1)
    Phi -= surface_integral(A, pA, pB, *args)

    # Back
    pA = (x0,y1,z0)
    pB = (x1, y1, z1)
    Phi += surface_integral(A, pA, pB, *args)

    # Right
    pA = (x1,y0,z0)
    pB = (x1, y1, z1)
    Phi += surface_integral(A, pA, pB, *args)

    # Left
    pA = (x0,y0,z0)
    pB = (x0, y1, z1)
    Phi -= surface_integral(A, pA, pB, *args)

    # Top
    pA = (x0,y0,z1)
    pB = (x1, y1, z1)
    Phi += surface_integral(A, pA, pB, *args)

    # Bottom
    pA = (x0,y0,z0)
    pB = (x1, y1, z0)
    Phi -= surface_integral(A, pA, pB, *args)

    return Phi


# Plot field and surface used to compute flux.
def draw_box(A, corner, dX, dY, dZ, X, Y, Z, ds):
    """
    Draw the vector field A and a box.

    A = 3D vector field
    corner = coordinates of lower left front corner of box
    dX, dY, dZ = length of box along x, y, and z directions
    X,Y,Z = grid of points
    ds = grid spacing
    """
    # Draw the vector field.
    ax = draw_vector_field(X,Y,Z,*A)

    # Add the box.
    ax.bar3d(*corner,dX,dY,dZ,alpha=0.2,color='green')

    return ax


# Plot field and path used to compute contour integral.
def draw_path(A, points, X, Y, Z, ds):
    """
    Draw the vector field A and a contour through points.

    A = 3D vector field
    points = list of vertices along the path
    X,Y,Z = grid of points
    ds = grid spacing

    Return the Axes used to create the plot.
    """
    # Draw the vector field.
    ax = draw_vector_field(X,Y,Z,*A)

    # Add the contour.
    path = list(zip(*points))
    ax.plot3D(*path)

    return ax



