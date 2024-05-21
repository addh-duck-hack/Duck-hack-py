import reflex as rx
import duck_hack.styles.styles as styles
from duck_hack.styles.colors import Color
from duck_hack.components.team_item import team_item

def team() -> rx.Component:
    return rx.flex(
        rx.center(
            rx.text(
                "Equipo de profesionales",
                align="center",
                style=styles.text_title1,
                ),
                width="100%",
                margin_bottom=[styles.Size.BIG.value,styles.Size.BIG.value,styles.Size.DEFAULT.value,styles.Size.SMALL.value,styles.Size.SMALL.value]
        ),
        rx.center(
            rx.center(
                team_item("pato1.jpeg","Adrian Cabrera Jacobo","Líder técnico","Colaborador de coppel y accionista principal","https://www.linkedin.com/in/adrian-jacobo-3323171b2/","https://www.facebook.com/jacobobeat","",""),
                team_item("pato2.jpeg","Cesar Cabrera Jacobo","Programador Flutter","Actualmente trabajando en compañia como desarrollador flutter","","","https://www.facebook.com/jacobobeat","https://www.facebook.com/jacobobeat"),
                team_item("pato3.jpeg","Gerardo Jacobo Luna","Desarrollador iOS Jr","Colaborador de Banregio, desarrollando aplicaciones para iPhone","https://facebook.com/jacobeat","","","https://www.facebook.com/jacobobeat"),
                team_item("pato4.jpeg","Jose Alfonso Quezada Ibarra","Desarrollador Full Stack Sr","Desarrollador para varia empresas","https://facebook.com/jacobeat","https://www.facebook.com/jacobobeat","https://www.facebook.com/jacobobeat","https://www.facebook.com/jacobobeat"),
                flex_wrap="wrap",
                width=["100%","100%","100%","70%","70%"]
            ),
            width="100%",
            margin_top=[styles.Size.SMALL.value,styles.Size.SMALL.value,styles.Size.DEFAULT.value,styles.Size.VERY_BIG.value,styles.Size.VERY_BIG.value]
        ),
        padding_y=[styles.Size.DEFAULT.value,styles.Size.DEFAULT.value,styles.Size.DEFAULT.value,styles.Size.VERY_BIG.value,styles.Size.VERY_BIG.value],
        background_color=Color.PRIMARY.value,
        flex_wrap="wrap",
        width="100%",
        margin_top=[styles.Size.SMALL.value,styles.Size.SMALL.value,styles.Size.DEFAULT.value,styles.Size.VERY_BIG.value,styles.Size.VERY_BIG.value]
    )