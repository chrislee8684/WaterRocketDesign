import machine
led = machine.Pin("LED", machine.Pin.OUT)
timer = machine.Timer()

def blink(timer):
    led.toggle()
    
timer.init(freq=2.5, mode=machine.Timer.PERIODIC, callback=blink)