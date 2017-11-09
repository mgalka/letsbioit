SLIDES := $(patsubst %-slides.md,%-slides.pdf,$(wildcard *-slides.md))
INC_SLIDES := $(patsubst %-slides.md,%-slides-inc.pdf,$(wildcard *-slides.md))
EXERCISES := $(patsubst %-exercises.md,%-exercises.pdf,$(wildcard *-exercises.md))
PRINTOUTS := $(patsubst %-slides.md,%-slides-print.pdf,$(wildcard *-slides.md))

all : $(SLIDES) $(INC_SLIDES) $(PRINTOUTS)
slides : $(SLIDES)
presentation : $(INC_SLIDES)
exercises : $(EXERCISES)
print : $(SLIDES) $(PRINTOUTS)

%-slides.pdf : %-slides.md
	PATH=$$PATH:beamer/themes pandoc -t beamer -V theme:metropolis -H beamer/header.tex \
	--slide-level 2 -V handout --listings $^ -o $@ -fmarkdown-implicit_figures

%-slides-inc.pdf : %-slides.md
	PATH=$$PATH:beamer/themes pandoc -t beamer -V theme:metropolis -H beamer/header.tex \
	--slide-level 2 --incremental --listings $^ -o $@ -fmarkdown-implicit_figures
		
%-exercises.pdf : %-exercises.md
	pandoc $^ -o $@

%-slides-print.pdf : %-slides.pdf
	pdfnup $^ --nup 1x2 --no-landscape --keepinfo --paper a4 --frame true --scale 0.9 --suffix "print"


clean : 
	rm -f $(SLIDES)
	rm -f $(INC_SLIDES)
	rm -f $(EXERCISES)
	rm -f $(PRINTOUTS)