''' This is a translation module that allows you to translate between english and french'''
import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)

language_translator.set_service_url(url)


def english_to_french(english_text):
    '''
    This function takes a string of english text and translates it to french
    '''
    try:
        # Translate the input text to french
        translation = language_translator.translate(
        text=english_text, model_id='en-fr').get_result()

        # Take the translated text from the dict & turn it into a string
        french_text = str(translation["translations"][0]["translation"])

    except ApiException as ex:
        return "Method failed with status code " + str(ex.code) + ": " + ex.message

    return french_text


def french_to_english(french_text):
    '''
    This function takes a string of french text and translates it to english
    '''
    try:
        # Translate the input text to french
        translation = language_translator.translate(
        text=french_text, model_id='fr-en').get_result()

        # Take the translated text from the dict & turn it into a string
        english_text = str(translation["translations"][0]["translation"])

    except ApiException as ex:
        return "Method failed with status code " + str(ex.code) + ": " + ex.message

    return english_text
