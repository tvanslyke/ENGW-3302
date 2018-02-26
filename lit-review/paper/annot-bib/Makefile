TEXC = pdflatex
BIBC = bibtex
SYSVIEWER = xdg-open
THE_BIB = annotated-bibliography.pdf

$(THE_BIB): annotated-bibliography.tex annot.bib
	$(TEXC) -output-directory=pdfbuild annotated-bibliography.tex
	$(BIBC) pdfbuild/annotated-bibliography.aux
	$(TEXC) -output-directory=pdfbuild annotated-bibliography.tex
	$(TEXC) -output-directory=pdfbuild annotated-bibliography.tex
	cp pdfbuild/annotated-bibliography.pdf $(THE_BIB)

	

.PHONY: pdf
pdf: $(THE_BIB)
	# makes the bibliography

.PHONY: view
view: pdf
	$(SYSVIEWER) $(THE_BIB)

.PHONY: clean
clean:
	rm pdfbuild/annotated-bibliography.*
	rm annotated-bibliography.pdf

