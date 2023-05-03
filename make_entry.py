from entry import Word, RawEntry, Entry

def make_entry(obj):
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
        []
    )

