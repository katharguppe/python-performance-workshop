"""
Session 2 - Topic 5
===================
Solution: Mini Bytecode Visualizer + Compare Constructs
"""

# =====================================
# Imports
# =====================================
import dis

# =====================================
# 1. Function: viz(fn)
# =====================================

def viz(fn):
    """
    Disassembles the given function and prints instruction stack effects,
    cumulative running depth, and maximum observed depth.
    """
    depth = 0
    max_depth = 0

    print(f"\nDisassembly and Stack Trace for {fn.__name__}()")
    print("="*60)
    print(f"{'Offset':<8} {'Opcode':<25} {'Effect':<8} {'Depth after'}")
    print("-"*60)

    for instr in dis.Bytecode(fn):
        try:
            effect = dis.stack_effect(instr.opcode, instr.arg, jump=False)
        except TypeError:
            # Some opcodes have optional args
            effect = dis.stack_effect(instr.opcode, jump=False)
        
        depth += effect
        max_depth = max(max_depth, depth)

        print(f"{instr.offset:<8} {instr.opname:<25} {effect:+8} {depth:>10}")

    print("="*60)
    print(f"Max stack depth reached during execution: {max_depth}")
    print(f"Total instructions: {len(list(dis.Bytecode(fn)))}\n")

# =====================================
# 2. Define Example Functions
# =====================================

# Example 1: For Loop Sum
def sum_with_for(n):
    total = 0
    for i in range(n):
        total += i*i
    return total

# Example 2: List Comprehension Sum
def sum_with_listcomp(n):
    return sum([i*i for i in range(n)])

# =====================================
# 3. Run Visualization
# =====================================

# Visualize for both functions
viz(sum_with_for)
viz(sum_with_listcomp)

# =====================================
# 4. Observations
# =====================================
"""
Observations:

- List comprehension introduces a few extra instructions
  (LIST_APPEND, BUILD_LIST), which temporarily increase stack usage.

- for-loop is slightly deeper at peak because it maintains:
    - loop counter
    - accumulator
    - loop bounds

- List comprehension benefits from internal optimizations in BUILD_LIST
  but materializes the whole list at once (memory tradeoff).

- In large data cases, generator expressions would beat both,
  but here list comprehension is somewhat bytecode denser.

- Stack effects correspond precisely to expected pushes/pops:
    LOAD_FAST → push
    BINARY_OP → pop2 push1
    RETURN_VALUE → pop1
"""

# ===========================
# END OF SOLUTION FILE
# ===========================

