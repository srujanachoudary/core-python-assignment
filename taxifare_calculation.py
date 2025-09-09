def calculate_fare(distance):
    base_fare = 50
    per_km_rate = 10
    return base_fare + (distance * per_km_rate)


# Input
trips = [5, 10, 3]

total_fare = 0

# Process each trip
for i, distance in enumerate(trips, start=1):
    fare = calculate_fare(distance)
    print(f"Trip {i}: ${fare}")
    total_fare += fare

# Output total
print("Total Fare:", f"${total_fare}")
