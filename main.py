import vk
import yaml
import time

from settings import *
from utils import *

EXIT_CODE = 0

setup_logger()
session, api = auth()
config = yaml.load(open(config_file_namme))
data = open(data_file_name, "a+")

# Main loop
while EXIT_CODE == 0:
    new_messages = check_messages()

    if len(new_messages) != 0: EXIT_CODE = answer_messages(new_messages, config.get("dialogs"))

    group_parsing(config.get("groups_id"))

    time.sleep(update_message_interval)