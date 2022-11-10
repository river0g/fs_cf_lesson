from firestore.main import FireStore
# from cloudfunctions import
from config import client_id, client_email, private_key, private_key_id, client_x509_cert_url, product_id

firestore_client = FireStore(
    product_id,
    private_key_id,
    private_key,
    client_email,
    client_id,
    client_x509_cert_url
)

print(firestore_client.fetch_collection_data('users'))
