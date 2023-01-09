import pygame
from singletonMeta import SingletonMeta


class Sound(metaclass=SingletonMeta):

    def __init__(self):
        self.__current_requestor = 'main'
        self.__music = pygame.mixer.music
        self.__music_priority = 0
        self.__sound_channel = pygame.mixer.Channel(1)
        self.__sounds = {'pilha': pygame.mixer.Sound('sounds/pilha.wav'),
                         'sem_pilha': pygame.mixer.Sound('sounds/sem_pilha.wav'),
                         'key': pygame.mixer.Sound('sounds/key.wav'),
                         'lanterna': pygame.mixer.Sound('sounds/lanterna.wav')}
        self.__songs = {'main': 'sounds/musica-tema.wav',
                        'el': 'sounds/musica-enemylowdmg.wav',
                        'eh': 'sounds/musica-enemyhighdmg.wav',
                        'pilha': 'sounds/musica-sem-pilha.wav'}
        self.__priorities = {'main': 0,
                        'el': 2,
                        'eh': 3,
                        'pilha': 1}

    def playSound(self, sound_name):
        self.__sound_channel.play(self.__sounds[sound_name])

    def stopSound(self):
        if self.__sound_channel.get_busy():
            self.__sound_channel.stop()

    def playMusic(self, requestor):
        try:
            if self.__priorities[requestor] > self.__music_priority:
                self.__music.stop()
                self.__music.unload()
                self.__music.load(self.__songs[requestor])
                self.__music.play(loops=-1)

                self.__music_priority = self.__priorities[requestor]
        except KeyError:
            print('Chave Invalida!')
            return 0
        self.__current_requestor = requestor

    def songUpdate(self):
        if not self.__music.get_busy():
            self.__music.unload()
            self.__music.load(self.__songs['main'])
            self.__music.play()

    def stopMusic(self, requestor):
        if requestor == self.__current_requestor:
            self.__music.stop()

    def setVolume(self, volume: float):
        self.__music.set_volume(volume/200)
        self.__sound_channel.set_volume(volume/100)
