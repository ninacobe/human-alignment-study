#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib
from sklearn.metrics.cluster import adjusted_rand_score

def get_fig_dim(width=900, fraction=1, aspect_ratio=None):
    """Set figure dimensions to avoid scaling in LaTeX.
    Parameters
    ----------
    width: float
            Document textwidth or columnwidth in pts
    fraction: float, optional
            Fraction of the width which you wish the figure to occupy
    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    # Width of figure (in pts)
    fig_width_pt = width * fraction

    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    if aspect_ratio is None:
      aspect_ratio = (1 + 5**.5) / 2

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    fig_height_in = fig_width_in / aspect_ratio

    fig_dim = (fig_width_in,fig_height_in)

    return fig_dim

def latexify(font_serif='Computer Modern', mathtext_font='cm', font_size=10, small_font_size=None, usetex=True):
    """Set up matplotlib's RC params for LaTeX plotting.
    Call this before plotting a figure.
    Parameters
    ----------
    fig_width : float, optional, inches
    fig_height : float,  optional, inches
    columns : {1, 2}
    """
    # code adapted from http://www.scipy.org/Cookbook/Matplotlib/LaTeX_Examples

    if small_font_size is None:
      small_font_size = font_size

    params = {'backend': 'ps',
              'text.latex.preamble': """\\usepackage{gensymb} \\usepackage{bm} """,
              # fontsize for x and y labels (was 10)
            #   'axes.labelsize': font_scale * 10 if largeFonts else font_scale * 7,
            #   'axes.titlesize': font_scale * 10 if largeFonts else font_scale * 7,
            #   'font.size': font_scale * 10 if largeFonts else font_scale * 7,  # was 10
            #   'legend.fontsize': font_scale * 10 if largeFonts else font_scale * 7,  # was 10
            #   'xtick.labelsize': font_scale * 10 if largeFonts else font_scale * 7,
            #   'ytick.labelsize': font_scale * 10 if largeFonts else font_scale * 7,
              'axes.labelsize': font_size,
              'axes.titlesize': font_size,
              'font.size': font_size,  # was 10
              'legend.fontsize': small_font_size,  # was 10
              'legend.title_fontsize': small_font_size,
              'xtick.labelsize': small_font_size,
              'ytick.labelsize': small_font_size,
              'text.usetex': usetex,
            #   'figure.figsize': [fig_width, fig_height],
              'font.family' : 'serif',
              'font.serif' : font_serif,
              'mathtext.fontset' : mathtext_font
            #   'xtick.minor.size': 0.5,
            #   'xtick.major.pad': 1.5,
            #   'xtick.major.size': 1,
            #   'ytick.minor.size': 0.5,
            #   'ytick.major.pad': 1.5,
            #   'ytick.major.size': 1,
            # #   'lines.linewidth': 1.5,
            # 'lines.linewidth': 1,
            # #   'lines.markersize': 0.1,
            #   'lines.markersize': 8.0,
            #   'hatch.linewidth': 0.5
              }

    matplotlib.rcParams.update(params)
    plt.rcParams.update(params)

