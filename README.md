## Prerequisites

- [Python 3.12](https://docs.python.org/3.12/)
- [Poetry](https://python-poetry.org/)
- [Node](https://nodejs.org/en)

The backend uses [uvicorn](https://www.uvicorn.org/) and [fastapi](https://fastapi.tiangolo.com) which are installed using Poetry into a virtual environment. The frontend is the default [SvelteKit](https://kit.svelte.dev/) demo app.

## Running

To run, call the following:

```
concurrently --raw --name "backend,frontend" "cd backend && poetry run server" "cd frontend && npm run dev"
```

Of course, you can run the commands manually to compare how everything runs without concurrently.

To run as a subprocess, run:

```
python -m run
```

or in Windows:

```
py -3.12 -m run
```

## Issues

There are a couple of issues I observe in Windows 10:

1.  Uvicorn's HMR crashes the main process; to reproduce, edit `main.py`, for example the `hello` function
2.  ANSI color codes are not propegated correctly without the `--raw` flag
3.  Exceptions are not printed until the process exits in certain situations (not able to reproduce yet)
