#write  program to accept time in minutes and display in hour and minute format

minutes=int(input('enter the time in minutes : '))

print(str(minutes//60) + 'hours' + ' ' + str(minutes%60) + 'minutes')

