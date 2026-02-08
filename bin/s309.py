from amis import (
    compare,
    get_model,
    reconstruct,
)
from utils import *


def parse_args():
    import argparse

    parser = argparse.ArgumentParser(description="S309 analysis")
    parser.add_argument("--namespace", type=str, default="s309", help="Model namespace")
    parser.add_argument(
        "--model-name",
        type=str,
        default="esm1b",
        help="Type of language model (e.g., esm1b, esm-msa)",
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()

    model = get_model(args)

    vh = "QVQLVQSGAEVKKPGASVKVSCKASGYPFTSYGISWVRQAPGQGLEWMGWISTYNGNTNYAQKFQGRVTMTTDTSTTTGYMELRRLRSDDTAVYYCARDYTRGAWFGESLIGGFDNWGQGTLVTVSS"
    vl = "EIVLTQSPGTLSLSPGERATLSCRASQTVSSTSLAWYQQKPGQAPRLLIYGASSRATGIPDRFSGSGSGTDFTLTISRLEPEDFAVYYCQQHDTSLTFGGGTKVEIK"

    new = reconstruct(vh, model, decode_kwargs={"exclude": "unnatural"})
    compare(vh, new, namespace="S309 VH")
    print("")

    new = reconstruct(vl, model, decode_kwargs={"exclude": "unnatural"})
    compare(vl, new, namespace="S309 VK")
