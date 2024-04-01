import reflex as rx
import duck_hack.styles.styles as styles
from duck_hack.styles.colors import Color

def dropdown_services() -> rx.Component:
    return rx.menu.root(
        rx.menu.trigger(
            rx.flex(
                rx.text("Servicios "),
                rx.spacer(),
                rx.icon(
                    "chevron-down",
                    size= styles.SizeIcons.SMALL.value,
                    margin= "auto"
                    ),
                style= styles.text_link,
                cursor= "pointer"
            )
        ),
        rx.menu.content(
            rx.menu.item("Paginas web"),
            rx.menu.item("Aplicaciones nativas"),
            rx.menu.item("Servicios en la nube")
        )
    )