# Swagger/OAI MITM Proxy

This tool will generate Swagger/Open API Initiative (OAI) docs based
on real web traffic.

## Setup

You will need a recent version of node.js:

```sh
$ node -v
v6.8.1
```

Clone this repo, and run:

```sh
$ npm install
```

## Usage

Run the following command to start the server:

```sh
$ npm start
```

Configure your computer to use the following proxy info:

```
HTTP: 127.0.0.1 port 8888
HTTPS: 127.0.0.1 port 8889
```

## HSTS Reset

You may need to clear HSTS for target domains in Chrome: [chrome://net-internals/#hsts](chrome://net-internals/#hsts). FireFox
doesn't have an easy way to clear HSTS settings, so it might be better to just use Chrome for this tool.
