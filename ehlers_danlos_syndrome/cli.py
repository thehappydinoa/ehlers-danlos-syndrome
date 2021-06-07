import os
import sys

import arv
import click
from rich import print

from .genome import get_genome_from_file
from .rsids import read_rsids_from_file, read_rsids_from_link
from .snpedia import get_snp_details

here = os.path.dirname(os.path.realpath(__file__))
data = os.path.join(here, "data")
rsids_path = os.path.join(data, "rsids.txt")


@click.command()
@click.argument("genome_path", type=click.Path(exists=True))
@click.option(
    "--rsids-path", is_flag=False, type=click.Path(exists=True), default=rsids_path
)
@click.option("--rsids-link", is_flag=False)
def main(genome_path, rsids_path, rsids_link):
    genome = get_genome_from_file(click.format_filename(genome_path))
    if rsids_link:
        rsids = read_rsids_from_link(rsids_link)
    else:
        rsids = read_rsids_from_file(click.format_filename(rsids_path))

    if not rsids:
        print("No rsIDs found from input.")
        sys.exit(1)

    for rsid in rsids:
        if rsid == "":
            continue

        link = f"https://www.snpedia.com/index.php/{rsid}"

        try:
            snp = genome[rsid]
        except KeyError:
            print(f"No SNP found for {rsid}")
            print(f"For more information please visit {link}.\n")
            continue

        snp_details = get_snp_details(rsid)
        snp_row = None
        try:
            snp_row = arv.unphased_match(snp, snp_details.table)
        except (KeyError, TypeError):
            pass
        if not snp_row:
            print(f"We are unable to identify geno {snp} for {rsid}")
            print(f"For more information please visit {link}.\n")
            continue

        description = f"({snp_details.description})" if snp_details.description else ""
        print(
            "\n".join(
                (
                    f"rsID: [yellow]{rsid}[/yellow] {description}",
                    f"You have [blue]{snp}[/blue] alleles "
                    + f"with a magnitude of {snp_row.mag}.",
                    f"Summary: {snp_row.summary}.",
                    f"For more information please visit {link}.\n",
                )
            )
        )


if __name__ == "__main__":
    main()
