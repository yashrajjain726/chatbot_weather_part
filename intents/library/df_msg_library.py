class df_rich_responses():
    def fulfillment_messages(self, message, responses):
        return {
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            message
                        ]
                    }
                },
                {
                    "payload": {
                        "richContent": responses
                    }
                }
            ]
        }
    def follow_up_response(self, event_name, parameters):
        return {
            "followupEventInput": {
                "name": event_name,
                "parameters": parameters,
                "languageCode": "en-US"
            }
        }
    def list_response(self, emp_ids, emp_list, emp_companies, emp_cities, emp_addresses):
        buttonsList = []
        for (emp_id, name, company, city, address) \
                in zip(emp_ids[:-1], emp_list[:-1], emp_companies[:-1], emp_cities[:-1], emp_addresses[:-1]):
            buttonsList.append({
                "type": "list",
                "title": name.capitalize() + ", "+city.capitalize(),
                "subtitle": address+"\n"
                + company,
                "event": {
                    "name": "add_more_participants",
                    "languageCode": "en-IN",
                    "parameters": {
                        "emp_id": emp_id
                    }
                }
            })
            buttonsList.append({
                "type": "divider"
            })
        buttonsList.append({
            "type": "list",
            "title": emp_list[-1:][0].capitalize() + ", " +
            emp_cities[-1:][0].capitalize(),
            "subtitle": emp_addresses[-1:][0] + "\n"
                    + emp_companies[-1:][0],
            "event": {
                "name": "add_more_participants",
                "languageCode": "en-IN",
                "parameters": {
                    'emp_id': emp_ids[-1:][0]
                }
            }
        })
        return buttonsList
    def suggestion_chip_response(self, text_array):
        options = []
        for text in text_array:
            options.append({
                "text": text
            })
        return [
            {
                "type": "chips",
                "options": options
            }
        ]
    def description_response(self, titles, texts):
        cardList = []
        for (title, text) in zip(titles, texts):
            cardList.append({
                "type": "description",
                "title": title,
                "text": text
            })
        return cardList
    def simple_image_response(self, rawUrl, text):
        return {
            "type": "image",
            "rawUrl": rawUrl,
            "accessibilityText": text
        }
    def simple_accordion_response(self, title, text):
        return {
            "type": "accordion",
            "title": title,
            "text": text
        }
    def simple_list_response(self, title, event_name, parameters):
        return {
            "type": "list",
            "title": title,
            "event": {
                "name": event_name,
                "languageCode": "en-IN",
                "parameters": parameters
            }
        }
    def simple_divider(self):
        return {
            "type": "divider"
        }
    def simple_description_response(self, title, text):
        return {
            "title": title,
            "text": text,
            "type": "description"
        }
    def simple_button_response(self, text,  icon_details, event_details):
        return {
            "type": "button",
            "icon": icon_details,
            "text": text,
            "event": {
                "name": event_details['name'],
                "languageCode": "en-IN"
            }
        }