<h1>README</h1>
<h2>SETUP</h2>

`Virtualenv `
```

python -m venv env

source env/bin/activate 
OR 
./Scripts/activate
pip install -r requirements.txt
```


`ENVIORNMENT VARIABLES`
```
DEBUG=True
EMAIL_SENDER=
MAIL_USER=
EMAIL_RECIEVER=
MAIL_SERVER=
```

`package.json file for tailwind`
```
{
  "scripts": {
    "watch": "npx tailwindcss -i ./app/public/css/src/input.css -o ./app/public/css/dist/output.css --watch"
  },
  "dependencies": {
    "flowbite": "^1.6.3",
    "tailwindcss": "^3.2.7"
  }
}
```


`tailwind.config.js`

```
/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: ["./app/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```
`npm run watch` To Watch CSS changes
```
python run.py
OR
export FLASK_APP=run.py
flask run
```