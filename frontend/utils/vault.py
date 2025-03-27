from azure.identity import EnvironmentCredential
from azure.keyvault.secrets import SecretClient
import os

def get_secret(secret_name):
    try:
        key_vault_name = os.getenv('KEY_VAULT_NAME')
        print(key_vault_name)
        vault_url = f"https://{key_vault_name}.vault.azure.net"
        credential = EnvironmentCredential()
        client = SecretClient(vault_url=vault_url, credential=credential)
        return client.get_secret(secret_name).value
    except Exception as e:
        return None
