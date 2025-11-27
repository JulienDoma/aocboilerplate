#!/usr/bin/env python3
import sys
from pathlib import Path
from aoc_input.input import get_data


def main():
    if len(sys.argv) != 3:
        print("Usage: create_day.py <year> <day>")
        sys.exit(1)

    year = int(sys.argv[1])
    day = int(sys.argv[2])

    root = Path(__file__).resolve().parent.parent

    year_dir = root / str(year)
    year_dir.mkdir(parents=True, exist_ok=True)

    inputs_dir = year_dir / "inputs"
    inputs_dir.mkdir(parents=True, exist_ok=True)

    # -------------------------
    # Create TXT file
    # -------------------------
    input_path = inputs_dir / f"day{day}.txt"

    if not input_path.exists():
        print(f"Fetching input for {year} day {day}...")
        data = get_data(year, day)
        input_path.write_text("\n".join(data))
        print(f"Created: {input_path}")
    else:
        print(f"Input already exists: {input_path}")

    # -------------------------
    # Create PYTHON file
    # -------------------------
    py_file = year_dir / f"day{day}.py"

    if not py_file.exists():
        py_file.write_text(
            f"""def part1(data):
    pass


def part2(data):
    pass


if __name__ == "__main__":
    from pathlib import Path

    input_file = Path(__file__).parent / "inputs" / "day{day}.txt"
    data = input_file.read_text().splitlines()
    if len(data) == 1:
        data = data[0]

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
"""
        )
        print(f"Created: {py_file}")
    else:
        print(f"Python file already exists: {py_file}")


if __name__ == "__main__":
    main()
