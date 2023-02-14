item = 0
led.enable(True)

def on_forever():
    pass
basic.forever(on_forever)

def on_forever2():
    global item
    item = sonar.ping(DigitalPin.P2, DigitalPin.P1, PingUnit.CENTIMETERS)
    basic.show_number(item)
    basic.pause(50)
    serial.write_value("distance(cm)", item)
basic.forever(on_forever2)
