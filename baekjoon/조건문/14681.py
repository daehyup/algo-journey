numberOne = int(input())
numberTwo = int(input())

if -1000 <= numberOne <= 1000 and numberOne != 0 and -1000 <= numberTwo <= 1000 and numberTwo != 0:
  if numberOne > 0 and numberTwo > 0:
    print('1')
  elif numberOne < 0 and numberTwo > 0:
    print('2')
  elif numberOne < 0 and numberTwo < 0:
    print('3')
  else:
    print('4')