# python-amazon-scraper

Navigates to amazon, searches for samsung phones and pulls the title and price data.

## Crawl a link on the fly

```bash
scrapy shell 'https://quotes.toscrape.com/page/1/'

```

## Installation

Make sure you have [Docker Compose](https://docs.docker.com/compose/install/) installed.

## Setup

```bash
cp .env.example .env
pip3 install virtualenv && \
  virtualenv env && \
  source env/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
alias compose='docker-compose'
compose build
compose up 
```

## Using Linux?

```
make start # build & run your script
make stop  # stop your docker container
```

## Using Windows?

```
.\ps\run.ps1 start # build & run your script
.\ps\run.ps1 stop  # stop your docker container
```

## Want to use PhP instead? 
[PhP Docker Skeleton](https://github.com/kkamara/php-docker-skeleton)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[BSD](https://opensource.org/licenses/BSD-3-Clause)
