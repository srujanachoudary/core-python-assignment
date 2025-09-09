def reserveseat(seat,booked,total_seats):
    if seat<1 or seat>total_seats:
        print(f"{seat} is invalid")
    elif seat in booked:
        print(f"{seat} is already booked")
    else:
        booked.append(seat)
        print(f"{seat} is booked successfully")
def cancel_seat_func(seat,booked):
    if seat in booked:
        booked.remove(seat)
        print(f"{seat} booking cancelled")
    else:
        print(f"{seat} was not booked")
def available_seats(total_seats,booked):
    return [s for s in range(1,total_seats+1) if s not in booked]
#input
total_seats=10
booked=[2,5,7]

book_seat=3
cancel_seat=5

reserveseat(book_seat,booked,total_seats)
cancel_seat_func(cancel_seat,booked)

print("Available seats:",available_seats(total_seats,booked))