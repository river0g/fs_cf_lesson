# import sys
# import os
# root = os.path.dirname(os.path.abspath(__file__))
# print("root", root)
# sys.path.append(root)

from src.firestore.main import FireStore
from src.config import client_id, client_email, private_key, private_key_id, client_x509_cert_url, product_id

firestore_client = FireStore(
    product_id,
    private_key_id,
    private_key,
    client_email,
    client_id,
    client_x509_cert_url
)

print(firestore_client.fetch_collection_data('users'))


# print(a)
