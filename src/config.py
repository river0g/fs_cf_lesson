import os
from os.path import join, dirname
from typing import Union
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def get_env(key: str) -> Union[str, None]:
    value = os.environ.get(key, None)
    # envから読み取ったエスケープシーケンスがそのまま文字列として認識されるのでここでエスケープシーケンスに変換
    new_value = value.replace(r"\n", '\n')
    return new_value


ENV = get_env('ENVIRONMENT')  # DEVELOPMENT or PRODUCTION

# if ENV == "DEVELOPMENT":

# elif ENV == "PRODUCTION":


client_id = get_env('CLIENT_ID')
client_email = get_env('CLIENT_EMAIL')
private_key = get_env('PRIVATE_KEY')
private_key_id = get_env('PRIVATE_KEY_ID')
client_x509_cert_url = get_env('CLIENT_X509_CERT_URL')
product_id = get_env('PRODUCT_ID')
