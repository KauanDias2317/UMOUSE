import API
import sys
from collections import deque

class MicroMouse:
    def __init__(self):
        # Configurações iniciais
        self.maze_width = API.mazeWidth()
        self.maze_height = API.mazeHeight()
        self.x = 0
        self.y = 0
        self.orient = 0  # 0: Norte, 1: Leste, 2: Sul, 3: Oeste
        
        # ETAPA 1 (PDF): Matriz M (Paredes) e Matriz D (Distâncias)
        # Inicializamos paredes como False (Otimista: assume passagem livre até provar contrário)
        self.walls = [[[False] * 4 for _ in range(self.maze_height)] for _ in range(self.maze_width)]
        self.dist_map = [[-1] * self.maze_height for _ in range(self.maze_width)]
        
        # Definição do Objetivo (Centro do labirinto)
        self.goals = self.get_center_goals()
        
    def get_center_goals(self):
        """Identifica as células centrais (objetivo)."""
        if self.maze_width % 2 == 1:
            return [(self.maze_width // 2, self.maze_height // 2)]
        # Labirintos pares (ex: 16x16) têm 4 células centrais
        cx, cy = self.maze_width // 2, self.maze_height // 2
        return [(cx, cy), (cx-1, cy), (cx, cy-1), (cx-1, cy-1)]

    def update_walls(self):
        """Lê sensores e marca paredes na Matriz M (Mundo)."""
        walls_detected = []
        if API.wallFront(): walls_detected.append(self.orient)
        if API.wallRight(): walls_detected.append((self.orient + 1) % 4)
        if API.wallLeft():  walls_detected.append((self.orient + 3) % 4)
        
        for d in walls_detected:
            self.set_wall(self.x, self.y, d)

    def set_wall(self, x, y, direction):
        """Registra parede na célula atual e na vizinha (bloqueio bidirecional)."""
        self.walls[x][y][direction] = True
        API.setWall(x, y, self.dir_char(direction))
        
        nx, ny = self.get_neighbor(x, y, direction)
        if self.is_valid(nx, ny):
            opp_dir = (direction + 2) % 4
            self.walls[nx][ny][opp_dir] = True

    def flood_fill(self):
        """ETAPA 2 (PDF): Preencher distâncias como ondas."""
        # Reinicia a Matriz D com "infinito" (valor alto) para recálculo
        for x in range(self.maze_width):
            for y in range(self.maze_height):
                self.dist_map[x][y] = 9999
                API.setText(x, y, "")

        queue = deque()
        
        # Configura objetivos com valor 0
        for gx, gy in self.goals:
            self.dist_map[gx][gy] = 0
            queue.append((gx, gy))
            API.setText(gx, gy, "0")

        # Algoritmo de Onda (BFS) [cite: 37]
        while queue:
            cx, cy = queue.popleft()
            current_dist = self.dist_map[cx][cy]

            for d in range(4):
                # Se existe parede (M=1), a onda não passa
                if self.walls[cx][cy][d]:
                    continue

                nx, ny = self.get_neighbor(cx, cy, d)
                if self.is_valid(nx, ny):
                    # Se encontrou um caminho mais curto, atualiza e propaga
                    if self.dist_map[nx][ny] > current_dist + 1:
                        self.dist_map[nx][ny] = current_dist + 1
                        queue.append((nx, ny))
                        API.setText(nx, ny, str(self.dist_map[nx][ny]))

    def step(self):
        """Executa um ciclo de controle do robô."""
        # 1. Ler sensores e atualizar mapa (Matriz M)
        self.update_walls()
        API.setColor(self.x, self.y, "G") # Visualização do rastro
        
        # 2. Recalcular distâncias (Matriz D - Ondas)
        self.flood_fill()

        # 3. Verificar Objetivo
        if self.dist_map[self.x][self.y] == 0:
            return True

        # ETAPA 3 (PDF): Encontrar o caminho de volta (mover para menor valor)
        best_dir = -1
        min_dist = 99999

        # Verifica os 4 vizinhos
        possible_moves = []
        for d in range(4):
            if not self.walls[self.x][self.y][d]: # Se livre
                nx, ny = self.get_neighbor(self.x, self.y, d)
                if self.is_valid(nx, ny):
                    dist = self.dist_map[nx][ny]
                    possible_moves.append((dist, d))
                    if dist < min_dist:
                        min_dist = dist
                        best_dir = d
        
        # Se houver movimento válido, executa
        if best_dir != -1:
            self.move(best_dir)
        
        return False

    def move(self, direction):
        """Gira e move para frente."""
        turns = (direction - self.orient) % 4
        if turns == 1: API.turnRight()
        elif turns == 2: 
            API.turnRight(); API.turnRight()
        elif turns == 3: API.turnLeft()
        
        self.orient = direction
        API.moveForward()
        self.x, self.y = self.get_neighbor(self.x, self.y, self.orient)

    def get_neighbor(self, x, y, direction):
        if direction == 0: return x, y + 1 # Norte (API MMS usa Y crescendo pra cima)
        if direction == 1: return x + 1, y # Leste
        if direction == 2: return x, y - 1 # Sul
        if direction == 3: return x - 1, y # Oeste
        return x, y

    def is_valid(self, x, y):
        return 0 <= x < self.maze_width and 0 <= y < self.maze_height

    def dir_char(self, d): return ['n', 'e', 's', 'w'][d]

def main():
    bot = MicroMouse()
    API.log("Iniciando Algoritmo de Ondas...")
    while True:
        if bot.step():
            API.log("Objetivo Alcancado!")
            API.ackReset()
            break

if __name__ == "__main__":
    main()