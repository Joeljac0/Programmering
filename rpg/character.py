class Character:
    def __init__(self, x_pos, y_pos, health, speed, damage):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.health = health
        self.speed = speed
        self.damage = damage

    def set_pos(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def change_pos(self, x, y):
        self.x_pos += x
        self.y_pos += y

    def get_pos(self):
        return(self.x_pos, self.y_pos)