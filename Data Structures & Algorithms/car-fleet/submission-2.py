class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed), reverse = True)
        prev_time = (target - cars[0][0]) / cars[0][1]
        fleet = 1
        for car in cars:
            time = (target - car[0]) / car[1]
            if time > prev_time:
                fleet += 1
                prev_time = time

        return fleet
                

