# Van Gogh

This is a code test for an unnamed company. You can vote on your favorite artist from a list of artists or enter a new
one.

## Bringing this up

This app uses Docker + Docker Compose, so bringing this up is as simple as:

```shell
$ docker-compose up
```

Then you can just visit [http://localhost](http://localhost) and play around with it.

## Design Decisions

* This app uses Flask + SQLAlchemy. I left a bunch of comments in the `requirements.txt` about my package decisions.
* The database is Postgres because I like it the most.
* I was going to craft the frontend in React, but time got away from me and I got neck deep in Webpack before I just
  wanted to finish this, so I went super hacky with jQuery + Bootstrap + Handlebars.
