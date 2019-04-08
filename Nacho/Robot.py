import users
import map

class Robot:

    def __init__(self, name, position):
        self.name = name
        self.x = None
        self.y = None
        self.ressources = {}
        self.position = position
        self.ressources = {}
        self.isPaused = False

    def __str__(self):
        return f"{self.name} {'PAUSED' if self.isPaused else 'In_Acivity'} ({self.x},{self.y})"

    def move_up(ip):
        username = users.getIP(ip)
