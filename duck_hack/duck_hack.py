import reflex as rx
import duck_hack.styles.styles as styles
from duck_hack.views.navbar import navbar
from duck_hack.views.section1 import section1
from duck_hack.views.section2 import section2
from duck_hack.views.statistics import statistics
from duck_hack.views.services import services
from duck_hack.views.customers import customers
from duck_hack.views.team import team
from duck_hack.views.contact import contact

class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        section1(),
        section2(),
        statistics(),
        services(),
        customers(),
        contact(),
        width="100%"
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
    )
app.add_page(
    index,
    title="Hosting a tu medida"
    )
