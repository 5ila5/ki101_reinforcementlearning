ScenesToRender: list = ["Start"]


class Text_Helper:
    SCENE_TEXTS: dict[str, dict] = {
        "Start": {
            "title": "Reinforcement learning",
        },
    }

    @staticmethod
    def get_text(scene_name: str, text_part: str) -> str:
        return Text_Helper.SCENE_TEXTS[scene_name][text_part]
