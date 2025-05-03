# -*- coding: utf-8 -*-
"""Generators vs. Lists


Original file is located at
    https://colab.research.google.com/drive/10iY9tdAq_G25IGyM0WFImyvTOsMnR9PI
"""

"""
Day 3, Session 1, Topic 2: Generators vs. Lists

This file focuses specifically on the comparison between generators and lists in Python,
explaining their differences, advantages, disadvantages, and use cases.
"""

# 2. Generators vs. Lists
# ---------------------------------------
# Concept:
#    -   Lists: Store all elements in memory at once.
#    -   Generators: A special type of iterator, created using a function with
#        the `yield` keyword or a generator expression, that produces values on
#        demand.
#
# Why is it important?
#    -   Memory Efficiency: Generators are much more memory-efficient than lists,
#        especially for large sequences.
#    -   Lazy Evaluation: Generators produce values on demand, avoiding
#        unnecessary computations.
#    -   Performance: For large datasets, using generators can significantly
#        improve performance by reducing memory usage and computation time.
#
# Internal Implementation:
#    -   Lists: Internally, Python lists are implemented as dynamic arrays.
#        They store pointers to the actual data elements, allowing for efficient
#        random access. The memory occupied by a list is contiguous.
#    -   Generators:
#        -   When a generator function is called, it doesn't execute the
#            function body immediately. Instead, it returns a generator object.
#        -   The generator object's `__next__` method resumes the function's
#            execution from the last `yield` statement.
#        -   The state of the function (local variables, instruction pointer)
#            is saved between calls to `__next__`. This is typically implemented
#            using frame objects in CPython.
#        -   Generator expressions are implemented similarly, creating a
#            generator object that evaluates an expression lazily.
#
# How to Use:
#    -   Lists: Create them using square brackets `[]` or the `list()`
#        constructor.
#    -   Generators: Define a function with `yield` statements or use a
#        generator expression `(expr for var in iterable)`.
#
# How it Works:
#    -   Lists:
#        -   Elements are stored in a contiguous block of memory.
#        -   Accessing an element by index is very fast (O(1)).
#        -   Appending to the end is usually fast (amortized O(1)), but
#            inserting or deleting in the middle is slow (O(n)).
#    -   Generators:
#        -   Generator functions use the `yield` keyword to return a value
#            and pause execution.
#        -   Each time `__next__` is called on the generator, execution
#            resumes from where it left off until the next `yield` or the
#            end of the function.
#
# When Not to Use:
#    -   Lists: Use when you need to store a collection of items and access
#        them frequently by index, and when the size of the collection is
#        relatively small. Avoid for very large datasets where memory usage
#        is a concern.
#    -   Generators: Use when you need to create iterators in a concise and
#        readable way, especially for large or infinite sequences, or when
#        you want to process items one at a time. If you need a simple in-memory container and/or need to modify the container, a list is fine.
#
# Example:
import sys

def list_example():
    """Demonstrates using lists."""
    my_list = [1, 2, 3, 4, 5]
    print("List:", my_list)
    print("Memory size of list:", sys.getsizeof(my_list), "bytes")

def generator_example():
    """Demonstrates using generators."""
    def my_generator(n):
        """A generator function."""
        for i in range(n):
            yield i * 2

    my_gen = my_generator(5)
    print("Generator:", my_gen)
    print("Memory size of generator:", sys.getsizeof(my_gen), "bytes")

    print("Iterating through the generator:")
    for item in my_gen:
        print(item)

def compare_memory_usage(n):
    """
    Compares the memory usage of a list and a generator for a given range.
    """
    # Create a list
    list_data = list(range(n))
    list_memory = sys.getsizeof(list_data)
    print(f"Memory used by list of size {n}: {list_memory} bytes")

    # Create a generator
    def gen_generator(n):
        for i in range(n):
            yield i
    generator_data = gen_generator(n)
    generator_memory = sys.getsizeof(generator_data)
    print(f"Memory used by generator of size {n}: {generator_memory} bytes")
    print(f"The generator is {list_memory/generator_memory} times smaller than the list for {n} elements")


list_example()
generator_example()
compare_memory_usage(10)
compare_memory_usage(1000)
compare_memory_usage(100000) #Examine the difference when the number of elements increases.