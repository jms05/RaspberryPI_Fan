
import RPi.GPIO as GPIO
import time
import os
import sys
import signal

def signal_handler(signal,frame):
        GPIO.cleanup()
        sys.exit(0)

signal.signal(signal.SIGINT,signal_handler)

pinNOK=18
pinOK=23
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinNOK, GPIO.OUT) #Onde está ligada a ventoinha
GPIO.setup(pinOK, GPIO.OUT)
state = True

# Return CPU temperature as a character string
def getCPUtemperature():
        res = os.popen('vcgencmd measure_temp').readline()
        return(res.replace("TEMP=","").replace("'C\n",""))



def fan(limit,vari,sleepOK,sleepNOK,pinOK,pinNOK):
        off = True
        GPIO.output(pinNOK,False)
        GPIO.output(pinOK,True)
        lim=limit
        var=vari
        sup=lim
        inf=lim-var
        while (True):
                tmp = float(getCPUtemperature().split("=")[1])
                if (tmp<lim):
                        if(lim==inf):
                                lim=sup
                        print "OK " + str(tmp) + " lim: " + str(lim)
                        if(not(off)):
                                off=True
                                GPIO.output(pinNOK,False)
                                GPIO.output(pinOK,True)
                        time.sleep(sleepOK)
                else:
                        lim=inf
                        print "NOT OK " + str(tmp) + " lim: " + str(lim)
                        if(off):
                                off=False
                                GPIO.output(pinNOK,True)
                                GPIO.output(pinOK,False)
                        time.sleep(sleepNOK)

fan(44,7,1,10,pinOK,pinNOK)
