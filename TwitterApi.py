import requests
import os
import json
import pandas as pd

# To set your enviornment variables in your terminal run the following line:
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAPYUVQEAAAAA2gS99BYCk2EB8DGq9w68SdWqux0%3DyDEVUib347dkVmH18WESS7ZPUGsql6JuZZYJ7UMdVFqHKhQ6n7'


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FilteredStreamPython"
    return r


def get_rules():
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", auth=bearer_oauth
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))
    return response.json()


def delete_all_rules(rules):
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot delete rules (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    print(json.dumps(response.json()))


def set_rules(delete):
    # You can adjust the rules if needed
    #sample_rules = [
     #   {"value": "dog has:images", "tag": "dog pictures"},
    #    {"value": "cat has:images -grumpy", "tag": "cat pictures"},
    #]
    sample_rules = [
        {"value": "(chatGPT OR AI OR ai OR chatgpt) from:elonmusk lang:en -is:retweet", "tag": "chatgpt tweets"}
    ]
    payload = {"add": sample_rules}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload,
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))


def get_stream(set):
    set_id = []
    set_text = []
    nb = 0
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream", auth=bearer_oauth, stream=True,
    )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            set_id.append(json_response['data']['id'])
            set_text.append(json_response['data']['text'])
            nb += 1
            print(json.dumps(json_response, indent=4, sort_keys=True))
            
        if (nb == 10): 
            break
            
    data = {'id': set_id, 'text': set_text}
    df = pd.DataFrame(data)
    df.to_csv('response_test.csv')


def main():
    rules = get_rules()
    delete = delete_all_rules(rules)
    set = set_rules(delete)
    get_stream(set)


if __name__ == "__main__":
    main()