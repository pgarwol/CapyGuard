from components.default_components import defaults
from components.component import Component
from views.view import View
import flet as ft


settings = View(name="settings", route="/settings")
settings.add_component(defaults["STATISTICS_BAR"])
settings.add_component(
    Component([ft.Text("USTAWIENIA")], "View representing Settings.")
)
settings.add_component(defaults["NAVIGATION_BAR"])
print(settings)