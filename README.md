# GASH (Git Dash)

Rudimentary Git dashboard for multiple projects and environments. Displays which branch each is on in a Flask app.

## Setup

Create a `settings.py` file in the root application directory and add a dict with the following structure:

```python
projects = {
	'project_1': {
		'environ_1': {
			'user': '<username>',
			'cert': '/path/to/cert.pem',
			'host': '<IP or URL>',
			'path': '/path/to/project/on/remote/host'
		},
	},
}
```

**Note**: if `cert == None` then will assume there is a key. *Username/password* access is **not** supported.

## Usage

Locally, you can just run the Flask app using its built-in development server:

```bash
python3 app.py
```
