import reflex as rx
import duck_hack.styles.styles as styles
from duck_hack.styles.colors import Color

def social_media_item(icon: str, url: str) -> rx.Component:
    if(url == ""):
        return ""
    return rx.box(
                rx.link(
                    rx.icon(
                        icon,
                        size=20,
                        color=Color.LIGHT_TEXT.value
                    ),
                    href=url,
                    target="_blank"
                ),
                border_radius="50%",
                padding=styles.Size.SMALL.value,
                background_color=Color.BACKGROUND.value,
                cursor= "pointer",
                _hover={
                    "background_color": f"{Color.BLUE_TEXT.value}"
                }
            )