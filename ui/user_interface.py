import pygame
import sys
import pygame_gui
from core.grid_generator import RandomProblemGenerator
from core.unweight_search import UnweightedSearch
from core.weight_search import WeightedSearch
from core.system_messages import SystemMessages

class UserInterface:
    def __init__(self, grid_size = (10, 10), obstacles = 20):
        # Configurações da grid
        self.nx, self.ny = grid_size
        self.qtd_obstacles = obstacles
        
        # Posições iniciais
        self.sx = 0
        self.sy = 0
        
        self.cost = 0
        
        # Posições finais
        self.ex = grid_size[0] - 1
        self.ey = grid_size[1] - 1
        
        # Gera a grid inicial
        self.reset_grid()
        
        # Configurações do pygame
        pygame.init()
        
        # Configuração do Ícone
        pygame.display.set_icon(pygame.image.load("assets/PR_ATO_ICON.png"))
        
        # Configuração do dropdown
        self.sel_selection = "Sem Peso"
        self.sel_algorithm = "Amplitude"
        
        # Criando configurações para trocar de peso
        self.algorithm_option = ['Amplitude', 'Profundidade', 'Profundidade Lim.', 'Aprof. Interativo', 'Bidirecional']
        
        #Configurações da tela
        self.menu_width = 200
        self.grid_size_pixels = 600
        self.screen = pygame.display.set_mode((self.grid_size_pixels + self.menu_width, self.grid_size_pixels), pygame.RESIZABLE)

        pygame.display.set_caption("Animação de Algoritmos de Busca")
        self.clock = pygame.time.Clock()
        
        # Carrega a imagem do personagem
        self.load_character_image()
        
        # Configurações de animação
        self.animation_speed = 0.5  # Segundos por célula
        self.last_move_time = 0
        self.current_segment = 0
        
        # Inicializa o manager ANTES de criar o dropdown
        self.manager = pygame_gui.UIManager((self.grid_size_pixels + self.menu_width, self.grid_size_pixels))
        
        base_x = self.grid_size_pixels + 20
        base_y = 200
        # espaco = 40

        # Legenda do Switch Button (Método de Busca)
        self.label_mode_selection = pygame_gui.elements.UILabel(
            relative_rect = pygame.Rect((base_x, base_y), (160, 20)),
            text = "Método de Busca:",
            manager = self.manager
        )

        # Switch Button (Com Peso / Sem Peso)
        self.dropdown_mode_selection = pygame_gui.elements.UIDropDownMenu(
            options_list = ['Sem Peso', 'Com Peso'],
            starting_option = self.sel_selection,
            relative_rect = pygame.Rect((base_x, base_y + 20), (160, 30)),
            manager = self.manager
        )

        # Legenda do Dropdown (Algoritmo)
        self.label_dropdown = pygame_gui.elements.UILabel(
            relative_rect = pygame.Rect((base_x, base_y + 60), (160, 20)),
            text = "Algoritmo:",
            manager = self.manager
        )

        # Dropdown (Algoritmo)
        self.dropdown = pygame_gui.elements.UIDropDownMenu(
            options_list = self.algorithm_option,
            starting_option = self.sel_algorithm,
            relative_rect = pygame.Rect((base_x, base_y + 80), (160, 40)),
            manager = self.manager
        )

        # Legenda da Posição Inicial
        self.label_x = pygame_gui.elements.UILabel(
            relative_rect = pygame.Rect((base_x, base_y + 130), (160, 20)),
            text = "Posição Inicial (X, Y)",
            manager = self.manager
        )

        # Campo Inicial
        self.input_text = pygame_gui.elements.UITextEntryLine(
            relative_rect = pygame.Rect((base_x, base_y + 150), (160, 30)),
            manager = self.manager
        )

        # Legenda da Posição Final
        self.label_y = pygame_gui.elements.UILabel(
            relative_rect = pygame.Rect((base_x, base_y + 190), (160, 20)),
            text = "Posição Final (X, Y):",
            manager = self.manager
        )

        # Campo Final
        self.input_text2 = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((base_x, base_y + 210), (160, 30)),
            manager=self.manager
        )

        # Botão de Início
        self.botao_ler_texto = pygame_gui.elements.UIButton(
            relative_rect = pygame.Rect((base_x, base_y + 250), (160, 30)),
            text = 'Iniciar',
            manager = self.manager
        )
        
    def draw_button(self, text, rect, font):
        pygame.draw.rect(self.screen, (70, 70, 70), rect, border_radius = 8)
        pygame.draw.rect(self.screen, (200, 200, 200), rect, 2, border_radius = 8)
        label = font.render(text, True, (255, 255, 255))
        label_rect = label.get_rect(center = (rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
        self.screen.blit(label, label_rect)
    
    def update_algorithm_dropdown(self):
        self.dropdown.kill()
        
        self.sel_algorithm = self.algorithm_option[0]
        
        # Cria um novo dropdown com as opções atualizadas
        self.dropdown = pygame_gui.elements.UIDropDownMenu(
            options_list = self.algorithm_option,
            starting_option = self.sel_algorithm,
            relative_rect = pygame.Rect((self.grid_size_pixels + 20, 280), (160, 40)),
            manager = self.manager
        )
    
    def reset_grid(self):
        """
            Gera uma nova grid com obstáculos
        """
        self.grid = RandomProblemGenerator(self.nx, self.ny, self.qtd_obstacles)
        self.start_pos = (self.sx, self.sy)
        self.end_pos = (self.ex, self.ey)
        
        # Garante que início e fim não são obstáculos
        self.grid[self.start_pos[0]][self.start_pos[1]] = 0
        self.grid[self.end_pos[0]][self.end_pos[1]] = 0
        
        # Reseta o estado da animação
        self.character_pos = list(self.start_pos)
        self.current_segment = 0
        self.last_move_time = pygame.time.get_ticks()
        self.animation_started = False  # Reseta a flag de animação
        
        # Não calcula o caminho automaticamente
        self.path = []
    
    def load_character_image(self):
        """
            Carrega a imagem do personagem ou cria uma padrão
        """
        try:
            original_image = pygame.image.load("assets/PR_ATO.png");
            
            # Manter proporções mas limitar ao tamanho máximo da célula
            cell_size = min(self.grid_size_pixels // self.ny, self.grid_size_pixels // self.nx)
            max_size = int(cell_size * 0.8)  # 80% do tamanho da célula
            
            # Redimensionar mantendo proporção
            width = min(original_image.get_width(), max_size)
            height = min(original_image.get_height(), max_size)
            self.character_image = pygame.transform.scale(original_image, (width, height))
        except:
        # Fallback visual se a imagem não carregar
            cell_size = min(self.grid_size_pixels // self.ny, self.grid_size_pixels // self.nx)
            size = int(cell_size * 0.6)
            self.character_image = pygame.Surface((size, size), pygame.SRCALPHA)
            pygame.draw.circle(self.character_image, (0, 0, 255), (size // 2, size // 2), size // 2)

    def find_path(self):
        """
        Selects the search algorithm based on user's choice
        """
        unweighted_search = UnweightedSearch(self.grid, self.nx, self.ny)
        weighted_search = WeightedSearch(self.grid, self.nx, self.ny)
        self.cost = 0
        
        algorithm_actions = {
            "Amplitude": lambda: unweighted_search.breadthFirstSearch(self.start_pos, self.end_pos),
            "Profundidade": lambda: unweighted_search.depthFirstSearch(self.start_pos, self.end_pos),
            "Profundidade Lim.": lambda: unweighted_search.depthLimitedSearch(self.start_pos, self.end_pos, 99),
            "Aprof. Interativo": lambda: unweighted_search.iterativeDeepeningSearch(self.start_pos, self.end_pos),
            "Bidirectional": lambda: unweighted_search.bidirectionalSearch(self.start_pos, self.end_pos),
            "Custo Uniforme": lambda: weighted_search.uniformCostSearch(self.start_pos, self.end_pos),
            "Guloso": lambda: weighted_search.greedySearch(self.start_pos, self.end_pos),
            "A*": lambda: weighted_search.aStarSearch(self.start_pos, self.end_pos),
            "AAI*": lambda: weighted_search.idaStarSearch(self.start_pos, self.end_pos, 99)
        }

        result = algorithm_actions.get(self.sel_algorithm, lambda: None)()
        
        if result is not None:
            if isinstance(result, tuple):
                self.path, self.cost = result
            else:
                self.path = result
    
    def update_animation(self):
        """
            Atualiza a posição do personagem na animação
        """
        # Carregando as mensagens para o usuário
        message = SystemMessages(self.screen.get_size(), self.manager)
        
        if not self.animation_started or not self.path or self.current_segment >= len(self.path) - 1:
            return False  # Animação não iniciada ou concluída
        
        
        current_time = pygame.time.get_ticks()
        elapsed = (current_time - self.last_move_time) / 1000  # Segundos
        
        # Suavização da animação usando uma curva de ease-in-out
        progress = min(1.0, elapsed / self.animation_speed)
        smoothed_progress = progress * progress * (3 - 2 * progress)  # Suavização cúbica

        # Calcula posição interpolada
        start = self.path[self.current_segment]
        end = self.path[self.current_segment + 1]
    
        self.character_pos[0] = start[0] + (end[0] - start[0]) * smoothed_progress
        self.character_pos[1] = start[1] + (end[1] - start[1]) * smoothed_progress

        # Avança para o próximo segmento quando completar
        if progress >= 1.0:
            self.current_segment += 1
            self.last_move_time = current_time
        if self.current_segment >= len(self.path) - 1:
            self.character_pos = list(self.end_pos)
            
            if(self.sel_selection == 'Com Peso'):
                message.weightedSucessMessage(self.sel_algorithm, self.cost)

            return False  # Animação concluída

        return True  # Animação em andamento
    
    def draw(self):
        """
            Desenha toda a cena
        """
        width, height = self.screen.get_size()
        cell_size = min(width // self.ny, height // self.nx)
        
        # Desenha a grid
        for x in range(self.nx):
            for y in range(self.ny):
                color = (255, 255, 255) if self.grid[x][y] == 0 else (255, 0, 0)
                pygame.draw.rect(self.screen, color, 
                                (y * cell_size, x * cell_size, cell_size, cell_size))
                pygame.draw.rect(self.screen, (0, 0, 0), 
                                (y * cell_size, x * cell_size, cell_size, cell_size), 1)
        
        # Desenha o caminho
        if self.path:
            for i in range(len(self.path) - 1):
                start = self.path[i]
                end = self.path[i+1]
                pygame.draw.line(self.screen, (0, 255, 0),
                               (start[1] * cell_size + cell_size//2, start[0] * cell_size + cell_size//2),
                               (end[1] * cell_size + cell_size//2, end[0] * cell_size + cell_size//2), 3)
        
        # Desenha início e fim
        pygame.draw.circle(self.screen, (0, 255, 0), 
                         (self.start_pos[1] * cell_size + cell_size // 2, 
                          self.start_pos[0] * cell_size + cell_size // 2), 10)
        pygame.draw.circle(self.screen, (255, 0, 0), 
                         (self.end_pos[1] * cell_size + cell_size // 2, 
                          self.end_pos[0] * cell_size + cell_size // 2), 10)
        
        # Desenha o personagem
        char_rect = self.character_image.get_rect(
            center = (self.character_pos[1] * cell_size + cell_size // 2, 
                    self.character_pos[0] * cell_size + cell_size // 2))
        self.screen.blit(self.character_image, char_rect)
        
        
        # Desenha o menu lateral
        menu_x = self.grid_size_pixels
        pygame.draw.rect(self.screen, (30, 30, 30), (menu_x, 0, self.menu_width, self.grid_size_pixels))

        # Títulos e botões
        font = pygame.font.SysFont(None, 28)
        title = font.render("MENU", True, (255, 255, 255))
        self.screen.blit(title, (menu_x + 60, 20))

        button_font = pygame.font.SysFont(None, 24)

        # Botões
        self.draw_button("Reset Grid", (menu_x + 20, 80, 160, 40), button_font)
    
    def run(self):
        """
            Loop principal
        """
        running = True
        while running:
            time_delta = self.clock.tick(60) / 1000.00  # Tempo em segundos
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_r:
                        self.reset_grid()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    # Verifica cliques nos botões do menu
                    if self.grid_size_pixels + 20 <= mx <= self.grid_size_pixels + 180:
                        if 80 <= my <= 120:
                            self.reset_grid()
                    
                self.manager.process_events(event)
                
                # Verificando seleção no dropdown
                if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                    if event.ui_element == self.dropdown:
                        self.sel_algorithm = event.text
                    
                    if event.ui_element == self.dropdown_mode_selection:
                        self.sel_selection = event.text
                        if(self.sel_selection == 'Com Peso'):
                            self.algorithm_option = ['Custo Uniforme', 'Guloso', 'A*', 'AAI*']
                        else:
                            self.algorithm_option = ['Amplitude', 'Profundidade', 'Profundidade Lim.', 'Aprof. Interativo', 'Bidirecional']
                        self.update_algorithm_dropdown()
                
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.botao_ler_texto:
                        starting_pos = self.input_text.get_text()
                        
                        ending_pos = self.input_text2.get_text()
                        
                        if(self.input_text.get_text() == ""):
                            self.sx = 0
                            self.sy = 0
                        else:
                            starting_pos = starting_pos.strip("()").split(",")
                            self.sx = int(starting_pos[0]) - 1
                            self.sy = int(starting_pos[1]) - 1
                        
                        if(self.input_text2.get_text() == ""):
                            self.ex = 9
                            self.ey = 9
                        else:
                            ending_pos = ending_pos.strip("()").split(",")
                            self.ex = int(ending_pos[0]) - 1
                            self.ey = int(ending_pos[1]) - 1
                            
                        # Atualiza as posições e calcula o caminho
                        self.start_pos = (self.sx, self.sy)
                        self.end_pos = (self.ex, self.ey)
                        
                        # Garante que início e fim não são obstáculos
                        self.grid[self.start_pos[0]][self.start_pos[1]] = 0
                        self.grid[self.end_pos[0]][self.end_pos[1]] = 0
                        
                        # Calcula o caminho
                        self.find_path()
                        
                        # Prepara a animação
                        self.character_pos = list(self.start_pos)
                        self.current_segment = 0
                        self.last_move_time = pygame.time.get_ticks()
                        self.animation_started = True  # Habilita a animação
                
            # Atualiza elementos da interface
            self.manager.update(time_delta)
            
            # Atualiza animação (só se estiver habilitada)
            if self.animation_started:
                self.update_animation()
            
            # Desenha tudo
            self.screen.fill((0, 0, 0))
            self.draw()
            self.manager.draw_ui(self.screen)  # desenha o dropdown por cima
            pygame.display.flip()
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    app = UserInterface()
    app.run()