# -----------------------------------------------------------------------------
# Electrodynamics.py
# ----------------------------------------------------------------------------- 
# Functions to study electric fields of point charges.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


# Generate a coordinate grid.
def coordinates(L, N):
    """
    Generate a grid of Cartesian coordinates:
    An NxNxN mesh that extends from -L to +L along each dimension.
    """
    s = np.linspace(-L, L, N)
    X,Y,Z = np.meshgrid(s,s,s, indexing='ij')

    return X, Y, Z


# Compute the potential of a point charge.
def point_charge_potential(charge, location, X, Y, Z, epsilon=1e-6):
    """
    Return the potential of point charge at the given location on the
    mesh of Cartesian coordinates defined by X, Y, and Z.

    epsilon is a small parameter to prevent division by zero at the location of
    the charge.
    """
    x0, y0, z0 = location
    q = charge

    R = np.sqrt((X-x0)**2 + (Y-y0)**2 + (Z-z0)**2 + epsilon**2)
    V = q/R
    
    return V


# Compute the electric field of a point charge.
def point_charge_field(charge, location, X, Y, Z, epsilon=1e-6):
    """
    Return the electric field of point charge at the given location on the mesh
    of Cartesian coordinates defined by X, Y, and Z.

    epsilon is a small parameter to prevent division by zero at the location of
    the charge.
    """
    x0, y0, z0 = location
    q = charge

    R = np.sqrt((X-x0)**2 + (Y-y0)**2 + (Z-z0)**2 + epsilon**2)
    Ex = q*(X-x0)/R**3
    Ey = q*(Y-y0)/R**3
    Ez = q*(Z-z0)/R**3
    
    return np.stack([Ex, Ey, Ez])


# Draw a vector field.
def draw_vector_field(X,Y,Z,U,V,W, stride=25):
    """
    Takes coordinate arrays X,Y,Z and vector field component
    arrays U,V,W and draws a quiver plot where all of the arrows
    have the same length.

    stride determines how many points to skip in sampling the arrays

    Returns the Axes object used to create the plot.
    """
    # Use a coarser grid for plotting.
    x = X[::stride,::stride,::stride]
    y = Y[::stride,::stride,::stride]
    z = Z[::stride,::stride,::stride]
    u = U[::stride,::stride,::stride]
    v = V[::stride,::stride,::stride]
    w = W[::stride,::stride,::stride]
    
    # Create a quiver plot.
    fig = plt.figure(dpi=200)
    ax = fig.add_subplot(projection='3d')
    ax.quiver3D(x,y,z,u,v,w, pivot='middle', length=0.7, normalize=True, linewidth=0.5, color='red', alpha=0.5)
    
    return ax

# Draw a slice through a scalar field.
def draw_scalar_field(X, Y, Z, V, z0=0, cutoff=20):
    """
    Takes coordinate arrays X,Y,Z and scalar field array V and draws a heatmap
    of V(x,y,z0), the slice through V at constant z = z0 (or the closest value
    in the coordinate grid).

    cutoff sets the maximum and minimum values for the colormap.

    Returns the Axes object used to create the plot.
    """
    # Determine z-coordinate index for slices.
    zI = np.argmin(np.abs(Z[0,0,:]-z0))

    # Get slice.
    x = X[:,:,zI]
    y = Y[:,:,zI]
    v = V[:,:,zI]

    # Draw heatmap.
    fig, ax = plt.subplots(dpi=200)
    image = plt.pcolormesh(x,y,v, shading='gouraud', cmap='jet')
    plt.colorbar(image, use_gridspec=True, extend='both')
    plt.clim(-cutoff,cutoff)
    ax.axis('scaled')

    return ax
