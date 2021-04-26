import pygame

class SpriteSheet:
    def __init__(self, files):
        self.files = files
        self.sheets = []
        for i in range(len(files)):
            self.sheets.append(pygame.image.load(f'Assets/{self.files[i][0]}.png'))


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