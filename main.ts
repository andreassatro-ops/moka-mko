let start = 0
let score = 0
let elapsed = 0
input.onButtonPressed(Button.A, function () {
    start = 7 - 1
})
input.onButtonPressed(Button.B, function () {
    start = 6 - 1
    score += 1
    elapsed = 9
    basic.showLeds(`
        # . . . #
        . # # # .
        . . . . .
        . # # # .
        # . . . #
        `)
    basic.showLeds(`
        # # # # #
        # # . # #
        # . # . #
        # # . # #
        # # # # #
        `)
})
