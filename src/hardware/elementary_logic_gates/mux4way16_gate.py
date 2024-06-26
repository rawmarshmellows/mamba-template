from .mux16_gate import Mux16Gate, mux16_gate
from src.hardware.types.bits import Bits2, Bits16


def mux4way16_gate(
    a0: int,
    a1: int,
    a2: int,
    a3: int,
    a4: int,
    a5: int,
    a6: int,
    a7: int,
    a8: int,
    a9: int,
    a10: int,
    a11: int,
    a12: int,
    a13: int,
    a14: int,
    a15: int,
    b0: int,
    b1: int,
    b2: int,
    b3: int,
    b4: int,
    b5: int,
    b6: int,
    b7: int,
    b8: int,
    b9: int,
    b10: int,
    b11: int,
    b12: int,
    b13: int,
    b14: int,
    b15: int,
    c0: int,
    c1: int,
    c2: int,
    c3: int,
    c4: int,
    c5: int,
    c6: int,
    c7: int,
    c8: int,
    c9: int,
    c10: int,
    c11: int,
    c12: int,
    c13: int,
    c14: int,
    c15: int,
    d0: int,
    d1: int,
    d2: int,
    d3: int,
    d4: int,
    d5: int,
    d6: int,
    d7: int,
    d8: int,
    d9: int,
    d10: int,
    d11: int,
    d12: int,
    d13: int,
    d14: int,
    d15: int,
    sel0: int,
    sel1: int,
):
    ac_mux_result = mux16_gate(
        a0,
        a1,
        a2,
        a3,
        a4,
        a5,
        a6,
        a7,
        a8,
        a9,
        a10,
        a11,
        a12,
        a13,
        a14,
        a15,
        c0,
        c1,
        c2,
        c3,
        c4,
        c5,
        c6,
        c7,
        c8,
        c9,
        c10,
        c11,
        c12,
        c13,
        c14,
        c15,
        sel0,
    )
    bd_mux_result = mux16_gate(
        b0,
        b1,
        b2,
        b3,
        b4,
        b5,
        b6,
        b7,
        b8,
        b9,
        b10,
        b11,
        b12,
        b13,
        b14,
        b15,
        d0,
        d1,
        d2,
        d3,
        d4,
        d5,
        d6,
        d7,
        d8,
        d9,
        d10,
        d11,
        d12,
        d13,
        d14,
        d15,
        sel0,
    )

    return mux16_gate(
        ac_mux_result[0],
        ac_mux_result[1],
        ac_mux_result[2],
        ac_mux_result[3],
        ac_mux_result[4],
        ac_mux_result[5],
        ac_mux_result[6],
        ac_mux_result[7],
        ac_mux_result[8],
        ac_mux_result[9],
        ac_mux_result[10],
        ac_mux_result[11],
        ac_mux_result[12],
        ac_mux_result[13],
        ac_mux_result[14],
        ac_mux_result[15],
        bd_mux_result[0],
        bd_mux_result[1],
        bd_mux_result[2],
        bd_mux_result[3],
        bd_mux_result[4],
        bd_mux_result[5],
        bd_mux_result[6],
        bd_mux_result[7],
        bd_mux_result[8],
        bd_mux_result[9],
        bd_mux_result[10],
        bd_mux_result[11],
        bd_mux_result[12],
        bd_mux_result[13],
        bd_mux_result[14],
        bd_mux_result[15],
        sel1,
    )


class Mux4Way16Gate:
    def __init__(self):
        self.mux16_gate = Mux16Gate()

    def __call__(
        self, a: Bits16, b: Bits16, c: Bits16, d: Bits16, sel: Bits2
    ) -> Bits16:
        return self.mux16_gate(
            self.mux16_gate(a, c, sel[0]), self.mux16_gate(b, d, sel[0]), sel[1]
        )
