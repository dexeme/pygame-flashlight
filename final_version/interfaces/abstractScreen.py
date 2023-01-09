import pygame
from abc import ABC, abstractmethod

class AbstractScreen(ABC):
    def __init__(self, screen, file_background_image, buttons):
        self.__screen = screen
        self.__background = pygame.image.load(file_background_image)
        self.__buttons = buttons
        self.__pressed_time = 60
        self.__button_pressed = False
        self.__change_screen = False

    def setButtonPressed(self):
        self.__button_pressed = not self.__button_pressed
    
    def getScreen(self):
        return self.__screen
    
    def getBackground(self):
        return self.__background
    
    def getChangeScreen(self):
        return self.__change_screen

    def getKey(self):
        return self.__key
    
    def setKey(self, key):
        self.__key = key
    
    def getButtons(self):
        return self.__buttons
    
    def run(self):
        self.update()
        if pygame.mouse.get_pressed(num_buttons=3)[0]:
            for button in self.getButtons():
                if button.colliding():
                    self.setKey(button.key)
                    self.setButtonPressed()
            
        key = self.nextAction()
        if key != None:
            self.setKey(None)
            return key
        
        self.cooldownBottonPressed()
        
    @abstractmethod
    def update(self):
        pass
    
    def nextAction(self):
        if self.getChangeScreen():
            return self.getKey()

    
    def cooldownBottonPressed(self):
        current_time = pygame.time.get_ticks()
        if self.__button_pressed:
            if current_time - self.__pressed_time > self.__pressed_time:
                self.__change_screen = True
        else:
            self.__change_screen = False
    
    
    
    
    