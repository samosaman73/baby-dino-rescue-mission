info.onCountdownEnd(function () {
    game.over(true)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite2, otherSprite2) {
    projectile2.destroy()
    info.changeLifeBy(-1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function (sprite, otherSprite) {
    projectile.destroy()
    info.changeScoreBy(1)
})
let projectile: Sprite = null
let projectile2: Sprite = null
scene.setBackgroundImage(assets.image`Freeway`)
let mySprite = sprites.create(assets.image`Mama`, SpriteKind.Player)
controller.moveSprite(mySprite, 0, 100)
mySprite.setStayInScreen(true)
scroller.scrollBackgroundWithSpeed(-50, 0)
info.startCountdown(60)
animation.runImageAnimation(
mySprite,
assets.animation`Mama Moving`,
100,
true
)
forever(function () {
    projectile = sprites.createProjectileFromSide(assets.image`Baby`, -90, 0)
    projectile.y = randint(15, 100)
    animation.runImageAnimation(
    projectile,
    assets.animation`Animated Baby`,
    100,
    true
    )
    pause(1000)
})
forever(function () {
    projectile2 = sprites.createProjectileFromSide(assets.image`Tourist`, -90, 0)
    projectile2.y = randint(15, 115)
    projectile2.setKind(SpriteKind.Enemy)
    animation.runImageAnimation(
    projectile2,
    assets.animation`Animated Tourist`,
    100,
    true
    )
    pause(2100)
})
