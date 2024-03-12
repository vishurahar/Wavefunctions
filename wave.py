import numpy as np
import plotly.graph_objects as go
from scipy.special import sph_harm, genlaguerre

def prob(n, l, m, r, theta, phi):
    radial = np.sqrt((2 / n)**3 * np.math.factorial(n - l - 1) / (2 * n * np.math.factorial(n + l))) * np.exp(-r / n) * (2 * r / n)**l * genlaguerre(n - l - 1, 2 * l + 1)(2 * r / n)
    angular = sph_harm(m, l, phi, theta)
    wave = radial * angular
    prob = np.abs(wave * wave)
    return prob

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)

z_value = 0

r = np.sqrt(X**2 + Y**2 + z_value**2)
theta = np.arccos(z_value / np.sqrt(X**2 + Y**2 + z_value**2))
phi = np.arctan2(Y, X)




n = 3
l = 2
m = 2
probability_density = prob(n,l,m,r,theta,phi)*10**3
# Plotting
trace1 = go.Surface(
    x=X,
    y=Y,
    z=probability_density,
    colorscale='Viridis',
    #colorscale = 'plasma',
)

data = [trace1]

layout = go.Layout(
    scene=dict(
        xaxis=dict(title='X'),
        yaxis=dict(title='Y'),
        zaxis=dict(title='Probability Density'),
    ),
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0
    )
)

fig = go.Figure(data=data, layout=layout)
fig.show()

