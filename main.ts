let item = 0
led.enable(true)
basic.forever(function on_forever() {
    
})
basic.forever(function on_forever2() {
    
    item = sonar.ping(DigitalPin.P2, DigitalPin.P1, PingUnit.Centimeters)
    basic.showNumber(item)
    basic.pause(50)
    serial.writeValue("distance(cm)", item)
})
