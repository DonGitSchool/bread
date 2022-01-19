input.onPinPressed(TouchPin.P0, function () {
    if (button_on == true) {
        pins.digitalWritePin(DigitalPin.P1, 0)
        button_on = false
    } else {
        pins.digitalWritePin(DigitalPin.P1, 1)
        if (true) {
            pins.digitalWritePin(DigitalPin.P1, 1)
            button_on = true
        }
    }
})
input.onButtonPressed(Button.A, function () {
    if (button_on == true) {
        pins.digitalWritePin(DigitalPin.P1, 0)
        button_on = false
    } else {
        pins.digitalWritePin(DigitalPin.P1, 1)
        if (true) {
            pins.digitalWritePin(DigitalPin.P1, 1)
            button_on = true
        }
    }
})
input.onButtonPressed(Button.B, function () {
    pins.digitalWritePin(DigitalPin.P1, 0)
})
let button_on = false
pins.digitalWritePin(DigitalPin.P1, 1)
basic.pause(5000)
pins.digitalWritePin(DigitalPin.P1, 0)
basic.forever(function () {
	
})
