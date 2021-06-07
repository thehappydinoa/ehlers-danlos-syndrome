import re
from typing import Optional, List, NamedTuple, Dict, Any

import requests
import bs4

GENO_REGEX = re.compile(r"\(.;.\)")

DESC_STYLE = (
    "border: 1px; background-color: #FFFFC0;"
    + "border-style: solid; margin:1em; width:90%;"
)


class SNP:
    def __init__(
        self, rsid: str, table: Optional[list] = None, description: Optional[str] = None
    ):
        self.rsid = rsid
        self.table = table
        self.description = description


def table_to_dict(table: bs4.element.Tag) -> Dict[str, Any]:
    html_headers = table.find_all("th")
    headers: List[str] = []
    for header in html_headers:
        h_str = header.string
        if not h_str:
            link = header.find("a")
            h_str = link.string

        headers.append(h_str.strip().lower())

    DataTuple = NamedTuple("Row", ((header, str) for header in headers))  # type: ignore

    html_rows = table.find_all("tr")
    data: Dict[str, DataTuple] = {}
    for row in html_rows:
        cols = row.find_all("td")
        if not cols:
            continue

        row_data = []
        for col in cols:
            data_str = col.string
            if not data_str:
                link = col.find("a")
                data_str = link.string
            data_str = data_str.strip()
            if re.match(GENO_REGEX, data_str):
                data_str = "".join(c for c in data_str if c not in ["(", ";", ")"])
            row_data.append(data_str)

        tup = DataTuple(*row_data)
        data[tup.geno] = tup  # type: ignore

    return data


def get_snp_details(rsid: str) -> SNP:
    snp_kwargs: Dict[str, Any] = {}

    snp_url = f"https://bots.snpedia.com/index.php/{rsid}"

    res = requests.get(snp_url)

    if not res.ok:
        raise Exception(f"Received code: {res.status_code} from {snp_url}")

    bs = bs4.BeautifulSoup(res.text, "html.parser")

    table = bs.find("table", {"class": "sortable smwtable"})
    if table:
        snp_kwargs["table"] = table_to_dict(table)

    description_table = bs.find("table", {"style": DESC_STYLE})
    if description_table:
        description_html = description_table.find("td")
        if description_html:
            snp_kwargs["description"] = description_html.string

    return SNP(rsid, **snp_kwargs)


if __name__ == "__main__":
    snp = get_snp_details("rs28937869")
    print(snp.table)
