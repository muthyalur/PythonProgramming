#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
def addition(num1, num2, num3, num4):
	answer = num1+num2+num3+num4
	return answer
	
print(addition(5,6,7,8))


def website(fnt_name, fnt_size, fnt_color):
	print('Font Name:-', fnt_name)
	print('Font Size:-', fnt_size)
	print('Font Color:-', fnt_color)
	
website('Times New Roman',12,'black')
	
def website(fnt_name='default_name', fnt_size=14, fnt_color=12, bg_color='red'):
	print('Font Name:-', fnt_name)
	print('Font Size:-', fnt_size)
	print('Font Color:-', fnt_color)
	print('Background Color:-', bg_color)
	
website(fnt_size = 12,fnt_color = 'black',fnt_name = 'TNR',bg_color='White')
website(fnt_name='Calibri')