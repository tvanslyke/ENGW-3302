TEXC = pdflatex
SYSVIEWER = xdg-open

THE_BIB = annotated-bibliography.pdf

pdfbuild/annotated-bibliography.pdf: annotated-bibliography.tex annot.bib
	cp ./$(THE_BIB) ./$(THE_BIB).bak
	$(TEXC) -output-directory=pdfbuild/

	
$(THE_BIB): pdfbuild/annotated-bibliography.pdf
	make pdfbuild/annotated-bibliography.pdf
	cp pdfbuild/annotated-bibliography.pdf $(THE_BIB)
	

.PHONY: pdf
pdf: $(THE_BIB)
	# makes the bibliography

.PHONY: view
view: pdf
	$(SYSVIEWER) $(THE_BIB)

