from flask import Flask, render_template
import yaml

study = Flask(__name__)


# HELPERS

def load_items():
	return yaml.load(open('config/items.yaml', 'r'))

def load_sequences():
	return yaml.load(open('config/sequences.yaml', 'r'))

def get_item(item):
	return load_items()[item]

def get_sequence(sid):
	return load_sequences()['seq' + sid]

def get_trial_pair(sid, tid):

    trial = get_sequence(sid)[int(tid)-1]
    b = get_item(trial[0])
    q = get_item(trial[1])
    
    return { 'base': b, 'question': q }



# ACTIONS

@study.route('/sequence/<sid>/trial/<tid>')
def trial(sid, tid):	
	pair = get_trial_pair(sid, tid)
	return render_template('trial.html', pair = pair)


if __name__ == '__main__':
	study.run(debug = True)