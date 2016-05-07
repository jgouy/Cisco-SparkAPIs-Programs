import serial # Import Serial Library
from visual import * # import all the vPython library

arduinoserialData = serial.Serial('com10', 9600)
tempLabel = label(text = 'Temperature is: ', pos = (0, 0, 0), color=color.green ,depth=-0.3,height = 30, box=true)

while (1==1): # loop forever
    rate(20)
    if (arduinoserialData.inWaiting()>0): #check to see if there is data 
        myData = arduinoserialData.readline() #if data is there, read it
        findTemp = myData [0:12]
        if findTemp == 'Temperatura:':
            Temp = myData [13:18]
            Humi = myData [29:35]
            EnvTemp = float(Temp)
            if EnvTemp < 28.00:
                tempLabel.color = color.green
            elif (EnvTemp >= 28.00) and (EnvTemp < 32.00):
                tempLabel.color = color.orange
            else:
                tempLabel.color = color.red
            TemperatureLabel = 'Temperature is: ' + Temp + ' C' + ' & Humidity is: ' + Humi + ' %'
            tempLabel.text = TemperatureLabel

            
        
