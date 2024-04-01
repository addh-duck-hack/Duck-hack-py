import reflex as rx
import duck_hack.styles.styles as styles
from duck_hack.styles.colors import Color
from duck_hack.components.statistic_element import statistics_element

def statistics() -> rx.Component:
    return rx.flex(
            rx.center(
                statistics_element("bell-electric", "50K", "Horas trabajadas"),
                statistics_element("smile", "8+", "Clientes satisfechos"),
                statistics_element("bug", "1,300+", "Bugs solucionados"),
                width="100%",
                flex_wrap="wrap"
            ),
            padding_y=styles.Size.VERY_BIG.value,
            width="100%"
    )