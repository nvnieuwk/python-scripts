import base64
import json
import zlib
import argparse

def deflate_and_base64_encode(session_dict):
    session_string = json.dumps(session_dict).encode()
    compressed_string = zlib.compress(session_string)
    parsed_compressed_string = compressed_string[2:-4] # Remove headers and tails from compressed string
    return base64.b64encode(parsed_compressed_string).decode().replace("+",".").replace("/","_").replace("=","-")

if __name__ == "__main__": 
    # Setting up argparser
    parser = argparse.ArgumentParser(description="Create an igv.js session link")
    parser.add_argument('url', metavar='URL', type=str, help="The URL of the IGV.js instance")
    parser.add_argument('--json', metavar='FILE', type=str, help="A JSON file containing the session details (https://github.com/igvteam/igv.js/wiki/Tracks-2.0)", default="./igv_session.json")

    args = parser.parse_args()
    url = args.url
    json_file = args.json

    session_dict = json.load(open(json_file,"r"))
    deflated_session = deflate_and_base64_encode(session_dict)

    print(f'{url}/?sessionURL=blob:{deflated_session}')
