import reflex as rx
import python_web.styles.styles as styles
from python_web.styles.colors import Color

def team() -> rx.Component:
    return rx.flex(
            rx.text("Equipo"),
            padding_y=[styles.Size.DEFAULT.value,styles.Size.DEFAULT.value,styles.Size.DEFAULT.value,styles.Size.VERY_BIG.value,styles.Size.VERY_BIG.value],
            background_color=Color.PRIMARY.value,
            flex_wrap="wrap",
            width="100%",
            margin_top=[styles.Size.SMALL.value,styles.Size.SMALL.value,styles.Size.DEFAULT.value,styles.Size.VERY_BIG.value,styles.Size.VERY_BIG.value]
    )