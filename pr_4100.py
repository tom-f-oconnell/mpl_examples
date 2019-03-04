#!/usr/bin/env python3

import matplotlib
matplotlib.use('webagg')
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(np.random.rand(10))


def onkeyevent(event):
    fig.suptitle('%s: %s' % (event.name, event.key))
    print('%s\n%s\n' % (event.name, event.guiEvent))
    fig.canvas.draw()

cid = fig.canvas.mpl_connect('key_press_event', onkeyevent)
cid = fig.canvas.mpl_connect('button_press_event', onkeyevent)
plt.show()
