import vk
from settings import *
from utils import *


setup_logger()
session, api = auth()
print(api.users.get(user_ids=1))

