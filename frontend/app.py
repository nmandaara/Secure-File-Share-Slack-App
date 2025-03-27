from flask import Flask, request, render_template
from utils.vault import get_secret
from utils.storage import upload_file_to_blob, store_metadata_in_table
from azure.identity import EnvironmentCredential

app = Flask(__name__)
credential = EnvironmentCredential()

# Load from Key Vault
_storage_conn_str = None
CONTAINER_NAME = "secure-files"
TABLE_NAME = "webappdata"

@app.route('/', methods=['GET'])
def home():
    global _storage_conn_str
    if not _storage_conn_str:
        _storage_conn_str = get_secret("storage-conn-str")
    return render_template("upload.html")

@app.route('/upload', methods=['POST'])
def upload():

    file = request.files['file']
    from_user = request.form['from_user']
    to_user = request.form['to_user']

    blob_name = upload_file_to_blob(_storage_conn_str, CONTAINER_NAME, file)
    store_metadata_in_table(_storage_conn_str, TABLE_NAME, blob_name, from_user, to_user)

    return render_template("upload.html", message="File uploaded successfully!", blob_name=blob_name)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
