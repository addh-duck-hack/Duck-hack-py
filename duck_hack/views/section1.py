import reflex as rx
import duck_hack.styles.styles as styles
from duck_hack.styles.colors import Color

def section1() -> rx.Component:
    return rx.flex(
            rx.flex(
                rx.vstack(
                    rx.text(
                        "BIENVENIDO A ",
                        rx.text.strong("DUCK HACK"),
                        style=styles.text_title2
                    ),
                    rx.text(
                        "Donde la innovación y la creatividad se unen para dar vida a tus ideas digitales.",
                        style=styles.text_title1
                    ),
                    rx.button(
                        rx.icon("mail", stroke_width=3),
                        "CONTACTANOS",
                        style=styles.button_principal
                    )
                ),
                width=["100%","100%","50%","50%","50%"],
                padding_x=[styles.Size.SMALL.value,styles.Size.SMALL.value,styles.Size.DEFAULT.value,styles.Size.VERY_BIG.value,styles.Size.VERY_BIG.value],
                margin_bottom=[styles.Size.BIG.value,styles.Size.BIG.value,styles.Size.BIG.value,styles.Size.ZERO.value,styles.Size.ZERO.value]
            ),
            rx.flex(
                rx.center(
                    rx.flex(
                        rx.image(
                            src="pato1.jpeg",
                            width=styles.SizeImg.DEFAULT.value,
                            border_radius=styles.Size.DEFAULT.value
                        )
                    ),
                    rx.flex(
                        rx.image(
                            src="pato2.jpeg",
                            width=styles.SizeImg.MEDIUM.value,
                            border_radius=styles.Size.DEFAULT.value
                        ),
                        align_self="end"
                    ),
                    spacing="5",
                    width="100%"
                ),
                rx.center(
                    rx.flex(
                        rx.image(
                            src="pato3.jpeg",
                            width=styles.SizeImg.BIG.value,
                            border_radius=styles.Size.DEFAULT.value
                        )
                    ),
                    rx.flex(
                        rx.image(
                            src="pato4.jpeg",
                            width=styles.SizeImg.LARGE.value,
                            border_radius=styles.Size.DEFAULT.value
                        ),
                        align_self="start"
                    ),
                    spacing="5",
                    width="100%"
                ),
                spacing="5",
                flex_wrap="wrap",
                width=["100%","100%","100%","50%","50%"]
            ),
            flex_wrap="wrap",
            width="100%",
            margin_top=[styles.Size.SMALL.value,styles.Size.SMALL.value,styles.Size.DEFAULT.value,styles.Size.VERY_BIG.value,styles.Size.VERY_BIG.value]
    )