x = input("Enter a number")
try:
    num = int(x)
    print(100 / num)

except ZeroDivisionError:
    print("ZeroDivisionError")

except ValueError:
    print("value error")

else:
    print(f"no error")

finally:
    print("success")
