class OptionButton:
    def __init__(self, text, y, width, font, pygame, window):
        self.text = text
        self.x = width / 2 - font.size(text)[0] / 2 - 10
        self.y = 300 + y - 10
        self.width = font.size(text)[0] + 20
        self.height = font.size(text)[1] + 20
        self.font = font
        self.pygame = pygame
        self.window = window

    def draw(self, window):
        color = (0, 0, 0, 128)
        if self.is_hovering():
            color = (115, 179, 206, 128)
        self.pygame.draw.rect(window, color, (self.x, self.y, self.width, self.height), 0, 10)
        self.window.blit(self.font.render(self.text, True, (255, 255, 255)), (self.x + 10, self.y + 10))

    def is_hovering(self):
        # get the mouse position
        mouse_x, mouse_y = self.pygame.mouse.get_pos()
        # check if the mouse is inside the option's rectangle
        if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
            return True
        else:
            return False

    def is_clicked(self):
        if self.is_hovering():
            if self.pygame.mouse.get_pressed()[0]:
                return True
        return False
