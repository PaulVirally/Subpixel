# Subpixel
This is a graphics engine built for TUI applications. If you were to try to use a terminal as graphical output, you may be tempted to use characetrs such as █ for a pixel. The problem is that that does not give you a whole lot of resolution. Instead, you can do everything in braille. A braille cell has 8 subpixels (arranged in a 4 row by 2 column grid) that we can individually turn on or off. This leads to resolution that is increased by a factor of √8 ≈ 2.83.

This library is built entirely in pure Python. The graphical output is rendered using [curses](https://docs.python.org/3/library/curses.html).

## Demo
![demo](https://gfycat.com/ancientringedivorybackedwoodswallow)
To run the demos, simply clone the repo and run the script from the root directory of the repo.
```sh
$ git clone https://github.com/PaulVirally/Subpixel
$ cd Subpixel
$ python ./examples/3d.py
```
