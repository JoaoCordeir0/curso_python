import calendar

# print(calendar.calendar(2024)) 
# print(calendar.month(2024, 8)) 
primeiro_dia, ultimo_dia = calendar.monthrange(2024, 8)

print(calendar.day_name[primeiro_dia])
print(calendar.day_name[calendar.weekday(2024, 12, ultimo_dia)])