#!/usr/bin/env python
import paperplot
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


if __name__ == '__main__':
    sns.set_style('ticks') 

    # create some random data
    x = np.arange(100)
    y = np.random.randn(100)

    # load the setup (with some specific update)
    paperplot.setup({'font.size':8})   

    # create a figure of the correct size
    fig = paperplot.paper_figure(220,110)

    # plotting
    plt.plot(x,y,'-', color=(0.22, 0.42, 0.69))
    plt.xlabel('x axis', fontsize=8)
    plt.ylabel('y axis', fontsize=8)
    plt.tick_params(axis='x', labelsize=8)
    plt.tick_params(axis='y', labelsize=8)
    plt.title('A simple demo figure')
    plt.grid(True)
    plt.tight_layout(pad=0.2, w_pad=0.1)

    # output
    plt.savefig('figure.pdf')

