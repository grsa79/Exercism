"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record : tuple) -> str:
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    return record[-1]


def convert_coordinate(coordinate: str) -> tuple:
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    return tuple(coordinate)


def compare_records(azara_record: tuple, rui_record: tuple) -> bool:
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    if convert_coordinate(get_coordinate(azara_record)) == rui_record[1]: return True
    return False


def create_record(azara_record: tuple, rui_record: tuple) -> tuple:
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    if compare_records(azara_record, rui_record):
        return tuple([azara_record[0], azara_record[1], rui_record[0], rui_record[1], rui_record[2]])
    return "not a match"


def clean_up(combined_record_group : tuple) -> str:
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    report = ""
    for item in combined_record_group:
        line = tuple([item[0], item[2], item[3], item[4]])
        report = report +  str(line) + "\n"
    return report

    
def test_clean_up():
    record = create_record(("Tres", "1A"), ("loc", ("1", "A"),"quad"))
    record2 = create_record(("Tres2", "2A"), ("loc2", ("2", "A"),"quad2") )
    return clean_up((record, record2))