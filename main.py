start = 0
score = 0
elapsed = 0

def on_button_pressed_a():
    global start
    start = 7 - 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global start, score, elapsed
    start = 6 - 1
    score += 1
    elapsed = 9
    basic.show_leds("""
        # . . . #
        . # # # .
        . . . . .
        . # # # .
        # . . . #
        """)
    basic.show_leds("""
        # # # # #
        # # . # #
        # . # . #
        # # . # #
        # # # # #
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)
