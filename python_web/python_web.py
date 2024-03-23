import reflex as rx
import python_web.styles.styles as styles
from python_web.views.navbar import navbar
from python_web.views.section1 import section1
from python_web.views.section2 import section2
from python_web.views.statistics import statistics
from python_web.views.services import services
from python_web.views.customers import customers
from python_web.views.team import team

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
        team(),

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
