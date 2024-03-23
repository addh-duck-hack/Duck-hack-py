import reflex as rx
import python_web.styles.styles as styles
from python_web.styles.colors import Color
from python_web.components.statistic_element import statistics_element

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