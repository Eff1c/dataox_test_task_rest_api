# dataox_test_task_rest_api
This program was developed as a test task!

You have to only install docker and run:
```
docker build -t dataox_test_rest_api .
docker run --rm --name web -e PROXY_SERVER=<PROXY_SERVER> -p 5000:80 dataox_test_rest_api
```

For run tests: `docker exec -ti dataox_rest_api pytest`