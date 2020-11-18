
screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.55

        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("Start") action Start() xpos int(1.1*99)

            textbutton _("Load") action ShowMenu("load") xpos int(1.4*99) ypos 0.4

            textbutton _("Options") action ShowMenu("preferences") xpos int(1.6*99) ypos 0.8

            textbutton _("About") action ShowMenu("about") xpos int(1.9*99) ypos 1.2

            textbutton _("Gallery") action ShowMenu("gallery") xpos int(1.9*95) ypos 1.6

            if renpy.variant("pc"):
                textbutton _("Help") action ShowMenu("help") xpos int(1.6*95) ypos 2.0

                textbutton _("Quit") action Quit(confirm=not main_menu) xpos int(1.4*95) ypos 2.4

                textbutton _("Patreon") action OpenURL("http://www.patreon.com/musex") xpos int(1.1*95) ypos 2.8

        else:
            textbutton _("Mod Options") action Show("modOptions")

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

            textbutton _("Load") action ShowMenu("load")


        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

screen save():
    tag menu

    use file_slots(_("Save"))
    vbox:
        align(0.28, 0.185)
        text "{color=#fff}Save Name:{/color}"
        input:
            yalign 0.05
            value VariableInputValue("save_name")
