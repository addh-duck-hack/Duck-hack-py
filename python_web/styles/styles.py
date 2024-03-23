import reflex as rx
from enum import Enum
from .colors import Color, TextColor
from .fonts import Font, FontWeight

# Fuentes personalizadas
STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Rubik:ital,wght@0,300..900;1,300..900&family=Space+Grotesk:wght@300..700&display=swap"
]

# Tamaños
class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    MEDIUM_BIG= "3.5em"
    VERY_BIG = "4em"
    SUPER_BIG = "8em"

class SizeImg(Enum):
    MINI=["2em","2em","4em","6em","6em"]
    SMALL=["4em","4em","6em","8em","10em"]
    MEDIUM=["6em","6em","8em","10em","12em"]
    DEFAULT=["8em","8em","10em","12em","14em"]
    LARGE=["10em","10em","12em","14em","16em"]
    BIG=["12em","12em","14em","16em","18em"]

class SizeIcons(Enum):
    SMALL= 15
    MEDIUM= 20
    LARGE= 25
    BIG= 30
    VERYBIG= 40

class Spacing(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "6"
    MEDIUM_BIG = "7"
    VERY_BIG = "9"

# Estilos base para toda la pagina
BASE_STYLE = {
    "font_family": Font.PRIMARY.value,
    "font_weight": FontWeight.MEDIUM.value,
    "background_color": Color.BACKGROUND.value
}

name_icon = dict(
    font_family= Font.SECONDARY.value,
    font_weight= FontWeight.BOLD.value,
    color= Color.SECONDARY.value,
    font_size= Size.BIG.value
)

text_link = dict(
    font_family= Font.PRIMARY.value,
    font_weight= FontWeight.MEDIUM.value,
    color= Color.SECONDARY.value,
    font_size= Size.DEFAULT.value
)

text_title2= dict(
    font_family= Font.PRIMARY.value,
    font_weight= FontWeight.MEDIUM.value,
    color= Color.LIGHT_TEXT.value,
    font_size= [Size.LARGE.value,Size.LARGE.value,Size.LARGE.value,Size.BIG.value,Size.BIG.value]
)

text_title1= dict(
    font_family= Font.PRIMARY.value,
    font_weight= FontWeight.BOLD.value,
    color= Color.BLUE_TEXT.value,
    font_size= [Size.BIG.value,Size.BIG.value,Size.BIG.value,Size.MEDIUM_BIG.value,Size.MEDIUM_BIG.value],
    text_transform= "uppercase",
    line_height= "1"
)

text_body= dict(
    font_family= Font.PRIMARY.value,
    font_weight= FontWeight.MEDIUM.value,
    color= Color.LIGHT_TEXT.value,
    font_size= [Size.DEFAULT.value,Size.DEFAULT.value,Size.DEFAULT.value,Size.LARGE.value,Size.LARGE.value]
)

text_body2= dict(
    font_family= Font.PRIMARY.value,
    font_weight= FontWeight.MEDIUM.value,
    color= Color.LIGHT_TEXT.value,
    font_size= [Size.MEDIUM.value,Size.MEDIUM.value,Size.MEDIUM.value,Size.DEFAULT.value,Size.DEFAULT.value]
)

text_body2_bold= dict(
    font_family= Font.PRIMARY.value,
    font_weight= FontWeight.BOLD.value,
    color= Color.LIGHT_TEXT.value,
    font_size= [Size.MEDIUM.value,Size.MEDIUM.value,Size.MEDIUM.value,Size.DEFAULT.value,Size.DEFAULT.value]
)

text_comment= dict(
    font_family= Font.PRIMARY.value,
    font_weight= FontWeight.MEDIUM.value,
    color= Color.LIGHT_TEXT.value,
    font_size= [Size.MEDIUM.value,Size.MEDIUM.value,Size.MEDIUM.value,Size.DEFAULT.value,Size.DEFAULT.value],
    font_style= "italic"
)

text_title3 = dict(
    font_family= Font.PRIMARY.value,
    font_weight= FontWeight.MEDIUM.value,
    color= Color.BLUE_TEXT.value,
    font_size= [Size.LARGE.value,Size.LARGE.value,Size.LARGE.value,Size.BIG.value,Size.BIG.value]
)

button_principal= dict(
    font_family= Font.PRIMARY.value,
    font_weight= FontWeight.MEDIUM.value,
    color= Color.LIGHT_TEXT.value,
    font_size= [Size.DEFAULT.value,Size.DEFAULT.value,Size.DEFAULT.value,Size.LARGE.value,Size.LARGE.value],
    padding_y=Size.LARGE.value,
    padding_x=Size.BIG.value,
    margin_top=Size.LARGE.value,
    border_radius=Size.SMALL.value,
    background_color=Color.BLUE_TEXT.value,
    border_width= "3px",
    border_color= Color.BLUE_TEXT.value,
    border_style= "solid",
    cursor="pointer",
    _hover={
        "color": f"{Color.BLUE_TEXT.value}",
        "background_color": "transparent"
    }
)

button_dot_box= dict(
    border_width= "2px",
    border_style="solid",
    border_color= Color.LIGHT_TEXT.value,
    border_radius="50%",
    width="15px",
    height="15px",
    cursor="pointer"
)