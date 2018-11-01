A spike to see if I can ipdb working in Docker

`docker-compose build`

`docker-compose up`

To run an interactive ipdb sesh in terminal:

1. `ctrl-c` to kill the server if it's running
2. Bring it up in the background with `docker-compose up -d`
3. OPTIONAL: check if it's still running with `docker ps` (it should be in the background)
4. `docker attach django_server` will present you with a blank line, but if you refresh browser, you'll see server output in the terminal
5. Stick `import ipdb; ipdb.set_trace()` somewhere and go wild (or comment it out in `hello_world/views.py`)