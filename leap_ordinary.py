user_year = int(input())

print("Leap" if not user_year % 4 and user_year % 100 or not user_year % 400 else "Ordinary")
