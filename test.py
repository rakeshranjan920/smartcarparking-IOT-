import serial
from pubnub import Pubnub
ser = serial.Serial('/dev/ttyUSB0',9600)
pubnub = Pubnub(publish_key='pub-c-9cf3429e-6d23-4ad0-bb31-3d615ded76c9',subscribe_key='sub-c-6a806678-ca9b-11e7-9628-f616d8b03518')
ser.flush()
prev_a1,prev_a2,prev_a3,prev_a4,prev_a5,prev_a6,prev_a7,prev_a8 = -1,-1,-1,-1,-1,-1,-1,-1

def callback(message):
    print(message)

while True:
	val = ser.readline().split()
	if len(val) == 8:
		a1,a2,a3,a4,a5,a6,a7,a8 = val
		if int(a1) != prev_a1:
			pubnub.publish(channel='parking', message={'a1':a1}, callback=callback, error=callback)
			prev_a1 = int(a1)

		if int(a2) != prev_a2:
			pubnub.publish(channel='parking', message={'a2':a2}, callback=callback, error=callback)
			prev_a2 = int(a2)

		if int(a3) != prev_a3:
			pubnub.publish(channel='parking', message={'a3':a3}, callback=callback, error=callback)
			prev_a3 = int(a3)

		if int(a4) != prev_a4:
			pubnub.publish(channel='parking', message={'a4':a4}, callback=callback, error=callback)
			prev_a4 = int(a4)

		if int(a5) != prev_a5:
			pubnub.publish(channel='parking', message={'a5':a5}, callback=callback, error=callback)
			prev_a5 = int(a5)

		if int(a6) != prev_a6:
			pubnub.publish(channel='parking', message={'a6':a6}, callback=callback, error=callback)
			prev_a6 = int(a6)

		if int(a7) != prev_a7:
			pubnub.publish(channel='parking', message={'a7':a7}, callback=callback, error=callback)
			prev_a7 = int(a7)

		if int(a8) != prev_a8:
			pubnub.publish(channel='parking', message={'a8':a8}, callback=callback, error=callback)
			prev_a8 = int(a8)

