import reflex as rx
import python_web.styles.styles as styles
from python_web.styles.colors import Color
from python_web.components.dropdown_services import dropdown_services
from python_web.components.dropdown_menu import dropdown_menu

def menu_navbar() -> rx.Component:
    return rx.box(
            rx.tablet_and_desktop(
                rx.flex(
                    rx.link(
                    "Nosotros",
                    style= styles.text_link
                    ),
                    rx.spacer(),
                    dropdown_services(),
                    rx.spacer(),
                    rx.link(
                        "Clientes",
                        style= styles.text_link
                    ),
                    rx.spacer(),
                    rx.link(
                        "Equipo",
                        style= styles.text_link
                    ),
                    rx.spacer(),
                    rx.link(
                        "Contacto",
                        style= styles.text_link
                    ),
                    width="100%"
                )
            ),
            rx.mobile_only(
                rx.center(
                    dropdown_menu()
                )
            ),
            width=["29%","29%","59%","69%","69%"]
    )