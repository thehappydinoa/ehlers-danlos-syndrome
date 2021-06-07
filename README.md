# EDS

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue?logo=python)](https://www.python.org/downloads/)

This project uses [SNPedia][snpedia] which is a collaborative and community built SNP ([Single Nucleotide Polymorphism](snp)) database to cross-reference known EDS ([Ehlers-Danlos syndrome][eds]) SNPs with your [23andme genome file][23andme-file].

## Install

Please note this project uses [`poetry`](https://python-poetry.org/docs/#installation).

```bash
poetry install
```

## Usage

```bash
poetry run eds <PATH_TO_GENOME_FILE>
```

## Learn More

- Learn about the SNPs identified [here][eds].
- Learn about other SNPs being researched [here](https://livewello.com/library/ehlers-danlos-syndrome-snps-being-researched-in-connection-to-eds-4352?id=3564048).

## Medical Disclaimer

> The information, including but not limited to, text, graphics, images and other material contained on this website are for informational purposes only. The purpose of this project is to promote broad understanding and knowledge of various health topics. It is not intended to be a substitute for professional medical advice, diagnosis or treatment. Always seek the advice of your physician or other qualified health care provider with any questions you may have regarding a medical condition or treatment and before undertaking a new health care regimen, and never disregard professional medical advice or delay in seeking it because of something you have read on this website.

## License

This software is licensed under [MIT License](https://opensource.org/licenses/MIT).

[snpedia]: <https://www.snpedia.com/index.php/SNPedia:About> "SNPedia"
[snp]: <https://www.snpedia.com/index.php/Single_Nucleotide_Polymorphism> "Single Nucleotide Polymorphism"
[eds]: <https://www.snpedia.com/index.php/Ehlers-Danlos_syndrome> "Ehlers-Danlos syndrome"
[23andme-file]: <https://customercare.23andme.com/hc/en-us/articles/212196868-Accessing-Your-Raw-Genetic-Data> "23andme genome file"
