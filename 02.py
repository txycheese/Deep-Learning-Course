Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> def quadratic(a,b,c):
	if a==0 and b!=0:
		errorStatus = "a=0&&b!=0,该方程非一元二次方程"
		return errorStatus
	else:
		delta = b*b-4*a*c
		if delta > 0:
			x1 = (-b+math.sqrt(delta))/2/a
			x2 = (-b-math.sqrt(delta))/2/a
			elif delta == 0:
				
SyntaxError: invalid syntax
>>> import math
>>> def quadratic(a,b,c):
	if a==0 and b!=0:
		errorStatus = "a=0&&b!=0,该方程非一元二次方程"
		return errorStatus
	else:
		delta = b*b-4*a*c
		if delta > 0:
			x1 = (-b+math.sqrt(delta))/2/a
			x2 = (-b-math.sqrt(delta))/2/a
		elif delta == 0:
			x1 = x2 = -b/2/a
			else:
				
SyntaxError: invalid syntax
>>> import math
>>> def quadratic(a,b,c):
	if a==0 and b!=0:
		errorStatus = "a=0&&b!=0,该方程非一元二次方程"
		return errorStatus
	else:
		delta = b*b-4*a*c
		if delta > 0:
			x1 = (-b+math.sqrt(delta))/2/a
			x2 = (-b-math.sqrt(delta))/2/a
		elif delta == 0:
			x1 = x2 = -b/2/a
		else:
			errorStatus = "delta<0,该方程无实根"
			return errorStatus
		return x1,x2
	print('quadratic(0,1,2) 测试结果:',quadratic(0,1,2))
	print('quadratic(2,4,4) 测试结果:',quadratic(2,4,4))
	print('quadratic(2,4,2) 测试结果:',quadratic(2,4,2))
	print('quadratic(2,3,1) 测试结果:',quadratic(2,3,1))
	
