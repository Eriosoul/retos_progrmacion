"""
 * Crea una función que sea capaz de detectar si existe un viernes 13
 * en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
"""
import calendar
import time
c = calendar.calendar(2023)
print(c)

year = 1984
month = 12


while True:
    cal = calendar.monthcalendar(year, month)

    for week in cal:
        for day in week:
            if day == 13 and week[calendar.FRIDAY] == 13:
                print(f"El viernes 13 fue encontrado en : {day} {calendar.month_name[month]} del {year}")
                break

    month += 1
    if month > 12:
        year += 1
        month = 1

    time.sleep(1)

#
# import calendar
# c = calendar.calendar(2018)
# m = calendar.monthcalendar(2018, 7)
# mo = calendar.month(2018, 5)
#
# print(c)
# print("*********")
# print(m)
# print(mo)
#
#
# print("==================================")
# obj = calendar.Calendar(firstweekday=5)
# for day in obj.itermonthdays2(2018, 6):
#     print(day)
