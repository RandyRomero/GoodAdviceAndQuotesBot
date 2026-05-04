from get_random_note_bot.bot.repository import Entities

def _format_note(note_from_db: str) -> str:
    """Format a note from the database."""
    note = note_from_db["note"]
    topic = note_from_db["topic"]
    author = note_from_db["author"]
    info = note_from_db["info"]
    formatted_note = f"Note: {note}\nTopic: {topic}\nAuthor: {author}"
    if info:
        formatted_note = f"{formatted_note}\nAdditional info: {info}"
    return formatted_note

async def get_a_random_note(entities: Entities) -> str:
    """Get a formatted string with a random note."""
    random_note = await entities.notes.get_random_one()
    return _format_note(random_note)


async def get_be_relentless_note(entities: Entities) -> str:
    """Get a formatted string with a Be Relentless note."""
    be_relentless_note = await entities.notes.get_be_relentless_note()
    return _format_note(be_relentless_note)