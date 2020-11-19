space = [0]*20
Id = {}
class parking_spaces():
	 
	 def __init__(self):
	 	
	 	print(f"parking for vehicles slot ")

	 def small(self,val,Id):
	 	space[int(val)-1] = 1
	 	Id[Id] = space[int(val)-1]
	 	#print(f"motorcycle(small)")

	 def medium(self,val,Id):
	 	space[int(val)-1] = 2
	 	Id[Id] = space[int(val)-1]
	 	# print("car(medium)")

	 def large(self,val,Id):
	 	space[int(val)-1] = 3
	 	Id[Id] = space[int(val)-1]
	 	# print("bus(large)")

	 def unfilled_slot(self):
	 	self.__space = []
	 	for i,j in enumerate(space):
	 		if j ==0:
	 			self.__space.append(i+1)
	 	print(f'\n free space for parking slot {self.__space}')

	 def check(self,count=0):
	 	if count == 0:
	 		print(f'filled slot {space} \n filled id with parking slot {Id}')
	 	else:
	 		count = space.count(count)
	 	return count

class parking_lot(parking_spaces):

	def __init__(self):
		super().__init__()
		# print("parking lot")

def tic(vehicle_type,vehicle_ID):
	pk = parking_lot()

	if vehicle_type == 'small':
		print('small:',vehicle_ID)
		pk.unfilled_slot()
		val = input('Enter the slot:')
		c = pk.check(1)
		if c != 10:
			pk.small(val,vehicle_ID)
		else:
			print("filled")

	elif vehicle_type == 'medium':
		print('medium:',vehicle_ID) 
		pk.unfilled_slot()
		val = input('Enter the slot:')
		c = pk.check(2)
		if c != 7:
			pk.medium(val,vehicle_ID)
		else:
			print("filled")

	elif vehicle_type == 'large':
		print('large:',vehicle_ID) 
		pk.unfilled_slot()
		val = input('Enter the slot:')
		c = pk.check(3)
		if c != 3:
			pk.large(val,vehicle_ID)
		else:
			print("***************--filled--***************")

	else:
		print('type : small or medium or large \n')
		
	print('you want to quit enter quit')
	che = input('check the filled slot enter yes or no or quit:')
	if che == 'yes':
	
		pk.check()

	elif che == 'quit':
		return che
	else:
		pass

	pk.unfilled_slot()

	
while True:
	
	print('For example: \n two wheels \n  Enter the vehicle_type : small \n\ncar is light vechile \n Enter the vehicle_type : medium \n\n lorry is heavy vechile \n Enter the vehicle_type : large \n')
	vehicle_type = input('Enter the vehicle_type :')
	print()
	vehicle_ID = input('enter the vechicle ID:')

	s = tic(vehicle_type,vehicle_ID)
	if s == 'quit':
		break
	
	
	
	
	
	
