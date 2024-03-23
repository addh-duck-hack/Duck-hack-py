import reflex as rx
import python_web.styles.styles as styles
from python_web.styles.colors import Color

def dropdown_menu() -> rx.Component:
    return rx.menu.root(
        rx.menu.trigger(
            rx.flex(
                rx.icon(
                    "menu",
                    color=Color.SECONDARY.value,
                ),
                cursor= "pointer"
            )
        ),
        rx.menu.content(
            rx.menu.item("Nosotros"),
            rx.menu.sub(
                rx.menu.sub_trigger("Servicios"),
                rx.menu.sub_content(
                    rx.menu.item("Paginas web"),
                    rx.menu.item("Aplicaciones nativas"),
                    rx.menu.item("Servicios en la nube")
                )
            ),
            rx.menu.item("Clientes"),
            rx.menu.item("Equipo"),
            rx.menu.item("Contacto")
        )
    )