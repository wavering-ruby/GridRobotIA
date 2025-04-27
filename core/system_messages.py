import pygame
import pygame_gui

class SystemMessages():
    def weightedSucessMesage(algorithm, cost, screen_size, manager):
        window_width, window_height = screen_size
        popup_width, popup_height = 300, 120
        popup_x = (window_width - popup_width) // 2
        popup_y = (window_height - popup_height) // 2

        pygame_gui.windows.UIMessageWindow(
            rect = pygame.Rect((popup_x, popup_y), (popup_width, popup_height)),
            html_message = f'<b>Caminho concluído!</b><br>Custo total: {cost}',
            manager = manager,
            window_title = f'Algoritmo utilizado: {algorithm}'
        )