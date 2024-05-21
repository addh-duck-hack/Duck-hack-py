import reflex as rx
import duck_hack.styles.styles as styles
from duck_hack.styles.colors import Color

def form_contact() -> rx.Component:
    return rx.form.root(
            rx.form.field(
                rx.flex(
                    rx.form.label("Email"),
                    rx.form.control(
                        rx.input(
                            placeholder="Email Address",
                            # type attribute is required for "typeMismatch" validation
                            type="email",
                        ),
                        as_child=True,
                    ),
                    rx.form.message(
                        "Please enter a valid email",
                        match="typeMismatch",
                    ),
                    rx.form.submit(
                        rx.button("Submit"),
                        as_child=True,
                    ),
                    direction="column",
                    spacing="2",
                    align="stretch",
                ),
                name="email",
            ),
            on_submit=lambda form_data: rx.window_alert(
                form_data.to_string()
            ),
            reset_on_submit=True,
        )