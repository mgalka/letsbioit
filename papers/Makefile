SLIDES := $(patsubst %-slides.md,%-slides.pdf,$(wildcard *-slides.md))
INC_SLIDES := $(patsubst %-slides.md,%-slides-inc.pdf,$(wildcard *-slides.md))
EXERCISES := $(patsubst %-exercises.md,%-exercises.pdf,$(wildcard *-exercises.md))

all : $(SLIDES) $(INC_SLIDES)
slides : $(SLIDES)
presentation : $(INC_SLIDES)
exercises : $(EXERCISES)

%-slides.pdf : %-slides.md
	PATH=$$PATH:beamer/themes pandoc -t beamer -V theme:metropolis -H beamer/header.tex \
	--slide-level 2 -V handout --listings $^ -o $@ -fmarkdown-implicit_figures

%-slides-inc.pdf : %-slides.md
	PATH=$$PATH:beamer/themes pandoc -t beamer -V theme:metropolis -H beamer/header.tex \
	--slide-level 2 --incremental --listings $^ -o $@ -fmarkdown-implicit_figures
		
%-exercises.pdf : %-exercises.md
	pandoc $^ -o $@


clean : 
	rm -f $(SLIDES)
	rm -f $(INC_SLIDES)
	rm -f $(EXERCISES)