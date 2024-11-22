result = []
def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a/b
data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}
for key, value in data.items():
    try:
        key = int(key)
        res = divider(key, value)
        result.append(res)
    except ZeroDivisionError:
        print(f"ZeroDivisionError for ({key}, {value})")
    except ValueError:
        print(f"ValueError for ({key}, {value})")
    except IndexError:
        print(f"IndexError for ({key}, {value})")
print(result)