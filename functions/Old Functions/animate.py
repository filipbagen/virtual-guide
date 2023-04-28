import pygame
from pygame.math import Vector2
import cv2
import math


def read_face(cap, face_cascade):
    # Read a frame from the camera
    ret, frame = cap.read()

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw a rectangle around each detected face and print its position
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # print("Face position: x = %d, y = %d" % (x, y))
        return x, y

    # Return 0, 0 if no faces are detected
    return 0, 0


def main():

    # initialize Pygame
    pygame.init()

    # set the screen dimensions
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    # set the ellipse parameters
    ellipse_size = (40, 20)
    ellipse_color = (255, 255, 255)

    # set the start and finish positions of the ellipse
    start_pos = (0, screen_height // 2)
    finish_pos = (screen_width // 2, screen_height // 2)

    # set the duration of the animation in milliseconds
    animation_duration = 2000

    # set the initial time of the animation
    start_time = pygame.time.get_ticks()

    # set the initial position of the ellipse
    ellipse_x = start_pos[0]
    ellipse_y = start_pos[1]

    # start the game loop
    running = True
    while running:
       # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # calculate the current time of the animation
        current_time = pygame.time.get_ticks() - start_time

        # calculate the progress of the animation as a value between 0 and 1
        progress = min(current_time / animation_duration, 1)

        # calculate the size of the ellipse using an easing function
        easing_progress = math.sin(progress * math.pi / 2)
        ellipse_width = ellipse_size[0] * easing_progress
        ellipse_height = ellipse_size[1] * easing_progress

        # calculate the position of the ellipse using an easing function
        ellipse_x = start_pos[0] + \
            (finish_pos[0] - start_pos[0]) * easing_progress
        ellipse_y = start_pos[1] + \
            (finish_pos[1] - start_pos[1]) * easing_progress

        # fill the screen with black
        screen.fill((0, 0, 0))

        # draw the ellipse on the screen
        pygame.draw.ellipse(screen, ellipse_color, (int(ellipse_x - ellipse_width / 2), int(
            ellipse_y - ellipse_height / 2), int(ellipse_width), int(ellipse_height)))

        # update the display
        pygame.display.update()

        # wait for a short amount of time
        pygame.time.delay(10)

    # quit Pygame
    pygame.quit()

    # Release the camera and close the window
    # cap.release()
    cv2.destroyAllWindows()
    print('Ended program!')


main()
