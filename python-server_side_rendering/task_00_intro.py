import os
import logging

def generate_invitations(template, attendees):
    """Generate invitation files from a template and attendee list."""
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    # Type checks
    if not isinstance(template, str):
        logging.error(f"Invalid template type: expected str, got {type(template).__name__}")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        logging.error("Invalid attendees type: expected list of dicts.")
        return

    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.info("No data provided, no output files generated.")
        return

    fields = ["name", "event_title", "event_date", "event_location"]

    for idx, guest in enumerate(attendees, 1):
        content = template
        for field in fields:
            value = guest.get(field)
            if value is None:
                value = "N/A"
            content = content.replace(f"{{{field}}}", str(value))
        filename = f"output_{idx}.txt"
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            logging.error(f"Error writing file {filename}: {e}")
