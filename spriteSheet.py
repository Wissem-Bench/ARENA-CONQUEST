import pygame, pygame.transform, pygame.image

class SpriteSheet:
    def __init__(self, files, scale):
        self.scale = scale
        self.files = files
        self.sheets = []
        
        for i in range(len(files)):
            self.sheets.append(pygame.image.load(f'Assets/{self.files[i][0]}.png'))
            for j in range(len(self.sheets)):
                x_scale = int(self.sheets[j].get_width()/scale[0])
                y_scale = int(self.sheets[j].get_height()/scale[1])
                self.sheets[j] = pygame.transform.scale(self.sheets[j], (x_scale, y_scale))
            
            # for k in range(len(self.sheets)) :
            #     self.sheets[k].fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)


    def strip(self): # fill frames array with a group of sub images by striping the sheet
        right_frames = []
        left_frames = []
        for i in range(len(self.files)):
            r = self.sheets[i].get_rect() # rect. x y w h of the hole sprite
            columns = self.files[i][1]
            rows = self.files[i][2]
            im_width=r.w/columns # sub-image
            im_height=r.h/rows
            for row in range(rows):
                for col in range(columns):
                    rect=pygame.Rect(col*im_width,row*im_height,im_width,im_height)
                    right_frames.append(self.sheets[i].subsurface(rect))
                    left_frames.append(pygame.transform.flip(self.sheets[i].subsurface(rect),True,False))
        self.frames = [right_frames, left_frames]
        return self.frames