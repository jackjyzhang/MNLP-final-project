#!/bin/bash

curl -X POST \
-H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
-H "Content-Type: application/json; charset=utf-8" \
-d @mtinput.json \
https://translation.googleapis.com/language/translate/v2 > mtoutput.json

# curl -s -X POST -H "Content-Type: application/json" \
#     -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
#     --data "{
#   'q': 'The Great Pyramid of Giza (also known as the Pyramid of Khufu or the
#         Pyramid of Cheops) is the oldest and largest of the three pyramids in
#         the Giza pyramid complex.',
#   'source': 'en',
#   'target': 'zh-CN',
#   'format': 'text'
# }" "https://translation.googleapis.com/language/translate/v2" > mtoutput.json