# Swagger/OAI MITM Proxy

This tool will generate Swagger/Open API Initiative (OAI) docs based
on real web traffic.

## Setup

You will need to install the latest version of `mitmproxy`:

```sh
$ pip install mitmproxy
```

Clone this repo:

```sh
git clone git@github.com:adafruit/swagger-mitm.git && cd swagger-mitm
```

## Usage

Run the following command to start the server:

```sh
$ ./mitm
```

Configure your computer to use the following proxy info:

```
HTTP: 127.0.0.1 port 8080
HTTPS: 127.0.0.1 port 8080
```

## HSTS Reset

You may need to clear HSTS for target domains in Chrome: [chrome://net-internals/#hsts](chrome://net-internals/#hsts). FireFox
doesn't have an easy way to clear HSTS settings, so it might be better to just use Chrome for this tool.
