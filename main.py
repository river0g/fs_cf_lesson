from src.firestore.main import FireStore
from src.config import client_id, client_email, private_key, private_key_id, client_x509_cert_url, product_id


# スクレイピング


# 取得したデータのクレンジングを行う

# firestoreの起動
fs_client = FireStore(
    product_id,
    private_key_id,
    private_key,
    client_email,
    client_id,
    client_x509_cert_url
)

# data
data = {

}

# スクレイピングしたデータをfirestoreに登録
fs_client.create_collection_data(collection_name='users', data=data)
