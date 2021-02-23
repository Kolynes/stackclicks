import requests

class Paystack:
    base_url = "https://api.paystack.co"

    def __init__(self, api_key):
        self.api_key = api_key

    def verify_transaction(self, reference_number):
        return requests.get(
            "%s/%s/%s" %(Paystack.base_url, "transactions/verify", reference_number),
            headers={"Authorization": "Bearer %s" %self.api_key}
        ).json() 