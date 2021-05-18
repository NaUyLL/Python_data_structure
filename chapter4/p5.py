'''
author: Luo ly
'''
from random import randint
from .p2 import SQueue
from .p4 import PrioQueue

class Simulation:
    def __init__(self, duration):
        self._eventq = PrioQueue()
        self._time = 0
        self._duration = duration

    def run(self):
        while not self._eventq.is_empty():
            event = self._eventq.dequeue()
            self._time = event.time()
            if self._time > self._duration:
                break
            event.run()

    def add_event(self, event):
        self._eventq.enqueue(event)

    def cur_time(self):
        return self._time

class Event:
    def __init__(self, event_time, host):
        self._ctime = event_time
        self._host = host

    def __lt__(self, other):
        return self._ctime < other._ctime

    def __le__(self, other):
        return self._ctime <= other._ctime

    def host(self):
        return self._host

    def time(self):
        return self._ctime

    def run(self):
        pass

class Customs:
    def __init__(self, gate_num, duration, arrive_interval, check_interval):
        self.simulation = Simulation(duration)
        self.waitline = SQueue()
        self._duration = duration
        self.gates = [0] * gate_num
        self.total_wait_time = 0
        self.total_used_time = 0
        self.car_num = 0
        self.arrive_interval = arrive_interval
        self.check_interval = check_interval

    def wait_time_acc(self, n):
        self.total_wait_time += n

    def total_time_acc(self, n):
        self.total_used_time += n

    def car_count_1(self):
        self.car_num += 1

    def add_event(self, event):
        self.simulation.add_event(event)

    def cur_time(self):
        return self.simulation.cur_time()

    def enqueue(self, car):
        self.waitline.enqueue(car)

    def has_queued_car(self):
        return not self.waitline.is_empty()

    def next_car(self):
        return self.waitline.dequeue()

    def find_gate(self):
        for i in range(len(self.gates)):
            if self.gates[i] == 0:
                self.gates[i] = 1
                return i
        return None

    def free_gate(self, i):
        if self.gates[i] == 1:
            self.gates[i] = 0
        else:
            raise ValueError("Clear gate error.")

    def simulate(self):
        Arrive(0, self)
        self.simulation.run()
        self.statistics()

    def statistics(self):
        print("Simulate " + str(self.duration) + " minutes, for " + str(len(self.gates)) + " gates")
        print(self.car_num, "cars pass the customs")
        print("Average waiting time:", self.total_wait_time/self.car_num)
        print("Average passing time:", self.total_used_time/self.car_num)
        i = 0
        while not self.waitline.is_empty():
            self.waitline.dequeue()
            i += 1
        print(i, "cars are in waiting line.")

class Car:
    def __init__(self, arrive_time):
        self.time= arrive_time

    def arrive_time(self):
        return self.time

def event_log(time, name):
    print("Event: " + name + ", happens at " + str(time))
    pass

class Arrive(Event):
    def __init__(self, arrive_time, customs):
        Event.__init__(self, arrive_time, customs)
        customs.add_event(self)

    def run(self):
        pass


if __name__ == "__main__":
    pass
