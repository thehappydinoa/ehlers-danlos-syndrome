import arv


def get_genome_from_file(file_path: str) -> arv.Genome:
    return arv.load(file_path)
