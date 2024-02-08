from pathlib import Path

from manim_voiceover.helper import remove_bookmarks
from manim_voiceover.services.base import SpeechService

from ai101_video.text_helper import Text_Helper


class AudioService(SpeechService):
    """Custom SpeechService for audio files in the audio folder."""

    def __init__(self, **kwargs):
        SpeechService.__init__(self, **kwargs)

    def generate_from_text(
        self, text: str, cache_dir: str | None = None, path: str | None = None, **kwargs
    ) -> dict:
        """"""

        input_text = remove_bookmarks(text)
        input_data = {"input_text": input_text, "service": "own_audio"}

        scene, audio = Text_Helper.get_keys(text)

        audio_path = Path(__file__).parent.joinpath("audio", f"{scene}.{audio}.mp3")
        if not audio_path.exists():
            raise FileNotFoundError(f"Audio file {audio_path} not found")

        json_dict = {
            "input_text": text,
            "input_data": input_data,
            "original_audio": str(audio_path.absolute()),
        }
        return json_dict
