def positive_feedback_percentage(ratings):
    if not ratings:  # handle empty case
        return "No ratings available."
    
    total = len(ratings)
    positive = sum(1 for r in ratings if r >= 4)
    percentage = (positive / total) * 100
    return round(percentage, 2)


# Input
ratings = [5, 4, 3, 5, 2, 4, 1, 5]

# Process
result = positive_feedback_percentage(ratings)

# Output
if isinstance(result, str):
    print(result)
else:
    print("Positive Feedback Percentage:", result, "%")
