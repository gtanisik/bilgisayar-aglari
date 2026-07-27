# Makefile for building Marp presentations

SLIDES_DIR = slides
DIST_DIR = dist

MD_FILES = $(shell find $(SLIDES_DIR) -name "*.md" 2>/dev/null)
PDF_FILES = $(patsubst $(SLIDES_DIR)/%.md, $(DIST_DIR)/%.pdf, $(MD_FILES))
HTML_FILES = $(patsubst $(SLIDES_DIR)/%.md, $(DIST_DIR)/%.html, $(MD_FILES))

.PHONY: all pdf html clean help

all: pdf html

pdf: $(PDF_FILES)

html: $(HTML_FILES)

THEME_CSS = templates/custom-theme.css

$(DIST_DIR)/%.pdf: $(SLIDES_DIR)/%.md
	@mkdir -p $(dir $@)
	marp --theme-set $(THEME_CSS) --pdf $< -o $@

$(DIST_DIR)/%.html: $(SLIDES_DIR)/%.md
	@mkdir -p $(dir $@)
	marp --theme-set $(THEME_CSS) $< -o $@

clean:
	rm -rf $(DIST_DIR)

help:
	@echo "Kullanılabilir Komutlar:"
	@echo "  make pdf   : Tüm Marp slaytlarını PDF olarak derler"
	@echo "  make html  : Tüm Marp slaytlarını HTML olarak derler"
	@echo "  make clean : Derlenmiş dosyaları siler"
