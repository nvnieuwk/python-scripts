# Python scripts

<details>
<summary>Concatenate RTG vcfeval summary outputs</summary>

[cat_rtg_summaries.py](./cat_rtg_summaries.py)

This script takes a folder as input. The script will then search that folder for RTG vcfeval summary files and concatenate them into a single file. The script will also add a column to the output file that contains the name of the file that the row came from.
</details>

<details>
<summary>Decode igv.js URL blobs</summary>

[decode_igv_session.py](./decode_igv_session.py)

This script takes an URL to igv.js with an encoded blob as input. The script will then decode the URL blob and print the decoded JSON to stdout or a specified JSON file.
</details>

<details>
<summary>Encode an igv.js session into an URL</summary>

[encode_igv_session.py](./encode_igv_session.py)

This script takes an URL to igv.js and a session JSON file as input. The script will then encode the session file into an URL blob and print the URL to stdout.
</details>