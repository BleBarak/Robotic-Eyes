import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
import numpy as np

def draw_eyes(emotion):
    fig, ax = plt.subplots()

    # Set background color to black
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    # Draw the eyes as semi-rectangles
    left_eye = patches.Rectangle((0.25, 0.4), 0.2, 0.2, color='white', ec='black')  # Left eye
    right_eye = patches.Rectangle((0.55, 0.4), 0.2, 0.2, color='white', ec='black')  # Right eye

    ax.add_patch(left_eye)
    ax.add_patch(right_eye)

    # Function to toggle eye state
    def blink(i):
        if i % 10 == 0:  # Blink every 10 frames
            left_eye.set_height(0.01)  # Close the left eye
            right_eye.set_height(0.01)  # Close the right eye
        elif i % 10 == 5:  # Open the eyes halfway through the interval
            left_eye.set_height(0.2)  # Open the left eye
            right_eye.set_height(0.2)  # Open the right eye
        return left_eye, right_eye

    # Animate the blinking
    ani = animation.FuncAnimation(fig, blink, frames=1000, interval=np.random.randint(500, 5000), blit=True)

    # Add emotion expressions
    if emotion == 'neutral':
        pass  # No additional expressions for neutral
    elif emotion == 'happy':
        left_eye.set_height(0.25)  # Widen the left eye
        right_eye.set_height(0.25)  # Widen the right eye
    elif emotion == 'sad':
        left_eye.set_y(0.3)  # Move the left eye down
        right_eye.set_y(0.3)  # Move the right eye down
    elif emotion == 'angry':
        left_eye.set_height(0.15)  # Narrow the left eye
        right_eye.set_height(0.15)  # Narrow the right eye
        ax.plot([0.2, 0.4], [0.5, 0.48], color='white', linewidth=2)  # Angry expression (left eyebrow)
        ax.plot([0.6, 0.8], [0.48, 0.5], color='white', linewidth=2)  # Angry expression (right eyebrow)

    # Set axis limits and remove ticks
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.show()

# Prompt the user to input emotion
emotion = input("Enter emotion (neutral, happy, sad, angry): ")

# Test different emotions
draw_eyes(emotion)
