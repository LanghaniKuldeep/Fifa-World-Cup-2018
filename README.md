# Fifa World Cup Russia 2018 APIs

Scrapped www.fifa.com for fetching data of Fifa World Cup Russia 2018.

## Platform
Programming language for this scraper is python 2.7 and frameworks being used are Django 1.8 and Django rest.

## Getting Started
These instructions will get you a copy of the project up and run on your local machine for development and testing purposes.

### Prerequisites
Python 2.7 and Pip.

### Installing
 For running on your local machine or any hosting server for development and testing purpose follow the below steps.

Step 1: Clone this repo 

```
git clone https://github.com/Kuldeeplanghani/Fifa-World-Cup-2018.git
```

Step 2: Change Directory

```
cd Fifa-World-Cup-2018
```

Step 3: Install requirements

```
sudo pip install -r requirments.txt
```

### Running the Server:

```
python manage.py runserver 
```
## APIs Endpoints

### [Live Score](https://fifa-2018-apis.herokuapp.com/fifa/live/worldcup/matches/match/300331503/)
Please Add match ID(e.g: 300331503) for specific match in url at the end, You can get that from fixtures API.

URL: https://fifa-2018-apis.herokuapp.com/fifa/live/worldcup/matches/match/<match_id>

Include: 
* Score
* Status
* Home Goal Scorers with Time
* Away Goal Scorers with Time

### [Fixtures](https://fifa-2018-apis.herokuapp.com/fifa/fixtures)

URL: https://fifa-2018-apis.herokuapp.com/fifa/fixtures

Include: 
* Date time in ISO format
* Group
* Teams
* Team Flags
* Stadium 
* Venue
* Match ID (Which is needed for live Score)

### [Group Table](https://fifa-2018-apis.herokuapp.com/fifa/grouptable)

URL: https://fifa-2018-apis.herokuapp.com/fifa/grouptable

Include: 
* Team Display Name
* Team flag
* Matches Players
* Matches Won
* Matches Lost
* Matches Draw
* Goal For
* Goal Against
* Goal Goal Diff
* Points

### [News](https://fifa-2018-apis.herokuapp.com/fifa/news)
It provides upto 40 news in a request.

URL: https://fifa-2018-apis.herokuapp.com/fifa/news

Include: 
* News Title
* Thumbnail Src
* Date
* Link to News


## Authors

* **Kuldeep Kumar** - *Github* -> [Kuldeeplanghani](https://github.com/Kuldeeplanghani)

See also the list of [contributors](https://github.com/Kuldeeplanghani/Fifa-World-Cup-2018/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License.

## Acknowledgments

* www.fifa.com
* Fifa Mobile App
