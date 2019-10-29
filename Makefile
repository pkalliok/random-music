
stamps/install-requisites:
	sudo apt install abcmidi timidity
	touch $@

random.abc: make_tune.py generate.py transform.py render.py
	python3 $< 0 z | tee $@

%.midi: %.abc
	abc2midi $< -o $@

play-%: %.midi
	timidity $<

