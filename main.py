def on_pin_pressed_p0():
    global button_on
    if button_on == True:
        pins.digital_write_pin(DigitalPin.P1, 0)
        button_on = False
    else:
        pins.digital_write_pin(DigitalPin.P1, 1)
        if True:
            pins.digital_write_pin(DigitalPin.P1, 1)
            button_on = True
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    global button_on
    if button_on == True:
        pins.digital_write_pin(DigitalPin.P1, 0)
        button_on = False
    else:
        pins.digital_write_pin(DigitalPin.P1, 1)
        if True:
            pins.digital_write_pin(DigitalPin.P1, 1)
            button_on = True
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pins.digital_write_pin(DigitalPin.P1, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

button_on = False
pins.digital_write_pin(DigitalPin.P1, 1)
basic.pause(5000)
pins.digital_write_pin(DigitalPin.P1, 0)

def on_forever():
    pass
basic.forever(on_forever)
