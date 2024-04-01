import reflex as rx
import duck_hack.styles.styles as styles
from duck_hack.styles.colors import Color

def team() -> rx.Component:
    return rx.flex(
            rx.text("Equipo"),
            padding_y=[styles.Size.DEFAULT.value,styles.Size.DEFAULT.value,styles.Size.DEFAULT.value,styles.Size.VERY_BIG.value,styles.Size.VERY_BIG.value],
            background_color=Color.PRIMARY.value,
            flex_wrap="wrap",
            width="100%",
            margin_top=[styles.Size.SMALL.value,styles.Size.SMALL.value,styles.Size.DEFAULT.value,styles.Size.VERY_BIG.value,styles.Size.VERY_BIG.value]
    )