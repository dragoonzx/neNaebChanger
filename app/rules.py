from flask import render_template
from app import app, LINK


@app.route('/rules')
@app.route('/rules/')
def rules():
	return render_template('sosaka.html',
		LINK = LINK,
		url = 'rules',
	)