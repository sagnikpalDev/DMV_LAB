import matplotlib.pyplot as plt
x = float(input("Enter starting X position: "))
y = float(input("Enter starting Y position: "))
radius = float(input("Enter radius of circle: "))
speed = float(input("Enter speed (movement per key press): "))
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
circle = plt.Circle((x, y), radius, color='blue')
ax.add_patch(circle)
def on_key(event):
    global x, y
    
    if event.key == 'up':
        y += speed
    elif event.key == 'down':
        y -= speed
    elif event.key == 'left':
        x -= speed
    elif event.key == 'right':
        x += speed
    circle.center = (x, y)
    fig.canvas.draw()
fig.canvas.mpl_connect('key_press_event', on_key)

plt.show()