# List
lst = [10, 20, 30, 40]
print(30 in lst)   # ✅ True

# Set
st = {10, 20, 30, 40}
print(30 in st)    # ✅ True

# Dictionary (checks only KEYS by default)
dct = {"a": 10, "b": 20, "c": 30}
print(30 in dct)          # ❌ False (because it checks KEYS, not values)
print(30 in dct.values()) # ✅ True (now checking values)

