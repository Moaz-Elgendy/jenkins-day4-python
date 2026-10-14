# jenkins-day4-python

A tiny Python project plus a `Jenkinsfile` that runs its tests and a smoke build on Jenkins.

## Layout

```
app.py            # sample functions and a CLI entry point
tests/test_app.py # unittest suite
Jenkinsfile       # Checkout -> Test -> Build
```

## Local usage

```bash
python3 app.py
python3 -m unittest discover -s tests -v
```

## Jenkins

1. Create a new **Pipeline** job in Jenkins.
2. Under *Pipeline*, choose **Pipeline script from SCM**, select Git, and point it at this repository.
3. Set the script path to `Jenkinsfile` and run the build.

Stages: **Checkout** (from SCM) -> **Test** (unit tests) -> **Build** (runs `app.py`).