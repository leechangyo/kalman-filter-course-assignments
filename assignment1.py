import numpy as np
from sim.sim1d import sim_run

# Simulator options.
options = {}
options['FIG_SIZE'] = [8,8]
options['CONSTANT_SPEED'] = True

class KalmanFilterToy:
    def __init__(self):
        self.v = 0
        self.prev_x = 0
        self.prev_t = 0
    def predict(self,t):
        return self.v*(t-self.prev_time) + self.prev_x
    def measure_and_update(self,x,t):
        measured_v = (x-self.prev_x)/(t-self.prev_time)
        self.v + = 0.5*(measured_v - self.v)
        # 0.5 is the weight, so to need to find out which weight is best to reduce error(Deep Learning idea)
        
        self.prev_x =x
        self.prev_time = t
        return
    # 내생각에는 그냥 밸류를 사용하거나 업데이트 시키는 것이다.


sim_run(options,KalmanFilterToy)
