import pygame
from itertools import cycle

carpetaImgs = "rostro/"
IMAGEN_SIN_PALABRAS = carpetaImgs + "Initial.png"
IMAGEN_FELIZ = carpetaImgs + "Rutina 2.png"
IMAGEN_MUY_FELIZ =  carpetaImgs + "Rutina 3.png"
IMAGEN_TRISTE = carpetaImgs + "Rutina 4.png"
IMAGEN_CANSADO = carpetaImgs + "Rutina 5.png"
IMAGEN_ENOJADO = carpetaImgs + "Rutina 6.png"
IMAGEN_ASOMBRADO = carpetaImgs + "Rutina 7.png"

# Inicializa Pygame
pygame.init()

# Dimensiones de la ventana
window_width = 800
window_height = 480

# Crea la ventana sin bordes
window = pygame.display.set_mode((window_width, window_height), pygame.NOFRAME)
pygame.display.set_caption("Cambio de Imágenes")

# Lista de rutas de imágenes
imagenes = [IMAGEN_SIN_PALABRAS, IMAGEN_ENOJADO, IMAGEN_ASOMBRADO]

timer = pygame.time.Clock()
expressions = cycle(imagenes)
current = next(expressions)
pygame.time.set_timer(pygame.USEREVENT, 5000)

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