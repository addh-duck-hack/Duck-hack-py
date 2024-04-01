import reflex as rx
import duck_hack.styles.styles as styles
from duck_hack.styles.colors import Color

def service(icon: str, title: str, body: str) -> rx.Component:
    return rx.vstack( 
        rx.center(
            rx.box(
                rx.icon(
                    icon,
                    size=40,
                    color=Color.LIGHT_TEXT.value
                ),
                padding=styles.Size.MEDIUM.value,
                background_color=Color.BACKGROUND.value,
                border_radius="50%",
                margin_right=styles.Size.DEFAULT.value
            ),
            rx.text.strong(
                title,
                style=styles.text_title3
            ),
            width="100%"
        ),
        rx.center(
            rx.text(
                body,
                text_align="center",
                style=styles.text_body2,
                padding_x=styles.Size.VERY_BIG.value,
                margin_bottom=styles.Size.VERY_BIG.value
            ),
            width="100%"
        ),
        width=["100%","100%","30%","30%","30%"]
    )