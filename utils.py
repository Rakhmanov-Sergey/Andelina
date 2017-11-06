import os
import vk
import logging
from vk.exceptions import VkAPIError
from settings import *

def setup_logger():
    if os.path.isfile(logging_file): os.remove(logging_file)

    if logging_file == "":
        logging.basicConfig(level=logging_level, format=logging_format)
    else:
        logging.basicConfig(level=logging_level, format=logging_format, filename=logging_file)


def auth():
    logging.info("Authorizing...")

    try:
        logging.info("Trying with access_token")
        session = vk.Session(access_token)
        api = vk.API(session)

        api.users.get(user_ids=1) # Test call

        logging.info("Successfully authorized")
    except VkAPIError:
        logging.error("Failed authorization with access token! Trying with login and password...")
        session = vk.AuthSession(app_id, login, password)
        api = vk.API(session)

        api.users.get(user_ids=1) # Test call

        if access_token != session.access_token: logging.warning("Wrong access_token stored in settings. Use: " + session.access_token)

        logging.info("Successfully authorized")

    return session, api
