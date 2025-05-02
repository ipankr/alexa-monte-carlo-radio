from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type
from ask_sdk_model import Response
from ask_sdk_model.ui import PlayBehavior
from ask_sdk_model.interfaces.audioplayer import PlayDirective, AudioItem, Stream

RADIO_STREAM_URL = "https://your-radio-stream-url.com/stream.mp3"

class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        speech_text = "Включаю!"
        stream = Stream(token="123", url=RADIO_STREAM_URL, offset_in_milliseconds=0)
        audio_item = AudioItem(stream=stream)
        play_directive = PlayDirective(play_behavior=PlayBehavior.REPLACE_ALL, audio_item=audio_item)
        
        return handler_input.response_builder.speak(speech_text).add_directive(play_directive).response

sb = SkillBuilder()
sb.add_request_handler(LaunchRequestHandler())

lambda_handler = sb.lambda_handler()
