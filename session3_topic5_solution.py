"""
Session 3 - Topic 5
===================
SOLUTION: Time‑Machine Closure
"""

def make_time_machine(start_year):
    year = start_year  # captured via closure

    def jump(delta):
        nonlocal year
        year += delta
        return year

    def set_year(new_year):
        nonlocal year
        year = new_year

    jump.set_year = set_year
    return jump


# Demo tests
if __name__ == "__main__":
    tm = make_time_machine(2000)
    print("Expect 2005 ->", tm(5))
    print("Expect 2002 ->", tm(-3))
    tm.set_year(1990)
    print("Expect 1991 ->", tm(1))
