def on_countdown_end():
    game.over(True)
info.on_countdown_end(on_countdown_end)

def on_on_overlap(sprite, otherSprite):
    projectile.destroy()
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    projectile2.destroy()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

projectile2: Sprite = None
projectile: Sprite = None
scene.set_background_image(assets.image("""
    Freeway
"""))
mySprite = sprites.create(assets.image("""
    Mama
"""), SpriteKind.player)
controller.move_sprite(mySprite, 0, 100)
mySprite.set_stay_in_screen(True)
scroller.scroll_background_with_speed(-50, 0)
info.start_countdown(15)
animation.run_image_animation(mySprite,
    assets.animation("""
        Mama Moving
    """),
    100,
    True)

def on_forever():
    global projectile2
    projectile2 = sprites.create_projectile_from_side(assets.image("""
        Tourist
    """), -90, 0)
    projectile2.y = randint(15, 115)
    projectile2.set_kind(SpriteKind.enemy)
    animation.run_image_animation(projectile2,
        assets.animation("""
            Animated Tourist
        """),
        100,
        True)
    pause(2100)
forever(on_forever)

def on_forever2():
    global projectile
    projectile = sprites.create_projectile_from_side(assets.image("""
        Baby
    """), -90, 0)
    projectile.y = randint(15, 100)
    animation.run_image_animation(projectile,
        assets.animation("""
            Animated Baby
        """),
        100,
        True)
    pause(1000)
forever(on_forever2)
