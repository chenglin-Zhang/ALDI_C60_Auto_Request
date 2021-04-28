import os
from configparser import ConfigParser

cur_path = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(cur_path, "cfg.ini")
conf = ConfigParser()
conf.read(config_path)

server = conf.get("email", "server")
port = conf.get("email", "port")
from_user = conf.get("email", "from_user")
password = conf.get("email", "password")
to_user = conf.get("email", "to_user")