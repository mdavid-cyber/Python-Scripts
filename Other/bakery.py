victoria_sponge = {"flour", "sugar", "eggs", "milk", "cream", "jam"}
lemon_drizzle = {"sugar", "eggs", "butter", "lemon"}

unique_to_sponge = victoria_sponge.difference(lemon_drizzle)
print("Ingredients only in Victoria sponge: ", unique_to_sponge)
