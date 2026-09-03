movies = ["Inception", "The Matrix", "Interstellar"]

movie = input("Enter movie name: ")

if movie in movies:
    print("Already added!")
else:
    movies.append(movie)
    print("Added", movie + "!")

movies.sort()

print("Alphabetical Playlist:", movies)