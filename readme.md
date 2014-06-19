screencap

Dependencies
---

- Pillow (an older PIL installation will probably work too.)
- pywin32

What does it do?
---

![example](https://raw.github.com/Azeirah/screencap/master/video.gif)

With this program you can record your screen, it will output your "video" as png files. Which can be converted into .webm and .gif with the provided html file. It only seems to be working in Chrome currently, FireFox gives an error.

Using it
---

**Step 1: capturing**
Run screencap.py from the command line.
Press F4 to start capturing
Press F5 to stop capturing
Press F1 to take a single screenshot
Press F2 to quit the program ):

**Step 2: videoing**
1: Start a local webserver (sorry, you can't convert to .gif without running on a local webserver)
I recommend using `python -m http.server` from the command line.
2: Open concat.html in your browser `localhost:8000/concat.html`
3: Select your video width, height and framerate
4: Select your images or drop them in.
5: Press the button.
6: Reap the souls of the generated videos


Thanks to
---

- Whammy.js for pngs to .webm