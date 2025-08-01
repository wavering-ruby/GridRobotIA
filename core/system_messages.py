import pygame
import pygame_gui

class SystemMessages():
    def __init__(self, screen_size, manager):
        self.manager = manager
        self.window_width, self.window_height = screen_size
    
    def weightedSucessMessage(self, algorithm, cost):
        popup_width, popup_height = 250, 160
        popup_x = (self.window_width - popup_width) // 2
        popup_y = (self.window_height - popup_height) // 2

        pygame_gui.windows.UIMessageWindow(
            rect = pygame.Rect((popup_x, popup_y), (popup_width, popup_height)),
            html_message = f'<b>Caminho concluído!</b><br>Custo total: {cost}',
            manager = self.manager,
            window_title = f'Algoritmo utilizado: {algorithm}'
        )
        
    def notPathMessage(self):
        popup_width = 250
        popup_height = 160
        popup_x = (self.window_width - popup_width) // 2
        popup_y = (self.window_height - popup_height) // 2

        pygame_gui.windows.UIMessageWindow(
            rect = pygame.Rect((popup_x, popup_y), (popup_width, popup_height)),
            html_message = f"O sistema não conseguiu encontrar um caminho viável até o destino, verifique se o destino não está com obstáculos ou se o limite está menor!",
            manager = self.manager,
            window_title = "Caminho Incompleto"
        )

    def start_message(self):
        popup_width = 300
        popup_height = 200
        popup_x = (self.window_width - popup_width) // 2
        popup_y = (self.window_height - popup_height) // 2

        pygame_gui.windows.UIMessageWindow(
            rect = pygame.Rect((popup_x, popup_y), (popup_width, popup_height)),
            html_message = (
                f"Hello! <br><br>"
                "Thanks for trying this project. This project was created by <b>Mateus Gabriel</b>"
                "together with <b>Caio Viana</b>, under the guidance of our teacher <b> Luis Fernando de Almeida</b>"
                "We hope you enjoy it!"
            ),
            manager = self.manager,
            window_title = "Thank you so much!"
        )