# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

ALLOWED_CITY_NAMES = ["berlin", "hamburg", "dresden", "kiel", "bremen", "hannover", "frankfurt", "stuttgart", "koeln",
                      "muenchen"]

#Validierung für City_form1
class ValidateCityForm1(FormValidationAction):

    def name(self) -> Text:
        return "validate_city_form1"

    def validate_first_city(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate ´first_city´ value."""

        if slot_value.lower() not in ALLOWED_CITY_NAMES:
            dispatcher.utter_message(text=f"We only offer journeys to this cities {'/'.join(ALLOWED_CITY_NAMES)}.")
            return{"first_city": None}
        dispatcher.utter_message(text=f"Ok! You want to travel {slot_value}.")
        return {"first_city": slot_value}

#Validierung für City_form2
class ValidateCityForm2(FormValidationAction):

    def name(self) -> Text:
        return "validate_city_form2"

    def validate_first_city(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate ´first_city´ value."""

        if slot_value.lower() not in ALLOWED_CITY_NAMES:
            dispatcher.utter_message(text=f"We only offer journeys to this cities {'/'.join(ALLOWED_CITY_NAMES)}.")
            return{"first_city": None}
        dispatcher.utter_message(text=f"Ok! You want to travel {slot_value}.")
        return {"first_city": slot_value}

    def validate_second_city(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate ´second_city´ value."""

        if slot_value.lower() not in ALLOWED_CITY_NAMES:
            dispatcher.utter_message(text=f"We only offer journeys to this cities {'/'.join(ALLOWED_CITY_NAMES)}.")
            return{"second_city": None}
        dispatcher.utter_message(text=f"Ok! You want to travel {slot_value}.")
        return {"second_city": slot_value}

#Vaöidierung für City_form3
class ValidateCityForm3(FormValidationAction):

    def name(self) -> Text:
        return "validate_city_form3"

    def validate_first_city(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate ´first_city´ value."""

        if slot_value.lower() not in ALLOWED_CITY_NAMES:
            dispatcher.utter_message(text=f"We only offer journeys to this cities {'/'.join(ALLOWED_CITY_NAMES)}.")
            return{"first_city": None}
        dispatcher.utter_message(text=f"Ok! You want to travel {slot_value}.")
        return {"first_city": slot_value}

    def validate_second_city(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate ´second_city´ value."""

        if slot_value.lower() not in ALLOWED_CITY_NAMES:
            dispatcher.utter_message(text=f"We only offer journeys to this cities {'/'.join(ALLOWED_CITY_NAMES)}.")
            return{"second_city": None}
        dispatcher.utter_message(text=f"Ok! You want to travel {slot_value}.")
        return {"second_city": slot_value}


    def validate_third_city(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate ´third_city´ value."""

        if slot_value.lower() not in ALLOWED_CITY_NAMES:
            dispatcher.utter_message(text=f"We only offer journeys to this cities {'/'.join(ALLOWED_CITY_NAMES)}.")
            return{"third_city": None}
        dispatcher.utter_message(text=f"Ok! You want to travel {slot_value}.")
        return {"third_city": slot_value}

#Validierung für City_form4
class ValidateCityForm4(FormValidationAction):

    def name(self) -> Text:
        return "validate_city_form4"

    def validate_first_city(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate ´first_city´ value."""

        if slot_value.lower() not in ALLOWED_CITY_NAMES:
            dispatcher.utter_message(text=f"We only offer journeys to this cities {'/'.join(ALLOWED_CITY_NAMES)}.")
            return{"first_city": None}
        dispatcher.utter_message(text=f"Ok! You want to travel {slot_value}.")
        return {"first_city": slot_value}


    def validate_second_city(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate ´second_city´ value."""

        if slot_value.lower() not in ALLOWED_CITY_NAMES:
            dispatcher.utter_message(text=f"We only offer journeys to this cities {'/'.join(ALLOWED_CITY_NAMES)}.")
            return{"second_city": None}
        dispatcher.utter_message(text=f"Ok! You want to travel {slot_value}.")
        return {"second_city": slot_value}

    def validate_third_city(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate ´third_city´ value."""

        if slot_value.lower() not in ALLOWED_CITY_NAMES:
            dispatcher.utter_message(text=f"We only offer journeys to this cities {'/'.join(ALLOWED_CITY_NAMES)}.")
            return{"third_city": None}
        dispatcher.utter_message(text=f"Ok! You want to travel {slot_value}.")
        return {"third_city": slot_value}

    def validate_fourth_city(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate ´fourth_city´ value."""

        if slot_value.lower() not in ALLOWED_CITY_NAMES:
            dispatcher.utter_message(text=f"We only offer journeys to this cities {'/'.join(ALLOWED_CITY_NAMES)}.")
            return{"fourth_city": None}
        dispatcher.utter_message(text=f"Ok! You want to travel {slot_value}.")
        return {"fourth_city": slot_value}

#Vaöidierung für City_form5
class ValidateCityForm5(FormValidationAction):

    def name(self) -> Text:
        return "validate_city_form5"

    def validate_first_city(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate ´first_city´ value."""

        if slot_value.lower() not in ALLOWED_CITY_NAMES:
            dispatcher.utter_message(text=f"We only offer journeys to this cities {'/'.join(ALLOWED_CITY_NAMES)}.")
            return {"first_city": None}
        dispatcher.utter_message(text=f"Ok! You want to travel {slot_value}.")
        return {"first_city": slot_value}

    def validate_second_city(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate ´second_city´ value."""

        if slot_value.lower() not in ALLOWED_CITY_NAMES:
            dispatcher.utter_message(text=f"We only offer journeys to this cities {'/'.join(ALLOWED_CITY_NAMES)}.")
            return {"second_city": None}
        dispatcher.utter_message(text=f"Ok! You want to travel {slot_value}.")
        return {"second_city": slot_value}

    def validate_third_city(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate ´third_city´ value."""

        if slot_value.lower() not in ALLOWED_CITY_NAMES:
            dispatcher.utter_message(text=f"We only offer journeys to this cities {'/'.join(ALLOWED_CITY_NAMES)}.")
            return {"third_city": None}
        dispatcher.utter_message(text=f"Ok! You want to travel {slot_value}.")
        return {"third_city": slot_value}

    def validate_fourth_city(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate ´fourth_city´ value."""

        if slot_value.lower() not in ALLOWED_CITY_NAMES:
            dispatcher.utter_message(text=f"We only offer journeys to this cities {'/'.join(ALLOWED_CITY_NAMES)}.")
            return {"fourth_city": None}
        dispatcher.utter_message(text=f"Ok! You want to travel {slot_value}.")
        return {"fourth_city": slot_value}

    def validate_fifth_city(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate ´fifth_city´ value."""

        if slot_value.lower() not in ALLOWED_CITY_NAMES:
            dispatcher.utter_message(text=f"We only offer journeys to this cities {'/'.join(ALLOWED_CITY_NAMES)}.")
            return{"fifth_city": None}
        dispatcher.utter_message(text=f"Ok! You want to travel {slot_value}.")
        return {"fifth_city": slot_value}
