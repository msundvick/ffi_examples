import nimpy

proc run(): string {.exportpy.} =
    var a: float64 = 0
    for i in 0..1_000_000:
        a += (float64 (i mod 2)) + 0.5
    echo a
    return "Nim"