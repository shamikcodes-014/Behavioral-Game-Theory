import pygame  
FPS = 60  
pygame.init()  
pygame.mixer.quit()  
clock = pygame.time.Clock()  
movie = pygame.movie.Movie(r'F:\Final Year Project\Game version updated\Game-theory-master\assets\videos\vid_3.mp4')  
screen = pygame.display.set_mode(movie.get_size())  
movie_screen = pygame.Surface(movie.get_size()).convert()  
movie.set_display(movie_screen)  
movie.play()  
playing = True  
while playing:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            movie.stop()  
            playing = False  
screen.blit(movie_screen,(0,0))  
pygame.display.update()  
clock.tick(FPS)  
pygame.quit()