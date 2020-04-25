# [Test exercise](https://hackmd.io/@D-ARXLgbRCme4OuhySva7w/S1lwRgJKU#Stack) for O.Dev internship
## Run server
`python manage.py runserver`
## Use API
`http://127.0.0.1:8000/api/?start_at=START_DATE&end_at=END_DATE&base=CURRENCY`

## Example
### Query
`http://127.0.0.1:8000/api/?start_at=2018-01-01&end_at=2018-09-01&base=USD`

or 

`GET http://127.0.0.1:8000/api/?start_at=2018-01-01&end_at=2018-09-01&base=USD&format=json HTTP/1.1`
### Response
`{
    "CAD": {
        "std_dev": 0.02616930925984189,
        "avg": 1.2858033720807018,
        "var": 0.0006848327471372465
    },
    "HKD": {
        "std_dev": 0.011986382344390631,
        "avg": 7.840678740349708,
        "var": 0.00014367336170591943
    },
    "ISK": {
        "std_dev": 3.4104851361910016,
        "avg": 103.69502862098993,
        "var": 11.631408864179756
    },
    ...
`