from pprint import pprint
import firebase_admin
from firebase_admin import credentials, firestore


class FireStore():
    def __init__(self, product_id, private_key_id, private_key, client_email, client_id, client_x509_cert_url):
        self.cred_obj = {
            "type": "service_account",
            "project_id": product_id,
            "private_key_id": private_key_id,
            "private_key": private_key,
            "client_email": client_email,
            "client_id": client_id,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": client_x509_cert_url
        }

        cred = firebase_admin.credentials.Certificate(self.cred_obj)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def fetch_collection_data(self, collection_name: str):
        collection_ref = self.db.collection(collection_name)
        docs = collection_ref.stream()
        docs_list = [doc.to_dict() for doc in docs]
        return docs_list

    def create_collection_data(self, collection_name: str, data: dict):
        """
            param:
                collection_name: str
                data: {
                    name: str
                    datetime: datetime.now()

                }
        """
        if collection_name == "" and data == None:
            return None

        doc_ref = self.db.collection(collection_name).document()
        doc_ref.set(data, merge=True)
