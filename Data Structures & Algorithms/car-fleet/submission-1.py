class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        #Tuple会先比较第一个值，也就是位置, 按位置从大到小排序，也就是越靠近target越在前
        fleets = 0 #目前数到了几个车队
        front_fleet_time = 0 #最近一个已形成的前方车队到达终点的时间

        for pos, speed in cars:
            time = (target - pos) / speed #这辆车“独自开”的到达时间

            if time > front_fleet_time: #判断是否形成新车队, if > ,无法相遇，车队+1
                fleets += 1
                front_fleet_time = time #只处理最后面这辆

        return fleets
# 排序需要 O(n log n) 时间。
# for 循环处理每辆车一次，需要 O(n) 时间。
# 因此总时间是 O(n log n)；cars 存储所有车辆，需要 O(n) 空间。
# I pair each car’s position with its speed. Then I sort the cars by position, from closest to the target to farthest.
# For each car, I calculate how long it would take to reach the target if it drove alone. I compare that time with the arrival time of the nearest fleet ahead of it.
# If the car would arrive later, it cannot catch that fleet, so it starts a new fleet. I increase the fleet count and update the fleet’s arrival time. Otherwise, it catches the fleet before or at the target, so the fleet count stays the same.
# After I’ve checked all the cars, I return the fleet count.
# I only need to keep the arrival time of the nearest fleet ahead. Sorting takes O(n log n) time, and the scan takes O(n) time. The space complexity is O(n).