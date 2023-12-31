import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


@dataclass(init=True)
class StackMove:
    num_items: int
    from_stack: int
    to_stack: int


def parse_move(line: str) -> Optional[StackMove]:
    if line.startswith("move"):
        regex = re.match(r"move (\d+) from (\d+) to (\d+)", line)
        if regex is not None:
            return StackMove(*tuple(map(int, regex.groups())))
    return None


def parse_stack_level(line: str) -> List[str]:
    split_line: List[str] = []
    for i in range(0, len(line), 4):
        split_line.append(line[i : i + 3].strip("[] "))
    return split_line


def parse_stacks_and_moves(input_path: Path) -> Tuple[Dict[int, List[str]], List[StackMove]]:
    stacks: Dict[int, List[str]] = {}
    moves: List[StackMove] = []
    with open(input_path, mode="r") as fp:
        lines: List[str] = fp.readlines()
        stack_start: List[List[str]] = []
        for line in lines:
            move = parse_move(line)
            if move is not None:
                moves.append(move)
            elif not line.startswith("\n"):
                stack_start.append(parse_stack_level(line))

        stack_indices = stack_start.pop()
        for i in stack_indices:
            idx = int(i)
            stacks[idx] = [stack_level[idx - 1] for stack_level in stack_start if stack_level[idx - 1] != ""]
            stacks[idx].reverse()
    return stacks, moves


def solve_part_1(input_path: Optional[Path]) -> Any:
    if input_path is not None:
        stacks, moves = parse_stacks_and_moves(input_path)
        for move in moves:
            for _ in range(move.num_items):
                item = stacks[move.from_stack].pop()
                stacks[move.to_stack].append(item)
        top_of_stacks = [stacks[stack].pop() for stack in stacks]
        return "".join(top_of_stacks)


def solve_part_2(input_path: Optional[Path]) -> Any:
    if input_path is not None:
        stacks, moves = parse_stacks_and_moves(input_path)
        for move in moves:
            items = stacks[move.from_stack][-move.num_items : :]
            for _ in range(move.num_items):
                stacks[move.from_stack].pop()
            stacks[move.to_stack].extend(items)
        top_of_stacks = [stacks[stack].pop() for stack in stacks]
        return "".join(top_of_stacks)
