"""
Session 3 - Topic 4
===================
CHALLENGE: Time‑Machine Closure
Goal:
    Build a closure that keeps its own internal year and can:
    1) Jump forward/backward by delta years.
    2) Be manually reset via .set_year(new_year).

Fill in the TODO sections.
"""

def make_time_machine(start_year):
    year = start_year  # captured variable

    def jump(delta):
        """Advance or rewind time by *delta* years and return new year."""
        # TODO: declare nonlocal year, update year, return updated value
        raise NotImplementedError("Implement delta jumping")

    # Provide placeholder to avoid AttributeError in tests
    def set_year(new_year):
        raise NotImplementedError("Implement set_year once jump works")

    jump.set_year = set_year
    return jump


# -------------------------------------------------
# Simple tests (will raise NotImplementedError until you finish)
if __name__ == "__main__":
    tm = make_time_machine(2000)
    try:
        print("2005 expected ->", tm(5))
    except NotImplementedError:
        print("jump(delta) not yet implemented")
    try:
        tm.set_year(1990)
    except NotImplementedError:
        print("set_year(new_year) not yet implemented")
