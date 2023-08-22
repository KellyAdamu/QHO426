import matplotlib.animation as a
import matplotlib.pyplot as plt

def animate(frame):
    print(f"Frame {frame}")


def run():
    fig = plt.figure()
    bob = a.FuncAnimation(fig, animate, interval=100, frames=12, repeat=False)
    plt.show()


run()

