data = "string"
print(hasattr(data, "reverse"))
print(hasattr(data, "index"))

print(f"!!! {data.startswith('st')} !!!")

starts = getattr(data, "startswith", "st")

print(type(starts))