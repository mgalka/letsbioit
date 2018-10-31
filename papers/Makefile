SLIDES := $(patsubst %-slides.md,%-slides.pdf,$(wildcard *-slides.md))
REVEAL_SLIDES := $(patsubst %-slides.md,%-slides.html,$(wildcard *-slides.md))
INC_SLIDES := $(patsubst %-slides.md,%-slides-inc.pdf,$(wildcard *-slides.md))
EXERCISES := $(patsubst %-exercises.md,%-exercises.pdf,$(wildcard *-exercises.md))
PRINTOUTS := $(patsubst %-slides.md,%-slides-print.pdf,$(wildcard *-slides.md))

BEAMER_DIR := texfiles/beamer
BEAMER_THEME_DIR := $(BEAMER_DIR)/themes
TEMPLATE_DIR := texfiles
REVEAL_DIR := ./reveal-js
_PATH := $$PATH:$(BEAMER_THEME_DIR):$(TEMPLATE_DIR)


all : $(SLIDES) $(INC_SLIDES) $(PRINTOUTS) $(EXERCISES)
slides : $(SLIDES)
presentation : $(INC_SLIDES)
exercises : $(EXERCISES)
print : $(SLIDES) $(PRINTOUTS)
reveal : $(REVEAL_SLIDES)

%-slides.html : %-slides.md
	pandoc -t revealjs -s $^ -o $@ -V revealjs-url=$(REVEAL_DIR)

%-slides.pdf : %-slides.md
	PATH=$(_PATH) pandoc -t beamer -V theme:metropolis -H $(BEAMER_DIR)/header.tex \
	--slide-level 2 -V handout --listings $^ -o $@ -fmarkdown-implicit_figures

%-slides-inc.pdf : %-slides.md
	PATH=$(_PATH) pandoc -t beamer -V theme:metropolis -H $(BEAMER_DIR)/header.tex \
	--slide-level 2 --incremental --listings $^ -o $@ -fmarkdown-implicit_figures
		
%-exercises.pdf : %-exercises.md
	pandoc --from markdown --template $(TEMPLATE_DIR)/eisvogel $^ -o $@

%-slides-print.pdf : %-slides.pdf
	pdfnup $^ --nup 1x2 --no-landscape --keepinfo --paper a4 --frame true --scale 0.9 --suffix "print"


clean : 
	rm -f $(SLIDES)
	rm -f $(INC_SLIDES)
	rm -f $(EXERCISES)
	rm -f $(PRINTOUTS)
	rm -f $(HTML_SLIDES)
