import reflex as rx
import python_web.styles.styles as styles
from python_web.styles.colors import Color

def section2() -> rx.Component:
    return rx.flex(
            rx.flex(
                rx.image(
                    src="pato1.jpeg",
                    border_top_left_radius= "50%",
                    border_top_right_radius= "50%",
                ),
                margin_top=[styles.Size.BIG.value,styles.Size.BIG.value,styles.Size.BIG.value,styles.Size.DEFAULT.value,styles.Size.DEFAULT.value],
                padding_x=[styles.Size.DEFAULT.value,styles.Size.DEFAULT.value,styles.Size.DEFAULT.value,styles.Size.VERY_BIG.value,styles.Size.VERY_BIG.value],
                width=["100%","100%","100%","50%","50%"]
            ),
            rx.flex(
                rx.vstack(
                    rx.text(
                        "En ",
                        rx.text.strong("Duck Hack", color=Color.BACKGROUND.value),
                        ", combinamos la experiencia y el conocimiento",
                        style=styles.text_title1
                    ),
                    rx.text(
                        "Nuestros colaboradores, quienes cuentan con más de 5 años de experiencia en el campo de la tecnología, te ofrecerán las mejores soluciones digitales a medida.",
                        style=styles.text_body
                    ),
                    rx.text(
                        "Nuestra pasión por la tecnología y el diseño nos impulsa a superar tus expectativas. Conoce al equipo que hará realidad tus proyectos.",
                        style=styles.text_body
                    ),
                    margin="auto"
                ),
                margin_top=[styles.Size.BIG.value,styles.Size.BIG.value,styles.Size.BIG.value,styles.Size.DEFAULT.value,styles.Size.DEFAULT.value],
                padding_x=[styles.Size.DEFAULT.value,styles.Size.DEFAULT.value,styles.Size.DEFAULT.value,styles.Size.VERY_BIG.value,styles.Size.VERY_BIG.value],
                width=["100%","100%","100%","50%","50%"]
            ),
            padding_y=[styles.Size.DEFAULT.value,styles.Size.DEFAULT.value,styles.Size.DEFAULT.value,styles.Size.VERY_BIG.value,styles.Size.VERY_BIG.value],
            background_color=Color.PRIMARY.value,
            flex_wrap="wrap",
            width="100%",
            margin_top=[styles.Size.SMALL.value,styles.Size.SMALL.value,styles.Size.DEFAULT.value,styles.Size.VERY_BIG.value,styles.Size.VERY_BIG.value]
    )