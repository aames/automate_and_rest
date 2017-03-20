# Automate & REST

The easiest way to automate REST API testing for non-programmers. (Note: Example code to follow.)

## Introduction

Q: Are you working with test analysts who are interested in test automation?

This basic project is designed to be extended (it's a pattern for you to use) and to make it accessible for anyone who understands how to test a REST API (using PostMan or similar) to make the leap into writing automated tests.

The intention is to provide a simple, reliable, expandable foundation on which tests can be built and run by wrapping up all and any bootstrapping activities and then running tests in a basic Python UnitTest style. Sounds simple? It kinda is.

So if your aim is to have non-programmer, functional testers write automation for REST APIs then you're in the right place. Even if you can code, this is a pretty decent way to lay out your REST API tests and make them accessible to your peers.

## What's provided

- An endpoint class (feel free to extend) that models the HTTP functions related to REST and returns responses in the [Requests](docs.python-requests.org/) format. 
- A helper class of utilities to do things (like convert json template files using jinja2 template format to JSON strings)
- A docker-compose file for Redis - so you can share useful variables between test cases easily and reliably (note: some CI tools don't support env, so this works everywhere!)
- An example pattern of a test module (tests/example)

## What's not included
- Your application (see bootstrap.py)
- Your tests (see tests/example)
- CI scripts (but basically docker-compose up and then bootstrap and then run_suites is all)
- XML support (If you're really using XML then feel free to extend this yourself)
- Magic - you'll need to set things up, this project is provided as a pattern with this as a reference prototype only!

## Getting started: Requirements
- Docker (for running Redis) Redis removes the dependency on environment variables, by giving us a transient data store to store values.
- Docker compose (to setup Redis and any other services you require easily from this suite)
- Python 2 (to execute tests)
- Optional: PyCharm (or some text editor if you prefer, I like the enforced PEP8 style and built in test runner)

### Mac installation details
You probably already use homebrew (if you don't, why not?! go to [http://brew.sh]() right now)

#### Docker
```
$ brew cask install virtualbox
$ brew install docker docker-machine
```

#### Python 2
```
$ brew install python
```

### Windows installation links

#### Docker 
Install Docker for Windows from [https://docs.docker.com/docker-for-windows/install/]()

#### Python 2 
(do install to path when it asks)

[https://www.python.org/downloads/]()

