"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

NUM_CHECK_ROUNDS = ...

@dataclass
class MonkeyTest:
    divisor: int
    true_recipient: Optional[int] = ...
    false_recipient: Optional[int] = ...
    def execute(self, worry_level: int) -> int: ...

@dataclass
class Monkey:
    starting_items: List[int] = ...
    operation: Optional[Operation] = ...
    test: Optional[MonkeyTest] = ...

@dataclass
class OperatorWrapper:
    char: str
    func: Callable[[int, int], int]
    ...

class Operator(Enum):
    ADD = ...
    MULTIPLY = ...
    @staticmethod
    def from_char(char: str) -> Optional[Operator]: ...

class Operation:
    def __init__(self, operator: Operator, operand: Optional[int] = ...) -> None: ...
    def execute(self, old: int) -> int: ...

def parse_monkeys(input_path: Path) -> List[Monkey]: ...
def do_inspection_rounds(monkeys: List[Monkey], num_rounds: int, worry_level_function: Callable[[int], int]) -> Dict[int, int]: ...
def solve_part_1(input_path: Optional[Path]) -> Any: ...
def solve_part_2(input_path: Optional[Path]) -> Any: ...
