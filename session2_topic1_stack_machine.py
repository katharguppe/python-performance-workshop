"""
Session 2 - Topic 1
===================
Bytecode, dis module, Stack Machine Architecture - DEEP DIVE
"""

# =====================================
# 1. Why Python uses a Stack Machine
# =====================================
"""
- Simplicity: Stack machines are easier to implement compared to register machines.
- Portability: No assumptions about CPU register layout; everything pushes/pops from virtual stack.
- Matching recursive structure: Python functions and expressions naturally map to stack operations.
- Historical: First interpreters (Forth, Java VM, Python) all preferred stack models for simplicity.

In CPython:
    - Each opcode operates on the value stack (`f_valuestack` inside PyFrameObject)
    - No registers. Stack-based manipulation means instructions are very compact.
"""

# =====================================
# 2. Basic Structure of Python Bytecode
# =====================================
"""
Python 3.6+ uses a "wordcode" format:
    - 1 byte for opcode
    - 1 byte for oparg (optional argument)
    (Earlier Python versions used a different layout)

Internally:
    - The eval loop reads 2 bytes at a time: opcode + oparg
    - EXTENDED_ARG is used to form 32-bit arguments if needed

Disassembling reveals this structure neatly.
"""

import dis
import sys

# Example function to disassemble
def sample_function(x, y):
    return (x + 1) * y

# Inspect code object
print(dis.code_info(sample_function))

# Disassemble using dis
print("\nDisassembly of sample_function:")
dis.dis(sample_function)

# =====================================
# 3. Using the dis Module Properly
# =====================================
"""
Useful dis functions:
- dis.dis(obj)          : Pretty disassembly to stdout
- dis.Bytecode(obj)     : Iterable Bytecode object
- dis.stack_effect(op, arg) : Predicts stack effect of an opcode

Every instruction (`Instruction`) object has:
- opname: mnemonic (e.g., 'LOAD_FAST')
- opcode: integer value
- arg: argument integer (may be None)
- argval: resolved argument (constant value, variable name)
- is_jump_target: bool
"""

print("\nDetailed dis.Bytecode output:")
for instr in dis.Bytecode(sample_function):
    print(instr)

# =====================================
# 4. Understanding Stack Behavior
# =====================================
"""
Python's evaluation pushes/pops operands to/from a virtual stack.

Example:
    - LOAD_FAST x   → push x onto stack
    - LOAD_CONST 1  → push 1 onto stack
    - BINARY_ADD    → pop 2 values, add, push result
    - LOAD_FAST y   → push y
    - BINARY_MULTIPLY → pop 2 values, multiply, push result
    - RETURN_VALUE → pop return value

Use dis.stack_effect() to predict stack depth changes.
"""

print("\nStack Effects of Each Instruction:")
depth = 0
max_depth = 0
for instr in dis.Bytecode(sample_function):
    effect = dis.stack_effect(instr.opcode, instr.arg)
    depth += effect
    max_depth = max(max_depth, depth)
    print(f"{instr.opname:<20} stack_effect={effect:+} depth_now={depth}")
print(f"Maximum stack depth during execution: {max_depth}")

# =====================================
# 5. Internals: CPython Source Snippets
# =====================================
"""
In CPython's ceval.c:

while (1) {
    opcode = NEXTOP();
    oparg = NEXTARG();
    switch(opcode) {
        case LOAD_FAST:
            PUSH(f->localsplus[oparg]);
            break;
        case BINARY_ADD:
            right = POP();
            left = TOP();
            SET_TOP(left + right);
            DECREF(right);
            break;
        ...
    }
}

Each opcode manipulates the virtual stack explicitly.

TARGET(opcode) macros expand into C case labels.
"""

# =====================================
# 6. When Disassembly Matters (and When It Doesn't)
# =====================================
"""
- Matters:
    - When diagnosing slow paths (e.g., attribute lookup, globals access)
    - When tuning critical loops (e.g., choosing generator vs list comp)
    - When reverse engineering code behavior without source

- Doesn't Matter:
    - For general readability or maintainability — prefer clean Python code first.
    - For minor performance differences outside hot loops.
"""

# ===========================
# END OF TOPIC 1
# ===========================

