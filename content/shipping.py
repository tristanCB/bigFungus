def getShippingOptionsStripe():
    ship = [
            {
                'shipping_rate_data': {
                'type': 'fixed_amount',
                'fixed_amount': {
                    'amount': 0,
                    'currency': 'cad',
                },
                'display_name': 'Free shipping',
                # Delivers between 5-7 business days
                'delivery_estimate': {
                    'minimum': {
                    'unit': 'business_day',
                    'value': 5,
                    },
                    'maximum': {
                    'unit': 'business_day',
                    'value': 7,
                    },
                }
                }
            },
            {
                'shipping_rate_data': {
                'type': 'fixed_amount',
                'fixed_amount': {
                    'amount': 1500,
                    'currency': 'cad',
                },
                'display_name': 'Next day air',
                # Delivers in exactly 1 business day
                'delivery_estimate': {
                    'minimum': {
                    'unit': 'business_day',
                    'value': 1,
                    },
                    'maximum': {
                    'unit': 'business_day',
                    'value': 1,
                    },
                }
                }
            },
        ]
    return ship