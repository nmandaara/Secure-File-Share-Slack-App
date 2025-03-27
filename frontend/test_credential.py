from azure.identity import EnvironmentCredential
from azure.core.exceptions import ClientAuthenticationError

try:
    cred = EnvironmentCredential()
    token = cred.get_token("https://vault.azure.net/.default")
    print("✅ Token retrieved successfully!")
    print(f"Access Token: {token.token[:50]}...")  # Print first 50 chars for security
except ClientAuthenticationError as e:
    print("❌ Authentication failed.")
    print(f"Details: {e}")
except Exception as ex:
    print("❌ Unexpected error.")
    print(f"Details: {ex}")