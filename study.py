from flask import Flask
study = Flask(__name__)

@study.route('/intro/<slug>')
def intro(slug):
	return 'intro: ' + slug

@study.route('/<sequence>/<trial>')
def trial(sequence, trial):
	return 'sequence: ' + sequence + '| trial: ' + trial

if __name__ == '__main__':
	study.run(debug = True)