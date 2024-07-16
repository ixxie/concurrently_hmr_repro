import subprocess
import shlex
import os


def run():
    command = f'concurrently{".cmd" if os.name == "nt" else ""} --raw --name "backend,frontend" "cd backend && poetry run server" "cd frontend && npm run dev"'
    subprocess.run(shlex.split(command), cwd=".", stderr=subprocess.STDOUT)


if __name__ == "__main__":
    run()
