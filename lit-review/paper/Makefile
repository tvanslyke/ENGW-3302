TEXC = pdflatex
BIBC = bibtex
SYSVIEWER = xdg-open
THE_PAPER = compiler-optimizations.pdf

$(THE_PAPER): compiler-optimizations.tex
	$(TEXC) -output-directory=pdfbuild compiler-optimizations.tex
	$(BIBC) pdfbuild/compiler-optimizations.aux
	$(TEXC) -output-directory=pdfbuild compiler-optimizations.tex
	$(TEXC) -output-directory=pdfbuild compiler-optimizations.tex
	cp pdfbuild/$(THE_PAPER) $(THE_PAPER)

	

.PHONY: pdf
pdf: $(THE_PAPER)

.PHONY: view
view: pdf
	$(SYSVIEWER) $(THE_PAPER)

.PHONY: clean

clean:
	rm pdfbuild/compiler-optimizations.*
	rm compiler-optimizations.pdf

