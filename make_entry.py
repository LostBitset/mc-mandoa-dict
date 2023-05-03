from entry import Word, RawEntry, Entry

def make_entry(obj):
    examples = []
    if "Examples" in obj:
        examples = obj["Examples"]
    return Entry(
        obj["type"],
        RawEntry({
            "english": Word(
                obj["e"],
                None
            ),
            "mando'a": Word(
                obj["m"],
                obj["p"]
            )
        }),
        [
            RawEntry({
                "english": Word(
                    example["eng"],
                    None
                ),
                "mando'a": Word(
                    example["mandoa"],
                    None
                )
            })
            for example in examples
        ]
    )

