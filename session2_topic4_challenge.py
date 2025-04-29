"""
Session 2 - Topic 4
===================
Challenge: Build a Mini Bytecode Visualizer + Compare Constructs
"""

# =====================================
# Objective
# =====================================
"""
1. Build a mini bytecode visualizer function `viz(fn)` that:
   - Disassembles function `fn` using dis.Bytecode.
   - Tracks the stack effect of each instruction.
   - Prints:
       - Instruction offset
       - Opcode name
       - Immediate stack effect
       - Cumulative running stack depth

2. Define two Python functions:
   - One using a `for` loop
   - One using a `list comprehension`

3. Run `viz()` on both functions and compare:
   - Maximum stack depth
   - Total instruction count
   - Observations on bytecode differences

Optional:
- Highlight warnings if cumulative stack depth exceeds a threshold.
- Pretty-format the output (colorized or tabular) if you wish.
"""

# =====================================
# Imports
# =====================================
import dis

# =====================================
# 1. Function to Implement: viz(fn)
# =====================================

def viz(fn):
    """
    Disassembles the given function and prints instruction stack effects.

    Parameters:
    fn (function): Function to disassemble.

    Output:
    Prints each instruction along with stack effect and running depth.
    """
    depth = 0
    max_depth = 0

    print(f"\nDisassembly and Stack Trace for {fn.__name__}():")

    # Student to complete from here
    # ----------------------------------------
    # Hints:
    # - Use dis.Bytecode(fn)
    # - Loop through instructions
    # - Use dis.stack_effect(instr.opcode, instr.arg)
    # - Update depth
    # - Print nicely formatted output
    # - Track max_depth
    # ----------------------------------------
    pass

# =====================================
# 2. Define Two Example Functions
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
# 3. Analysis
# =====================================
"""
After completing viz(fn):

- Run viz(sum_with_for)
- Run viz(sum_with_listcomp)

Then answer:

- Which one had deeper maximum stack usage?
- Which one had fewer total bytecode instructions?
- Which is more efficient for large n?

(Hint: Generators and comprehensions may reduce peak stack depth.)
"""

# ===========================
# END OF CHALLENGE FILE
# ===========================

