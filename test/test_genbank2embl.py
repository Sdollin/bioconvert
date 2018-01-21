from bioconvert import bioconvert_data
from easydev import TempFile, md5
import pytest
from bioconvert.genbank2embl import GENBANK2EMBL



@pytest.mark.parametrize("method", GENBANK2EMBL.available_methods)
def test_conv(method):
    infile = bioconvert_data("testing/genbank2fasta/JB409847.gbk")

    with TempFile(suffix=".embl") as tempfile:
        converter = GENBANK2EMBL(infile, tempfile.name)
        converter(method=method)

        # FIXME
        """# Check that the output is correct with a checksum
        if method == "biopython":
            assert md5(tempfile.name) == "cdd34902975a68e58ad5f105b44ff495"
        elif method == "squizz":
            pass
            # TODO
            # embl input is not understood by squizz if generated by biopython
            #     assert md5(tempfile.name) == "????"
        else:
            raise NotImplementedError

        """
