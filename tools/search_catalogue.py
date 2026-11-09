"""Search citation text extracted from the survey. New companion utility."""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", default="", help="case-insensitive citation text search")
    parser.add_argument("--reference", type=int, help="exact survey bibliography number")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--json", action="store_true", help="emit JSON records")
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("--limit must be positive")
    path = Path(__file__).resolve().parents[1] / "catalogue" / "references.json"
    try:
        records = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        parser.error(f"Cannot read catalogue: {exc}")
    matches = [r for r in records
               if args.query.casefold() in r["citation_text"].casefold()
               and (args.reference is None or r["reference_number"] == args.reference)]
    shown = matches[:args.limit]
    if args.json:
        print(json.dumps({"matches": len(matches), "shown": len(shown), "records": shown},
                         indent=2, ensure_ascii=False))
    else:
        print(f"Showing {len(shown)} of {len(matches)} matching references")
        for record in shown:
            print(f"[{record['reference_number']}] {record['citation_text']}")
            print(f"  Survey page {record['source_page']}; extracted citation, not independently verified.\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
