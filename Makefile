
stamps/install-requisites:
	sudo apt install abcmidi timidity
	touch $@

%.midi: %.abc
	abc2midi $< -o $@

play-%: %.midi
	timidity $<

