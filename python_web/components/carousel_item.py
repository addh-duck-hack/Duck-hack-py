import reflex as rx
import python_web.styles.styles as styles
from python_web.styles.colors import Color

def carousel_item(image:str, comment:str, name:str, position:str) -> rx.Component:
    return rx.flex(
            rx.center(
                rx.image(
                    src=f"{image}",
                    width=styles.Size.SUPER_BIG.value,
                    height= styles.Size.SUPER_BIG.value,
                    border_radius= "50%"
                ),
                width= "100%",
                position="relative",
                z_index="2"
            ),
            rx.center(
                rx.vstack(
                    rx.text(
                        f"{comment}",
                        style=styles.text_comment,
                        width="100%",
                        text_align="center"
                    ),
                    rx.text(
                        f"{name}",
                        style=styles.text_title3,
                        width="100%",
                        text_align="center"
                    ),
                    rx.text(
                        f"{position}",
                        style=styles.text_body2_bold,
                        width="100%",
                        text_align="center",
                        margin_top="-18px"
                    ),
                    background_color=Color.PRIMARY.value,
                    padding_top=styles.Size.VERY_BIG.value,
                    padding_bottom=styles.Size.LARGE.value,
                    padding_x=styles.Size.VERY_BIG.value,
                    border_radius= "400px",
                    width=["80%","80%","70%","60%","60%"]
                ),
                width= "100%",
                position="relative",
                margin_top=f"-{styles.Size.MEDIUM_BIG.value}"
            ),
            flex_wrap="wrap",
            margin_top= styles.Size.DEFAULT.value,
            width= "100%"
    )