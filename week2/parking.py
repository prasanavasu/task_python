space = [0]*20
Idd = {}
class parkingspaces():
	 
	 def __init__(self):
	 	
	 	print(f"parking for vehicles slot ")

	 def small(self,val,Id):
	 	space[int(val)-1] = 1
	 	Idd[Id] = str(space[int(val)-1])
	 	#print(f"motorcycle(small)")

	 def medium(self,val,Id):
	 	space[int(val)-1] = 2
	 	Idd[Id] = str(space[int(val)-1])
	 	# print("car(medium)")

	 def large(self,val,Id):
	 	space[int(val)-1] = 3
	 	Idd[Id] = str(space[int(val)-1])
	 	# print("bus(large)")

	 def unfilledslot(self):
	 	self.__space = []
	 	for i,j in enumerate(space):
	 		if j ==0:
	 			self.__space.append(i+1)
	 	print(f'\n free space for parking slot {self.__space}')
	 	print("****************************** \n")

	 def check(self,count=0):
	 	if count == 0:
	 		print(f'filled slot {space} \n ****************************** \n filled id with parking slot {Idd}')
	 		print("******************************\n")
	 	else:
	 		count = space.count(count)
	 	return count

class parkinglot(parkingspaces):

	def __init__(self):
		super().__init__()
		# print("parking lot")

def ticket(vehicletype,vehicleID):
	pk = parking_lot()

	if vehicletype == 'small':
		#print('small:',vehicle_ID)
		pk.unfilled_slot()
		val = input('Enter the slot:')
		c = pk.check(1)
		if c != 10:
			pk.small(val,vehicleID)
		else:
			print("filled")

	elif vehicletype == 'medium':
		#print('medium:',vehicle_ID) 
		pk.unfilled_slot()
		val = input('Enter the slot:')
		c = pk.check(2)
		if c != 7:
			pk.medium(val,vehicleID)
		else:
			print("filled")

	elif vehicletype == 'large':
		#print('large:',vehicle_ID) 
		pk.unfilledslot()
		val = input('Enter the slot:')
		c = pk.check(3)
		if c != 3:
			pk.large(val,vehicleID)
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

	

	
while True:
	print("******************************")
	print('For example: \n two wheels \n  Enter the vehicle_type : small \n\ncar is light vechile \n Enter the vehicle_type : medium \n\n lorry is heavy vechile \n Enter the vehicle_type : large \n')
	print("******************************")
	vehicle_type = input('Enter the vehicle_type :')
	print()
	vehicle_ID = input('enter the vechicle ID:')
	print("******************************")
	s = ticket(vehicle_type,vehicle_ID)
	if s == 'quit':
		break
	
	
	
	
	
	
