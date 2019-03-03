import logging

import requests
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard

sb = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "Ciao bello, dimmi..."

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("crypto", speech_text)).set_should_end_session(
            False)
        return handler_input.response_builder.response


class CitazioneIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("CitazioneIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        speech_text = "Marco entra in una città, vede qualcuno in una piazza vivere una vita o un istante che " \
                      "potevano essere suoi. Al posto di quell’uomo ora avrebbe potuto esserci lui se si fosse " \
                      "fermato nel tempo tanto tempo prima, oppure se tanto tempo prima ad un crocevia, invece " \
                      "di prendere una strada avesse preso quella opposta, e dopo un lungo giro fosse venuto a " \
                      "trovarsi al posto di quell’uomo in quella piazza."

        logger.info(speech_text)
        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("crypto", speech_text)).set_should_end_session(False)
        return handler_input.response_builder.response


class CiaoIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("CiaoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        speech_text = "ciao ragazzi è stato piacere parlare con vuoi. Alla prossima!"

        logger.info(speech_text)
        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("crypto", speech_text)).set_should_end_session(True)
        return handler_input.response_builder.response


class DimmiqualcosaIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("DimmiqualcosaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        try:
            persona = handler_input.request_envelope.request.intent.slots["persona"].value
        except AttributeError:
            logger.info("Could not resolve persona name")
            persona = None

        speech_text = "boh non saprei cosa dirti"
        if (persona is not None):
            if persona == "rodrigo":
                speech_text = "cosa posso dire di Rodrigo il Mago, lui me ha creato!"
            if persona == "gianluigi":
                speech_text = "ha ha ha, grande Gianluigi, devo chiedere a lui dei consigli riguardo blockchain!"

        logger.info(speech_text)
        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("crypto", speech_text)).set_should_end_session(False)
        return handler_input.response_builder.response


class PrezzoIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("PrezzoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        try:
            moneta = handler_input.request_envelope.request.intent.slots["tipo_moneta"].value
        except AttributeError:
            logger.info("Could not resolve tipo_moneta name")
            moneta = None

        try:
            day = handler_input.request_envelope.request.intent.slots["day"].value
        except AttributeError:
            logger.info("Could not resolve day name")
            day = None

        speech_text = "non saprei dirti"
        if (moneta is not None) and (day is None):
            values = getTicker()
            speech_text = "Secondo Rodrigo, costa attualmente " + str(values[2]) + " euro"

        logger.info(speech_text)
        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("crypto", speech_text)).set_should_end_session(False)
        return handler_input.response_builder.response


class HelpIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "You can say hello to me!"

        handler_input.response_builder.speak(speech_text).ask(
            speech_text).set_card(SimpleCard(
            "crypto", speech_text))
        return handler_input.response_builder.response


class CancelOrStopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "ciao ciao!"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("crypto", speech_text))
        return handler_input.response_builder.response


class NavigateHomeIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.NavigateHomeIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "ciao ciao!"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("crypto", speech_text))
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        return handler_input.response_builder.response


class CatchAllExceptionHandler(AbstractExceptionHandler):

    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speech = "scusa Rod non mi ha programmato bene. potresti ripetere??"
        handler_input.response_builder.speak(speech).ask(speech)

        return handler_input.response_builder.response


def getTicker():
    r = requests.session().get("https://api.hitbtc.com/api/2/public/ticker/BTCUSD")
    if r.status_code == 200:
        data = r.json()
        return float(data["ask"]), float(data["bid"]), float(data["last"])
    return None, None, None


sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(PrezzoIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(NavigateHomeIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(DimmiqualcosaIntentHandler())
sb.add_request_handler(CitazioneIntentHandler())
sb.add_request_handler(CiaoIntentHandler())


sb.add_exception_handler(CatchAllExceptionHandler())

handler = sb.lambda_handler()
