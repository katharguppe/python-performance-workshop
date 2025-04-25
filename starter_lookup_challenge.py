import random, string, sys, time

# DO NOT MODIFY THIS
random.seed(42)
keys = ["user_" + random.choice(string.ascii_letters) for _ in range(10000)]

# ✅ Your task begins here

# 1. Create an interned dictionary and time the lookup
start = time.time()

# TODO: Create interned dictionary using sys.intern()
# TODO: Perform lookup in loop

interned_lookup_time = time.time() - start

# 2. Create a plain dictionary and time the lookup
start = time.time()

# TODO: Create plain dictionary
# TODO: Perform lookup in loop

plain_lookup_time = time.time() - start

# 3. Calculate the difference
lookup_time_difference = plain_lookup_time - interned_lookup_time
print("lookup_time_difference =", lookup_time_difference)
