import pygame

class RemoteCentral:
    def __init__(self):
        pygame.init()
        pygame.display.init()

        j = pygame.joystick.Joystick(0)
        j.init()

        try:
            while True:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.JOYBUTTONDOWN:
                        print(event.dict, event.joy, event.button, 'pressed')
                    elif event.type == pygame.JOYBUTTONUP:
                        print(event.dict, event.joy, event.button, 'released')

        except KeyboardInterrupt:
            print("ERROR in RemoteCentral")
            j.quit()

remote_central = RemoteCentral()