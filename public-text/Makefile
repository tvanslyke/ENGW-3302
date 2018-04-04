TEXC = pdflatex
BIBC = bibtex
SYSVIEWER = xdg-open
THE_PAPER = open-letter.pdf

$(THE_PAPER): open-letter.tex
	$(TEXC) -output-directory=pdfbuild open-letter.tex
	cp pdfbuild/$(THE_PAPER) $(THE_PAPER)

	

.PHONY: pdf
pdf: $(THE_PAPER)

.PHONY: view
view: pdf
	$(SYSVIEWER) $(THE_PAPER)

.PHONY: clean

clean:
	rm pdfbuild/open-letter.*
	rm open-letter.pdf

