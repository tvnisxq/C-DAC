# build the machine.

def compile_feedback(ratings_dict):
    result = {}
    for course, ratings in ratings_dict.items():
        total = 0
        count = 0
        for rating in ratings:
            try:
                number =float(rating)
                total = total + number
                count = count + 1

            except(ValueError, TypeError):
                print(f"warning : Invalid rating value for '{rating}' in course '{course}'.skipped.")

        try:
            average  = total / count
            result[course] = round(average, 2)

        except ZeroDivisionError:
            print (f"warning :Warning: No valid ratings found for course '{course}'. Rating set to 0.0.")
            result [course] = 0.0

    return result



# giving some data to machine 

feedback_data = {
    "Python Programming": [5, 4, "4", "Great", 5],
    "Machine Learning": [],
    "Deep Learning": ["Good", "Average", None]
}

# runnig and showing the answer
final_ratings = compile_feedback(feedback_data)
print(final_ratings)

            
