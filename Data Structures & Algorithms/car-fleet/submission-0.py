class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed), reverse = True)
        fleet = 0
        fleet_arrive_time = 0
        for pos, speed in cars:
            time = (target - pos)/speed;
            if time > fleet_arrive_time:
                fleet += 1
                fleet_arrive_time = time
        return fleet
        