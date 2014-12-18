from __future__ import division

import numpy as np
from bokeh.sampledata.iris import flowers
from bokeh import embed
import bokeh.resources
from bokeh.plotting import *

N = 20

img = np.empty((N,N), dtype=np.uint32)

view = img.view(dtype=np.uint8).reshape((N, N, 4))
for i in range(N):
    for j in range(N):
        view[i, j, 0] = int(i/N*255)
        view[i, j, 1] = 158
        view[i, j, 2] = int(j/N*255)
        view[i, j, 3] = 255

output_server("rbga")

graph = image_rgba(
    image=[img], x=[0], y=[0], dw=[10], dh=[10],
    x_range=[0,10], y_range=[0,10],
    tools="pan,wheel_zoom,box_zoom,reset,previewsave", name="image_example",
    plot_width=300, plot_height=300)

tag = embed.autoload_server(graph, cursession())