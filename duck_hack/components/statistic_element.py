import reflex as rx
import duck_hack.styles.styles as styles
from duck_hack.styles.colors import Color

def statistics_element(icon: str, number: str, body: str) -> rx.Component:
    return rx.flex( 
        rx.center(
            rx.box(
                rx.icon(
                    icon,
                    stroke_width=1.5,
                    size=80,
                    margin_y=styles.Size.LARGE.value                
                ),
                width="30%",
                float="right"
            ),
            rx.box(
                background_color=Color.LIGHT_TEXT.value,
                width="2px",
                height="100%",
                margin_x=styles.Size.DEFAULT.value
            ),
            rx.vstack(
                rx.text(
                    number,
                    style=styles.text_title1
                ),
                rx.text(
                    body,
                    style=styles.text_body2
                ),
                width="50%"
            ),
            color= Color.LIGHT_TEXT.value,
            width="100%"
        ),
        width=["100%","100%","25%","25%","25%"]
    )