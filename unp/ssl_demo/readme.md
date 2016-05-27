create certificate:

    openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout key.pem

The scripts are as follow:

- `ssl_client.py` SSL client script
- `ssl_server.py` SSL service script
- `ssl_demo.py` SSL script requests for https://www.python.org/


