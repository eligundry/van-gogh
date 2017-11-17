# Van Gogh

This is a code test for an unnamed company. You can vote on your favorite artist from a list of artists or enter a new
one.

## Bringing this up

This app uses Docker + Docker Compose, so bringing this up is as simple as:

```shell
$ docker-compose up
```

This might take a sec to build and run migrations. Please note that this requires a Docker setup that supports Docker
Compose version files >= 2.1 (Docker for Mac should just handle this, but my Linux machine required an update to run
it).

Then you can just visit [http://localhost:8000](http://localhost:8000) and play around with it.

## Design Decisions & Notes

* This app uses Flask + SQLAlchemy. I left a bunch of comments in the `requirements.txt` about my package decisions.
* The database is Postgres because I like it the most.
* I was going to craft the frontend in React, but time got away from me and I got neck deep in Webpack before I just
  wanted to finish this, so I went super hacky with jQuery + Bootstrap + Handlebars.
* This site is ugly as sin, I know. I have better taste than this.
* Is using Marshmallow for such a simple app overkill? Probably, but I want to show the types of APIs I build using
  Flask and what I can bring to the table.
* Usually, I would make a component for the operations involving 2+ models, but I figured because this is such a small
  app, I would toss everything on the model.
* Flask-Migrate has gotten a lot better than when I last used it seriously 2 years ago!
* I wrote some tests for the backend, coverage isn't 100%, but whatever. The frontend is completely untested, which I am
  not okay with. If I had gone the React route, this would have tests, but now I just want to go to sleep.
* I wanted to have an nginx reverse proxy in front of the app, and usually that image just works (it has some magic
  where it will generate an nginx config based upon envvars from other containers), but it's been giving me problems in
  the past month or so on this and other projects I have. I'm fine with raw gunicorn for this, but in production, that
  is a no go.
