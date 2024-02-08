from manim_voiceover import VoiceoverScene

from ai101_video.AudioService import AudioService


class DefaultVoiceScene(VoiceoverScene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_speech_service(AudioService(lang="de", tld="de"))


class DefaultMainVoiceScene(DefaultVoiceScene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
