import base64
import json
import zlib
import argparse

def base64_decode_and_inflate(blob):
    expected_output_parsed = blob.replace(".","+").replace("_","/").replace("-","=")
    base64_expected = base64.b64decode(expected_output_parsed)
    return json.loads(zlib.decompress(base64_expected, wbits=-15).decode())

if __name__ == "__main__": 
    # Setting up argparser
    parser = argparse.ArgumentParser(description="Create an igv.js session link")
    parser.add_argument('url', metavar='URL', type=str, help="The URL with an encoded session blob")
    parser.add_argument('--output', metavar='FILE', type=str, help="A JSON file to use as output. Default: stdout")

    args = parser.parse_args()
    url = args.url
    output = args.output

    blob = url.split("?sessionURL=blob:")[1]
    session = base64_decode_and_inflate(blob)

    out_session = json.dumps(session, indent=4)

    if output != None:
        open(output,"w").write(out_session)
    else:
        print(out_session)
