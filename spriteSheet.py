import pygame

class SpriteSheet:
    def __init__(self, filePath, columns, rows):
        self.filePath = filePath
        self.columns = columns
        self.rows = rows

    def strip(self,flipped):
        self.frames = []
        sheet = pygame.image.load(f'Assets/{self.filePath}.png') # file
        r = sheet.get_rect() # rect. x y w h of the hole sprite
        im_width=r.w/self.columns # sub-image
        im_height=r.h/self.rows
        for row in range(self.rows): 
            for col in range(self.columns):
                rect=pygame.Rect(col*im_width,row*im_height,im_width,im_height)
                if flipped == False:
                    self.frames.append(sheet.subsurface(rect))
                else:
                    self.frames.append(pygame.transform.flip(sheet.subsurface(rect),True,False))
        return self.frames
    




# def load_animation (sprite_name):
#     images = []
#     path = f"Assets/{sprite_name}/{sprite_name}"
#     print('ok1')
#     for num in range(1,9):
#         print('ok2')
#         image_path = path + str(num) + '.png'
#         print('ok3')
#         images.append(pygame.image.load(image_path))
#         print('ok4')
#     print('ok5')
#     return images




# def draw_window():
#     BLACK = (0,0,0)
#     WIN = pygame.display.set_mode((900,500))
#     a = 'run.png'
#     b = strip(a,8,1,False)
#     dest = (100, 100)
#     WIN.fill(BLACK)
#     for i in b:
#         WIN.blit(i,dest)
#     pygame.display.flip()

# def main():
#     clock = pygame.time.Clock()
#     run = True
#     FPS = 60
#     while run:
#         clock.tick(FPS)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#                 pygame.quit()
#         draw_window()  

# if __name__ == "__main__":
#     main()