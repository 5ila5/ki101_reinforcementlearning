from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


class DefaultVoiceScene(VoiceoverScene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_speech_service(GTTSService())

class DefaultMainVoiceScene(DefaultVoiceScene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

