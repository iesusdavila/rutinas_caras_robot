import pygame
from itertools import cycle

# Inicializa Pygame
pygame.init()

# Dimensiones de la ventana
window_width = 800
window_height = 480

# Crea la ventana sin bordes
window = pygame.display.set_mode((window_width, window_height), pygame.NOFRAME)
pygame.display.set_caption("Cambio de Imágenes")

# Lista de rutas de imágenes
imagenes = ["rostro/Initial.png", "rostro/Rutina 2.png", "rostro/Rutina 3.png"]

timer = pygame.time.Clock()
expressions = cycle(imagenes)
current = next(expressions)
pygame.time.set_timer(pygame.USEREVENT, 1000)

# Bucle principal
running = True
while running:
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT: 
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
        if e.type == pygame.USEREVENT:
            current = next(expressions)
            
    imagen = pygame.image.load(current)        
    window.blit(imagen, (0, 0))
    
    # Muestra la ventana
    pygame.display.flip()
    
    timer.tick(1)
    pygame.display.update()

# Finaliza Pygame
pygame.quit()