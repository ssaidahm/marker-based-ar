from PIL import Image, ImageSequence
transparent_foreground = Image.open(...)
animated_gif = Image.open("5AhIZhC.gif")

frames = []
for frame in ImageSequence.Iterator(animated_gif):
    frame = frame.copy()
    frame.paste(transparent_foreground, mask=transparent_foreground)
    frames.append(frame)
frames[0].save('output.gif', save_all=True, append_images=frames[1:])