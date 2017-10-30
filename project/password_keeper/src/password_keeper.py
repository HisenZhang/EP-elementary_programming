import sys

def emmm():
	print (' eeeee    mmm mmm     mmm mmm    mmm mmm                 ')
	print ('e     e  m   m   m   m   m   m  m   m   m                ')
	print ('eeeeeee  m   m   m   m   m   m  m   m   m   ..   ..   .. ')
	print ('e        m   m   m   m   m   m  m   m   m  .... .... ....')
	print (' eeeee   m   m   m   m   m   m  m   m   m   ..   ..   .. ')
print ('Welcome to the brilliant password keeper!')
import getpass
name1 = 'Mr. Agent 47(GCaesar)'
passwd = '123456789'
print ('username:',name1)  # use comma to seperate parameters
password = getpass.getpass ('please enter the password:')
if password == passwd:
	print ('Welcome back')
	print ('Common password:(abc)123456789')
	print ('pay password:666666')
	d = input ('>>> Please give out command.')
	if d == exit:	# 'if' is at the same level as the previous structure, not indent needed this line
		print ('>>> Goodbye.')
		sys.exit(0)
	else:
			print ('-HFLS2017-')
else:
	print ('-Unkown visitor-')
	print ('>>> program rebooting...')
	print ('>>> Hello, Im an artificial intelligence written by Jerry.')
	print('>>> Whats your name?')
	input('Im ')
	print ('>>> Hello,') # comma
	print ('>>> If you are looking at me, that means you are using my computer and browsed a security program.')
	print ('>>> Its not allowed.')
	b = input ('>>> clear?')
	emmm()
	print ('>>> Its time for you to leave. [exit]')
	sys.exit(0)	# indent not consistant
