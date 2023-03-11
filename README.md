# mindful-main Team API
## skaperdagene

`pip install flask`
`pip install flask_cors`

run server:
`python flask_app.py`

App runs on port 5000

## EndPoints

Get Average Mood Score:
`GET http://127.0.0.1:8000/mood`

Get Last Feedback Score & Feeling
`GET til http://127.0.0.1:5000/lastvote`


Get All Mood Score & Feeling
`GET til http://127.0.0.1:5000/get_all`

Write Your Mood & Feeling 
`POST to http://127.0.0.1:5000/write`

Posting a JSON payload
```
{
	"mood": 0.2,
	"feeling": "jeg hater skattetaten"
}
```
Write Batch-Data
`POST to http://127.0.0.1:5000/batch_write`


Nuke the entire table in DB
`GET to http://127.0.0.1:5000/nukemofo`


The Database is SQLite with a table called 'minddata' and contains
![image](https://user-images.githubusercontent.com/59558890/224514444-3cf31aff-5a9e-4807-8030-547cb928e894.png)

