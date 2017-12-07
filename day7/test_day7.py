from day7 import parse_input_line

def test_parse_input_line_no_children():
    line = "pbga (66)"

    expected_name = "pbga"
    expected_weight = 66
    expected_child_programs = list()

    actual_program_record = parse_input_line(line)

    assert expected_name == actual_program_record.name
    assert expected_weight == actual_program_record.weight
    assert expected_child_programs == actual_program_record.child_program_names


def test_parse_input_line_with_children():
    line = "fwft (72) -> ktlj, cntj, xhth"

    expected_name = "fwft"
    expected_weight = 72
    expected_child_programs = ["ktlj", "cntj", "xhth"]

    actual_program_record = parse_input_line(line)
    print(actual_program_record.child_program_names)

    assert expected_name == actual_program_record.name
    assert expected_weight == actual_program_record.weight
    assert expected_child_programs == actual_program_record.child_program_names
