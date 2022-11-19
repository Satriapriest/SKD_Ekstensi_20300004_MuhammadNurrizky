![Toplogi](https://user-images.githubusercontent.com/65015846/202858921-5a0fe7fa-11ef-4c71-aca0-539229122ccd.png)


from gpio import *
from time import *

def handleSensorData () :
	value = digitalRead (0)
	if value == 0:
		customWrite (1, '0')
		print ("Garasi Terbuka")
		customWrite (2, '0')
		print ("Lampu Menyala")
	else :
		customWrite (1, '1')
		customWrite (2, '1')
		
def main () :
	add_event_detect(0, handleSensorData)
	
	while True :
		delay (1000)
		
if __name__ == "__main__":
	main()
	
