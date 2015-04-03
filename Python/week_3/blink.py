import mosquitto, serial

port = serial.Serial("/dev/cu.usbmodem1421",9600,timeout=2) 

client = mosquitto.Mosquitto("DAT2052")
client.connect("141.163.83.22")

client.subscribe("lights")

def messageReceived(broker, obj, msg):
    global client
    print("Message " + msg.topic + " containing: " + msg.payload)
    global message
    message = msg.payload
    if msg.payload == "ON":
        port.write(str(1))
    elif msg.payload == "OFF":
        port.write(str(0))
        
client.on_message = messageReceived

while (client != None): client.loop()
    
port.close()