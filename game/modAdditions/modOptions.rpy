init python:
    gr = "{color=#0f0}"
    red = "{color=#f00}"
    blue = "{color=#00f}"
    purp = "{color=#800080}"

define mod = Character("OscarSix", color="#0f0")

screen modOptions():
    modal True

    add "#23272a"

    vbox:
        xcenter 0.5
        ypos 33
        spacing 33

        text "Mod Options" style "modTextHeader"

        textbutton "Change In-Game Names" action ui.callsinnewcontext("changeIngameNames") text_style "modTextButtonHeader"

    textbutton _("Return") action Hide("modOptions"):
        text_style "modTextButtonHeader"
        yanchor 1.0
        align (0.1, 0.9)

label changeIngameNames:
    mod "Make sure to do this in the save you wish to change names for."
    $ MC = renpy.input("What is your name?", default="Alex").strip() or "Alex"
    scene wake up 5 with dissolve
    $ Nova = renpy.input("What is her name?", default="Nova").strip() or "Nova"
    mod "Names successful changed"
    return
