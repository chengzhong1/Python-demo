import pymunk as pm
class Physis():
    def __init__(self):
        self.reset()
    def reset(self,level=None):
        self.space=pm.Space
        self.space.gravity=(0.0,-700.0)
        self.dt=0.002
        self.swk=[]
        self.dragons=[]
        self.path_timer=0
        self.check_collide=False
        self.setup_lines()
        self.setup_collision_handler()
    def setup_lines(self):
        x,y=to_pymunk(c.SCREEN_WIDTH,c.GROUND_HEIGHT)
        static_body=pm.Body(body_type=pm.Body.STATIC)
        static_lines=[pm.Segment(static_body,(0.0,y),(x,y),0.0)]
        for line in static_lines:
            line.elasticity=0.95
            line.friction=1
            line.collision_type=COLLISION_LINE
        self.space.add(static_lines)
        self.static_lines=static_lines