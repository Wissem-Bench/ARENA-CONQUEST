from spriteSheet import SpriteSheet 

class Assets:

    def __init__(self):
        self.heroknight = self.parceling(SpriteSheet([["HeroKnight", 10, 9]]), [8, 18, 24])
        self.skeleton = self.parceling(SpriteSheet([["Skeleton Idle", 11, 1], 
                                                    ["Skeleton Walk", 13, 1],
                                                    ["Skeleton Attack", 18, 1]]), [11, 24, 42])


        # self.heroknight = self.parceling(SpriteSheet([["HeroKnight", 8, 1], ["file 2", 8, 1]]), [8, 18, 24])

    def parceling(self, spritesheet, indexes):
        result = []
        lastIndex = 0
        frames = spritesheet.strip()
        for index in indexes:
            result.append(frames[0][lastIndex: index])
            result.append(frames[1][lastIndex: index])
            lastIndex = index
        return result # array of arrays (group of frames)
