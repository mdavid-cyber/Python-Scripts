classical_entrants = {"ann", "bob", "cam", "dan"}
modern_entrants = {"cam", "dan", "eve", "fay"}

exclusive_students = classical_entrants.symmetric_difference(modern_entrants)
print("Students entered for a single genre: ", exclusive_students)
