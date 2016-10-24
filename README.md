# OpenAPI/Swagger MITM Proxy

This tool will generate [Swagger][1]/[OpenAPI Initiative (OAI)][2] docs based
on real web traffic.

## Setup

You will need to install the latest version of [mitmproxy][3]:

```sh
$ pip install mitmproxy
```

Clone this repo:

```sh
git clone https://github.com/adafruit/openapi-mitm.git && cd openapi-mitm
```

## Usage

Run the following command to start the server and target `www.example.com`:

```sh
$ ./mitm www.example.com
```

Configure your computer to use the following proxy info:

```
HTTP: 127.0.0.1 port 8081
HTTPS: 127.0.0.1 port 8081
```

## HSTS Reset

You may need to clear HSTS for target domains in Chrome: `chrome://net-internals/#hsts`. FireFox
doesn't seem to have an easy way to clear HSTS settings, so it might be easier to use Chrome with this tool.

## License
Copyright (c) 2016 [Adafruit Industries](https://adafruit.com). Licensed under the [MIT license](/LICENSE?raw=true).

[Adafruit](https://adafruit.com) invests time and resources providing this open source code. Please support Adafruit and open-source hardware by purchasing products from [Adafruit](https://adafruit.com).

[1]: http://swagger.io/
[2]: https://openapis.org/
[3]: https://mitmproxy.org/
