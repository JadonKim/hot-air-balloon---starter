@namespace
class SpriteKind:
    Background = SpriteKind.create()
    Mountain = SpriteKind.create()
def createAnimationArrays():
    global flyingSaucer, birdGoingLeft, birdGoingRight
    flyingSaucer = [img("""
            .........fff.........
                    .......ff888ff.......
                    ......f8888998f......
                    .....f888888998f.....
                    ....f888a8a88998f....
                    ...ff88888888898ff...
                    ..fdddddddddddddddf..
                    .fbbbbbbbbbbbbbbbbbf.
                    fa9b9bb9bb9bb9bb9b9af
                    .facccccccccccccccaf.
                    ..faacccccccccccaaf..
                    ...ffaacccccccaaff...
                    .....fffffffffff.....
                    .....f999999999f.....
                    ......fffffffff......
        """),
        img("""
            .........fff.........
                    .......ff888ff.......
                    ......f8888998f......
                    .....f888888998f.....
                    ....f888a8a88998f....
                    ...ff88888888898ff...
                    ..fdddddddddddddddf..
                    .fbbbbbbbbbbbbbbbbbf.
                    fab4b44b44b44b44b4baf
                    .facccccccccccccccaf.
                    ..faacccccccccccaaf..
                    ...ffaacccccccaaff...
                    .....fffffffffff.....
                    .....f999999999f.....
                    ......fffffffff......
        """)]
    birdGoingLeft = [img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . f f f f . . . . . . . . . 
                    . . f 8 8 8 8 f f f f . f f f . 
                    . f 8 f 8 8 8 8 8 8 8 f 8 8 8 f 
                    f 4 5 8 8 8 8 8 8 8 8 8 f f 8 f 
                    f 5 5 5 8 8 f 8 8 8 8 8 8 8 f . 
                    . f f f 8 8 8 f 8 8 8 8 8 8 f . 
                    . . . . f f f f f 8 8 8 f f . . 
                    . . . . . . . . f f f f . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . . 
                    . . . f f f f . . . . . . . . . . 
                    . . f 8 8 8 8 f f f f . f f f . . 
                    . f 8 f 8 8 8 8 8 f 8 f 8 8 8 f . 
                    f 4 5 8 8 8 8 8 8 8 f 8 8 8 8 f . 
                    f 5 5 5 8 8 f 8 8 8 8 f 8 8 f . . 
                    . f f f 8 8 8 f 8 8 8 8 f 8 f . . 
                    . . . . f f a f f 8 8 8 8 f f . . 
                    . . . . . . . . f 8 8 8 f . . . . 
                    . . . . . . . . . f 8 8 f . . . . 
                    . . . . . . . . . . f f . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . f f f f . . . . . . . . . 
                    . . f 8 8 8 8 f f f f . f f f . 
                    . f 8 f 8 8 8 8 8 8 8 f 8 8 8 f 
                    f 4 5 8 8 8 8 8 8 8 8 8 f f 8 f 
                    f 5 5 5 8 8 f 8 8 8 8 8 8 8 f . 
                    . f f f 8 8 8 f 8 8 8 8 8 8 f . 
                    . . . . f f f f f 8 8 8 f f . . 
                    . . . . . . . . f f f f . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        img("""
            . . . . . . . . . . . f f . . . 
                    . . . . . . . . . . f 8 8 f . . 
                    . . . f f f f . f f 8 8 8 f . . 
                    . . f 8 8 8 8 f f 8 8 8 f f f . 
                    . f 8 f 8 8 8 8 8 8 8 f 8 8 8 f 
                    f 4 5 8 8 8 8 8 8 8 f 8 f f 8 f 
                    f 5 5 5 8 8 8 8 8 f 8 8 8 8 f . 
                    . f f f 8 8 8 8 8 8 8 8 8 8 f . 
                    . . . . f f f f f 8 8 8 f f . . 
                    . . . . . . . . f f f f . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """)]
    birdGoingRight = [img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . f f f f . . . 
                    . f f f . f f f f 8 8 8 8 f . . 
                    f 8 8 8 f 8 8 8 8 8 8 8 f 8 f . 
                    f 8 f f 8 8 8 8 8 8 8 8 8 5 4 f 
                    . f 8 8 8 8 8 8 8 f 8 8 5 5 5 f 
                    . f 8 8 8 8 8 8 f 8 8 8 f f f . 
                    . . f f 8 8 8 f f f f f . . . . 
                    . . . . f f f f . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . f f f f . . . 
                    . f f f . f f f f 8 8 8 8 f . . 
                    f 8 8 8 f 8 f 8 8 8 8 8 f 8 f . 
                    f 8 8 8 8 f 8 8 8 8 8 8 8 5 4 f 
                    . f 8 8 f 8 8 8 8 f 8 8 5 5 5 f 
                    . f 8 f 8 8 8 8 f 8 8 8 f f f . 
                    . . f f 8 8 8 8 f f f f . . . . 
                    . . . f 8 8 8 f . . . . . . . . 
                    . . . f 8 8 f . . . . . . . . . 
                    . . . . f f . . . . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . f f f f . . . 
                    . f f f . f f f f 8 8 8 8 f . . 
                    f 8 8 8 f 8 8 8 8 8 8 8 f 8 f . 
                    f 8 f f 8 8 8 8 8 8 8 8 8 5 4 f 
                    . f 8 8 8 8 8 8 8 f 8 8 5 5 5 f 
                    . f 8 8 8 8 8 8 f 8 8 8 f f f . 
                    . . f f 8 8 8 f f f f f . . . . 
                    . . . . f f f f . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        img("""
            . . . f f . . . . . . . . . . . 
                    . . f 8 8 f . . . . . . . . . . 
                    . . f 8 8 8 f f . f f f f . . . 
                    . f f f 8 8 8 f f 8 8 8 8 f . . 
                    f 8 8 8 f 8 8 8 8 8 8 8 f 8 f . 
                    f 8 f f 8 f 8 8 8 8 8 8 8 5 4 f 
                    . f 8 8 8 8 f 8 8 8 8 8 5 5 5 f 
                    . f 8 8 8 8 8 8 8 8 8 8 f f f . 
                    . . f f 8 8 8 f f f f f . . . . 
                    . . . . f f f f . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """)]
birdGoingRight: List[Image] = []
birdGoingLeft: List[Image] = []
flyingSaucer: List[Image] = []
balloonDeflated = img("""
    ...................
        ...................
        .......fffff.......
        .....ff22222ff.....
        ....f222222442f....
        ...f22222222442f...
        ..f2222222222442f..
        .f222322223222422f.
        .f222322223222222f.
        .f222322223222222f.
        .f222232222322222f.
        .f222222222222222f.
        ..f2222322232222f..
        ..f2222233322222f..
        ...ff222222222ff...
        ....ffff222ffff....
        .....f.fffff.f.....
        .....f.......f.....
        .....f.......f.....
        ......f.....f......
        ......f.....f......
        .......f...f.......
        .......f.2.f.......
        ......fffffff......
        .....fcccccccf.....
        .....fcbbbbbcf.....
        .....fcabbbacf.....
        .....fcbaaabcf.....
        .....fcbbbbbcf.....
        .....fcabbbacf.....
        .....fccaaaccf.....
        ......fcccccf......
        .......fffff.......
""")
balloonInflated = img("""
    ...................
        ......fffffff......
        ....ff2222222ff....
        ...f22222222442f...
        ..f2222222222442f..
        .f222222222222442f.
        f22232222223222422f
        f22232222223222222f
        f22232222223222222f
        f22223222222322222f
        f22222222222222222f
        f22222222222222222f
        .f222232222232222f.
        .f222223333322222f.
        ..ff22222222222ff..
        ....ffff222ffff....
        .....f.fffff.f.....
        .....f.......f.....
        .....f.......f.....
        ......f.....f......
        ......f.....f......
        .......f...f.......
        .......f.2.f.......
        ......fffffff......
        .....fcccccccf.....
        .....fcbbbbbcf.....
        .....fcabbbacf.....
        .....fcbaaabcf.....
        .....fcbbbbbcf.....
        .....fcabbbacf.....
        .....fccaaaccf.....
        ......fcccccf......
        .......fffff.......
""")
balloon = sprites.create(balloonDeflated, SpriteKind.player)
balloon.ay = 35
balloon.z = 100
balloon.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
music.set_volume(0)
info.set_score(0)
info.set_life(3)
scene.set_background_color(9)
createAnimationArrays()