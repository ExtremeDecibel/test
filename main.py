makerbit.connect_serial_mp3(DigitalPin.P0, DigitalPin.P2)
makerbit.play_mp3_track(1, 1)

def on_forever():
    pass
basic.forever(on_forever)
