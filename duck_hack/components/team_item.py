import reflex as rx
import duck_hack.styles.styles as styles
from duck_hack.styles.colors import Color
from duck_hack.components.social_media_item import social_media_item

def team_item(image: str, name: str, job: str, description: str, linkedin: str, facebook: str, instagram: str, twitter: str) -> rx.Component:
    return rx.hstack(
                rx.image(
                    src=image,
                    width="50%"
                ),
                rx.vstack(
                    rx.text(
                        name,
                        style=styles.text_title3,
                        line_height= "1"
                    ),
                    rx.text(
                        job,
                        style=styles.text_body2_bold
                    ),
                    rx.text(
                        description,
                        style=styles.text_body2,
                        margin_top=styles.Size.MEDIUM.value
                    ),
                    rx.hstack(
                        social_media_item("linkedin",linkedin),
                        social_media_item("facebook",facebook),
                        social_media_item("instagram",instagram),
                        social_media_item("twitter",twitter)
                    ),
                    width="50%"
                ),
                width=["100%","100%","100%","50%","50%"],
                align="center",
                padding_x=styles.Size.DEFAULT.value,
                margin_bottom=styles.Size.VERY_BIG.value
            )