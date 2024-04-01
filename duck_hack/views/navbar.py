import reflex as rx
import duck_hack.styles.styles as styles
from duck_hack.styles.colors import Color
from duck_hack.components.menu_navbar import menu_navbar

def navbar() -> rx.Component:
    return rx.center(
            rx.flex(
                rx.link(
                    rx.hstack(
                        rx.image(
                            src="Cyber.svg",
                            height= styles.Size.BIG.value,
                            margin_y="auto"
                        ),
                        rx.text(
                            "Duck-Hack",
                            style= styles.name_icon
                        ),
                        margin_y=styles.Size.DEFAULT.value,
                        margin_left=[styles.Size.BIG.value,styles.Size.BIG.value,"0","0","0"]
                    ),
                    width=["70%","70%","40%","30%","30%"]
                ),
                menu_navbar(),
                align="center",
                width= ["100%","100%","60%","60%","60%"]
            ),
            background_color= Color.PRIMARY.value,
            position= "sticky",
            z_index= "999",
            top= "0",
            width= "100%"
        )