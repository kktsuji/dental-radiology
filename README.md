# dental-radiology

## Usage

1. ``git clone git@github.com:kktsuji/dental-radiology.git`` on WSL
2. ``cd dental-radiology``
3. ``docker build -t pandoc/japanese .`` to build the Docker image
4. Execute following command to generate PDF file from Markdown file:

```bash
docker run --rm \
       --volume "$(pwd):/data" \
       --user $(id -u):$(id -g) \
       pandoc/japanese out/reports/report.md -o out/reports/report.pdf \
       --pdf-engine=lualatex \
       -V documentclass=ltjsarticle \
       -V luatexjapresetoptions=ipaex \
       -V geometry:top=25mm \
       -V geometry:headheight=10mm \
       -V geometry:headsep=5mm
       # -V classoption=twocolumn
```
