import reflex as rx
import duck_hack.styles.styles as styles
from duck_hack.styles.colors import Color
from duck_hack.components.form_contact import form_contact

def contact() -> rx.Component:
    return rx.flex(
            rx.vstack(
                rx.center(
                    rx.center(
                        rx.box(
                            rx.text(
                                "Mandanos un mensaje",
                                style=styles.text_body2_bold
                            ),
                            form_contact(),
                            background_color=Color.BACKGROUND.value,
                            margin_right=styles.Size.BIG.value,
                            padding=styles.Size.BIG.value,
                            width="50%"
                        ),
                        rx.box(
                            rx.text(
                                "Contactanos",
                                style=styles.text_body2_bold
                            ),
                            background_color=Color.BACKGROUND.value,
                            padding=styles.Size.BIG.value,
                            width="30%"
                        ),
                        width="80%"
                    ),
                    width="100%"
                ),
                width="100%",
                background_color=Color.TRANSPARENT.value,
                padding_top=styles.Size.VERY_BIG.value,
                padding_bottom=styles.Size.VERY_BIG.value 
            ),
            width="100%",
            margin_top="-20px",
            background="center/cover url('/background_map.png')"    
        )