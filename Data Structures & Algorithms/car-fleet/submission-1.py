class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair position with time to reach target
        cars = [(pos, (target - pos) / spd) for pos, spd in zip(position, speed)]
        # Sort by position descending
        cars.sort(reverse=True)

        fleets = 0
        curr_time = 0

        for pos, time in cars:
            if time > curr_time:
                fleets += 1
                curr_time = time
            # else: car joins the fleet ahead

        return fleets
