from ehlers_danlos_syndrome.snpedia import get_snp_details

TEST_RSID = "rs28937869"


def test_get_snp_details():
    snp = get_snp_details(TEST_RSID)
    assert snp.rsid == TEST_RSID
