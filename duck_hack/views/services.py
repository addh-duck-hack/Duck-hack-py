import reflex as rx
import duck_hack.styles.styles as styles
from duck_hack.styles.colors import Color
from duck_hack.components.service import service

def services() -> rx.Component:
    return rx.vstack(
            rx.center(
                rx.text(
                    "SERVICIOS",
                    style={
                        "-webkit-text-stroke": f"2px {Color.BACKGROUND.value}"
                    },
                    color=Color.PRIMARY.value,
                    font_weight=styles.FontWeight.BOLD.value,
                    font_size=styles.SizeImg.SMALL.value
                ),
                rx.desktop_only(
                    rx.text(
                        "NUESTROS SERVICIOS",
                        style=styles.text_title1,
                    ),
                    position="absolute"
                ),
                position="relative",
                width="100%"
            ),
            rx.center(
                service("paintbrush", "Diseño web","Diseños personalizados y funcionales que representan la esencia de tu marca."),
                service("boxes", "Desarrollo  web","Soluciones web escalables y eficientes que impulsan tu negocio en línea."),
                service("tablet-smartphone", "Aplicaciones nativas","Experiencias móviles fluidas y adaptadas a tus necesidades específicas."),
                service("satellite", "Hosting","Seguro, confiable y flexible. Ponemos tu negocio en línea sin complicaciones."),
                service("scan-eye", "Imagen corporativa","Identidad visual que cautiva y comunica la esencia de tu marca."),
                flex_wrap="wrap",
                width="100%"
            ),
            background_color=Color.PRIMARY.value,
            padding_y=styles.Size.MEDIUM.value,
            width="100%"
    )