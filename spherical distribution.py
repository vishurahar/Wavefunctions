import numpy as np
import plotly.graph_objects as go
from scipy.special import sph_harm

def plot_Y(l, m):

    theta = np.linspace(0, np.pi, 100)
    phi = np.linspace(0, 2 * np.pi, 100)
    theta, phi = np.meshgrid(theta, phi)
    
    xyz = np.array([np.sin(theta) * np.sin(phi),
                    np.sin(theta) * np.cos(phi),
                    np.cos(theta)])
    Y = sph_harm(abs(m), l, phi, theta)

    # Linear combination of Y_l,m and Y_l,-m to create the real form.
    if m < 0:
        Y = np.sqrt(2) * (-1)**m * Y.imag
    elif m > 0:
        Y = np.sqrt(2) * (-1)**m * Y.real
        

    Yx, Yy, Yz = np.abs(Y) * xyz
    return Yx, Yy, Yz
    
def wavefunction(l, m):

    theta = np.linspace(0, np.pi, 100)
    phi = np.linspace(0, 2 * np.pi, 100)
    theta, phi = np.meshgrid(theta, phi)
    
    xyz = np.array([np.sin(theta) * np.sin(phi),
                    np.sin(theta) * np.cos(phi),
                    np.cos(theta)])
                    
    Y = sph_harm(m, l, phi, theta) 

    Yx, Yy, Yz = np.abs(Y) * xyz
    return Yx, Yy, Yz


l = 3
m = 1

X, Y, Z = plot_Y(l, m)

#X1, Y1, Z1 = wavefunction(l=2, m=2)/np.sqrt(2)
#X2, Y2, Z2 = wavefunction(l=2, m=-2)/np.sqrt(2)
#X = X1+X2
#Y = Y1+Y2
#Z = Z1+Z2

# Plotting
trace1 = go.Surface(
    x=X,
    y=Y,
    z=Z,
    colorscale='magma',
    #colorscale = 'plasma',
    #colorscale = 'viridis',
)

data =[trace1]

layout = go.Layout(
    scene=dict(
        xaxis=dict(title='X',showbackground=False),
        yaxis=dict(title='Y',showbackground=False),
        zaxis=dict(title='Z',showbackground=False),
        bgcolor='rgb(0, 0, 20)',
    ),
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0,
    ),
    autosize=True,  
    width=1450, 
    height=800,
    title=dict(
        text=f'Orbital l = {l} m = {m}',
        x=0.5,  
        y=0.9,
        font=dict(size=22, color='white'),
    ),
)

fig = go.Figure(data=data, layout=layout)
fig.show()

