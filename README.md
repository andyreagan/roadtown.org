# roadtown.org

Run the development server with

```
export ROADTOWN_DJ_SECRET_KEY=insecure
export ROADTOWN_DJ_DEBUG=true
source .venv/bin/activate
python3 manage.py runserver
```

Visit the development site at
http://localhost:8000/
(note that localhost is on, but 127.0.0.1 is not allowed).


Deploy with

```
fly deploy
```

Save changes with

```
git commit -am "[description]"
git push
```
