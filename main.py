from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window

import random
from collections import Counter

Window.clearcolor = (0.035, 0.04, 0.055, 1)


class Card(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(
            orientation="vertical",
            padding=dp(14),
            spacing=dp(5),
            size_hint_y=None,
            height=dp(105),
            **kwargs
        )

        with self.canvas.before:
            Color(0.075, 0.09, 0.12, 1)
            self.background = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(14)]
            )

        self.bind(pos=self.update_bg, size=self.update_bg)

    def update_bg(self, *_):
        self.background.pos = self.pos
        self.background.size = self.size


class Dashboard(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(
            orientation="vertical",
            padding=dp(12),
            spacing=dp(10),
            **kwargs
        )

        self.history = []
        self.build_ui()

    def make_label(self, text, size=14, bold=False):
        return Label(
            text=text,
            font_size=dp(size),
            bold=bold,
            color=(0.9, 0.93, 0.97, 1),
            halign="left",
            valign="middle"
        )

    def build_ui(self):

        # HEADER
        header = BoxLayout(
            size_hint_y=None,
            height=dp(70),
            spacing=dp(8)
        )

        header.add_widget(
            self.make_label(
                "AI ANALYTICS",
                23,
                True
            )
        )

        header.add_widget(
            self.make_label(
                "Advanced Statistical Dashboard",
                11
            )
        )

        self.add_widget(header)

        # STAT CARDS
        cards = GridLayout(
            cols=2,
            spacing=dp(10),
            size_hint_y=None,
            height=dp(230)
        )

        # Status
        card = Card()
        card.add_widget(
            self.make_label("SYSTEM STATUS", 10)
        )

        self.status = self.make_label(
            "READY",
            20,
            True
        )

        card.add_widget(self.status)
        cards.add_widget(card)

        # Confidence
        card = Card()
        card.add_widget(
            self.make_label("MODEL CONFIDENCE", 10)
        )

        self.confidence = self.make_label(
            "—",
            25,
            True
        )

        card.add_widget(self.confidence)
        cards.add_widget(card)

        # Samples
        card = Card()
        card.add_widget(
            self.make_label("DATA SAMPLES", 10)
        )

        self.samples = self.make_label(
            "0",
            25,
            True
        )

        card.add_widget(self.samples)
        cards.add_widget(card)

        # Distribution
        card = Card()
        card.add_widget(
            self.make_label("DISTRIBUTION", 10)
        )

        self.distribution = self.make_label(
            "—",
            13,
            True
        )

        card.add_widget(self.distribution)
        cards.add_widget(card)

        self.add_widget(cards)

        # BUTTONS
        buttons = BoxLayout(
            size_hint_y=None,
            height=dp(55),
            spacing=dp(8)
        )

        run_button = Button(
            text="RUN ANALYSIS",
            font_size=dp(15)
        )

        run_button.bind(
            on_release=lambda *_: self.run_analysis()
        )

        reset_button = Button(
            text="RESET",
            font_size=dp(15)
        )

        reset_button.bind(
            on_release=lambda *_: self.reset()
        )

        buttons.add_widget(run_button)
        buttons.add_widget(reset_button)

        self.add_widget(buttons)

        # HISTORY TITLE
        self.add_widget(
            self.make_label(
                "RECENT ANALYSIS",
                15,
                True
            )
        )

        # HISTORY
        scroll = ScrollView()

        self.history_box = GridLayout(
            cols=1,
            spacing=dp(6),
            size_hint_y=None
        )

        self.history_box.bind(
            minimum_height=self.history_box.setter("height")
        )

        scroll.add_widget(self.history_box)
        self.add_widget(scroll)

        # DISCLAIMER
        note = self.make_label(
            "Demo analytics only. Results are statistical estimates "
            "from simulated data and are not guaranteed outcomes.",
            10
        )

        note.size_hint_y = None
        note.height = dp(42)

        self.add_widget(note)

    def run_analysis(self):

        self.status.text = "ANALYZING..."

        Clock.schedule_once(
            self.complete_analysis,
            1
        )

    def complete_analysis(self, *_):

        # Simulated dataset
        data = [
            random.choice(
                ["RED", "GREEN", "VIOLET"]
            )
            for _ in range(100)
        ]

        counts = Counter(data)
        total = len(data)

        probabilities = {
            key: counts[key] / total
            for key in counts
        }

        strongest = max(
            probabilities,
            key=probabilities.get
        )

        confidence = probabilities[strongest] * 100

        # Update dashboard
        self.status.text = "ANALYSIS COMPLETE"

        self.confidence.text = (
            f"{confidence:.1f}%"
        )

        self.samples.text = str(total)

        self.distribution.text = (
            f"RED {probabilities['RED'] * 100:.0f}%   "
            f"GREEN {probabilities['GREEN'] * 100:.0f}%   "
            f"VIOLET {probabilities['VIOLET'] * 100:.0f}%"
        )

        # Add history
        self.history.insert(
            0,
            strongest
        )

        self.history = self.history[:15]

        self.update_history()

    def update_history(self):

        self.history_box.clear_widgets()

        for index, result in enumerate(
            self.history,
            start=1
        ):

            row = Card()

            row.height = dp(48)
            row.orientation = "horizontal"

            row.add_widget(
                self.make_label(
                    f"#{index}",
                    12,
                    True
                )
            )

            row.add_widget(
                self.make_label(
                    result,
                    16,
                    True
                )
            )

            self.history_box.add_widget(row)

    def reset(self):

        self.history = []

        self.status.text = "READY"
        self.confidence.text = "—"
        self.samples.text = "0"
        self.distribution.text = "—"

        self.history_box.clear_widgets()


class AdvancedAnalyticsApp(App):

    title = "Advanced AI Analytics"

    def build(self):
        return Dashboard()


if __name__ == "__main__":
    AdvancedAnalyticsApp().run()
