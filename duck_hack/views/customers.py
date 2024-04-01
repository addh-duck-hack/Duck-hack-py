import reflex as rx
import duck_hack.styles.styles as styles
from duck_hack.styles.colors import Color
from duck_hack.components.carousel_item import carousel_item
import duck_hack.texts.texts_es as texts

class CarouselState(rx.State):
    index: int = 0
    totalItems: int = len(texts.IMAGE)
    background: list[str] = [f"{Color.LIGHT_TEXT.value}","transparent","transparent"]
    #Variables con textos
    IMAGE = texts.IMAGE
    COMMENT = texts.COMMENT
    NAME = texts.NAME
    POSITION = texts.POSITION

    def movToIndex(self, position: int):
        self.background = ["transparent","transparent","transparent"]
        self.background[position] = f"{Color.LIGHT_TEXT.value}"
        self.index = position


def customers() -> rx.Component:
    return rx.vstack(
            rx.center(
                rx.icon(
                    "quote",
                    size=80,
                    stroke_width=1,
                    color= styles.Color.LIGHT_TEXT.value
                ),
                width="100%"
            ),
            carousel_item(CarouselState.IMAGE[CarouselState.index],CarouselState.COMMENT[CarouselState.index],CarouselState.NAME[CarouselState.index],CarouselState.POSITION[CarouselState.index]),
            rx.center(
                rx.flex(
                    rx.box(
                        style=styles.button_dot_box,
                        background_color= CarouselState.background[0],
                        on_click= CarouselState.movToIndex(0),
                    ),
                    rx.box(
                        style=styles.button_dot_box,
                        background_color= CarouselState.background[1],
                        on_click= CarouselState.movToIndex(1)
                    ),
                    rx.box(
                        style=styles.button_dot_box,
                        background_color= CarouselState.background[2],
                        on_click= CarouselState.movToIndex(2)
                    ),                
                    spacing="2",
                    flex_wrap="wrap"
                ),
                width="100%"
            ),
            margin_top=styles.Size.VERY_BIG.value,
            width="100%"
    )