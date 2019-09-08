var = (int(input("Please enter minutes to be converted into hours: ")))
hour = (var) // 60
minute = (var) % 60

if 0 == minute:
    print("{} minutes converted into hours is equal to {} hours.".format(var, hour))
elif 1 == minute:
    print("{} minute converted into hours is equal to {} hours and {} minute.".format(var, hour, minute))
else:
    print("{} minutes is equal to {} hours and {} minutes.".format(var, hour, minute))
