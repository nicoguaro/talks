#!/bin/bash
#
# Generate an animation (.avi, .gif) from a sequence of image with
# the same name and a sequence of numbers.
#
# 
mencoder "mf://*.png" -mf type=png:fps=5 -ovc lavc -o ex1D.avi
ffmpeg -i ex1D.avi -sameq ex1D.flv
#convert ex1D*.png -delay 20 -loop 0 -channel Alpha  ex1D.gif

