class Level(object):
    """
    A class for our map. Maps in this implementation are one image; not
    tile based. This makes collision detection simpler but can have performance
    implications.
    """
    def __init__(self, map_image, viewport, player):
        """
        Takes an image from which to make a mask, a viewport rect, and a
        player instance.
        """
        self.image = map_image
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.player = player
        self.player.rect.center = self.rect.center
        self.viewport = viewport

    def update(self, keys):
        """
        Updates the player and then adjust the viewport with respect to the
        player's new position.
        """
        self.player.update(self.mask, keys)
        self.update_viewport()

    def update_viewport(self):
        """
        The viewport will stay centered on the player unless the player
        approaches the edge of the map.
        """
        self.viewport.center = self.player.rect.center
        self.viewport.clamp_ip(self.rect)

    def draw(self, surface):
        """
        Blit actors onto a copy of the map image; then blit the viewport
        portion of that map onto the display surface.
        """
        new_image = self.image.copy()
        self.player.draw(new_image)
        surface.fill((50,255,50))
        surface.blit(new_image, (0,0), self.viewport)