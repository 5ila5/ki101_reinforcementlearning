ScenesToRender: list = ["Start", "Environment"]


class Text_Helper:
    SCENE_TEXTS: dict[str, dict] = {
        "Start": {
            "title": "Reinforcement learning",
        },
        "Praxis-Environment": {
            "title": "Praxis: Environment",
            "start": "Jetzt ist es erstmal genug mit der Theorie. Wir wollen uns das Ganze jetzt mal an einem Beispiel anschauen.",
            "real_start": "In diesem Szenario ist ein Elf zu sehen, der versucht, das Geschenk zu erreichen. Der Elf erhält dann eine Belohnung, wenn er es geschafft hat.",
            "show_lake": "Dafür muss er sich über einen zugefrorenen See bewegen, indem er sich wie auf einem Schachbrett von Feld zu Feld bewegt."
            "Dabei muss er nicht nur den richtigen Weg finden und die Löcher in der Eisdecke umgehen, sondern auch damit umgehen, dass die Eisdecke rutschig ist.",
            "slippery": "Es kann also passieren, dass er statt in die gewählte Richtung auch in eine andere Richtung rutscht.",
        },
    }

    @staticmethod
    def get_text(scene_name: str, text_part: str) -> str:
        return Text_Helper.SCENE_TEXTS[scene_name][text_part]
