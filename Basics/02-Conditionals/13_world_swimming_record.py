import math
record_seconds = float(input())
distance_meters = float(input())
time_seconds_one_meter = float(input())

must_swimm = distance_meters * time_seconds_one_meter
every_15_meter_resistance = math.floor(distance_meters / 15)  * 12.5
total_time = must_swimm + every_15_meter_resistance

world_record = record_seconds - total_time
no_world_record = total_time - record_seconds

if total_time < record_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {no_world_record:.2f} seconds slower.")





