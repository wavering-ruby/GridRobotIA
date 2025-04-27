import pygame
import pygame_gui

class SystemMessages():
    def __init__(self, screen_size, manager):
        self.manager = manager
        self.window_width, self.window_height = screen_size
    
    def weightedSucessMessage(self, algorithm, cost):
        popup_width, popup_height = 300, 120
        popup_x = (self.window_width - popup_width) // 2
        popup_y = (self.window_height - popup_height) // 2

        pygame_gui.windows.UIMessageWindow(
            rect = pygame.Rect((popup_x, popup_y), (popup_width, popup_height)),
            html_message = f'<b>Caminho concluído!</b><br>Custo total: {cost}',
            manager = self.manager,
            window_title = f'Algoritmo utilizado: {algorithm}'
        )
        
    def notPathMessage(self, path):
        popup_width = 250
        popup_height = 160 + (len(path) * 5)
        popup_x = (self.window_width - popup_width) // 2
        popup_y = (self.window_height - popup_height) // 2

        pygame_gui.windows.UIMessageWindow(
            rect = pygame.Rect((popup_x, popup_y), (popup_width, popup_height)),
            html_message = f'O sistema não conseguiu encontrar o caminho até o fim. <br>O caminho encontrado foi: {path}',
            manager = self.manager,
            window_title = "Caminho Incompleto"
        )