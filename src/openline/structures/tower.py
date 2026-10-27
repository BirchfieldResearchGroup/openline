"""A lattice tower, by its parts."""

from dataclasses import replace

from openline.types.materials import Steel
from openline.types.structures import Ground, LineAngle, LowestCrossarm, Tower
from openline.types.structures.attachments import (
    DiscString,
    Hold,
    InsulatorString,
    Mount,
    Wire,
    WirePosition,
)
from openline.types.structures.geometry import Face, Point
from openline.types.structures.members import Bar, Role, Truss
from openline.types.structures.panels import (
    Base,
    Body,
    Bracing,
    Crossarm,
    Edge,
    Head,
    Leg,
    Panel,
    PanelRun,
    Peak,
)
from openline.types.units import degrees, ft_in, kv, m, mm


def _a_2_d_2004_4_we_wadiff_100() -> Tower[LowestCrossarm]:
    """A-2-D-2004.4 WE WAdiff 100: each joint written once, by its key."""
    j001 = Point(m(-0.08), m(0), m(12.5))
    j002 = Point(m(0), m(0), m(12.5))
    j003 = Point(m(0.09), m(0), m(12.5))
    j004 = Point(m(0.21), m(0), m(11.47))
    j005 = Point(m(-0.25), m(0), m(10.97))
    j006 = Point(m(0.32), m(0), m(10.52))
    j007 = Point(m(-0.37), m(0), m(9.92))
    j008 = Point(m(0.48), m(0), m(9.06))
    j009 = Point(m(-0.59), m(0), m(8.04))
    j010 = Point(m(0.72), m(0), m(6.95))
    j011 = Point(m(-0.87), m(0), m(5.56))
    j012 = Point(m(0), m(0), m(5.56))
    j013 = Point(m(0.88), m(0), m(5.56))
    j014 = Point(m(-0.87), m(0), m(5.24))
    j015 = Point(m(0), m(0), m(5.24))
    j016 = Point(m(0.88), m(0), m(5.24))
    j017 = Point(m(-3.67), m(0), m(5.07))
    j018 = Point(m(3.66), m(0), m(5.07))
    j019 = Point(m(-2.32), m(0), m(4.86))
    j020 = Point(m(-4.88), m(0), m(4.85))
    j021 = Point(m(2.33), m(0), m(4.85))
    j022 = Point(m(4.87), m(0), m(4.85))
    j023 = Point(m(-6.91), m(0), m(4.49))
    j024 = Point(m(6.91), m(0), m(4.49))
    j025 = Point(m(-7.4), m(0), m(4.41))
    j026 = Point(m(7.39), m(0), m(4.41))
    j027 = Point(m(-7.4), m(0), m(4.2))
    j028 = Point(m(-6.91), m(0), m(4.2))
    j029 = Point(m(-6.17), m(0), m(4.2))
    j030 = Point(m(-4.88), m(0), m(4.2))
    j031 = Point(m(-3.66), m(0), m(4.2))
    j032 = Point(m(-2.32), m(0), m(4.2))
    j033 = Point(m(-0.97), m(0), m(4.2))
    j034 = Point(m(-0.92), m(0), m(4.2))
    j035 = Point(m(0.93), m(0), m(4.2))
    j036 = Point(m(0.97), m(0), m(4.2))
    j037 = Point(m(2.32), m(0), m(4.2))
    j038 = Point(m(3.67), m(0), m(4.2))
    j039 = Point(m(4.88), m(0), m(4.2))
    j040 = Point(m(6.18), m(0), m(4.2))
    j041 = Point(m(6.9), m(0), m(4.2))
    j042 = Point(m(7.4), m(0), m(4.2))
    j043 = Point(m(-7.15), m(0), m(4.2))
    j044 = Point(m(7.15), m(0), m(4.2))
    j045 = Point(m(-0.96), m(0), m(3.36))
    j046 = Point(m(0.97), m(0), m(3.36))
    j047 = Point(m(-1.02), m(0), m(2.24))
    j048 = Point(m(1.02), m(0), m(2.24))
    j049 = Point(m(-1.04), m(0), m(1.7))
    j050 = Point(m(1.05), m(0), m(1.7))
    j051 = Point(m(-1.07), m(0), m(1.13))
    j052 = Point(m(1.08), m(0), m(1.13))
    j053 = Point(m(-4.2), m(0), m(1.06))
    j054 = Point(m(4.2), m(0), m(1.06))
    j055 = Point(m(-2.67), m(0), m(0.83))
    j056 = Point(m(2.67), m(0), m(0.83))
    j057 = Point(m(-6.27), m(0), m(0.76))
    j058 = Point(m(6.28), m(0), m(0.76))
    j059 = Point(m(-9.8), m(0), m(0.26))
    j060 = Point(m(9.81), m(0), m(0.26))
    j061 = Point(m(-10.4), m(0), m(0.17))
    j062 = Point(m(10.4), m(0), m(0.17))
    j063 = Point(m(-1.13), m(0), m(0.01))
    j064 = Point(m(1.13), m(0), m(0.01))
    j065 = Point(m(-10.1), m(0), m(0))
    j066 = Point(m(10.1), m(0), m(0))
    j067 = Point(m(-10.4), m(0), m(0))
    j068 = Point(m(-9.8), m(0), m(0))
    j069 = Point(m(-8.82), m(0), m(0))
    j070 = Point(m(-6.27), m(0), m(0))
    j071 = Point(m(-4.2), m(0), m(0))
    j072 = Point(m(-2.67), m(0), m(0))
    j073 = Point(m(-1.26), m(0), m(0))
    j074 = Point(m(1.26), m(0), m(0))
    j075 = Point(m(2.67), m(0), m(0))
    j076 = Point(m(4.2), m(0), m(0))
    j077 = Point(m(6.28), m(0), m(0))
    j078 = Point(m(8.83), m(0), m(0))
    j079 = Point(m(9.81), m(0), m(0))
    j080 = Point(m(10.4), m(0), m(0))
    j081 = Point(m(-1.19), m(0), m(-1.22))
    j082 = Point(m(1.19), m(0), m(-1.22))
    j083 = Point(m(-1.25), m(0), m(-2.45))
    j084 = Point(m(1.25), m(0), m(-2.45))
    j085 = Point(m(-1.33), m(0), m(-4.04))
    j086 = Point(m(1.33), m(0), m(-4.04))
    j087 = Point(m(-1.41), m(0), m(-5.7))
    j088 = Point(m(1.41), m(0), m(-5.7))
    j089 = Point(m(-1.5), m(0), m(-7.54))
    j090 = Point(m(1.5), m(0), m(-7.54))
    j091 = Point(m(-0.75), m(0), m(-8.37))
    j092 = Point(m(0.76), m(0), m(-8.37))
    j093 = Point(m(-1.58), m(0), m(-9.19))
    j094 = Point(m(0), m(0), m(-9.19))
    j095 = Point(m(1.58), m(0), m(-9.19))
    j096 = Point(m(-0.78), m(0), m(-10.06))
    j097 = Point(m(0.84), m(0), m(-10.11))
    j098 = Point(m(-1.67), m(0), m(-11.03))
    j099 = Point(m(1.67), m(0), m(-11.03))
    j100 = Point(m(-1.78), m(0), m(-11.66))
    j101 = Point(m(-0.84), m(0), m(-11.66))
    j102 = Point(m(0.84), m(0), m(-11.66))
    j103 = Point(m(1.78), m(0), m(-11.66))
    j104 = Point(m(-1.88), m(0), m(-12.29))
    j105 = Point(m(0), m(0), m(-12.29))
    j106 = Point(m(1.88), m(0), m(-12.29))
    j107 = Point(m(-2.01), m(0), m(-13.08))
    j108 = Point(m(-1.04), m(0), m(-13.08))
    j109 = Point(m(1.04), m(0), m(-13.08))
    j110 = Point(m(2.01), m(0), m(-13.08))
    j111 = Point(m(-2.08), m(0), m(-13.86))
    j112 = Point(m(2.08), m(0), m(-13.86))
    j113 = Point(m(-2.32), m(0), m(-14.91))
    j114 = Point(m(-1.04), m(0), m(-14.91))
    j115 = Point(m(1.04), m(0), m(-14.91))
    j116 = Point(m(2.32), m(0), m(-14.91))
    j117 = Point(m(-2.49), m(0), m(-15.93))
    j118 = Point(m(2.49), m(0), m(-15.93))
    j119 = Point(m(-2.65), m(0), m(-16.9))
    j120 = Point(m(-0.92), m(0), m(-16.9))
    j121 = Point(m(0.92), m(0), m(-16.9))
    j122 = Point(m(2.65), m(0), m(-16.9))
    j123 = Point(m(-2.78), m(0), m(-17.71))
    j124 = Point(m(-1.72), m(0), m(-17.71))
    j125 = Point(m(1.72), m(0), m(-17.71))
    j126 = Point(m(2.78), m(0), m(-17.71))
    j127 = Point(m(-3), m(0), m(-19))
    j128 = Point(m(3), m(0), m(-19))
    return Tower(
        name="A-2-D-2004.4 WE WAdiff 100",
        datum=LowestCrossarm((m(19), m(25), m(29))),
        voltages=(),
        line_angles=(),
        attachments=(
            Mount(Wire.SHIELD, Point(m(0), m(0), m(12.5)), Hold.CLAMP),
            Mount(Wire.PHASE, Point(m(-7.15), m(0), m(4.2)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(7.15), m(0), m(4.2)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-10.1), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-4.2), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(4.2), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(10.1), m(0), m(0)), Hold.STRAIN),
        ),
        bases=(),
        body=(
            Body(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j120, j115, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j114, role=Role.DIAGONAL_BRACE),
                        Bar(j118, j117, role=Role.TRANSVERSE_BRACE),
                        Bar(j034, j035, role=Role.TRANSVERSE_BRACE),
                        Bar(j063, j064, role=Role.TRANSVERSE_BRACE),
                        Bar(j049, j050, role=Role.TRANSVERSE_BRACE),
                        Bar(j084, j085, role=Role.DIAGONAL_BRACE),
                        Bar(j085, j088, role=Role.DIAGONAL_BRACE),
                        Bar(j088, j089, role=Role.DIAGONAL_BRACE),
                        Bar(j090, j087, role=Role.DIAGONAL_BRACE),
                        Bar(j087, j086, role=Role.DIAGONAL_BRACE),
                        Bar(j086, j083, role=Role.DIAGONAL_BRACE),
                        Bar(j093, j094, role=Role.TRANSVERSE_BRACE),
                        Bar(j094, j095, role=Role.TRANSVERSE_BRACE),
                        Bar(j099, j097, role=Role.DIAGONAL_BRACE),
                        Bar(j097, j094, role=Role.DIAGONAL_BRACE),
                        Bar(j094, j091, role=Role.DIAGONAL_BRACE),
                        Bar(j091, j089, role=Role.DIAGONAL_BRACE),
                        Bar(j098, j096, role=Role.DIAGONAL_BRACE),
                        Bar(j096, j094, role=Role.DIAGONAL_BRACE),
                        Bar(j094, j092, role=Role.DIAGONAL_BRACE),
                        Bar(j092, j090, role=Role.DIAGONAL_BRACE),
                        Bar(j091, j093, role=Role.DIAGONAL_BRACE),
                        Bar(j093, j096, role=Role.DIAGONAL_BRACE),
                        Bar(j092, j095, role=Role.DIAGONAL_BRACE),
                        Bar(j095, j097, role=Role.DIAGONAL_BRACE),
                        Bar(j105, j101, role=Role.DIAGONAL_BRACE),
                        Bar(j108, j105, role=Role.DIAGONAL_BRACE),
                        Bar(j105, j104, role=Role.TRANSVERSE_BRACE),
                        Bar(j098, j093, role=Role.CHORD),
                        Bar(j093, j089, role=Role.CHORD),
                        Bar(j089, j087, role=Role.CHORD),
                        Bar(j087, j085, role=Role.CHORD),
                        Bar(j085, j083, role=Role.CHORD),
                        Bar(j083, j081, role=Role.CHORD),
                        Bar(j081, j063, role=Role.CHORD),
                        Bar(j064, j081, role=Role.DIAGONAL_BRACE),
                        Bar(j081, j084, role=Role.DIAGONAL_BRACE),
                        Bar(j084, j086, role=Role.CHORD),
                        Bar(j086, j088, role=Role.CHORD),
                        Bar(j088, j090, role=Role.CHORD),
                        Bar(j090, j095, role=Role.CHORD),
                        Bar(j095, j099, role=Role.CHORD),
                        Bar(j063, j082, role=Role.DIAGONAL_BRACE),
                        Bar(j082, j083, role=Role.DIAGONAL_BRACE),
                        Bar(j063, j051, role=Role.CHORD),
                        Bar(j051, j049, role=Role.CHORD),
                        Bar(j049, j047, role=Role.CHORD),
                        Bar(j047, j045, role=Role.CHORD),
                        Bar(j045, j034, role=Role.CHORD),
                        Bar(j034, j014, role=Role.CHORD),
                        Bar(j016, j035, role=Role.CHORD),
                        Bar(j035, j046, role=Role.CHORD),
                        Bar(j046, j048, role=Role.CHORD),
                        Bar(j048, j050, role=Role.CHORD),
                        Bar(j050, j052, role=Role.CHORD),
                        Bar(j052, j064, role=Role.CHORD),
                        Bar(j064, j082, role=Role.CHORD),
                        Bar(j082, j084, role=Role.CHORD),
                        Bar(j013, j034, role=Role.DIAGONAL_BRACE),
                        Bar(j034, j046, role=Role.DIAGONAL_BRACE),
                        Bar(j064, j051, role=Role.DIAGONAL_BRACE),
                        Bar(j051, j048, role=Role.DIAGONAL_BRACE),
                        Bar(j048, j045, role=Role.DIAGONAL_BRACE),
                        Bar(j045, j035, role=Role.DIAGONAL_BRACE),
                        Bar(j035, j011, role=Role.DIAGONAL_BRACE),
                        Bar(j063, j052, role=Role.DIAGONAL_BRACE),
                        Bar(j052, j047, role=Role.DIAGONAL_BRACE),
                        Bar(j047, j046, role=Role.DIAGONAL_BRACE),
                        Bar(j011, j012, role=Role.TRANSVERSE_BRACE),
                        Bar(j012, j013, role=Role.TRANSVERSE_BRACE),
                        Bar(j015, j012, role=Role.TRANSVERSE_BRACE),
                        Bar(j014, j011, role=Role.TRANSVERSE_BRACE),
                        Bar(j016, j013, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        legs=(
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j127, j123, role=Role.CHORD),
                        Bar(j123, j119, role=Role.CHORD),
                        Bar(j119, j117, role=Role.CHORD),
                        Bar(j117, j113, role=Role.CHORD),
                        Bar(j113, j107, role=Role.CHORD),
                        Bar(j107, j104, role=Role.CHORD),
                        Bar(j104, j100, role=Role.CHORD),
                        Bar(j100, j098, role=Role.CHORD),
                        Bar(j127, j124, role=Role.DIAGONAL_BRACE),
                        Bar(j124, j120, role=Role.DIAGONAL_BRACE),
                        Bar(j114, j111, role=Role.DIAGONAL_BRACE),
                        Bar(j120, j119, role=Role.TRANSVERSE_BRACE),
                        Bar(j124, j123, role=Role.TRANSVERSE_BRACE),
                        Bar(j114, j113, role=Role.TRANSVERSE_BRACE),
                        Bar(j124, j119, role=Role.DIAGONAL_BRACE),
                        Bar(j120, j117, role=Role.DIAGONAL_BRACE),
                        Bar(j117, j114, role=Role.DIAGONAL_BRACE),
                        Bar(j101, j098, role=Role.DIAGONAL_BRACE),
                        Bar(j111, j108, role=Role.DIAGONAL_BRACE),
                        Bar(j104, j101, role=Role.DIAGONAL_BRACE),
                        Bar(j104, j108, role=Role.DIAGONAL_BRACE),
                        Bar(j107, j108, role=Role.TRANSVERSE_BRACE),
                        Bar(j100, j101, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j099, j103, role=Role.CHORD),
                        Bar(j103, j106, role=Role.CHORD),
                        Bar(j106, j110, role=Role.CHORD),
                        Bar(j110, j116, role=Role.CHORD),
                        Bar(j116, j118, role=Role.CHORD),
                        Bar(j118, j122, role=Role.CHORD),
                        Bar(j122, j126, role=Role.CHORD),
                        Bar(j126, j128, role=Role.CHORD),
                        Bar(j115, j112, role=Role.DIAGONAL_BRACE),
                        Bar(j128, j125, role=Role.DIAGONAL_BRACE),
                        Bar(j125, j121, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j122, role=Role.TRANSVERSE_BRACE),
                        Bar(j125, j126, role=Role.TRANSVERSE_BRACE),
                        Bar(j115, j116, role=Role.TRANSVERSE_BRACE),
                        Bar(j125, j122, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j118, role=Role.DIAGONAL_BRACE),
                        Bar(j118, j115, role=Role.DIAGONAL_BRACE),
                        Bar(j112, j109, role=Role.DIAGONAL_BRACE),
                        Bar(j109, j105, role=Role.DIAGONAL_BRACE),
                        Bar(j105, j102, role=Role.DIAGONAL_BRACE),
                        Bar(j102, j099, role=Role.DIAGONAL_BRACE),
                        Bar(j106, j105, role=Role.TRANSVERSE_BRACE),
                        Bar(j102, j106, role=Role.DIAGONAL_BRACE),
                        Bar(j106, j109, role=Role.DIAGONAL_BRACE),
                        Bar(j102, j103, role=Role.TRANSVERSE_BRACE),
                        Bar(j109, j110, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        head=(),
        crossarms=(
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j027, j043, role=Role.CHORD),
                        Bar(j043, j028, role=Role.CHORD),
                        Bar(j028, j029, role=Role.CHORD),
                        Bar(j029, j030, role=Role.CHORD),
                        Bar(j030, j031, role=Role.CHORD),
                        Bar(j031, j032, role=Role.CHORD),
                        Bar(j032, j033, role=Role.CHORD),
                        Bar(j033, j034, role=Role.CHORD),
                        Bar(j025, j023, role=Role.CHORD),
                        Bar(j023, j020, role=Role.CHORD),
                        Bar(j020, j017, role=Role.CHORD),
                        Bar(j017, j011, role=Role.CHORD),
                        Bar(j025, j027, role=Role.CHORD),
                        Bar(j023, j028, role=Role.TRANSVERSE_BRACE),
                        Bar(j033, j019, role=Role.DIAGONAL_BRACE),
                        Bar(j019, j032, role=Role.TRANSVERSE_BRACE),
                        Bar(j017, j031, role=Role.TRANSVERSE_BRACE),
                        Bar(j031, j019, role=Role.DIAGONAL_BRACE),
                        Bar(j019, j011, role=Role.DIAGONAL_BRACE),
                        Bar(j030, j020, role=Role.TRANSVERSE_BRACE),
                        Bar(j020, j031, role=Role.DIAGONAL_BRACE),
                        Bar(j020, j029, role=Role.DIAGONAL_BRACE),
                        Bar(j029, j023, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j035, j036, role=Role.CHORD),
                        Bar(j036, j037, role=Role.CHORD),
                        Bar(j037, j038, role=Role.CHORD),
                        Bar(j038, j039, role=Role.CHORD),
                        Bar(j039, j040, role=Role.CHORD),
                        Bar(j040, j041, role=Role.CHORD),
                        Bar(j041, j044, role=Role.CHORD),
                        Bar(j044, j042, role=Role.CHORD),
                        Bar(j042, j026, role=Role.CHORD),
                        Bar(j026, j024, role=Role.CHORD),
                        Bar(j024, j022, role=Role.CHORD),
                        Bar(j022, j018, role=Role.CHORD),
                        Bar(j018, j013, role=Role.CHORD),
                        Bar(j024, j041, role=Role.TRANSVERSE_BRACE),
                        Bar(j024, j040, role=Role.DIAGONAL_BRACE),
                        Bar(j039, j022, role=Role.TRANSVERSE_BRACE),
                        Bar(j022, j038, role=Role.DIAGONAL_BRACE),
                        Bar(j022, j040, role=Role.DIAGONAL_BRACE),
                        Bar(j018, j038, role=Role.TRANSVERSE_BRACE),
                        Bar(j038, j021, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j013, role=Role.DIAGONAL_BRACE),
                        Bar(j036, j021, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j037, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j067, j065, role=Role.CHORD),
                        Bar(j065, j068, role=Role.CHORD),
                        Bar(j068, j069, role=Role.CHORD),
                        Bar(j069, j070, role=Role.CHORD),
                        Bar(j070, j071, role=Role.CHORD),
                        Bar(j071, j072, role=Role.CHORD),
                        Bar(j072, j073, role=Role.CHORD),
                        Bar(j073, j063, role=Role.CHORD),
                        Bar(j067, j061, role=Role.CHORD),
                        Bar(j061, j059, role=Role.CHORD),
                        Bar(j059, j057, role=Role.CHORD),
                        Bar(j057, j053, role=Role.CHORD),
                        Bar(j053, j049, role=Role.CHORD),
                        Bar(j059, j068, role=Role.TRANSVERSE_BRACE),
                        Bar(j049, j055, role=Role.DIAGONAL_BRACE),
                        Bar(j055, j071, role=Role.DIAGONAL_BRACE),
                        Bar(j071, j053, role=Role.TRANSVERSE_BRACE),
                        Bar(j059, j069, role=Role.DIAGONAL_BRACE),
                        Bar(j069, j057, role=Role.DIAGONAL_BRACE),
                        Bar(j057, j071, role=Role.DIAGONAL_BRACE),
                        Bar(j070, j057, role=Role.TRANSVERSE_BRACE),
                        Bar(j073, j055, role=Role.DIAGONAL_BRACE),
                        Bar(j055, j072, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j064, j074, role=Role.CHORD),
                        Bar(j074, j075, role=Role.CHORD),
                        Bar(j075, j076, role=Role.CHORD),
                        Bar(j076, j077, role=Role.CHORD),
                        Bar(j077, j078, role=Role.CHORD),
                        Bar(j078, j079, role=Role.CHORD),
                        Bar(j079, j066, role=Role.CHORD),
                        Bar(j066, j080, role=Role.CHORD),
                        Bar(j080, j062, role=Role.CHORD),
                        Bar(j062, j060, role=Role.CHORD),
                        Bar(j060, j058, role=Role.CHORD),
                        Bar(j058, j054, role=Role.CHORD),
                        Bar(j054, j050, role=Role.CHORD),
                        Bar(j060, j079, role=Role.TRANSVERSE_BRACE),
                        Bar(j060, j078, role=Role.DIAGONAL_BRACE),
                        Bar(j078, j058, role=Role.DIAGONAL_BRACE),
                        Bar(j058, j076, role=Role.DIAGONAL_BRACE),
                        Bar(j076, j054, role=Role.TRANSVERSE_BRACE),
                        Bar(j077, j058, role=Role.TRANSVERSE_BRACE),
                        Bar(j074, j056, role=Role.DIAGONAL_BRACE),
                        Bar(j056, j075, role=Role.TRANSVERSE_BRACE),
                        Bar(j050, j056, role=Role.DIAGONAL_BRACE),
                        Bar(j056, j076, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        peaks=(
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j004, j005, role=Role.DIAGONAL_BRACE),
                        Bar(j005, j006, role=Role.DIAGONAL_BRACE),
                        Bar(j006, j007, role=Role.DIAGONAL_BRACE),
                        Bar(j007, j008, role=Role.DIAGONAL_BRACE),
                        Bar(j008, j009, role=Role.DIAGONAL_BRACE),
                        Bar(j009, j010, role=Role.DIAGONAL_BRACE),
                        Bar(j010, j011, role=Role.DIAGONAL_BRACE),
                        Bar(j011, j009, role=Role.CHORD),
                        Bar(j009, j007, role=Role.CHORD),
                        Bar(j007, j005, role=Role.CHORD),
                        Bar(j005, j001, role=Role.CHORD),
                        Bar(j001, j002, role=Role.CHORD),
                        Bar(j002, j003, role=Role.CHORD),
                        Bar(j003, j004, role=Role.CHORD),
                        Bar(j004, j006, role=Role.CHORD),
                        Bar(j006, j008, role=Role.CHORD),
                        Bar(j008, j010, role=Role.CHORD),
                        Bar(j010, j013, role=Role.CHORD),
                    ),
                )
            ),
        ),
    )


A_2_D_2004_4_WE_WADIFF_100 = _a_2_d_2004_4_we_wadiff_100()


def _a_2_e_01_2019_42_we_wadiff_140() -> Tower[LowestCrossarm]:
    """A-2-E-01-2019-42 WE WAdiff 140: each joint written once, by its key."""
    j001 = Point(m(-0.12), m(0), m(10.55))
    j002 = Point(m(0), m(0), m(10.55))
    j003 = Point(m(0.12), m(0), m(10.55))
    j004 = Point(m(-0.15), m(0), m(10.23))
    j005 = Point(m(0.15), m(0), m(10.23))
    j006 = Point(m(-0.23), m(0), m(9.44))
    j007 = Point(m(0.31), m(0), m(8.72))
    j008 = Point(m(-0.4), m(0), m(7.85))
    j009 = Point(m(0.49), m(0), m(7.01))
    j010 = Point(m(-0.57), m(0), m(6.17))
    j011 = Point(m(0.67), m(0), m(5.21))
    j012 = Point(m(-0.77), m(0), m(4.22))
    j013 = Point(m(-0.75), m(0), m(4.22))
    j014 = Point(m(0.75), m(0), m(4.22))
    j015 = Point(m(0.77), m(0), m(4.22))
    j016 = Point(m(-0.87), m(0), m(3.32))
    j017 = Point(m(0.87), m(0), m(3.32))
    j018 = Point(m(-0.99), m(0), m(2.12))
    j019 = Point(m(0.99), m(0), m(2.12))
    j020 = Point(m(-4.4), m(0), m(1.62))
    j021 = Point(m(4.4), m(0), m(1.62))
    j022 = Point(m(-1.03), m(0), m(1.06))
    j023 = Point(m(1.03), m(0), m(1.06))
    j024 = Point(m(-2.81), m(0), m(0.98))
    j025 = Point(m(2.82), m(0), m(0.98))
    j026 = Point(m(-9.3), m(0), m(0.91))
    j027 = Point(m(9.3), m(0), m(0.91))
    j028 = Point(m(-6.85), m(0), m(0.81))
    j029 = Point(m(6.85), m(0), m(0.81))
    j030 = Point(m(-10.96), m(0), m(0.68))
    j031 = Point(m(10.95), m(0), m(0.68))
    j032 = Point(m(-12.62), m(0), m(0.44))
    j033 = Point(m(12.6), m(0), m(0.44))
    j034 = Point(m(-13.72), m(0), m(0.28))
    j035 = Point(m(13.7), m(0), m(0.28))
    j036 = Point(m(-14.2), m(0), m(0.21))
    j037 = Point(m(14.2), m(0), m(0.21))
    j038 = Point(m(-14.2), m(0), m(0))
    j039 = Point(m(-13.72), m(0), m(0))
    j040 = Point(m(-12.62), m(0), m(0))
    j041 = Point(m(-10.96), m(0), m(0))
    j042 = Point(m(-9.3), m(0), m(0))
    j043 = Point(m(-6.85), m(0), m(0))
    j044 = Point(m(-4.4), m(0), m(0))
    j045 = Point(m(-2.81), m(0), m(0))
    j046 = Point(m(-1.08), m(0), m(0))
    j047 = Point(m(0), m(0), m(0))
    j048 = Point(m(1.07), m(0), m(0))
    j049 = Point(m(2.82), m(0), m(0))
    j050 = Point(m(4.4), m(0), m(0))
    j051 = Point(m(6.85), m(0), m(0))
    j052 = Point(m(9.3), m(0), m(0))
    j053 = Point(m(10.95), m(0), m(0))
    j054 = Point(m(12.6), m(0), m(0))
    j055 = Point(m(13.7), m(0), m(0))
    j056 = Point(m(14.2), m(0), m(0))
    j057 = Point(m(-1.15), m(0), m(-1.89))
    j058 = Point(m(1.15), m(0), m(-1.89))
    j059 = Point(m(-1.22), m(0), m(-3.51))
    j060 = Point(m(1.21), m(0), m(-3.51))
    j061 = Point(m(-1.29), m(0), m(-5.22))
    j062 = Point(m(1.28), m(0), m(-5.22))
    j063 = Point(m(-1.36), m(0), m(-6.94))
    j064 = Point(m(1.35), m(0), m(-6.94))
    j065 = Point(m(-1.43), m(0), m(-8.73))
    j066 = Point(m(1.42), m(0), m(-8.73))
    j067 = Point(m(-1.46), m(0), m(-9.61))
    j068 = Point(m(1.45), m(0), m(-9.61))
    j069 = Point(m(-1.5), m(0), m(-10.53))
    j070 = Point(m(1.49), m(0), m(-10.53))
    j071 = Point(m(-1.61), m(0), m(-11.25))
    j072 = Point(m(-0.75), m(0), m(-11.25))
    j073 = Point(m(0.75), m(0), m(-11.25))
    j074 = Point(m(1.6), m(0), m(-11.25))
    j075 = Point(m(-1.71), m(0), m(-11.95))
    j076 = Point(m(1.7), m(0), m(-11.95))
    j077 = Point(m(-1.86), m(0), m(-12.91))
    j078 = Point(m(-0.99), m(0), m(-12.91))
    j079 = Point(m(1), m(0), m(-12.91))
    j080 = Point(m(1.85), m(0), m(-12.91))
    j081 = Point(m(-2), m(0), m(-13.86))
    j082 = Point(m(1.99), m(0), m(-13.86))
    j083 = Point(m(-2.12), m(0), m(-14.68))
    j084 = Point(m(-0.99), m(0), m(-14.68))
    j085 = Point(m(1), m(0), m(-14.68))
    j086 = Point(m(2.11), m(0), m(-14.68))
    j087 = Point(m(-2.24), m(0), m(-15.48))
    j088 = Point(m(2.23), m(0), m(-15.48))
    j089 = Point(m(-2.4), m(0), m(-16.51))
    j090 = Point(m(-1.27), m(0), m(-16.51))
    j091 = Point(m(1.27), m(0), m(-16.51))
    j092 = Point(m(2.39), m(0), m(-16.51))
    j093 = Point(m(-2.55), m(0), m(-17.55))
    j094 = Point(m(2.54), m(0), m(-17.55))
    j095 = Point(m(-2.62), m(0), m(-18))
    j096 = Point(m(2.61), m(0), m(-18))
    return Tower(
        name="A-2-E-01-2019-42 WE WAdiff 140",
        datum=LowestCrossarm((m(18),)),
        voltages=(),
        line_angles=(),
        attachments=(
            Mount(Wire.SHIELD, Point(m(0), m(0), m(10.55)), Hold.CLAMP),
            Mount(Wire.PHASE, Point(m(-14.2), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-9.3), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-4.4), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(4.4), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(9.3), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(14.2), m(0), m(0)), Hold.STRAIN),
        ),
        bases=(),
        body=(
            Body(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j070, j068, role=Role.CHORD),
                        Bar(j068, j066, role=Role.CHORD),
                        Bar(j066, j064, role=Role.CHORD),
                        Bar(j064, j062, role=Role.CHORD),
                        Bar(j062, j060, role=Role.CHORD),
                        Bar(j060, j058, role=Role.CHORD),
                        Bar(j058, j048, role=Role.CHORD),
                        Bar(j048, j023, role=Role.CHORD),
                        Bar(j023, j019, role=Role.CHORD),
                        Bar(j019, j018, role=Role.TRANSVERSE_BRACE),
                        Bar(j018, j022, role=Role.CHORD),
                        Bar(j022, j046, role=Role.CHORD),
                        Bar(j046, j057, role=Role.CHORD),
                        Bar(j057, j059, role=Role.CHORD),
                        Bar(j059, j061, role=Role.CHORD),
                        Bar(j061, j063, role=Role.CHORD),
                        Bar(j063, j065, role=Role.CHORD),
                        Bar(j065, j067, role=Role.CHORD),
                        Bar(j067, j069, role=Role.CHORD),
                        Bar(j069, j070, role=Role.TRANSVERSE_BRACE),
                        Bar(j019, j022, role=Role.DIAGONAL_BRACE),
                        Bar(j022, j048, role=Role.DIAGONAL_BRACE),
                        Bar(j048, j057, role=Role.DIAGONAL_BRACE),
                        Bar(j057, j060, role=Role.DIAGONAL_BRACE),
                        Bar(j060, j061, role=Role.DIAGONAL_BRACE),
                        Bar(j061, j064, role=Role.DIAGONAL_BRACE),
                        Bar(j064, j065, role=Role.DIAGONAL_BRACE),
                        Bar(j065, j070, role=Role.DIAGONAL_BRACE),
                        Bar(j046, j058, role=Role.DIAGONAL_BRACE),
                        Bar(j058, j059, role=Role.DIAGONAL_BRACE),
                        Bar(j059, j062, role=Role.DIAGONAL_BRACE),
                        Bar(j062, j063, role=Role.DIAGONAL_BRACE),
                        Bar(j063, j066, role=Role.DIAGONAL_BRACE),
                        Bar(j066, j069, role=Role.DIAGONAL_BRACE),
                        Bar(j046, j023, role=Role.DIAGONAL_BRACE),
                        Bar(j023, j018, role=Role.DIAGONAL_BRACE),
                        Bar(j046, j047, role=Role.TRANSVERSE_BRACE),
                        Bar(j047, j048, role=Role.TRANSVERSE_BRACE),
                        Bar(j072, j079, role=Role.DIAGONAL_BRACE),
                        Bar(j085, j090, role=Role.DIAGONAL_BRACE),
                        Bar(j091, j084, role=Role.DIAGONAL_BRACE),
                        Bar(j078, j073, role=Role.DIAGONAL_BRACE),
                        Bar(j087, j088, role=Role.TRANSVERSE_BRACE),
                        Bar(j075, j076, role=Role.TRANSVERSE_BRACE),
                        Bar(j068, j067, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        legs=(
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j069, j071, role=Role.CHORD),
                        Bar(j071, j075, role=Role.CHORD),
                        Bar(j075, j077, role=Role.CHORD),
                        Bar(j077, j081, role=Role.CHORD),
                        Bar(j081, j083, role=Role.CHORD),
                        Bar(j083, j087, role=Role.CHORD),
                        Bar(j087, j089, role=Role.CHORD),
                        Bar(j089, j093, role=Role.CHORD),
                        Bar(j093, j095, role=Role.CHORD),
                        Bar(j069, j072, role=Role.DIAGONAL_BRACE),
                        Bar(j090, j093, role=Role.DIAGONAL_BRACE),
                        Bar(j084, j081, role=Role.DIAGONAL_BRACE),
                        Bar(j081, j078, role=Role.DIAGONAL_BRACE),
                        Bar(j089, j090, role=Role.TRANSVERSE_BRACE),
                        Bar(j090, j087, role=Role.DIAGONAL_BRACE),
                        Bar(j077, j078, role=Role.TRANSVERSE_BRACE),
                        Bar(j078, j075, role=Role.DIAGONAL_BRACE),
                        Bar(j071, j072, role=Role.TRANSVERSE_BRACE),
                        Bar(j072, j075, role=Role.DIAGONAL_BRACE),
                        Bar(j087, j084, role=Role.DIAGONAL_BRACE),
                        Bar(j084, j083, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j070, j074, role=Role.CHORD),
                        Bar(j074, j076, role=Role.CHORD),
                        Bar(j076, j080, role=Role.CHORD),
                        Bar(j080, j082, role=Role.CHORD),
                        Bar(j082, j086, role=Role.CHORD),
                        Bar(j086, j088, role=Role.CHORD),
                        Bar(j088, j092, role=Role.CHORD),
                        Bar(j092, j094, role=Role.CHORD),
                        Bar(j094, j096, role=Role.CHORD),
                        Bar(j079, j082, role=Role.DIAGONAL_BRACE),
                        Bar(j082, j085, role=Role.DIAGONAL_BRACE),
                        Bar(j094, j091, role=Role.DIAGONAL_BRACE),
                        Bar(j073, j070, role=Role.DIAGONAL_BRACE),
                        Bar(j088, j085, role=Role.DIAGONAL_BRACE),
                        Bar(j085, j086, role=Role.TRANSVERSE_BRACE),
                        Bar(j076, j073, role=Role.DIAGONAL_BRACE),
                        Bar(j073, j074, role=Role.TRANSVERSE_BRACE),
                        Bar(j080, j079, role=Role.TRANSVERSE_BRACE),
                        Bar(j079, j076, role=Role.DIAGONAL_BRACE),
                        Bar(j092, j091, role=Role.TRANSVERSE_BRACE),
                        Bar(j091, j088, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        head=(),
        crossarms=(
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j045, j024, role=Role.TRANSVERSE_BRACE),
                        Bar(j024, j046, role=Role.DIAGONAL_BRACE),
                        Bar(j018, j020, role=Role.CHORD),
                        Bar(j020, j026, role=Role.CHORD),
                        Bar(j026, j030, role=Role.CHORD),
                        Bar(j030, j032, role=Role.CHORD),
                        Bar(j032, j034, role=Role.CHORD),
                        Bar(j034, j036, role=Role.CHORD),
                        Bar(j036, j038, role=Role.CHORD),
                        Bar(j038, j039, role=Role.CHORD),
                        Bar(j039, j040, role=Role.CHORD),
                        Bar(j040, j041, role=Role.CHORD),
                        Bar(j041, j042, role=Role.CHORD),
                        Bar(j042, j043, role=Role.CHORD),
                        Bar(j043, j044, role=Role.CHORD),
                        Bar(j044, j045, role=Role.CHORD),
                        Bar(j045, j046, role=Role.CHORD),
                        Bar(j041, j030, role=Role.TRANSVERSE_BRACE),
                        Bar(j030, j040, role=Role.DIAGONAL_BRACE),
                        Bar(j040, j032, role=Role.TRANSVERSE_BRACE),
                        Bar(j030, j042, role=Role.DIAGONAL_BRACE),
                        Bar(j042, j028, role=Role.DIAGONAL_BRACE),
                        Bar(j028, j020, role=Role.DIAGONAL_BRACE),
                        Bar(j020, j044, role=Role.TRANSVERSE_BRACE),
                        Bar(j044, j028, role=Role.DIAGONAL_BRACE),
                        Bar(j028, j043, role=Role.TRANSVERSE_BRACE),
                        Bar(j042, j026, role=Role.TRANSVERSE_BRACE),
                        Bar(j040, j034, role=Role.DIAGONAL_BRACE),
                        Bar(j034, j039, role=Role.TRANSVERSE_BRACE),
                        Bar(j018, j024, role=Role.DIAGONAL_BRACE),
                        Bar(j024, j044, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j031, j054, role=Role.DIAGONAL_BRACE),
                        Bar(j054, j035, role=Role.DIAGONAL_BRACE),
                        Bar(j035, j055, role=Role.TRANSVERSE_BRACE),
                        Bar(j055, j056, role=Role.CHORD),
                        Bar(j056, j037, role=Role.CHORD),
                        Bar(j037, j035, role=Role.CHORD),
                        Bar(j035, j033, role=Role.CHORD),
                        Bar(j033, j031, role=Role.CHORD),
                        Bar(j031, j027, role=Role.CHORD),
                        Bar(j027, j021, role=Role.CHORD),
                        Bar(j021, j019, role=Role.CHORD),
                        Bar(j048, j049, role=Role.CHORD),
                        Bar(j049, j050, role=Role.CHORD),
                        Bar(j050, j051, role=Role.CHORD),
                        Bar(j051, j052, role=Role.CHORD),
                        Bar(j052, j053, role=Role.CHORD),
                        Bar(j053, j054, role=Role.CHORD),
                        Bar(j054, j055, role=Role.CHORD),
                        Bar(j053, j031, role=Role.TRANSVERSE_BRACE),
                        Bar(j031, j052, role=Role.DIAGONAL_BRACE),
                        Bar(j052, j029, role=Role.DIAGONAL_BRACE),
                        Bar(j029, j021, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j050, role=Role.TRANSVERSE_BRACE),
                        Bar(j050, j025, role=Role.DIAGONAL_BRACE),
                        Bar(j025, j019, role=Role.DIAGONAL_BRACE),
                        Bar(j054, j033, role=Role.TRANSVERSE_BRACE),
                        Bar(j052, j027, role=Role.TRANSVERSE_BRACE),
                        Bar(j048, j025, role=Role.DIAGONAL_BRACE),
                        Bar(j025, j049, role=Role.TRANSVERSE_BRACE),
                        Bar(j051, j029, role=Role.TRANSVERSE_BRACE),
                        Bar(j029, j050, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        peaks=(
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j019, j017, role=Role.CHORD),
                        Bar(j017, j015, role=Role.CHORD),
                        Bar(j015, j011, role=Role.CHORD),
                        Bar(j011, j009, role=Role.CHORD),
                        Bar(j009, j007, role=Role.CHORD),
                        Bar(j007, j005, role=Role.CHORD),
                        Bar(j005, j003, role=Role.CHORD),
                        Bar(j003, j002, role=Role.CHORD),
                        Bar(j002, j001, role=Role.CHORD),
                        Bar(j001, j004, role=Role.CHORD),
                        Bar(j004, j006, role=Role.CHORD),
                        Bar(j006, j008, role=Role.CHORD),
                        Bar(j008, j010, role=Role.CHORD),
                        Bar(j010, j012, role=Role.CHORD),
                        Bar(j012, j016, role=Role.CHORD),
                        Bar(j016, j018, role=Role.CHORD),
                        Bar(j019, j012, role=Role.DIAGONAL_BRACE),
                        Bar(j012, j013, role=Role.TRANSVERSE_BRACE),
                        Bar(j013, j011, role=Role.DIAGONAL_BRACE),
                        Bar(j011, j010, role=Role.DIAGONAL_BRACE),
                        Bar(j010, j009, role=Role.DIAGONAL_BRACE),
                        Bar(j009, j008, role=Role.DIAGONAL_BRACE),
                        Bar(j008, j007, role=Role.DIAGONAL_BRACE),
                        Bar(j007, j006, role=Role.DIAGONAL_BRACE),
                        Bar(j006, j005, role=Role.DIAGONAL_BRACE),
                        Bar(j005, j004, role=Role.TRANSVERSE_BRACE),
                        Bar(j018, j014, role=Role.DIAGONAL_BRACE),
                        Bar(j014, j013, role=Role.TRANSVERSE_BRACE),
                        Bar(j015, j014, role=Role.TRANSVERSE_BRACE),
                        Bar(j017, j016, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
    )


A_2_E_01_2019_42_WE_WADIFF_140 = _a_2_e_01_2019_42_we_wadiff_140()

AS4_AD = Tower(
    name="AS4 AD",
    datum=Ground((m(0),)),
    voltages=(kv(400),),
    line_angles=(LineAngle(degrees(0), degrees(2)),),
    attachments=(
        Mount(Wire.SHIELD, Point(mm(0), mm(0), mm(54566)), Hold.CLAMP),
        Mount(Wire.PHASE, Point(mm(-8400), mm(0), mm(27716 + 9500 + 10600)), Hold.SUSPENSION),
        Mount(Wire.PHASE, Point(mm(8400), mm(0), mm(27716 + 9500 + 10600)), Hold.SUSPENSION),
        Mount(Wire.PHASE, Point(mm(-11550), mm(0), mm(27716 + 9500)), Hold.SUSPENSION),
        Mount(Wire.PHASE, Point(mm(11550), mm(0), mm(27716 + 9500)), Hold.SUSPENSION),
        Mount(Wire.PHASE, Point(mm(-9550), mm(0), mm(27716)), Hold.SUSPENSION),
        Mount(Wire.PHASE, Point(mm(9550), mm(0), mm(27716)), Hold.SUSPENSION),
    ),
    bases=(Base(mm(0), mm(10323)),),
    body=(
        Body(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-4540), mm(0), mm(4780)), Point(mm(4540), mm(0), mm(4780))),
                panels=(
                    Panel(
                        Edge(Point(mm(-4120), mm(0), mm(7810)), Point(mm(4120), mm(0), mm(7810))),
                        Bracing.DIAMOND,
                        1,
                    ),
                    Panel(
                        Edge(Point(mm(-3570), mm(0), mm(12010)), Point(mm(3570), mm(0), mm(12010))),
                        Bracing.DIAMOND,
                        1,
                    ),
                    Panel(
                        Edge(Point(mm(-2800), mm(0), mm(18000)), Point(mm(2800), mm(0), mm(18000))),
                        Bracing.DIAMOND,
                        1,
                    ),
                    Panel(
                        Edge(Point(mm(-2040), mm(0), mm(23940)), Point(mm(2040), mm(0), mm(23940))),
                        Bracing.DIAMOND,
                        1,
                    ),
                    Panel(
                        Edge(Point(mm(-1660), mm(0), mm(26830)), Point(mm(1660), mm(0), mm(26830))),
                        Bracing.DIAMOND,
                        1,
                    ),
                    Panel(
                        Edge(Point(mm(-1380), mm(0), mm(29010)), Point(mm(1380), mm(0), mm(29010))),
                        Bracing.CROSS,
                        1,
                    ),
                    Panel(
                        Edge(Point(mm(-1180), mm(0), mm(36240)), Point(mm(1180), mm(0), mm(36240))),
                        Bracing.CROSS,
                        3,
                    ),
                    Panel(
                        Edge(Point(mm(-1100), mm(0), mm(39020)), Point(mm(1100), mm(0), mm(39020))),
                        Bracing.CROSS,
                        1,
                    ),
                    Panel(
                        Edge(Point(mm(-880), mm(0), mm(47030)), Point(mm(880), mm(0), mm(47030))),
                        Bracing.CROSS,
                        4,
                    ),
                    Panel(
                        Edge(Point(mm(-820), mm(0), mm(49060)), Point(mm(820), mm(0), mm(49060))),
                        Bracing.CROSS,
                        1,
                    ),
                    Panel(
                        Edge(Point(mm(-730), mm(0), mm(52390)), Point(mm(730), mm(0), mm(52390))),
                        Bracing.CROSS,
                        2,
                    ),
                    Panel(
                        Edge(Point(mm(-680), mm(0), mm(54390)), Point(mm(680), mm(0), mm(54390))),
                        Bracing.CROSS,
                        1,
                    ),
                ),
            )
        ),
    ),
    legs=(
        Leg(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-5160), mm(0), mm(0)), Point(mm(-5160), mm(0), mm(0))),
                panels=(
                    Panel(
                        Edge(Point(mm(-4540), mm(0), mm(4780)), Point(mm(0), mm(0), mm(6310))),
                        Bracing.PRATT,
                        3,
                    ),
                ),
            )
        ),
        Leg(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(5160), mm(0), mm(0)), Point(mm(5160), mm(0), mm(0))),
                panels=(
                    Panel(
                        Edge(Point(mm(4540), mm(0), mm(4780)), Point(mm(0), mm(0), mm(6310))),
                        Bracing.PRATT,
                        3,
                    ),
                ),
            )
        ),
    ),
    head=(),
    crossarms=(
        Crossarm(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-820), mm(0), mm(49060)), Point(mm(-880), mm(0), mm(47030))),
                panels=(
                    Panel(
                        Edge(
                            Point(mm(-8400), mm(0), mm(47816)), Point(mm(-8400), mm(0), mm(47816))
                        ),
                        Bracing.PRATT,
                        6,
                    ),
                ),
            )
        ),
        Crossarm(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(820), mm(0), mm(49060)), Point(mm(880), mm(0), mm(47030))),
                panels=(
                    Panel(
                        Edge(Point(mm(8400), mm(0), mm(47816)), Point(mm(8400), mm(0), mm(47816))),
                        Bracing.PRATT,
                        6,
                    ),
                ),
            )
        ),
        Crossarm(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-1100), mm(0), mm(39020)), Point(mm(-1180), mm(0), mm(36240))),
                panels=(
                    Panel(
                        Edge(
                            Point(mm(-11550), mm(0), mm(37216)), Point(mm(-11550), mm(0), mm(37216))
                        ),
                        Bracing.PRATT,
                        7,
                    ),
                ),
            )
        ),
        Crossarm(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(1100), mm(0), mm(39020)), Point(mm(1180), mm(0), mm(36240))),
                panels=(
                    Panel(
                        Edge(
                            Point(mm(11550), mm(0), mm(37216)), Point(mm(11550), mm(0), mm(37216))
                        ),
                        Bracing.PRATT,
                        7,
                    ),
                ),
            )
        ),
        Crossarm(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-1380), mm(0), mm(29010)), Point(mm(-1660), mm(0), mm(26830))),
                panels=(
                    Panel(
                        Edge(
                            Point(mm(-9550), mm(0), mm(27716)), Point(mm(-9550), mm(0), mm(27716))
                        ),
                        Bracing.PRATT,
                        6,
                    ),
                ),
            )
        ),
        Crossarm(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(1380), mm(0), mm(29010)), Point(mm(1660), mm(0), mm(26830))),
                panels=(
                    Panel(
                        Edge(Point(mm(9550), mm(0), mm(27716)), Point(mm(9550), mm(0), mm(27716))),
                        Bracing.PRATT,
                        6,
                    ),
                ),
            )
        ),
    ),
    peaks=(
        Peak(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-680), mm(0), mm(54390)), Point(mm(680), mm(0), mm(54390))),
                panels=(
                    Panel(
                        Edge(Point(mm(0), mm(0), mm(54566)), Point(mm(0), mm(0), mm(54566))),
                        Bracing.OPEN,
                        1,
                    ),
                ),
            )
        ),
    ),
)

AS4_AD90 = Tower(
    name="AS4 AD90",
    datum=Ground((m(0),)),
    voltages=(kv(400),),
    line_angles=(LineAngle(degrees(55), degrees(90)),),
    attachments=(
        Mount(Wire.SHIELD, Point(mm(-2000), mm(0), mm(57020)), Hold.CLAMP),
        Mount(Wire.PHASE, Point(mm(-11150), mm(0), mm(57020 - 14600)), Hold.STRAIN),
        Mount(Wire.PHASE, Point(mm(7150), mm(0), mm(57020 - 14600)), Hold.STRAIN),
        Mount(Wire.PHASE, Point(mm(-15850), mm(0), mm(57020 - 14600 - 11000)), Hold.STRAIN),
        Mount(Wire.PHASE, Point(mm(11850), mm(0), mm(57020 - 14600 - 11000)), Hold.STRAIN),
        Mount(Wire.PHASE, Point(mm(-13850), mm(0), mm(57020 - 14600 - 11000 - 9500)), Hold.STRAIN),
        Mount(Wire.PHASE, Point(mm(9850), mm(0), mm(57020 - 14600 - 11000 - 9500)), Hold.STRAIN),
    ),
    bases=(Base(mm(0), mm(22507)),),
    body=(
        Body(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-9260), mm(0), mm(6300)), Point(mm(9260), mm(0), mm(6300))),
                panels=(
                    Panel(
                        Edge(Point(mm(-8320), mm(0), mm(9290)), Point(mm(8320), mm(0), mm(9290))),
                        Bracing.DIAMOND,
                        1,
                    ),
                    Panel(
                        Edge(Point(mm(-5560), mm(0), mm(18060)), Point(mm(5560), mm(0), mm(18060))),
                        Bracing.DIAMOND,
                        1,
                    ),
                    Panel(
                        Edge(Point(mm(-4350), mm(0), mm(21920)), Point(mm(4350), mm(0), mm(21920))),
                        Bracing.DIAMOND,
                        1,
                    ),
                    Panel(
                        Edge(Point(mm(-3500), mm(0), mm(24620)), Point(mm(3500), mm(0), mm(24620))),
                        Bracing.CROSS,
                        1,
                    ),
                    Panel(
                        Edge(Point(mm(-2960), mm(0), mm(31430)), Point(mm(2960), mm(0), mm(31430))),
                        Bracing.CROSS,
                        2,
                    ),
                    Panel(
                        Edge(Point(mm(-2680), mm(0), mm(34930)), Point(mm(2680), mm(0), mm(34930))),
                        Bracing.CROSS,
                        1,
                    ),
                    Panel(
                        Edge(Point(mm(-2080), mm(0), mm(42430)), Point(mm(2080), mm(0), mm(42430))),
                        Bracing.CROSS,
                        2,
                    ),
                    Panel(
                        Edge(Point(mm(-1850), mm(0), mm(45260)), Point(mm(1850), mm(0), mm(45260))),
                        Bracing.CROSS,
                        1,
                    ),
                    Panel(
                        Edge(Point(mm(-1050), mm(0), mm(55350)), Point(mm(1050), mm(0), mm(55350))),
                        Bracing.CROSS,
                        5,
                    ),
                    Panel(
                        Edge(Point(mm(-920), mm(0), mm(57020)), Point(mm(920), mm(0), mm(57020))),
                        Bracing.CROSS,
                        1,
                    ),
                ),
            )
        ),
    ),
    legs=(
        Leg(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-11250), mm(0), mm(0)), Point(mm(-11250), mm(0), mm(0))),
                panels=(
                    Panel(
                        Edge(Point(mm(-9260), mm(0), mm(6300)), Point(mm(0), mm(0), mm(9200))),
                        Bracing.PRATT,
                        3,
                    ),
                ),
            )
        ),
        Leg(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(11250), mm(0), mm(0)), Point(mm(11250), mm(0), mm(0))),
                panels=(
                    Panel(
                        Edge(Point(mm(9260), mm(0), mm(6300)), Point(mm(0), mm(0), mm(9200))),
                        Bracing.PRATT,
                        3,
                    ),
                ),
            )
        ),
    ),
    head=(),
    crossarms=(
        Crossarm(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-1850), mm(0), mm(45260)), Point(mm(-2080), mm(0), mm(42430))),
                panels=(
                    Panel(
                        Edge(
                            Point(mm(-11150), mm(0), mm(42420)), Point(mm(-11150), mm(0), mm(42420))
                        ),
                        Bracing.PRATT,
                        4,
                    ),
                ),
            )
        ),
        Crossarm(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(1850), mm(0), mm(45260)), Point(mm(2080), mm(0), mm(42430))),
                panels=(
                    Panel(
                        Edge(Point(mm(7150), mm(0), mm(42420)), Point(mm(7150), mm(0), mm(42420))),
                        Bracing.PRATT,
                        4,
                    ),
                ),
            )
        ),
        Crossarm(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-2680), mm(0), mm(34930)), Point(mm(-2960), mm(0), mm(31430))),
                panels=(
                    Panel(
                        Edge(
                            Point(mm(-15850), mm(0), mm(31420)), Point(mm(-15850), mm(0), mm(31420))
                        ),
                        Bracing.PRATT,
                        6,
                    ),
                ),
            )
        ),
        Crossarm(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(2680), mm(0), mm(34930)), Point(mm(2960), mm(0), mm(31430))),
                panels=(
                    Panel(
                        Edge(
                            Point(mm(11850), mm(0), mm(31420)), Point(mm(11850), mm(0), mm(31420))
                        ),
                        Bracing.PRATT,
                        6,
                    ),
                ),
            )
        ),
        Crossarm(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-3500), mm(0), mm(24620)), Point(mm(-4350), mm(0), mm(21920))),
                panels=(
                    Panel(
                        Edge(
                            Point(mm(-13850), mm(0), mm(21920)), Point(mm(-13850), mm(0), mm(21920))
                        ),
                        Bracing.PRATT,
                        5,
                    ),
                ),
            )
        ),
        Crossarm(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(3500), mm(0), mm(24620)), Point(mm(4350), mm(0), mm(21920))),
                panels=(
                    Panel(
                        Edge(Point(mm(9850), mm(0), mm(21920)), Point(mm(9850), mm(0), mm(21920))),
                        Bracing.PRATT,
                        5,
                    ),
                ),
            )
        ),
    ),
    peaks=(
        Peak(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-920), mm(0), mm(57020)), Point(mm(-1050), mm(0), mm(55350))),
                panels=(
                    Panel(
                        Edge(
                            Point(mm(-2000), mm(0), mm(57020)), Point(mm(-2000), mm(0), mm(57020))
                        ),
                        Bracing.OPEN,
                        1,
                    ),
                ),
            )
        ),
    ),
)

AS4_ADT = Tower(
    name="AS4 ADT",
    datum=Ground((m(0),)),
    voltages=(kv(400),),
    line_angles=(),
    attachments=(
        Mount(Wire.SHIELD, Point(mm(0), mm(0), mm(59670)), Hold.CLAMP),
        Mount(Wire.PHASE, Point(mm(-10455), mm(0), mm(21920 + 9500 + 11000)), Hold.STRAIN),
        Mount(Wire.PHASE, Point(mm(10455), mm(0), mm(21920 + 9500 + 11000)), Hold.STRAIN),
        Mount(Wire.PHASE, Point(mm(-15940), mm(0), mm(21920 + 9500)), Hold.STRAIN),
        Mount(Wire.PHASE, Point(mm(15940), mm(0), mm(21920 + 9500)), Hold.STRAIN),
        Mount(Wire.PHASE, Point(mm(-13855), mm(0), mm(21920)), Hold.STRAIN),
        Mount(Wire.PHASE, Point(mm(13855), mm(0), mm(21920)), Hold.STRAIN),
    ),
    bases=(Base(mm(0), mm(22507)),),
    body=(
        Body(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-9270), mm(0), mm(6040)), Point(mm(9270), mm(0), mm(6040))),
                panels=(
                    Panel(
                        Edge(Point(mm(-8320), mm(0), mm(9060)), Point(mm(8320), mm(0), mm(9060))),
                        Bracing.DIAMOND,
                        1,
                    ),
                    Panel(
                        Edge(Point(mm(-5570), mm(0), mm(17870)), Point(mm(5570), mm(0), mm(17870))),
                        Bracing.DIAMOND,
                        1,
                    ),
                    Panel(
                        Edge(Point(mm(-4350), mm(0), mm(21730)), Point(mm(4350), mm(0), mm(21730))),
                        Bracing.DIAMOND,
                        1,
                    ),
                    Panel(
                        Edge(Point(mm(-3500), mm(0), mm(24440)), Point(mm(3500), mm(0), mm(24440))),
                        Bracing.CROSS,
                        1,
                    ),
                    Panel(
                        Edge(Point(mm(-2960), mm(0), mm(31280)), Point(mm(2960), mm(0), mm(31280))),
                        Bracing.CROSS,
                        2,
                    ),
                    Panel(
                        Edge(Point(mm(-2680), mm(0), mm(34800)), Point(mm(2680), mm(0), mm(34800))),
                        Bracing.CROSS,
                        1,
                    ),
                    Panel(
                        Edge(Point(mm(-2080), mm(0), mm(42340)), Point(mm(2080), mm(0), mm(42340))),
                        Bracing.CROSS,
                        2,
                    ),
                    Panel(
                        Edge(Point(mm(-1860), mm(0), mm(45220)), Point(mm(1860), mm(0), mm(45220))),
                        Bracing.CROSS,
                        1,
                    ),
                    Panel(
                        Edge(Point(mm(-860), mm(0), mm(57770)), Point(mm(860), mm(0), mm(57770))),
                        Bracing.CROSS,
                        6,
                    ),
                ),
            )
        ),
    ),
    legs=(
        Leg(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-11250), mm(0), mm(0)), Point(mm(-11250), mm(0), mm(0))),
                panels=(
                    Panel(
                        Edge(Point(mm(-9270), mm(0), mm(6040)), Point(mm(0), mm(0), mm(9260))),
                        Bracing.PRATT,
                        3,
                    ),
                ),
            )
        ),
        Leg(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(11250), mm(0), mm(0)), Point(mm(11250), mm(0), mm(0))),
                panels=(
                    Panel(
                        Edge(Point(mm(9270), mm(0), mm(6040)), Point(mm(0), mm(0), mm(9260))),
                        Bracing.PRATT,
                        3,
                    ),
                ),
            )
        ),
    ),
    head=(),
    crossarms=(
        Crossarm(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-1860), mm(0), mm(45220)), Point(mm(-2080), mm(0), mm(42340))),
                panels=(
                    Panel(
                        Edge(
                            Point(mm(-10455), mm(0), mm(42420)), Point(mm(-10455), mm(0), mm(42420))
                        ),
                        Bracing.PRATT,
                        8,
                    ),
                ),
            )
        ),
        Crossarm(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(1860), mm(0), mm(45220)), Point(mm(2080), mm(0), mm(42340))),
                panels=(
                    Panel(
                        Edge(
                            Point(mm(10455), mm(0), mm(42420)), Point(mm(10455), mm(0), mm(42420))
                        ),
                        Bracing.PRATT,
                        8,
                    ),
                ),
            )
        ),
        Crossarm(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-2680), mm(0), mm(34800)), Point(mm(-2960), mm(0), mm(31280))),
                panels=(
                    Panel(
                        Edge(
                            Point(mm(-15940), mm(0), mm(31420)), Point(mm(-15940), mm(0), mm(31420))
                        ),
                        Bracing.PRATT,
                        12,
                    ),
                ),
            )
        ),
        Crossarm(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(2680), mm(0), mm(34800)), Point(mm(2960), mm(0), mm(31280))),
                panels=(
                    Panel(
                        Edge(
                            Point(mm(15940), mm(0), mm(31420)), Point(mm(15940), mm(0), mm(31420))
                        ),
                        Bracing.PRATT,
                        12,
                    ),
                ),
            )
        ),
        Crossarm(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-3500), mm(0), mm(24440)), Point(mm(-4350), mm(0), mm(21730))),
                panels=(
                    Panel(
                        Edge(
                            Point(mm(-13855), mm(0), mm(21920)), Point(mm(-13855), mm(0), mm(21920))
                        ),
                        Bracing.PRATT,
                        9,
                    ),
                ),
            )
        ),
        Crossarm(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(3500), mm(0), mm(24440)), Point(mm(4350), mm(0), mm(21730))),
                panels=(
                    Panel(
                        Edge(
                            Point(mm(13855), mm(0), mm(21920)), Point(mm(13855), mm(0), mm(21920))
                        ),
                        Bracing.PRATT,
                        9,
                    ),
                ),
            )
        ),
    ),
    peaks=(
        Peak(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-860), mm(0), mm(57770)), Point(mm(860), mm(0), mm(57770))),
                panels=(
                    Panel(
                        Edge(Point(mm(0), mm(0), mm(59670)), Point(mm(0), mm(0), mm(59670))),
                        Bracing.OPEN,
                        1,
                    ),
                ),
            )
        ),
    ),
)


def _d_2_d_2018_3_t1() -> Tower[LowestCrossarm]:
    """D-2-D-2018.3 T1: each joint written once, by its key."""
    j001 = Point(m(-6.5), m(0), m(17.5))
    j002 = Point(m(6.5), m(0), m(17.5))
    j003 = Point(m(-6.21), m(0), m(17.18))
    j004 = Point(m(6.21), m(0), m(17.18))
    j005 = Point(m(-5.67), m(0), m(17.13))
    j006 = Point(m(5.68), m(0), m(17.13))
    j007 = Point(m(-5.64), m(0), m(16.58))
    j008 = Point(m(-4.38), m(0), m(16.58))
    j009 = Point(m(4.38), m(0), m(16.58))
    j010 = Point(m(5.65), m(0), m(16.58))
    j011 = Point(m(-3.09), m(0), m(16.07))
    j012 = Point(m(3.09), m(0), m(16.07))
    j013 = Point(m(-4.43), m(0), m(15.43))
    j014 = Point(m(4.43), m(0), m(15.43))
    j015 = Point(m(-1.18), m(0), m(15.36))
    j016 = Point(m(1.17), m(0), m(15.36))
    j017 = Point(m(-0.01), m(0), m(15.02))
    j018 = Point(m(-3.21), m(0), m(14.39))
    j019 = Point(m(3.21), m(0), m(14.39))
    j020 = Point(m(-1.44), m(0), m(13.03))
    j021 = Point(m(1.44), m(0), m(13.03))
    j022 = Point(m(-6.6), m(0), m(11.94))
    j023 = Point(m(6.6), m(0), m(11.94))
    j024 = Point(m(-4.03), m(0), m(11.51))
    j025 = Point(m(-1.52), m(0), m(11.51))
    j026 = Point(m(1.51), m(0), m(11.51))
    j027 = Point(m(4.02), m(0), m(11.51))
    j028 = Point(m(-9.95), m(0), m(11.22))
    j029 = Point(m(9.95), m(0), m(11.22))
    j030 = Point(m(-13.3), m(0), m(10.5))
    j031 = Point(m(13.3), m(0), m(10.5))
    j032 = Point(m(-13.3), m(0), m(10))
    j033 = Point(m(-11.62), m(0), m(10))
    j034 = Point(m(-9.95), m(0), m(10))
    j035 = Point(m(-8.28), m(0), m(10))
    j036 = Point(m(-6.6), m(0), m(10))
    j037 = Point(m(-4.04), m(0), m(10))
    j038 = Point(m(-1.59), m(0), m(10))
    j039 = Point(m(1.58), m(0), m(10))
    j040 = Point(m(4.02), m(0), m(10))
    j041 = Point(m(6.6), m(0), m(10))
    j042 = Point(m(8.28), m(0), m(10))
    j043 = Point(m(9.95), m(0), m(10))
    j044 = Point(m(11.62), m(0), m(10))
    j045 = Point(m(13.3), m(0), m(10))
    j046 = Point(m(-1.69), m(0), m(8))
    j047 = Point(m(1.68), m(0), m(8))
    j048 = Point(m(-1.78), m(0), m(6))
    j049 = Point(m(1.78), m(0), m(6))
    j050 = Point(m(-1.88), m(0), m(4))
    j051 = Point(m(1.88), m(0), m(4))
    j052 = Point(m(-9.95), m(0), m(2.09))
    j053 = Point(m(9.96), m(0), m(2.09))
    j054 = Point(m(-1.96), m(0), m(2))
    j055 = Point(m(1.96), m(0), m(2))
    j056 = Point(m(-7.2), m(0), m(1.49))
    j057 = Point(m(7.2), m(0), m(1.49))
    j058 = Point(m(-12.7), m(0), m(1.31))
    j059 = Point(m(12.7), m(0), m(1.31))
    j060 = Point(m(-15.6), m(0), m(0.5))
    j061 = Point(m(15.6), m(0), m(0.5))
    j062 = Point(m(-15.6), m(0), m(0))
    j063 = Point(m(-14.12), m(0), m(0))
    j064 = Point(m(-12.7), m(0), m(0))
    j065 = Point(m(-10.28), m(0), m(0))
    j066 = Point(m(-9.62), m(0), m(0))
    j067 = Point(m(-7.2), m(0), m(0))
    j068 = Point(m(-3.41), m(0), m(0))
    j069 = Point(m(-2.05), m(0), m(0))
    j070 = Point(m(2.05), m(0), m(0))
    j071 = Point(m(3.41), m(0), m(0))
    j072 = Point(m(7.2), m(0), m(0))
    j073 = Point(m(9.62), m(0), m(0))
    j074 = Point(m(10.28), m(0), m(0))
    j075 = Point(m(12.7), m(0), m(0))
    j076 = Point(m(14.13), m(0), m(0))
    j077 = Point(m(15.6), m(0), m(0))
    j078 = Point(m(-9.95), m(0), m(-0.46))
    j079 = Point(m(9.96), m(0), m(-0.46))
    j080 = Point(m(-2.2), m(0), m(-2.94))
    j081 = Point(m(2.2), m(0), m(-2.94))
    j082 = Point(m(-2.34), m(0), m(-5.76))
    j083 = Point(m(2.34), m(0), m(-5.76))
    j084 = Point(m(-2.48), m(0), m(-8.56))
    j085 = Point(m(2.48), m(0), m(-8.56))
    j086 = Point(m(-2.63), m(0), m(-11.54))
    j087 = Point(m(2.63), m(0), m(-11.54))
    j088 = Point(m(-2.79), m(0), m(-14.72))
    j089 = Point(m(2.79), m(0), m(-14.72))
    j090 = Point(m(-3.19), m(0), m(-16.52))
    j091 = Point(m(-0.01), m(0), m(-16.52))
    j092 = Point(m(3.19), m(0), m(-16.52))
    j093 = Point(m(-3.45), m(0), m(-17.71))
    j094 = Point(m(-1.86), m(0), m(-17.71))
    j095 = Point(m(1.86), m(0), m(-17.71))
    j096 = Point(m(3.45), m(0), m(-17.71))
    j097 = Point(m(-3.72), m(0), m(-18.91))
    j098 = Point(m(3.72), m(0), m(-18.91))
    j099 = Point(m(-4.1), m(0), m(-20.64))
    j100 = Point(m(-1.56), m(0), m(-20.64))
    j101 = Point(m(1.56), m(0), m(-20.64))
    j102 = Point(m(4.1), m(0), m(-20.64))
    j103 = Point(m(-4.37), m(0), m(-21.84))
    j104 = Point(m(-0.01), m(0), m(-21.84))
    j105 = Point(m(4.37), m(0), m(-21.84))
    j106 = Point(m(-4.68), m(0), m(-23.23))
    j107 = Point(m(-1.77), m(0), m(-23.23))
    j108 = Point(m(1.77), m(0), m(-23.23))
    j109 = Point(m(4.68), m(0), m(-23.23))
    j110 = Point(m(-4.98), m(0), m(-24.62))
    j111 = Point(m(-3.53), m(0), m(-24.62))
    j112 = Point(m(3.53), m(0), m(-24.62))
    j113 = Point(m(4.98), m(0), m(-24.62))
    j114 = Point(m(-5.29), m(0), m(-26))
    j115 = Point(m(5.29), m(0), m(-26))
    return Tower(
        name="D-2-D-2018.3 T1",
        datum=LowestCrossarm((m(26), m(29), m(32), m(35), m(38), m(41), m(44), m(47), m(50))),
        voltages=(kv(380),),
        line_angles=(),
        attachments=(
            Mount(Wire.SHIELD, Point(m(-6.5), m(0), m(17.5)), Hold.CLAMP),
            Mount(Wire.SHIELD, Point(m(6.5), m(0), m(17.5)), Hold.CLAMP),
            WirePosition(
                Wire.PHASE,
                Point(m(-9.95), m(0), m(6.55)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j032),
                    InsulatorString(mount=j036),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(9.95), m(0), m(6.55)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j041),
                    InsulatorString(mount=j045),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(-12.7), m(0), m(-3.91)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j062),
                    InsulatorString(mount=j078),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(-7.2), m(0), m(-3.91)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j078),
                    InsulatorString(mount=j068),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(7.2), m(0), m(-3.91)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j079),
                    InsulatorString(mount=j071),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(12.7), m(0), m(-3.91)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j077),
                    InsulatorString(mount=j079),
                ),
            ),
        ),
        bases=(),
        body=(
            Body(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j104, j105, role=Role.TRANSVERSE_BRACE),
                        Bar(j070, j080, role=Role.DIAGONAL_BRACE),
                        Bar(j080, j083, role=Role.DIAGONAL_BRACE),
                        Bar(j083, j084, role=Role.DIAGONAL_BRACE),
                        Bar(j085, j082, role=Role.DIAGONAL_BRACE),
                        Bar(j082, j081, role=Role.DIAGONAL_BRACE),
                        Bar(j081, j069, role=Role.DIAGONAL_BRACE),
                        Bar(j088, j086, role=Role.CHORD),
                        Bar(j086, j084, role=Role.CHORD),
                        Bar(j084, j082, role=Role.CHORD),
                        Bar(j082, j080, role=Role.CHORD),
                        Bar(j080, j069, role=Role.CHORD),
                        Bar(j069, j054, role=Role.CHORD),
                        Bar(j054, j050, role=Role.CHORD),
                        Bar(j051, j055, role=Role.CHORD),
                        Bar(j055, j070, role=Role.CHORD),
                        Bar(j070, j081, role=Role.CHORD),
                        Bar(j081, j083, role=Role.CHORD),
                        Bar(j083, j085, role=Role.CHORD),
                        Bar(j085, j087, role=Role.CHORD),
                        Bar(j087, j089, role=Role.CHORD),
                        Bar(j070, j054, role=Role.DIAGONAL_BRACE),
                        Bar(j054, j051, role=Role.DIAGONAL_BRACE),
                        Bar(j020, j025, role=Role.CHORD),
                        Bar(j025, j038, role=Role.CHORD),
                        Bar(j038, j046, role=Role.CHORD),
                        Bar(j046, j048, role=Role.CHORD),
                        Bar(j048, j050, role=Role.CHORD),
                        Bar(j050, j055, role=Role.DIAGONAL_BRACE),
                        Bar(j055, j069, role=Role.DIAGONAL_BRACE),
                        Bar(j039, j025, role=Role.DIAGONAL_BRACE),
                        Bar(j025, j021, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j026, role=Role.CHORD),
                        Bar(j026, j039, role=Role.CHORD),
                        Bar(j039, j047, role=Role.CHORD),
                        Bar(j047, j049, role=Role.CHORD),
                        Bar(j049, j051, role=Role.CHORD),
                        Bar(j051, j048, role=Role.DIAGONAL_BRACE),
                        Bar(j048, j047, role=Role.DIAGONAL_BRACE),
                        Bar(j047, j038, role=Role.DIAGONAL_BRACE),
                        Bar(j038, j026, role=Role.DIAGONAL_BRACE),
                        Bar(j026, j020, role=Role.DIAGONAL_BRACE),
                        Bar(j050, j049, role=Role.DIAGONAL_BRACE),
                        Bar(j049, j046, role=Role.DIAGONAL_BRACE),
                        Bar(j046, j039, role=Role.DIAGONAL_BRACE),
                        Bar(j104, j098, role=Role.DIAGONAL_BRACE),
                        Bar(j108, j104, role=Role.DIAGONAL_BRACE),
                        Bar(j095, j091, role=Role.DIAGONAL_BRACE),
                        Bar(j091, j089, role=Role.DIAGONAL_BRACE),
                        Bar(j091, j092, role=Role.TRANSVERSE_BRACE),
                        Bar(j088, j087, role=Role.DIAGONAL_BRACE),
                        Bar(j087, j084, role=Role.DIAGONAL_BRACE),
                        Bar(j089, j086, role=Role.DIAGONAL_BRACE),
                        Bar(j086, j085, role=Role.DIAGONAL_BRACE),
                        Bar(j070, j069, role=Role.TRANSVERSE_BRACE),
                        Bar(j039, j038, role=Role.TRANSVERSE_BRACE),
                        Bar(j021, j020, role=Role.TRANSVERSE_BRACE),
                        Bar(j051, j050, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        legs=(
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j114, j110, role=Role.CHORD),
                        Bar(j110, j106, role=Role.CHORD),
                        Bar(j106, j103, role=Role.CHORD),
                        Bar(j103, j099, role=Role.CHORD),
                        Bar(j099, j097, role=Role.CHORD),
                        Bar(j097, j093, role=Role.CHORD),
                        Bar(j093, j090, role=Role.CHORD),
                        Bar(j090, j088, role=Role.CHORD),
                        Bar(j103, j104, role=Role.TRANSVERSE_BRACE),
                        Bar(j114, j111, role=Role.DIAGONAL_BRACE),
                        Bar(j111, j107, role=Role.DIAGONAL_BRACE),
                        Bar(j107, j104, role=Role.DIAGONAL_BRACE),
                        Bar(j104, j100, role=Role.DIAGONAL_BRACE),
                        Bar(j100, j097, role=Role.DIAGONAL_BRACE),
                        Bar(j091, j088, role=Role.DIAGONAL_BRACE),
                        Bar(j097, j094, role=Role.DIAGONAL_BRACE),
                        Bar(j094, j091, role=Role.DIAGONAL_BRACE),
                        Bar(j111, j110, role=Role.TRANSVERSE_BRACE),
                        Bar(j107, j106, role=Role.TRANSVERSE_BRACE),
                        Bar(j100, j099, role=Role.TRANSVERSE_BRACE),
                        Bar(j111, j106, role=Role.DIAGONAL_BRACE),
                        Bar(j107, j103, role=Role.DIAGONAL_BRACE),
                        Bar(j103, j100, role=Role.DIAGONAL_BRACE),
                        Bar(j094, j093, role=Role.TRANSVERSE_BRACE),
                        Bar(j094, j090, role=Role.DIAGONAL_BRACE),
                        Bar(j090, j091, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j089, j092, role=Role.CHORD),
                        Bar(j092, j096, role=Role.CHORD),
                        Bar(j096, j098, role=Role.CHORD),
                        Bar(j098, j102, role=Role.CHORD),
                        Bar(j102, j105, role=Role.CHORD),
                        Bar(j105, j109, role=Role.CHORD),
                        Bar(j109, j113, role=Role.CHORD),
                        Bar(j113, j115, role=Role.CHORD),
                        Bar(j115, j112, role=Role.DIAGONAL_BRACE),
                        Bar(j112, j108, role=Role.DIAGONAL_BRACE),
                        Bar(j098, j095, role=Role.DIAGONAL_BRACE),
                        Bar(j092, j095, role=Role.DIAGONAL_BRACE),
                        Bar(j095, j096, role=Role.TRANSVERSE_BRACE),
                        Bar(j113, j112, role=Role.TRANSVERSE_BRACE),
                        Bar(j112, j109, role=Role.DIAGONAL_BRACE),
                        Bar(j109, j108, role=Role.TRANSVERSE_BRACE),
                        Bar(j108, j105, role=Role.DIAGONAL_BRACE),
                        Bar(j105, j101, role=Role.DIAGONAL_BRACE),
                        Bar(j101, j102, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        head=(
            Head(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j020, j017, role=Role.DIAGONAL_BRACE),
                        Bar(j017, j021, role=Role.DIAGONAL_BRACE),
                        Bar(j017, j015, role=Role.DIAGONAL_BRACE),
                        Bar(j020, j015, role=Role.CHORD),
                        Bar(j017, j016, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j016, role=Role.CHORD),
                    ),
                )
            ),
        ),
        crossarms=(
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j038, j037, role=Role.CHORD),
                        Bar(j037, j036, role=Role.CHORD),
                        Bar(j036, j035, role=Role.CHORD),
                        Bar(j035, j034, role=Role.CHORD),
                        Bar(j034, j033, role=Role.CHORD),
                        Bar(j033, j032, role=Role.CHORD),
                        Bar(j020, j022, role=Role.CHORD),
                        Bar(j022, j028, role=Role.CHORD),
                        Bar(j028, j030, role=Role.CHORD),
                        Bar(j030, j032, role=Role.CHORD),
                        Bar(j020, j024, role=Role.DIAGONAL_BRACE),
                        Bar(j024, j036, role=Role.DIAGONAL_BRACE),
                        Bar(j036, j022, role=Role.TRANSVERSE_BRACE),
                        Bar(j038, j024, role=Role.DIAGONAL_BRACE),
                        Bar(j024, j037, role=Role.TRANSVERSE_BRACE),
                        Bar(j034, j028, role=Role.TRANSVERSE_BRACE),
                        Bar(j022, j035, role=Role.DIAGONAL_BRACE),
                        Bar(j035, j028, role=Role.DIAGONAL_BRACE),
                        Bar(j028, j033, role=Role.DIAGONAL_BRACE),
                        Bar(j033, j030, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j045, j044, role=Role.CHORD),
                        Bar(j044, j043, role=Role.CHORD),
                        Bar(j043, j042, role=Role.CHORD),
                        Bar(j042, j041, role=Role.CHORD),
                        Bar(j041, j040, role=Role.CHORD),
                        Bar(j040, j039, role=Role.CHORD),
                        Bar(j021, j023, role=Role.CHORD),
                        Bar(j023, j029, role=Role.CHORD),
                        Bar(j029, j031, role=Role.CHORD),
                        Bar(j031, j045, role=Role.CHORD),
                        Bar(j021, j027, role=Role.DIAGONAL_BRACE),
                        Bar(j027, j041, role=Role.DIAGONAL_BRACE),
                        Bar(j041, j023, role=Role.TRANSVERSE_BRACE),
                        Bar(j039, j027, role=Role.DIAGONAL_BRACE),
                        Bar(j027, j040, role=Role.TRANSVERSE_BRACE),
                        Bar(j043, j029, role=Role.TRANSVERSE_BRACE),
                        Bar(j023, j042, role=Role.DIAGONAL_BRACE),
                        Bar(j042, j029, role=Role.DIAGONAL_BRACE),
                        Bar(j029, j044, role=Role.DIAGONAL_BRACE),
                        Bar(j044, j031, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j069, j068, role=Role.TRANSVERSE_BRACE),
                        Bar(j068, j067, role=Role.TRANSVERSE_BRACE),
                        Bar(j067, j066, role=Role.TRANSVERSE_BRACE),
                        Bar(j066, j065, role=Role.TRANSVERSE_BRACE),
                        Bar(j065, j064, role=Role.TRANSVERSE_BRACE),
                        Bar(j064, j063, role=Role.TRANSVERSE_BRACE),
                        Bar(j063, j062, role=Role.TRANSVERSE_BRACE),
                        Bar(j050, j052, role=Role.CHORD),
                        Bar(j052, j058, role=Role.CHORD),
                        Bar(j058, j060, role=Role.CHORD),
                        Bar(j060, j062, role=Role.CHORD),
                        Bar(j078, j065, role=Role.DIAGONAL_BRACE),
                        Bar(j065, j052, role=Role.DIAGONAL_BRACE),
                        Bar(j052, j066, role=Role.DIAGONAL_BRACE),
                        Bar(j066, j078, role=Role.DIAGONAL_BRACE),
                        Bar(j064, j058, role=Role.TRANSVERSE_BRACE),
                        Bar(j067, j056, role=Role.TRANSVERSE_BRACE),
                        Bar(j056, j068, role=Role.DIAGONAL_BRACE),
                        Bar(j068, j050, role=Role.DIAGONAL_BRACE),
                        Bar(j050, j056, role=Role.DIAGONAL_BRACE),
                        Bar(j056, j066, role=Role.DIAGONAL_BRACE),
                        Bar(j065, j058, role=Role.DIAGONAL_BRACE),
                        Bar(j058, j063, role=Role.DIAGONAL_BRACE),
                        Bar(j063, j060, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j077, j076, role=Role.TRANSVERSE_BRACE),
                        Bar(j076, j075, role=Role.TRANSVERSE_BRACE),
                        Bar(j075, j074, role=Role.TRANSVERSE_BRACE),
                        Bar(j074, j073, role=Role.TRANSVERSE_BRACE),
                        Bar(j073, j072, role=Role.TRANSVERSE_BRACE),
                        Bar(j072, j071, role=Role.TRANSVERSE_BRACE),
                        Bar(j071, j070, role=Role.TRANSVERSE_BRACE),
                        Bar(j061, j077, role=Role.CHORD),
                        Bar(j079, j074, role=Role.DIAGONAL_BRACE),
                        Bar(j074, j053, role=Role.DIAGONAL_BRACE),
                        Bar(j053, j073, role=Role.DIAGONAL_BRACE),
                        Bar(j073, j079, role=Role.DIAGONAL_BRACE),
                        Bar(j075, j059, role=Role.TRANSVERSE_BRACE),
                        Bar(j072, j057, role=Role.TRANSVERSE_BRACE),
                        Bar(j074, j059, role=Role.DIAGONAL_BRACE),
                        Bar(j059, j076, role=Role.DIAGONAL_BRACE),
                        Bar(j076, j061, role=Role.DIAGONAL_BRACE),
                        Bar(j061, j059, role=Role.CHORD),
                        Bar(j059, j053, role=Role.CHORD),
                        Bar(j053, j051, role=Role.CHORD),
                        Bar(j051, j057, role=Role.DIAGONAL_BRACE),
                        Bar(j057, j073, role=Role.DIAGONAL_BRACE),
                        Bar(j057, j071, role=Role.DIAGONAL_BRACE),
                        Bar(j071, j051, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        peaks=(
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j015, j011, role=Role.CHORD),
                        Bar(j011, j008, role=Role.CHORD),
                        Bar(j008, j005, role=Role.CHORD),
                        Bar(j005, j001, role=Role.CHORD),
                        Bar(j001, j003, role=Role.CHORD),
                        Bar(j003, j007, role=Role.CHORD),
                        Bar(j007, j013, role=Role.CHORD),
                        Bar(j013, j018, role=Role.CHORD),
                        Bar(j018, j020, role=Role.CHORD),
                        Bar(j015, j018, role=Role.DIAGONAL_BRACE),
                        Bar(j018, j011, role=Role.TRANSVERSE_BRACE),
                        Bar(j011, j013, role=Role.DIAGONAL_BRACE),
                        Bar(j013, j008, role=Role.DIAGONAL_BRACE),
                        Bar(j008, j007, role=Role.TRANSVERSE_BRACE),
                        Bar(j007, j005, role=Role.DIAGONAL_BRACE),
                        Bar(j005, j003, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j016, j012, role=Role.CHORD),
                        Bar(j012, j009, role=Role.CHORD),
                        Bar(j009, j006, role=Role.CHORD),
                        Bar(j006, j002, role=Role.CHORD),
                        Bar(j002, j004, role=Role.CHORD),
                        Bar(j004, j010, role=Role.CHORD),
                        Bar(j010, j014, role=Role.CHORD),
                        Bar(j014, j019, role=Role.CHORD),
                        Bar(j019, j021, role=Role.CHORD),
                        Bar(j016, j019, role=Role.DIAGONAL_BRACE),
                        Bar(j019, j012, role=Role.TRANSVERSE_BRACE),
                        Bar(j012, j014, role=Role.DIAGONAL_BRACE),
                        Bar(j014, j009, role=Role.DIAGONAL_BRACE),
                        Bar(j009, j010, role=Role.TRANSVERSE_BRACE),
                        Bar(j010, j006, role=Role.DIAGONAL_BRACE),
                        Bar(j006, j004, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
    )


D_2_D_2018_3_T1 = _d_2_d_2018_3_t1()


def _d_2_d_2018_3_t2() -> Tower[LowestCrossarm]:
    """D-2-D-2018.3 T2: each joint written once, by its key."""
    j001 = Point(m(-6.5), m(0), m(17.5))
    j002 = Point(m(6.5), m(0), m(17.5))
    j003 = Point(m(-6.24), m(0), m(17.18))
    j004 = Point(m(6.24), m(0), m(17.18))
    j005 = Point(m(-5.7), m(0), m(17.13))
    j006 = Point(m(5.7), m(0), m(17.13))
    j007 = Point(m(-5.7), m(0), m(16.6))
    j008 = Point(m(-4.42), m(0), m(16.6))
    j009 = Point(m(4.42), m(0), m(16.6))
    j010 = Point(m(5.7), m(0), m(16.6))
    j011 = Point(m(-3.13), m(0), m(16.07))
    j012 = Point(m(3.13), m(0), m(16.07))
    j013 = Point(m(-4.53), m(0), m(15.44))
    j014 = Point(m(4.53), m(0), m(15.44))
    j015 = Point(m(-1.18), m(0), m(15.36))
    j016 = Point(m(1.18), m(0), m(15.36))
    j017 = Point(m(-0.01), m(0), m(15.02))
    j018 = Point(m(-3.29), m(0), m(14.4))
    j019 = Point(m(3.29), m(0), m(14.4))
    j020 = Point(m(-1.44), m(0), m(13.03))
    j021 = Point(m(1.44), m(0), m(13.03))
    j022 = Point(m(-6.93), m(0), m(11.94))
    j023 = Point(m(6.93), m(0), m(11.94))
    j024 = Point(m(-4.18), m(0), m(11.51))
    j025 = Point(m(-1.52), m(0), m(11.51))
    j026 = Point(m(1.51), m(0), m(11.51))
    j027 = Point(m(4.18), m(0), m(11.51))
    j028 = Point(m(-10.5), m(0), m(11.22))
    j029 = Point(m(10.5), m(0), m(11.22))
    j030 = Point(m(-14.07), m(0), m(10.5))
    j031 = Point(m(14.07), m(0), m(10.5))
    j032 = Point(m(-14.07), m(0), m(10))
    j033 = Point(m(-12.28), m(0), m(10))
    j034 = Point(m(-10.5), m(0), m(10))
    j035 = Point(m(-8.72), m(0), m(10))
    j036 = Point(m(-6.93), m(0), m(10))
    j037 = Point(m(-4.18), m(0), m(10))
    j038 = Point(m(-1.59), m(0), m(10))
    j039 = Point(m(1.58), m(0), m(10))
    j040 = Point(m(4.18), m(0), m(10))
    j041 = Point(m(6.93), m(0), m(10))
    j042 = Point(m(8.72), m(0), m(10))
    j043 = Point(m(10.5), m(0), m(10))
    j044 = Point(m(12.28), m(0), m(10))
    j045 = Point(m(14.07), m(0), m(10))
    j046 = Point(m(-1.69), m(0), m(8.01))
    j047 = Point(m(1.68), m(0), m(8.01))
    j048 = Point(m(-1.78), m(0), m(6.01))
    j049 = Point(m(1.78), m(0), m(6.01))
    j050 = Point(m(-1.88), m(0), m(4))
    j051 = Point(m(1.88), m(0), m(4))
    j052 = Point(m(-10.51), m(0), m(2.09))
    j053 = Point(m(10.51), m(0), m(2.09))
    j054 = Point(m(-1.96), m(0), m(2))
    j055 = Point(m(1.96), m(0), m(2))
    j056 = Point(m(-7.2), m(0), m(1.49))
    j057 = Point(m(7.2), m(0), m(1.49))
    j058 = Point(m(-13.8), m(0), m(1.31))
    j059 = Point(m(13.8), m(0), m(1.31))
    j060 = Point(m(-17.29), m(0), m(0.5))
    j061 = Point(m(17.29), m(0), m(0.5))
    j062 = Point(m(-17.29), m(0), m(0))
    j063 = Point(m(-15.52), m(0), m(0))
    j064 = Point(m(-13.8), m(0), m(0))
    j065 = Point(m(-10.89), m(0), m(0))
    j066 = Point(m(-10.11), m(0), m(0))
    j067 = Point(m(-7.2), m(0), m(0))
    j068 = Point(m(-3.41), m(0), m(0))
    j069 = Point(m(-2.05), m(0), m(0))
    j070 = Point(m(2.05), m(0), m(0))
    j071 = Point(m(3.41), m(0), m(0))
    j072 = Point(m(7.2), m(0), m(0))
    j073 = Point(m(10.11), m(0), m(0))
    j074 = Point(m(10.89), m(0), m(0))
    j075 = Point(m(13.8), m(0), m(0))
    j076 = Point(m(15.52), m(0), m(0))
    j077 = Point(m(17.29), m(0), m(0))
    j078 = Point(m(-10.51), m(0), m(-0.46))
    j079 = Point(m(10.51), m(0), m(-0.46))
    j080 = Point(m(-2.17), m(0), m(-2.95))
    j081 = Point(m(2.17), m(0), m(-2.95))
    j082 = Point(m(-2.29), m(0), m(-6.26))
    j083 = Point(m(2.29), m(0), m(-6.26))
    j084 = Point(m(-2.45), m(0), m(-10.24))
    j085 = Point(m(2.45), m(0), m(-10.24))
    j086 = Point(m(-2.61), m(0), m(-14.46))
    j087 = Point(m(2.61), m(0), m(-14.46))
    j088 = Point(m(-2.79), m(0), m(-18.96))
    j089 = Point(m(2.79), m(0), m(-18.96))
    j090 = Point(m(-3.19), m(0), m(-21.52))
    j091 = Point(m(-0.01), m(0), m(-21.52))
    j092 = Point(m(3.19), m(0), m(-21.52))
    j093 = Point(m(-3.46), m(0), m(-23.23))
    j094 = Point(m(-1.86), m(0), m(-23.23))
    j095 = Point(m(1.86), m(0), m(-23.23))
    j096 = Point(m(3.46), m(0), m(-23.23))
    j097 = Point(m(-3.72), m(0), m(-24.93))
    j098 = Point(m(3.72), m(0), m(-24.93))
    j099 = Point(m(-4.1), m(0), m(-27.39))
    j100 = Point(m(-1.56), m(0), m(-27.39))
    j101 = Point(m(1.56), m(0), m(-27.39))
    j102 = Point(m(4.1), m(0), m(-27.39))
    j103 = Point(m(-4.37), m(0), m(-29.09))
    j104 = Point(m(-0.01), m(0), m(-29.09))
    j105 = Point(m(4.37), m(0), m(-29.09))
    j106 = Point(m(-4.68), m(0), m(-31.06))
    j107 = Point(m(-1.77), m(0), m(-31.06))
    j108 = Point(m(1.77), m(0), m(-31.06))
    j109 = Point(m(4.68), m(0), m(-31.06))
    j110 = Point(m(-4.98), m(0), m(-33.02))
    j111 = Point(m(-3.53), m(0), m(-33.02))
    j112 = Point(m(3.53), m(0), m(-33.02))
    j113 = Point(m(4.98), m(0), m(-33.02))
    j114 = Point(m(-5.29), m(0), m(-35))
    j115 = Point(m(5.29), m(0), m(-35))
    return Tower(
        name="D-2-D-2018.3 T2",
        datum=LowestCrossarm((m(35), m(38), m(41), m(44))),
        voltages=(kv(380),),
        line_angles=(),
        attachments=(
            Mount(Wire.SHIELD, Point(m(-6.5), m(0), m(17.5)), Hold.CLAMP),
            Mount(Wire.SHIELD, Point(m(6.5), m(0), m(17.5)), Hold.CLAMP),
            WirePosition(
                Wire.PHASE,
                Point(m(-10.5), m(0), m(6.55)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j032),
                    InsulatorString(mount=j036),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(10.5), m(0), m(6.55)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j041),
                    InsulatorString(mount=j045),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(-13.8), m(0), m(-3.92)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j062),
                    InsulatorString(mount=j078),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(-7.2), m(0), m(-3.92)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j078),
                    InsulatorString(mount=j068),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(7.2), m(0), m(-3.92)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j079),
                    InsulatorString(mount=j071),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(13.8), m(0), m(-3.92)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j077),
                    InsulatorString(mount=j079),
                ),
            ),
        ),
        bases=(),
        body=(
            Body(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j104, j105, role=Role.TRANSVERSE_BRACE),
                        Bar(j070, j080, role=Role.DIAGONAL_BRACE),
                        Bar(j080, j083, role=Role.DIAGONAL_BRACE),
                        Bar(j083, j084, role=Role.DIAGONAL_BRACE),
                        Bar(j085, j082, role=Role.DIAGONAL_BRACE),
                        Bar(j082, j081, role=Role.DIAGONAL_BRACE),
                        Bar(j081, j069, role=Role.DIAGONAL_BRACE),
                        Bar(j088, j086, role=Role.CHORD),
                        Bar(j086, j084, role=Role.CHORD),
                        Bar(j084, j082, role=Role.CHORD),
                        Bar(j082, j080, role=Role.CHORD),
                        Bar(j080, j069, role=Role.CHORD),
                        Bar(j069, j054, role=Role.CHORD),
                        Bar(j054, j050, role=Role.CHORD),
                        Bar(j051, j055, role=Role.CHORD),
                        Bar(j055, j070, role=Role.CHORD),
                        Bar(j070, j081, role=Role.CHORD),
                        Bar(j081, j083, role=Role.CHORD),
                        Bar(j083, j085, role=Role.CHORD),
                        Bar(j085, j087, role=Role.CHORD),
                        Bar(j087, j089, role=Role.CHORD),
                        Bar(j070, j054, role=Role.DIAGONAL_BRACE),
                        Bar(j054, j051, role=Role.DIAGONAL_BRACE),
                        Bar(j050, j055, role=Role.DIAGONAL_BRACE),
                        Bar(j055, j069, role=Role.DIAGONAL_BRACE),
                        Bar(j050, j048, role=Role.CHORD),
                        Bar(j048, j046, role=Role.CHORD),
                        Bar(j046, j038, role=Role.CHORD),
                        Bar(j038, j025, role=Role.CHORD),
                        Bar(j025, j020, role=Role.CHORD),
                        Bar(j039, j025, role=Role.DIAGONAL_BRACE),
                        Bar(j025, j021, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j026, role=Role.CHORD),
                        Bar(j026, j039, role=Role.CHORD),
                        Bar(j039, j047, role=Role.CHORD),
                        Bar(j047, j049, role=Role.CHORD),
                        Bar(j049, j051, role=Role.CHORD),
                        Bar(j038, j026, role=Role.DIAGONAL_BRACE),
                        Bar(j026, j020, role=Role.DIAGONAL_BRACE),
                        Bar(j038, j047, role=Role.DIAGONAL_BRACE),
                        Bar(j047, j048, role=Role.DIAGONAL_BRACE),
                        Bar(j048, j051, role=Role.DIAGONAL_BRACE),
                        Bar(j050, j049, role=Role.DIAGONAL_BRACE),
                        Bar(j049, j046, role=Role.DIAGONAL_BRACE),
                        Bar(j046, j039, role=Role.DIAGONAL_BRACE),
                        Bar(j104, j098, role=Role.DIAGONAL_BRACE),
                        Bar(j108, j104, role=Role.DIAGONAL_BRACE),
                        Bar(j095, j091, role=Role.DIAGONAL_BRACE),
                        Bar(j091, j089, role=Role.DIAGONAL_BRACE),
                        Bar(j091, j092, role=Role.TRANSVERSE_BRACE),
                        Bar(j088, j087, role=Role.DIAGONAL_BRACE),
                        Bar(j087, j084, role=Role.DIAGONAL_BRACE),
                        Bar(j089, j086, role=Role.DIAGONAL_BRACE),
                        Bar(j086, j085, role=Role.DIAGONAL_BRACE),
                        Bar(j070, j069, role=Role.TRANSVERSE_BRACE),
                        Bar(j039, j038, role=Role.TRANSVERSE_BRACE),
                        Bar(j021, j020, role=Role.TRANSVERSE_BRACE),
                        Bar(j051, j050, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        legs=(
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j114, j110, role=Role.CHORD),
                        Bar(j110, j106, role=Role.CHORD),
                        Bar(j106, j103, role=Role.CHORD),
                        Bar(j103, j099, role=Role.CHORD),
                        Bar(j099, j097, role=Role.CHORD),
                        Bar(j097, j093, role=Role.CHORD),
                        Bar(j093, j090, role=Role.CHORD),
                        Bar(j090, j088, role=Role.CHORD),
                        Bar(j103, j104, role=Role.TRANSVERSE_BRACE),
                        Bar(j114, j111, role=Role.DIAGONAL_BRACE),
                        Bar(j111, j107, role=Role.DIAGONAL_BRACE),
                        Bar(j107, j104, role=Role.DIAGONAL_BRACE),
                        Bar(j104, j100, role=Role.DIAGONAL_BRACE),
                        Bar(j100, j097, role=Role.DIAGONAL_BRACE),
                        Bar(j091, j088, role=Role.DIAGONAL_BRACE),
                        Bar(j097, j094, role=Role.DIAGONAL_BRACE),
                        Bar(j094, j091, role=Role.DIAGONAL_BRACE),
                        Bar(j111, j110, role=Role.TRANSVERSE_BRACE),
                        Bar(j107, j106, role=Role.TRANSVERSE_BRACE),
                        Bar(j100, j099, role=Role.TRANSVERSE_BRACE),
                        Bar(j111, j106, role=Role.DIAGONAL_BRACE),
                        Bar(j107, j103, role=Role.DIAGONAL_BRACE),
                        Bar(j103, j100, role=Role.DIAGONAL_BRACE),
                        Bar(j094, j093, role=Role.TRANSVERSE_BRACE),
                        Bar(j094, j090, role=Role.DIAGONAL_BRACE),
                        Bar(j090, j091, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j089, j092, role=Role.CHORD),
                        Bar(j092, j096, role=Role.CHORD),
                        Bar(j096, j098, role=Role.CHORD),
                        Bar(j098, j102, role=Role.CHORD),
                        Bar(j102, j105, role=Role.CHORD),
                        Bar(j105, j109, role=Role.CHORD),
                        Bar(j109, j113, role=Role.CHORD),
                        Bar(j113, j115, role=Role.CHORD),
                        Bar(j115, j112, role=Role.DIAGONAL_BRACE),
                        Bar(j112, j108, role=Role.DIAGONAL_BRACE),
                        Bar(j098, j095, role=Role.DIAGONAL_BRACE),
                        Bar(j092, j095, role=Role.DIAGONAL_BRACE),
                        Bar(j095, j096, role=Role.TRANSVERSE_BRACE),
                        Bar(j113, j112, role=Role.TRANSVERSE_BRACE),
                        Bar(j112, j109, role=Role.DIAGONAL_BRACE),
                        Bar(j109, j108, role=Role.TRANSVERSE_BRACE),
                        Bar(j108, j105, role=Role.DIAGONAL_BRACE),
                        Bar(j105, j101, role=Role.DIAGONAL_BRACE),
                        Bar(j101, j102, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        head=(
            Head(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j021, j017, role=Role.DIAGONAL_BRACE),
                        Bar(j017, j020, role=Role.DIAGONAL_BRACE),
                        Bar(j015, j017, role=Role.DIAGONAL_BRACE),
                        Bar(j020, j015, role=Role.CHORD),
                        Bar(j017, j016, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j016, role=Role.CHORD),
                    ),
                )
            ),
        ),
        crossarms=(
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j038, j037, role=Role.CHORD),
                        Bar(j037, j036, role=Role.CHORD),
                        Bar(j036, j035, role=Role.CHORD),
                        Bar(j035, j034, role=Role.CHORD),
                        Bar(j034, j033, role=Role.CHORD),
                        Bar(j033, j032, role=Role.CHORD),
                        Bar(j020, j022, role=Role.CHORD),
                        Bar(j022, j028, role=Role.CHORD),
                        Bar(j028, j030, role=Role.CHORD),
                        Bar(j030, j032, role=Role.CHORD),
                        Bar(j020, j024, role=Role.DIAGONAL_BRACE),
                        Bar(j024, j036, role=Role.DIAGONAL_BRACE),
                        Bar(j036, j022, role=Role.TRANSVERSE_BRACE),
                        Bar(j038, j024, role=Role.DIAGONAL_BRACE),
                        Bar(j024, j037, role=Role.TRANSVERSE_BRACE),
                        Bar(j034, j028, role=Role.TRANSVERSE_BRACE),
                        Bar(j022, j035, role=Role.DIAGONAL_BRACE),
                        Bar(j035, j028, role=Role.DIAGONAL_BRACE),
                        Bar(j028, j033, role=Role.DIAGONAL_BRACE),
                        Bar(j033, j030, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j045, j044, role=Role.CHORD),
                        Bar(j044, j043, role=Role.CHORD),
                        Bar(j043, j042, role=Role.CHORD),
                        Bar(j042, j041, role=Role.CHORD),
                        Bar(j041, j040, role=Role.CHORD),
                        Bar(j040, j039, role=Role.CHORD),
                        Bar(j021, j023, role=Role.CHORD),
                        Bar(j023, j029, role=Role.CHORD),
                        Bar(j029, j031, role=Role.CHORD),
                        Bar(j031, j045, role=Role.CHORD),
                        Bar(j021, j027, role=Role.DIAGONAL_BRACE),
                        Bar(j027, j041, role=Role.DIAGONAL_BRACE),
                        Bar(j041, j023, role=Role.TRANSVERSE_BRACE),
                        Bar(j039, j027, role=Role.DIAGONAL_BRACE),
                        Bar(j027, j040, role=Role.TRANSVERSE_BRACE),
                        Bar(j043, j029, role=Role.TRANSVERSE_BRACE),
                        Bar(j023, j042, role=Role.DIAGONAL_BRACE),
                        Bar(j042, j029, role=Role.DIAGONAL_BRACE),
                        Bar(j029, j044, role=Role.DIAGONAL_BRACE),
                        Bar(j044, j031, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j069, j068, role=Role.TRANSVERSE_BRACE),
                        Bar(j068, j067, role=Role.TRANSVERSE_BRACE),
                        Bar(j067, j066, role=Role.TRANSVERSE_BRACE),
                        Bar(j066, j065, role=Role.TRANSVERSE_BRACE),
                        Bar(j065, j064, role=Role.TRANSVERSE_BRACE),
                        Bar(j064, j063, role=Role.TRANSVERSE_BRACE),
                        Bar(j063, j062, role=Role.TRANSVERSE_BRACE),
                        Bar(j050, j052, role=Role.CHORD),
                        Bar(j052, j058, role=Role.CHORD),
                        Bar(j058, j060, role=Role.CHORD),
                        Bar(j060, j062, role=Role.CHORD),
                        Bar(j078, j065, role=Role.DIAGONAL_BRACE),
                        Bar(j065, j052, role=Role.DIAGONAL_BRACE),
                        Bar(j052, j066, role=Role.DIAGONAL_BRACE),
                        Bar(j066, j078, role=Role.DIAGONAL_BRACE),
                        Bar(j064, j058, role=Role.TRANSVERSE_BRACE),
                        Bar(j067, j056, role=Role.TRANSVERSE_BRACE),
                        Bar(j056, j068, role=Role.DIAGONAL_BRACE),
                        Bar(j068, j050, role=Role.DIAGONAL_BRACE),
                        Bar(j050, j056, role=Role.DIAGONAL_BRACE),
                        Bar(j056, j066, role=Role.DIAGONAL_BRACE),
                        Bar(j065, j058, role=Role.DIAGONAL_BRACE),
                        Bar(j058, j063, role=Role.DIAGONAL_BRACE),
                        Bar(j063, j060, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j077, j076, role=Role.TRANSVERSE_BRACE),
                        Bar(j076, j075, role=Role.TRANSVERSE_BRACE),
                        Bar(j075, j074, role=Role.TRANSVERSE_BRACE),
                        Bar(j074, j073, role=Role.TRANSVERSE_BRACE),
                        Bar(j073, j072, role=Role.TRANSVERSE_BRACE),
                        Bar(j072, j071, role=Role.TRANSVERSE_BRACE),
                        Bar(j071, j070, role=Role.TRANSVERSE_BRACE),
                        Bar(j061, j077, role=Role.CHORD),
                        Bar(j079, j074, role=Role.DIAGONAL_BRACE),
                        Bar(j074, j053, role=Role.DIAGONAL_BRACE),
                        Bar(j053, j073, role=Role.DIAGONAL_BRACE),
                        Bar(j073, j079, role=Role.DIAGONAL_BRACE),
                        Bar(j075, j059, role=Role.TRANSVERSE_BRACE),
                        Bar(j072, j057, role=Role.TRANSVERSE_BRACE),
                        Bar(j074, j059, role=Role.DIAGONAL_BRACE),
                        Bar(j059, j076, role=Role.DIAGONAL_BRACE),
                        Bar(j076, j061, role=Role.DIAGONAL_BRACE),
                        Bar(j061, j059, role=Role.CHORD),
                        Bar(j059, j053, role=Role.CHORD),
                        Bar(j053, j051, role=Role.CHORD),
                        Bar(j051, j057, role=Role.DIAGONAL_BRACE),
                        Bar(j057, j073, role=Role.DIAGONAL_BRACE),
                        Bar(j057, j071, role=Role.DIAGONAL_BRACE),
                        Bar(j071, j051, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        peaks=(
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j020, j018, role=Role.CHORD),
                        Bar(j018, j013, role=Role.CHORD),
                        Bar(j013, j007, role=Role.CHORD),
                        Bar(j007, j003, role=Role.CHORD),
                        Bar(j003, j001, role=Role.CHORD),
                        Bar(j001, j005, role=Role.CHORD),
                        Bar(j005, j008, role=Role.CHORD),
                        Bar(j008, j011, role=Role.CHORD),
                        Bar(j011, j015, role=Role.CHORD),
                        Bar(j015, j018, role=Role.DIAGONAL_BRACE),
                        Bar(j018, j011, role=Role.TRANSVERSE_BRACE),
                        Bar(j011, j013, role=Role.DIAGONAL_BRACE),
                        Bar(j013, j008, role=Role.DIAGONAL_BRACE),
                        Bar(j008, j007, role=Role.TRANSVERSE_BRACE),
                        Bar(j007, j005, role=Role.DIAGONAL_BRACE),
                        Bar(j005, j003, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j016, j012, role=Role.CHORD),
                        Bar(j012, j009, role=Role.CHORD),
                        Bar(j009, j006, role=Role.CHORD),
                        Bar(j006, j002, role=Role.CHORD),
                        Bar(j002, j004, role=Role.CHORD),
                        Bar(j004, j010, role=Role.CHORD),
                        Bar(j010, j014, role=Role.CHORD),
                        Bar(j014, j019, role=Role.CHORD),
                        Bar(j019, j021, role=Role.CHORD),
                        Bar(j016, j019, role=Role.DIAGONAL_BRACE),
                        Bar(j019, j012, role=Role.TRANSVERSE_BRACE),
                        Bar(j012, j014, role=Role.DIAGONAL_BRACE),
                        Bar(j014, j009, role=Role.DIAGONAL_BRACE),
                        Bar(j009, j010, role=Role.TRANSVERSE_BRACE),
                        Bar(j010, j006, role=Role.DIAGONAL_BRACE),
                        Bar(j006, j004, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
    )


D_2_D_2018_3_T2 = _d_2_d_2018_3_t2()


def _d_2_d_2018_3_wa120() -> Tower[LowestCrossarm]:
    """D-2-D-2018.3 WA120: each joint written once, by its key."""
    j001 = Point(m(-8.6), m(0), m(20.5))
    j002 = Point(m(8.6), m(0), m(20.5))
    j003 = Point(m(-8.46), m(0), m(20.04))
    j004 = Point(m(8.49), m(0), m(19.99))
    j005 = Point(m(-7.68), m(0), m(19.8))
    j006 = Point(m(7.72), m(0), m(19.76))
    j007 = Point(m(-6.17), m(0), m(18.86))
    j008 = Point(m(6.19), m(0), m(18.82))
    j009 = Point(m(-7.76), m(0), m(18.56))
    j010 = Point(m(7.78), m(0), m(18.52))
    j011 = Point(m(-4.28), m(0), m(17.88))
    j012 = Point(m(4.3), m(0), m(17.86))
    j013 = Point(m(-6.51), m(0), m(16.95))
    j014 = Point(m(6.53), m(0), m(16.93))
    j015 = Point(m(-1.63), m(0), m(16.81))
    j016 = Point(m(1.66), m(0), m(16.81))
    j017 = Point(m(0.01), m(0), m(16.35))
    j018 = Point(m(-4.74), m(0), m(15.3))
    j019 = Point(m(4.75), m(0), m(15.29))
    j020 = Point(m(-2.08), m(0), m(13.41))
    j021 = Point(m(2.1), m(0), m(13.41))
    j022 = Point(m(-7.17), m(0), m(12.24))
    j023 = Point(m(7.16), m(0), m(12.24))
    j024 = Point(m(-9.38), m(0), m(11.74))
    j025 = Point(m(9.37), m(0), m(11.74))
    j026 = Point(m(-2.19), m(0), m(11.7))
    j027 = Point(m(2.2), m(0), m(11.7))
    j028 = Point(m(-4.73), m(0), m(11.65))
    j029 = Point(m(4.73), m(0), m(11.65))
    j030 = Point(m(-13.07), m(0), m(10.89))
    j031 = Point(m(13.05), m(0), m(10.89))
    j032 = Point(m(-13.95), m(0), m(10.69))
    j033 = Point(m(13.94), m(0), m(10.69))
    j034 = Point(m(-11.69), m(0), m(10.02))
    j035 = Point(m(11.67), m(0), m(10.02))
    j036 = Point(m(-13.5), m(0), m(10))
    j037 = Point(m(13.5), m(0), m(10))
    j038 = Point(m(-13.94), m(0), m(10))
    j039 = Point(m(-13.07), m(0), m(10))
    j040 = Point(m(-11.6), m(0), m(10))
    j041 = Point(m(-9.39), m(0), m(10))
    j042 = Point(m(-7.18), m(0), m(10))
    j043 = Point(m(-4.74), m(0), m(10))
    j044 = Point(m(-2.29), m(0), m(10))
    j045 = Point(m(2.29), m(0), m(10))
    j046 = Point(m(4.74), m(0), m(10))
    j047 = Point(m(7.17), m(0), m(10))
    j048 = Point(m(9.37), m(0), m(10))
    j049 = Point(m(11.58), m(0), m(10))
    j050 = Point(m(13.05), m(0), m(10))
    j051 = Point(m(13.94), m(0), m(10))
    j052 = Point(m(-2.43), m(0), m(8.01))
    j053 = Point(m(2.43), m(0), m(8.01))
    j054 = Point(m(-2.56), m(0), m(6.01))
    j055 = Point(m(2.57), m(0), m(6.01))
    j056 = Point(m(-2.7), m(0), m(4))
    j057 = Point(m(2.7), m(0), m(4))
    j058 = Point(m(-10.01), m(0), m(2.61))
    j059 = Point(m(9.99), m(0), m(2.61))
    j060 = Point(m(-6.36), m(0), m(2))
    j061 = Point(m(-2.84), m(0), m(2))
    j062 = Point(m(2.84), m(0), m(2))
    j063 = Point(m(6.35), m(0), m(2))
    j064 = Point(m(-12.47), m(0), m(1.94))
    j065 = Point(m(12.46), m(0), m(1.94))
    j066 = Point(m(-16.65), m(0), m(0.79))
    j067 = Point(m(16.65), m(0), m(0.79))
    j068 = Point(m(-17.36), m(0), m(0.6))
    j069 = Point(m(17.34), m(0), m(0.6))
    j070 = Point(m(-17.36), m(0), m(0))
    j071 = Point(m(-16.65), m(0), m(0))
    j072 = Point(m(-15.5), m(0), m(0))
    j073 = Point(m(-12.47), m(0), m(0))
    j074 = Point(m(-10), m(0), m(0))
    j075 = Point(m(-6.36), m(0), m(0))
    j076 = Point(m(-2.98), m(0), m(0))
    j077 = Point(m(2.98), m(0), m(0))
    j078 = Point(m(6.35), m(0), m(0))
    j079 = Point(m(10), m(0), m(0))
    j080 = Point(m(12.46), m(0), m(0))
    j081 = Point(m(15.48), m(0), m(0))
    j082 = Point(m(16.65), m(0), m(0))
    j083 = Point(m(17.34), m(0), m(0))
    j084 = Point(m(-17), m(0), m(0))
    j085 = Point(m(17), m(0), m(0))
    j086 = Point(m(-3.16), m(0), m(-2.31))
    j087 = Point(m(3.16), m(0), m(-2.31))
    j088 = Point(m(-3.35), m(0), m(-4.71))
    j089 = Point(m(3.35), m(0), m(-4.71))
    j090 = Point(m(-3.57), m(0), m(-7.38))
    j091 = Point(m(3.57), m(0), m(-7.38))
    j092 = Point(m(-1.78), m(0), m(-8.58))
    j093 = Point(m(1.8), m(0), m(-8.58))
    j094 = Point(m(-3.76), m(0), m(-9.78))
    j095 = Point(m(0.01), m(0), m(-9.78))
    j096 = Point(m(3.76), m(0), m(-9.78))
    j097 = Point(m(-1.89), m(0), m(-11.04))
    j098 = Point(m(1.99), m(0), m(-11.11))
    j099 = Point(m(-3.97), m(0), m(-12.45))
    j100 = Point(m(3.97), m(0), m(-12.45))
    j101 = Point(m(-4.22), m(0), m(-13.36))
    j102 = Point(m(-1.99), m(0), m(-13.36))
    j103 = Point(m(1.99), m(0), m(-13.36))
    j104 = Point(m(4.22), m(0), m(-13.36))
    j105 = Point(m(-4.47), m(0), m(-14.28))
    j106 = Point(m(0.01), m(0), m(-14.28))
    j107 = Point(m(4.47), m(0), m(-14.28))
    j108 = Point(m(-4.78), m(0), m(-15.41))
    j109 = Point(m(-2.48), m(0), m(-15.41))
    j110 = Point(m(2.48), m(0), m(-15.41))
    j111 = Point(m(4.78), m(0), m(-15.41))
    j112 = Point(m(-4.97), m(0), m(-16.55))
    j113 = Point(m(4.97), m(0), m(-16.55))
    j114 = Point(m(-5.52), m(0), m(-18.08))
    j115 = Point(m(-2.48), m(0), m(-18.08))
    j116 = Point(m(2.48), m(0), m(-18.08))
    j117 = Point(m(5.52), m(0), m(-18.08))
    j118 = Point(m(-5.92), m(0), m(-19.54))
    j119 = Point(m(5.92), m(0), m(-19.54))
    j120 = Point(m(-6.3), m(0), m(-20.95))
    j121 = Point(m(-2.18), m(0), m(-20.95))
    j122 = Point(m(2.18), m(0), m(-20.95))
    j123 = Point(m(6.3), m(0), m(-20.95))
    j124 = Point(m(-6.63), m(0), m(-22.13))
    j125 = Point(m(-4.1), m(0), m(-22.13))
    j126 = Point(m(4.1), m(0), m(-22.13))
    j127 = Point(m(6.63), m(0), m(-22.13))
    j128 = Point(m(-7.14), m(0), m(-24))
    j129 = Point(m(7.14), m(0), m(-24))
    return Tower(
        name="D-2-D-2018.3 WA120",
        datum=LowestCrossarm((m(24), m(30), m(33), m(36), m(39), m(45))),
        voltages=(kv(380),),
        line_angles=(),
        attachments=(
            Mount(Wire.SHIELD, Point(m(-8.6), m(0), m(20.5)), Hold.CLAMP),
            Mount(Wire.SHIELD, Point(m(8.6), m(0), m(20.5)), Hold.CLAMP),
            Mount(Wire.PHASE, Point(m(-13.5), m(0), m(10)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(13.5), m(0), m(10)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-17), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-10), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(10), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(17), m(0), m(0)), Hold.STRAIN),
        ),
        bases=(),
        body=(
            Body(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j121, j116, role=Role.DIAGONAL_BRACE),
                        Bar(j122, j115, role=Role.DIAGONAL_BRACE),
                        Bar(j119, j118, role=Role.TRANSVERSE_BRACE),
                        Bar(j020, j021, role=Role.TRANSVERSE_BRACE),
                        Bar(j044, j045, role=Role.TRANSVERSE_BRACE),
                        Bar(j076, j077, role=Role.TRANSVERSE_BRACE),
                        Bar(j056, j057, role=Role.TRANSVERSE_BRACE),
                        Bar(j077, j086, role=Role.DIAGONAL_BRACE),
                        Bar(j086, j089, role=Role.DIAGONAL_BRACE),
                        Bar(j089, j090, role=Role.DIAGONAL_BRACE),
                        Bar(j091, j088, role=Role.DIAGONAL_BRACE),
                        Bar(j088, j087, role=Role.DIAGONAL_BRACE),
                        Bar(j087, j076, role=Role.DIAGONAL_BRACE),
                        Bar(j094, j095, role=Role.TRANSVERSE_BRACE),
                        Bar(j095, j096, role=Role.TRANSVERSE_BRACE),
                        Bar(j100, j098, role=Role.DIAGONAL_BRACE),
                        Bar(j098, j095, role=Role.DIAGONAL_BRACE),
                        Bar(j095, j092, role=Role.DIAGONAL_BRACE),
                        Bar(j092, j090, role=Role.DIAGONAL_BRACE),
                        Bar(j099, j097, role=Role.DIAGONAL_BRACE),
                        Bar(j097, j095, role=Role.DIAGONAL_BRACE),
                        Bar(j095, j093, role=Role.DIAGONAL_BRACE),
                        Bar(j093, j091, role=Role.DIAGONAL_BRACE),
                        Bar(j092, j094, role=Role.DIAGONAL_BRACE),
                        Bar(j094, j097, role=Role.DIAGONAL_BRACE),
                        Bar(j093, j096, role=Role.DIAGONAL_BRACE),
                        Bar(j096, j098, role=Role.DIAGONAL_BRACE),
                        Bar(j106, j102, role=Role.DIAGONAL_BRACE),
                        Bar(j109, j106, role=Role.DIAGONAL_BRACE),
                        Bar(j106, j105, role=Role.TRANSVERSE_BRACE),
                        Bar(j099, j094, role=Role.CHORD),
                        Bar(j094, j090, role=Role.CHORD),
                        Bar(j090, j088, role=Role.CHORD),
                        Bar(j088, j086, role=Role.CHORD),
                        Bar(j086, j076, role=Role.CHORD),
                        Bar(j076, j061, role=Role.CHORD),
                        Bar(j061, j056, role=Role.CHORD),
                        Bar(j057, j061, role=Role.DIAGONAL_BRACE),
                        Bar(j061, j077, role=Role.DIAGONAL_BRACE),
                        Bar(j077, j087, role=Role.CHORD),
                        Bar(j087, j089, role=Role.CHORD),
                        Bar(j089, j091, role=Role.CHORD),
                        Bar(j091, j096, role=Role.CHORD),
                        Bar(j096, j100, role=Role.CHORD),
                        Bar(j056, j062, role=Role.DIAGONAL_BRACE),
                        Bar(j062, j076, role=Role.DIAGONAL_BRACE),
                        Bar(j056, j054, role=Role.CHORD),
                        Bar(j054, j052, role=Role.CHORD),
                        Bar(j052, j044, role=Role.CHORD),
                        Bar(j044, j026, role=Role.CHORD),
                        Bar(j026, j020, role=Role.CHORD),
                        Bar(j045, j026, role=Role.DIAGONAL_BRACE),
                        Bar(j026, j021, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j027, role=Role.CHORD),
                        Bar(j027, j045, role=Role.CHORD),
                        Bar(j045, j053, role=Role.CHORD),
                        Bar(j053, j055, role=Role.CHORD),
                        Bar(j055, j057, role=Role.CHORD),
                        Bar(j057, j062, role=Role.CHORD),
                        Bar(j062, j077, role=Role.CHORD),
                        Bar(j057, j054, role=Role.DIAGONAL_BRACE),
                        Bar(j054, j053, role=Role.DIAGONAL_BRACE),
                        Bar(j053, j044, role=Role.DIAGONAL_BRACE),
                        Bar(j044, j027, role=Role.DIAGONAL_BRACE),
                        Bar(j027, j020, role=Role.DIAGONAL_BRACE),
                        Bar(j056, j055, role=Role.DIAGONAL_BRACE),
                        Bar(j055, j052, role=Role.DIAGONAL_BRACE),
                        Bar(j052, j045, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        legs=(
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j128, j124, role=Role.CHORD),
                        Bar(j124, j120, role=Role.CHORD),
                        Bar(j120, j118, role=Role.CHORD),
                        Bar(j118, j114, role=Role.CHORD),
                        Bar(j114, j108, role=Role.CHORD),
                        Bar(j108, j105, role=Role.CHORD),
                        Bar(j105, j101, role=Role.CHORD),
                        Bar(j101, j099, role=Role.CHORD),
                        Bar(j128, j125, role=Role.DIAGONAL_BRACE),
                        Bar(j125, j121, role=Role.DIAGONAL_BRACE),
                        Bar(j115, j112, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j120, role=Role.TRANSVERSE_BRACE),
                        Bar(j125, j124, role=Role.TRANSVERSE_BRACE),
                        Bar(j115, j114, role=Role.TRANSVERSE_BRACE),
                        Bar(j125, j120, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j118, role=Role.DIAGONAL_BRACE),
                        Bar(j118, j115, role=Role.DIAGONAL_BRACE),
                        Bar(j102, j099, role=Role.DIAGONAL_BRACE),
                        Bar(j112, j109, role=Role.DIAGONAL_BRACE),
                        Bar(j105, j102, role=Role.DIAGONAL_BRACE),
                        Bar(j105, j109, role=Role.DIAGONAL_BRACE),
                        Bar(j108, j109, role=Role.TRANSVERSE_BRACE),
                        Bar(j101, j102, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j100, j104, role=Role.CHORD),
                        Bar(j104, j107, role=Role.CHORD),
                        Bar(j107, j111, role=Role.CHORD),
                        Bar(j111, j117, role=Role.CHORD),
                        Bar(j117, j119, role=Role.CHORD),
                        Bar(j119, j123, role=Role.CHORD),
                        Bar(j123, j127, role=Role.CHORD),
                        Bar(j127, j129, role=Role.CHORD),
                        Bar(j116, j113, role=Role.DIAGONAL_BRACE),
                        Bar(j129, j126, role=Role.DIAGONAL_BRACE),
                        Bar(j126, j122, role=Role.DIAGONAL_BRACE),
                        Bar(j122, j123, role=Role.TRANSVERSE_BRACE),
                        Bar(j126, j127, role=Role.TRANSVERSE_BRACE),
                        Bar(j116, j117, role=Role.TRANSVERSE_BRACE),
                        Bar(j126, j123, role=Role.DIAGONAL_BRACE),
                        Bar(j122, j119, role=Role.DIAGONAL_BRACE),
                        Bar(j119, j116, role=Role.DIAGONAL_BRACE),
                        Bar(j113, j110, role=Role.DIAGONAL_BRACE),
                        Bar(j110, j106, role=Role.DIAGONAL_BRACE),
                        Bar(j106, j103, role=Role.DIAGONAL_BRACE),
                        Bar(j103, j100, role=Role.DIAGONAL_BRACE),
                        Bar(j107, j106, role=Role.TRANSVERSE_BRACE),
                        Bar(j103, j107, role=Role.DIAGONAL_BRACE),
                        Bar(j107, j110, role=Role.DIAGONAL_BRACE),
                        Bar(j103, j104, role=Role.TRANSVERSE_BRACE),
                        Bar(j110, j111, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        head=(
            Head(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j015, j017, role=Role.DIAGONAL_BRACE),
                        Bar(j017, j016, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j017, role=Role.DIAGONAL_BRACE),
                        Bar(j017, j020, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j016, role=Role.CHORD),
                        Bar(j020, j015, role=Role.CHORD),
                    ),
                )
            ),
        ),
        crossarms=(
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j038, j036, role=Role.CHORD),
                        Bar(j036, j039, role=Role.CHORD),
                        Bar(j039, j034, role=Role.CHORD),
                        Bar(j034, j040, role=Role.CHORD),
                        Bar(j040, j041, role=Role.CHORD),
                        Bar(j041, j042, role=Role.CHORD),
                        Bar(j042, j043, role=Role.CHORD),
                        Bar(j043, j044, role=Role.CHORD),
                        Bar(j032, j030, role=Role.CHORD),
                        Bar(j030, j024, role=Role.CHORD),
                        Bar(j024, j022, role=Role.CHORD),
                        Bar(j022, j020, role=Role.CHORD),
                        Bar(j032, j038, role=Role.CHORD),
                        Bar(j030, j039, role=Role.TRANSVERSE_BRACE),
                        Bar(j044, j028, role=Role.DIAGONAL_BRACE),
                        Bar(j028, j043, role=Role.TRANSVERSE_BRACE),
                        Bar(j022, j042, role=Role.TRANSVERSE_BRACE),
                        Bar(j042, j028, role=Role.DIAGONAL_BRACE),
                        Bar(j028, j020, role=Role.DIAGONAL_BRACE),
                        Bar(j041, j024, role=Role.TRANSVERSE_BRACE),
                        Bar(j024, j042, role=Role.DIAGONAL_BRACE),
                        Bar(j024, j034, role=Role.DIAGONAL_BRACE),
                        Bar(j030, j034, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j045, j046, role=Role.CHORD),
                        Bar(j046, j047, role=Role.CHORD),
                        Bar(j047, j048, role=Role.CHORD),
                        Bar(j048, j049, role=Role.CHORD),
                        Bar(j049, j035, role=Role.CHORD),
                        Bar(j035, j050, role=Role.CHORD),
                        Bar(j050, j037, role=Role.CHORD),
                        Bar(j037, j051, role=Role.CHORD),
                        Bar(j051, j033, role=Role.CHORD),
                        Bar(j033, j031, role=Role.CHORD),
                        Bar(j031, j025, role=Role.CHORD),
                        Bar(j025, j023, role=Role.CHORD),
                        Bar(j023, j021, role=Role.CHORD),
                        Bar(j031, j050, role=Role.TRANSVERSE_BRACE),
                        Bar(j031, j035, role=Role.DIAGONAL_BRACE),
                        Bar(j048, j025, role=Role.TRANSVERSE_BRACE),
                        Bar(j025, j047, role=Role.DIAGONAL_BRACE),
                        Bar(j025, j035, role=Role.DIAGONAL_BRACE),
                        Bar(j023, j047, role=Role.TRANSVERSE_BRACE),
                        Bar(j047, j029, role=Role.DIAGONAL_BRACE),
                        Bar(j029, j021, role=Role.DIAGONAL_BRACE),
                        Bar(j045, j029, role=Role.DIAGONAL_BRACE),
                        Bar(j029, j046, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j070, j084, role=Role.CHORD),
                        Bar(j084, j071, role=Role.CHORD),
                        Bar(j071, j072, role=Role.CHORD),
                        Bar(j072, j073, role=Role.CHORD),
                        Bar(j073, j074, role=Role.CHORD),
                        Bar(j074, j075, role=Role.CHORD),
                        Bar(j075, j076, role=Role.CHORD),
                        Bar(j070, j068, role=Role.CHORD),
                        Bar(j068, j066, role=Role.CHORD),
                        Bar(j066, j064, role=Role.CHORD),
                        Bar(j064, j058, role=Role.CHORD),
                        Bar(j058, j056, role=Role.CHORD),
                        Bar(j066, j071, role=Role.TRANSVERSE_BRACE),
                        Bar(j056, j060, role=Role.DIAGONAL_BRACE),
                        Bar(j060, j074, role=Role.DIAGONAL_BRACE),
                        Bar(j074, j058, role=Role.TRANSVERSE_BRACE),
                        Bar(j066, j072, role=Role.DIAGONAL_BRACE),
                        Bar(j072, j064, role=Role.DIAGONAL_BRACE),
                        Bar(j064, j074, role=Role.DIAGONAL_BRACE),
                        Bar(j073, j064, role=Role.TRANSVERSE_BRACE),
                        Bar(j076, j060, role=Role.DIAGONAL_BRACE),
                        Bar(j060, j075, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j077, j078, role=Role.CHORD),
                        Bar(j078, j079, role=Role.CHORD),
                        Bar(j079, j080, role=Role.CHORD),
                        Bar(j080, j081, role=Role.CHORD),
                        Bar(j081, j082, role=Role.CHORD),
                        Bar(j082, j085, role=Role.CHORD),
                        Bar(j085, j083, role=Role.CHORD),
                        Bar(j083, j069, role=Role.CHORD),
                        Bar(j069, j067, role=Role.CHORD),
                        Bar(j067, j065, role=Role.CHORD),
                        Bar(j065, j059, role=Role.CHORD),
                        Bar(j059, j057, role=Role.CHORD),
                        Bar(j067, j082, role=Role.TRANSVERSE_BRACE),
                        Bar(j067, j081, role=Role.DIAGONAL_BRACE),
                        Bar(j081, j065, role=Role.DIAGONAL_BRACE),
                        Bar(j065, j079, role=Role.DIAGONAL_BRACE),
                        Bar(j079, j059, role=Role.TRANSVERSE_BRACE),
                        Bar(j080, j065, role=Role.TRANSVERSE_BRACE),
                        Bar(j077, j063, role=Role.DIAGONAL_BRACE),
                        Bar(j063, j078, role=Role.TRANSVERSE_BRACE),
                        Bar(j057, j063, role=Role.DIAGONAL_BRACE),
                        Bar(j063, j079, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        peaks=(
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j001, j003, role=Role.CHORD),
                        Bar(j003, j009, role=Role.CHORD),
                        Bar(j009, j013, role=Role.CHORD),
                        Bar(j013, j018, role=Role.CHORD),
                        Bar(j018, j020, role=Role.CHORD),
                        Bar(j001, j005, role=Role.CHORD),
                        Bar(j005, j007, role=Role.CHORD),
                        Bar(j007, j011, role=Role.CHORD),
                        Bar(j011, j015, role=Role.CHORD),
                        Bar(j015, j018, role=Role.DIAGONAL_BRACE),
                        Bar(j018, j011, role=Role.TRANSVERSE_BRACE),
                        Bar(j011, j013, role=Role.DIAGONAL_BRACE),
                        Bar(j013, j007, role=Role.DIAGONAL_BRACE),
                        Bar(j007, j009, role=Role.DIAGONAL_BRACE),
                        Bar(j009, j005, role=Role.DIAGONAL_BRACE),
                        Bar(j005, j003, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j016, j012, role=Role.CHORD),
                        Bar(j012, j008, role=Role.CHORD),
                        Bar(j008, j006, role=Role.CHORD),
                        Bar(j006, j002, role=Role.CHORD),
                        Bar(j002, j004, role=Role.CHORD),
                        Bar(j004, j010, role=Role.CHORD),
                        Bar(j010, j014, role=Role.CHORD),
                        Bar(j014, j019, role=Role.CHORD),
                        Bar(j019, j021, role=Role.CHORD),
                        Bar(j016, j019, role=Role.DIAGONAL_BRACE),
                        Bar(j019, j012, role=Role.TRANSVERSE_BRACE),
                        Bar(j012, j014, role=Role.DIAGONAL_BRACE),
                        Bar(j014, j008, role=Role.DIAGONAL_BRACE),
                        Bar(j008, j010, role=Role.DIAGONAL_BRACE),
                        Bar(j010, j006, role=Role.DIAGONAL_BRACE),
                        Bar(j006, j004, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
    )


D_2_D_2018_3_WA120 = _d_2_d_2018_3_wa120()


def _d_2_d_2018_3_wa140() -> Tower[LowestCrossarm]:
    """D-2-D-2018.3 WA140: each joint written once, by its key."""
    j001 = Point(m(-8.6), m(0), m(20))
    j002 = Point(m(8.6), m(0), m(20))
    j003 = Point(m(-8.36), m(0), m(19.56))
    j004 = Point(m(8.38), m(0), m(19.52))
    j005 = Point(m(-7.53), m(0), m(19.32))
    j006 = Point(m(7.55), m(0), m(19.29))
    j007 = Point(m(-5.89), m(0), m(18.42))
    j008 = Point(m(5.91), m(0), m(18.39))
    j009 = Point(m(-7.41), m(0), m(18.15))
    j010 = Point(m(7.42), m(0), m(18.12))
    j011 = Point(m(-3.98), m(0), m(17.5))
    j012 = Point(m(4), m(0), m(17.49))
    j013 = Point(m(-6.04), m(0), m(16.62))
    j014 = Point(m(6.06), m(0), m(16.58))
    j015 = Point(m(-1.46), m(0), m(16.48))
    j016 = Point(m(1.49), m(0), m(16.47))
    j017 = Point(m(0.01), m(0), m(16.04))
    j018 = Point(m(-4.3), m(0), m(15.05))
    j019 = Point(m(4.31), m(0), m(15.03))
    j020 = Point(m(-1.87), m(0), m(13.24))
    j021 = Point(m(1.89), m(0), m(13.24))
    j022 = Point(m(-6.39), m(0), m(12.13))
    j023 = Point(m(6.38), m(0), m(12.13))
    j024 = Point(m(-8.35), m(0), m(11.65))
    j025 = Point(m(8.34), m(0), m(11.65))
    j026 = Point(m(-1.97), m(0), m(11.62))
    j027 = Point(m(1.98), m(0), m(11.62))
    j028 = Point(m(-4.23), m(0), m(11.56))
    j029 = Point(m(4.22), m(0), m(11.56))
    j030 = Point(m(-11.62), m(0), m(10.83))
    j031 = Point(m(11.6), m(0), m(10.83))
    j032 = Point(m(-12.39), m(0), m(10.64))
    j033 = Point(m(12.39), m(0), m(10.64))
    j034 = Point(m(-10.4), m(0), m(10.01))
    j035 = Point(m(10.38), m(0), m(10.01))
    j036 = Point(m(-12), m(0), m(10))
    j037 = Point(m(12), m(0), m(10))
    j038 = Point(m(-12.39), m(0), m(10))
    j039 = Point(m(-11.62), m(0), m(10))
    j040 = Point(m(-10.31), m(0), m(10))
    j041 = Point(m(-8.36), m(0), m(10))
    j042 = Point(m(-6.4), m(0), m(10))
    j043 = Point(m(-4.23), m(0), m(10))
    j044 = Point(m(-2.06), m(0), m(10))
    j045 = Point(m(2.06), m(0), m(10))
    j046 = Point(m(4.23), m(0), m(10))
    j047 = Point(m(6.39), m(0), m(10))
    j048 = Point(m(8.34), m(0), m(10))
    j049 = Point(m(10.3), m(0), m(10))
    j050 = Point(m(11.6), m(0), m(10))
    j051 = Point(m(12.39), m(0), m(10))
    j052 = Point(m(-2.18), m(0), m(8))
    j053 = Point(m(2.18), m(0), m(8))
    j054 = Point(m(-2.31), m(0), m(6))
    j055 = Point(m(2.31), m(0), m(6))
    j056 = Point(m(-2.43), m(0), m(3.99))
    j057 = Point(m(2.43), m(0), m(3.99))
    j058 = Point(m(-9.01), m(0), m(2.61))
    j059 = Point(m(8.99), m(0), m(2.61))
    j060 = Point(m(-5.72), m(0), m(2))
    j061 = Point(m(-2.55), m(0), m(2))
    j062 = Point(m(2.56), m(0), m(2))
    j063 = Point(m(5.71), m(0), m(2))
    j064 = Point(m(-11.29), m(0), m(1.93))
    j065 = Point(m(11.29), m(0), m(1.93))
    j066 = Point(m(-15.18), m(0), m(0.79))
    j067 = Point(m(15.17), m(0), m(0.79))
    j068 = Point(m(-15.83), m(0), m(0.59))
    j069 = Point(m(15.82), m(0), m(0.59))
    j070 = Point(m(-15.83), m(0), m(0))
    j071 = Point(m(-15.18), m(0), m(0))
    j072 = Point(m(-14.1), m(0), m(0))
    j073 = Point(m(-11.29), m(0), m(0))
    j074 = Point(m(-9), m(0), m(0))
    j075 = Point(m(-5.72), m(0), m(0))
    j076 = Point(m(-2.68), m(0), m(0))
    j077 = Point(m(2.68), m(0), m(0))
    j078 = Point(m(5.71), m(0), m(0))
    j079 = Point(m(9), m(0), m(0))
    j080 = Point(m(11.29), m(0), m(0))
    j081 = Point(m(14.09), m(0), m(0))
    j082 = Point(m(15.17), m(0), m(0))
    j083 = Point(m(15.82), m(0), m(0))
    j084 = Point(m(-15.5), m(0), m(0))
    j085 = Point(m(15.5), m(0), m(0))
    j086 = Point(m(-2.85), m(0), m(-2.03))
    j087 = Point(m(2.85), m(0), m(-2.03))
    j088 = Point(m(-3.02), m(0), m(-4.13))
    j089 = Point(m(3.02), m(0), m(-4.13))
    j090 = Point(m(-3.21), m(0), m(-6.46))
    j091 = Point(m(3.21), m(0), m(-6.46))
    j092 = Point(m(-1.6), m(0), m(-7.51))
    j093 = Point(m(1.62), m(0), m(-7.51))
    j094 = Point(m(-3.39), m(0), m(-8.56))
    j095 = Point(m(0.01), m(0), m(-8.56))
    j096 = Point(m(3.39), m(0), m(-8.56))
    j097 = Point(m(-1.7), m(0), m(-9.66))
    j098 = Point(m(1.79), m(0), m(-9.72))
    j099 = Point(m(-3.58), m(0), m(-10.89))
    j100 = Point(m(3.58), m(0), m(-10.89))
    j101 = Point(m(-3.81), m(0), m(-11.69))
    j102 = Point(m(-1.79), m(0), m(-11.69))
    j103 = Point(m(1.79), m(0), m(-11.69))
    j104 = Point(m(3.81), m(0), m(-11.69))
    j105 = Point(m(-4.03), m(0), m(-12.49))
    j106 = Point(m(0.01), m(0), m(-12.49))
    j107 = Point(m(4.03), m(0), m(-12.49))
    j108 = Point(m(-4.31), m(0), m(-13.48))
    j109 = Point(m(-2.23), m(0), m(-13.48))
    j110 = Point(m(2.23), m(0), m(-13.48))
    j111 = Point(m(4.31), m(0), m(-13.48))
    j112 = Point(m(-4.47), m(0), m(-14.48))
    j113 = Point(m(4.47), m(0), m(-14.48))
    j114 = Point(m(-4.97), m(0), m(-15.82))
    j115 = Point(m(-2.23), m(0), m(-15.82))
    j116 = Point(m(2.23), m(0), m(-15.82))
    j117 = Point(m(4.97), m(0), m(-15.82))
    j118 = Point(m(-5.33), m(0), m(-17.1))
    j119 = Point(m(5.33), m(0), m(-17.1))
    j120 = Point(m(-5.68), m(0), m(-18.33))
    j121 = Point(m(-1.96), m(0), m(-18.33))
    j122 = Point(m(1.96), m(0), m(-18.33))
    j123 = Point(m(5.68), m(0), m(-18.33))
    j124 = Point(m(-5.97), m(0), m(-19.36))
    j125 = Point(m(-3.69), m(0), m(-19.36))
    j126 = Point(m(3.69), m(0), m(-19.36))
    j127 = Point(m(5.97), m(0), m(-19.36))
    j128 = Point(m(-6.43), m(0), m(-21))
    j129 = Point(m(6.43), m(0), m(-21))
    return Tower(
        name="D-2-D-2018.3 WA140",
        datum=LowestCrossarm((m(21), m(30), m(36), m(39))),
        voltages=(kv(380),),
        line_angles=(),
        attachments=(
            Mount(Wire.SHIELD, Point(m(-8.6), m(0), m(20)), Hold.CLAMP),
            Mount(Wire.SHIELD, Point(m(8.6), m(0), m(20)), Hold.CLAMP),
            Mount(Wire.PHASE, Point(m(-12), m(0), m(10)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(12), m(0), m(10)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-15.5), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-9), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(9), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(15.5), m(0), m(0)), Hold.STRAIN),
        ),
        bases=(),
        body=(
            Body(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j121, j116, role=Role.DIAGONAL_BRACE),
                        Bar(j122, j115, role=Role.DIAGONAL_BRACE),
                        Bar(j119, j118, role=Role.TRANSVERSE_BRACE),
                        Bar(j020, j021, role=Role.TRANSVERSE_BRACE),
                        Bar(j044, j045, role=Role.TRANSVERSE_BRACE),
                        Bar(j076, j077, role=Role.TRANSVERSE_BRACE),
                        Bar(j056, j057, role=Role.TRANSVERSE_BRACE),
                        Bar(j077, j086, role=Role.DIAGONAL_BRACE),
                        Bar(j086, j089, role=Role.DIAGONAL_BRACE),
                        Bar(j089, j090, role=Role.DIAGONAL_BRACE),
                        Bar(j091, j088, role=Role.DIAGONAL_BRACE),
                        Bar(j088, j087, role=Role.DIAGONAL_BRACE),
                        Bar(j087, j076, role=Role.DIAGONAL_BRACE),
                        Bar(j094, j095, role=Role.TRANSVERSE_BRACE),
                        Bar(j095, j096, role=Role.TRANSVERSE_BRACE),
                        Bar(j100, j098, role=Role.DIAGONAL_BRACE),
                        Bar(j098, j095, role=Role.DIAGONAL_BRACE),
                        Bar(j095, j092, role=Role.DIAGONAL_BRACE),
                        Bar(j092, j090, role=Role.DIAGONAL_BRACE),
                        Bar(j099, j097, role=Role.DIAGONAL_BRACE),
                        Bar(j097, j095, role=Role.DIAGONAL_BRACE),
                        Bar(j095, j093, role=Role.DIAGONAL_BRACE),
                        Bar(j093, j091, role=Role.DIAGONAL_BRACE),
                        Bar(j092, j094, role=Role.DIAGONAL_BRACE),
                        Bar(j094, j097, role=Role.DIAGONAL_BRACE),
                        Bar(j093, j096, role=Role.DIAGONAL_BRACE),
                        Bar(j096, j098, role=Role.DIAGONAL_BRACE),
                        Bar(j106, j102, role=Role.DIAGONAL_BRACE),
                        Bar(j109, j106, role=Role.DIAGONAL_BRACE),
                        Bar(j106, j105, role=Role.TRANSVERSE_BRACE),
                        Bar(j099, j094, role=Role.CHORD),
                        Bar(j094, j090, role=Role.CHORD),
                        Bar(j090, j088, role=Role.CHORD),
                        Bar(j088, j086, role=Role.CHORD),
                        Bar(j086, j076, role=Role.CHORD),
                        Bar(j076, j061, role=Role.CHORD),
                        Bar(j061, j056, role=Role.CHORD),
                        Bar(j057, j061, role=Role.DIAGONAL_BRACE),
                        Bar(j061, j077, role=Role.DIAGONAL_BRACE),
                        Bar(j077, j087, role=Role.CHORD),
                        Bar(j087, j089, role=Role.CHORD),
                        Bar(j089, j091, role=Role.CHORD),
                        Bar(j091, j096, role=Role.CHORD),
                        Bar(j096, j100, role=Role.CHORD),
                        Bar(j056, j062, role=Role.DIAGONAL_BRACE),
                        Bar(j062, j076, role=Role.DIAGONAL_BRACE),
                        Bar(j056, j054, role=Role.CHORD),
                        Bar(j054, j052, role=Role.CHORD),
                        Bar(j052, j044, role=Role.CHORD),
                        Bar(j044, j026, role=Role.CHORD),
                        Bar(j026, j020, role=Role.CHORD),
                        Bar(j045, j026, role=Role.DIAGONAL_BRACE),
                        Bar(j026, j021, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j027, role=Role.CHORD),
                        Bar(j027, j045, role=Role.CHORD),
                        Bar(j045, j053, role=Role.CHORD),
                        Bar(j053, j055, role=Role.CHORD),
                        Bar(j055, j057, role=Role.CHORD),
                        Bar(j057, j062, role=Role.CHORD),
                        Bar(j062, j077, role=Role.CHORD),
                        Bar(j057, j054, role=Role.DIAGONAL_BRACE),
                        Bar(j054, j053, role=Role.DIAGONAL_BRACE),
                        Bar(j053, j044, role=Role.DIAGONAL_BRACE),
                        Bar(j044, j027, role=Role.DIAGONAL_BRACE),
                        Bar(j027, j020, role=Role.DIAGONAL_BRACE),
                        Bar(j056, j055, role=Role.DIAGONAL_BRACE),
                        Bar(j055, j052, role=Role.DIAGONAL_BRACE),
                        Bar(j052, j045, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        legs=(
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j128, j124, role=Role.CHORD),
                        Bar(j124, j120, role=Role.CHORD),
                        Bar(j120, j118, role=Role.CHORD),
                        Bar(j118, j114, role=Role.CHORD),
                        Bar(j114, j108, role=Role.CHORD),
                        Bar(j108, j105, role=Role.CHORD),
                        Bar(j105, j101, role=Role.CHORD),
                        Bar(j101, j099, role=Role.CHORD),
                        Bar(j128, j125, role=Role.DIAGONAL_BRACE),
                        Bar(j125, j121, role=Role.DIAGONAL_BRACE),
                        Bar(j115, j112, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j120, role=Role.TRANSVERSE_BRACE),
                        Bar(j125, j124, role=Role.TRANSVERSE_BRACE),
                        Bar(j115, j114, role=Role.TRANSVERSE_BRACE),
                        Bar(j125, j120, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j118, role=Role.DIAGONAL_BRACE),
                        Bar(j118, j115, role=Role.DIAGONAL_BRACE),
                        Bar(j102, j099, role=Role.DIAGONAL_BRACE),
                        Bar(j112, j109, role=Role.DIAGONAL_BRACE),
                        Bar(j105, j102, role=Role.DIAGONAL_BRACE),
                        Bar(j105, j109, role=Role.DIAGONAL_BRACE),
                        Bar(j108, j109, role=Role.TRANSVERSE_BRACE),
                        Bar(j101, j102, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j100, j104, role=Role.CHORD),
                        Bar(j104, j107, role=Role.CHORD),
                        Bar(j107, j111, role=Role.CHORD),
                        Bar(j111, j117, role=Role.CHORD),
                        Bar(j117, j119, role=Role.CHORD),
                        Bar(j119, j123, role=Role.CHORD),
                        Bar(j123, j127, role=Role.CHORD),
                        Bar(j127, j129, role=Role.CHORD),
                        Bar(j116, j113, role=Role.DIAGONAL_BRACE),
                        Bar(j129, j126, role=Role.DIAGONAL_BRACE),
                        Bar(j126, j122, role=Role.DIAGONAL_BRACE),
                        Bar(j122, j123, role=Role.TRANSVERSE_BRACE),
                        Bar(j126, j127, role=Role.TRANSVERSE_BRACE),
                        Bar(j116, j117, role=Role.TRANSVERSE_BRACE),
                        Bar(j126, j123, role=Role.DIAGONAL_BRACE),
                        Bar(j122, j119, role=Role.DIAGONAL_BRACE),
                        Bar(j119, j116, role=Role.DIAGONAL_BRACE),
                        Bar(j113, j110, role=Role.DIAGONAL_BRACE),
                        Bar(j110, j106, role=Role.DIAGONAL_BRACE),
                        Bar(j106, j103, role=Role.DIAGONAL_BRACE),
                        Bar(j103, j100, role=Role.DIAGONAL_BRACE),
                        Bar(j107, j106, role=Role.TRANSVERSE_BRACE),
                        Bar(j103, j107, role=Role.DIAGONAL_BRACE),
                        Bar(j107, j110, role=Role.DIAGONAL_BRACE),
                        Bar(j103, j104, role=Role.TRANSVERSE_BRACE),
                        Bar(j110, j111, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        head=(
            Head(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j015, j017, role=Role.DIAGONAL_BRACE),
                        Bar(j017, j016, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j017, role=Role.DIAGONAL_BRACE),
                        Bar(j017, j020, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j016, role=Role.CHORD),
                        Bar(j020, j015, role=Role.CHORD),
                    ),
                )
            ),
        ),
        crossarms=(
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j038, j036, role=Role.CHORD),
                        Bar(j036, j039, role=Role.CHORD),
                        Bar(j039, j034, role=Role.CHORD),
                        Bar(j034, j040, role=Role.CHORD),
                        Bar(j040, j041, role=Role.CHORD),
                        Bar(j041, j042, role=Role.CHORD),
                        Bar(j042, j043, role=Role.CHORD),
                        Bar(j043, j044, role=Role.CHORD),
                        Bar(j032, j030, role=Role.CHORD),
                        Bar(j030, j024, role=Role.CHORD),
                        Bar(j024, j022, role=Role.CHORD),
                        Bar(j022, j020, role=Role.CHORD),
                        Bar(j032, j038, role=Role.CHORD),
                        Bar(j044, j028, role=Role.DIAGONAL_BRACE),
                        Bar(j028, j043, role=Role.TRANSVERSE_BRACE),
                        Bar(j022, j042, role=Role.TRANSVERSE_BRACE),
                        Bar(j042, j028, role=Role.DIAGONAL_BRACE),
                        Bar(j028, j020, role=Role.DIAGONAL_BRACE),
                        Bar(j041, j024, role=Role.TRANSVERSE_BRACE),
                        Bar(j024, j042, role=Role.DIAGONAL_BRACE),
                        Bar(j024, j034, role=Role.DIAGONAL_BRACE),
                        Bar(j039, j030, role=Role.TRANSVERSE_BRACE),
                        Bar(j030, j040, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j045, j046, role=Role.CHORD),
                        Bar(j046, j047, role=Role.CHORD),
                        Bar(j047, j048, role=Role.CHORD),
                        Bar(j048, j049, role=Role.CHORD),
                        Bar(j049, j035, role=Role.CHORD),
                        Bar(j035, j050, role=Role.CHORD),
                        Bar(j050, j037, role=Role.CHORD),
                        Bar(j037, j051, role=Role.CHORD),
                        Bar(j051, j033, role=Role.CHORD),
                        Bar(j033, j031, role=Role.CHORD),
                        Bar(j031, j025, role=Role.CHORD),
                        Bar(j025, j023, role=Role.CHORD),
                        Bar(j023, j021, role=Role.CHORD),
                        Bar(j031, j050, role=Role.TRANSVERSE_BRACE),
                        Bar(j031, j049, role=Role.DIAGONAL_BRACE),
                        Bar(j048, j025, role=Role.TRANSVERSE_BRACE),
                        Bar(j025, j047, role=Role.DIAGONAL_BRACE),
                        Bar(j025, j035, role=Role.DIAGONAL_BRACE),
                        Bar(j023, j047, role=Role.TRANSVERSE_BRACE),
                        Bar(j047, j029, role=Role.DIAGONAL_BRACE),
                        Bar(j029, j021, role=Role.DIAGONAL_BRACE),
                        Bar(j045, j029, role=Role.DIAGONAL_BRACE),
                        Bar(j029, j046, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j070, j084, role=Role.CHORD),
                        Bar(j084, j071, role=Role.CHORD),
                        Bar(j071, j072, role=Role.CHORD),
                        Bar(j072, j073, role=Role.CHORD),
                        Bar(j073, j074, role=Role.CHORD),
                        Bar(j074, j075, role=Role.CHORD),
                        Bar(j075, j076, role=Role.CHORD),
                        Bar(j070, j068, role=Role.CHORD),
                        Bar(j068, j066, role=Role.CHORD),
                        Bar(j066, j064, role=Role.CHORD),
                        Bar(j064, j058, role=Role.CHORD),
                        Bar(j058, j056, role=Role.CHORD),
                        Bar(j066, j071, role=Role.TRANSVERSE_BRACE),
                        Bar(j056, j060, role=Role.DIAGONAL_BRACE),
                        Bar(j060, j074, role=Role.DIAGONAL_BRACE),
                        Bar(j074, j058, role=Role.TRANSVERSE_BRACE),
                        Bar(j066, j072, role=Role.DIAGONAL_BRACE),
                        Bar(j072, j064, role=Role.DIAGONAL_BRACE),
                        Bar(j064, j074, role=Role.DIAGONAL_BRACE),
                        Bar(j073, j064, role=Role.TRANSVERSE_BRACE),
                        Bar(j076, j060, role=Role.DIAGONAL_BRACE),
                        Bar(j060, j075, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j077, j078, role=Role.CHORD),
                        Bar(j078, j079, role=Role.CHORD),
                        Bar(j079, j080, role=Role.CHORD),
                        Bar(j080, j081, role=Role.CHORD),
                        Bar(j081, j082, role=Role.CHORD),
                        Bar(j082, j085, role=Role.CHORD),
                        Bar(j085, j083, role=Role.CHORD),
                        Bar(j083, j069, role=Role.CHORD),
                        Bar(j069, j067, role=Role.CHORD),
                        Bar(j067, j065, role=Role.CHORD),
                        Bar(j065, j059, role=Role.CHORD),
                        Bar(j059, j057, role=Role.CHORD),
                        Bar(j067, j082, role=Role.TRANSVERSE_BRACE),
                        Bar(j067, j081, role=Role.DIAGONAL_BRACE),
                        Bar(j081, j065, role=Role.DIAGONAL_BRACE),
                        Bar(j065, j079, role=Role.DIAGONAL_BRACE),
                        Bar(j079, j059, role=Role.TRANSVERSE_BRACE),
                        Bar(j080, j065, role=Role.TRANSVERSE_BRACE),
                        Bar(j077, j063, role=Role.DIAGONAL_BRACE),
                        Bar(j063, j078, role=Role.TRANSVERSE_BRACE),
                        Bar(j057, j063, role=Role.DIAGONAL_BRACE),
                        Bar(j063, j079, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        peaks=(
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j001, j003, role=Role.CHORD),
                        Bar(j003, j009, role=Role.CHORD),
                        Bar(j009, j013, role=Role.CHORD),
                        Bar(j013, j018, role=Role.CHORD),
                        Bar(j018, j020, role=Role.CHORD),
                        Bar(j001, j005, role=Role.CHORD),
                        Bar(j005, j007, role=Role.CHORD),
                        Bar(j007, j011, role=Role.CHORD),
                        Bar(j011, j015, role=Role.CHORD),
                        Bar(j015, j018, role=Role.DIAGONAL_BRACE),
                        Bar(j018, j011, role=Role.TRANSVERSE_BRACE),
                        Bar(j011, j013, role=Role.DIAGONAL_BRACE),
                        Bar(j013, j007, role=Role.DIAGONAL_BRACE),
                        Bar(j007, j009, role=Role.DIAGONAL_BRACE),
                        Bar(j009, j005, role=Role.DIAGONAL_BRACE),
                        Bar(j005, j003, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j016, j012, role=Role.CHORD),
                        Bar(j012, j008, role=Role.CHORD),
                        Bar(j008, j006, role=Role.CHORD),
                        Bar(j006, j002, role=Role.CHORD),
                        Bar(j002, j004, role=Role.CHORD),
                        Bar(j004, j010, role=Role.CHORD),
                        Bar(j010, j014, role=Role.CHORD),
                        Bar(j014, j019, role=Role.CHORD),
                        Bar(j019, j021, role=Role.CHORD),
                        Bar(j016, j019, role=Role.DIAGONAL_BRACE),
                        Bar(j019, j012, role=Role.TRANSVERSE_BRACE),
                        Bar(j012, j014, role=Role.DIAGONAL_BRACE),
                        Bar(j014, j008, role=Role.DIAGONAL_BRACE),
                        Bar(j008, j010, role=Role.DIAGONAL_BRACE),
                        Bar(j010, j006, role=Role.DIAGONAL_BRACE),
                        Bar(j006, j004, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
    )


D_2_D_2018_3_WA140 = _d_2_d_2018_3_wa140()


def _d_2_d_2018_3_wa160() -> Tower[LowestCrossarm]:
    """D-2-D-2018.3 WA160: each joint written once, by its key."""
    j001 = Point(m(-8.6), m(0), m(20))
    j002 = Point(m(8.6), m(0), m(20))
    j003 = Point(m(-8.3), m(0), m(19.56))
    j004 = Point(m(8.32), m(0), m(19.52))
    j005 = Point(m(-7.43), m(0), m(19.32))
    j006 = Point(m(7.44), m(0), m(19.29))
    j007 = Point(m(-5.7), m(0), m(18.42))
    j008 = Point(m(5.72), m(0), m(18.39))
    j009 = Point(m(-7.2), m(0), m(18.15))
    j010 = Point(m(7.21), m(0), m(18.12))
    j011 = Point(m(-3.76), m(0), m(17.5))
    j012 = Point(m(3.78), m(0), m(17.49))
    j013 = Point(m(-5.75), m(0), m(16.62))
    j014 = Point(m(5.77), m(0), m(16.58))
    j015 = Point(m(-1.3), m(0), m(16.48))
    j016 = Point(m(1.33), m(0), m(16.47))
    j017 = Point(m(0.01), m(0), m(16.04))
    j018 = Point(m(-4), m(0), m(15.05))
    j019 = Point(m(4.01), m(0), m(15.03))
    j020 = Point(m(-1.66), m(0), m(13.24))
    j021 = Point(m(1.68), m(0), m(13.24))
    j022 = Point(m(-5.94), m(0), m(12.13))
    j023 = Point(m(5.93), m(0), m(12.13))
    j024 = Point(m(-7.79), m(0), m(11.65))
    j025 = Point(m(7.78), m(0), m(11.65))
    j026 = Point(m(-1.75), m(0), m(11.62))
    j027 = Point(m(1.76), m(0), m(11.62))
    j028 = Point(m(-3.89), m(0), m(11.56))
    j029 = Point(m(3.88), m(0), m(11.56))
    j030 = Point(m(-10.89), m(0), m(10.83))
    j031 = Point(m(10.87), m(0), m(10.83))
    j032 = Point(m(-11.62), m(0), m(10.64))
    j033 = Point(m(11.62), m(0), m(10.64))
    j034 = Point(m(-9.73), m(0), m(10.01))
    j035 = Point(m(9.71), m(0), m(10.01))
    j036 = Point(m(-11.25), m(0), m(10))
    j037 = Point(m(11.25), m(0), m(10))
    j038 = Point(m(-11.62), m(0), m(10))
    j039 = Point(m(-10.89), m(0), m(10))
    j040 = Point(m(-9.65), m(0), m(10))
    j041 = Point(m(-7.8), m(0), m(10))
    j042 = Point(m(-5.94), m(0), m(10))
    j043 = Point(m(-3.89), m(0), m(10))
    j044 = Point(m(-1.83), m(0), m(10))
    j045 = Point(m(1.83), m(0), m(10))
    j046 = Point(m(3.89), m(0), m(10))
    j047 = Point(m(5.93), m(0), m(10))
    j048 = Point(m(7.78), m(0), m(10))
    j049 = Point(m(9.64), m(0), m(10))
    j050 = Point(m(10.87), m(0), m(10))
    j051 = Point(m(11.62), m(0), m(10))
    j052 = Point(m(-1.94), m(0), m(8))
    j053 = Point(m(1.94), m(0), m(8))
    j054 = Point(m(-2.05), m(0), m(6))
    j055 = Point(m(2.05), m(0), m(6))
    j056 = Point(m(-2.16), m(0), m(3.99))
    j057 = Point(m(2.17), m(0), m(3.99))
    j058 = Point(m(-8.01), m(0), m(2.61))
    j059 = Point(m(7.99), m(0), m(2.61))
    j060 = Point(m(-5.09), m(0), m(2))
    j061 = Point(m(-2.27), m(0), m(2))
    j062 = Point(m(2.28), m(0), m(2))
    j063 = Point(m(5.08), m(0), m(2))
    j064 = Point(m(-10.11), m(0), m(1.93))
    j065 = Point(m(10.11), m(0), m(1.93))
    j066 = Point(m(-13.7), m(0), m(0.79))
    j067 = Point(m(13.7), m(0), m(0.79))
    j068 = Point(m(-14.31), m(0), m(0.59))
    j069 = Point(m(14.29), m(0), m(0.59))
    j070 = Point(m(-14.31), m(0), m(0))
    j071 = Point(m(-13.7), m(0), m(0))
    j072 = Point(m(-12.71), m(0), m(0))
    j073 = Point(m(-10.11), m(0), m(0))
    j074 = Point(m(-8), m(0), m(0))
    j075 = Point(m(-5.09), m(0), m(0))
    j076 = Point(m(-2.39), m(0), m(0))
    j077 = Point(m(2.39), m(0), m(0))
    j078 = Point(m(5.08), m(0), m(0))
    j079 = Point(m(8), m(0), m(0))
    j080 = Point(m(10.11), m(0), m(0))
    j081 = Point(m(12.7), m(0), m(0))
    j082 = Point(m(13.7), m(0), m(0))
    j083 = Point(m(14.29), m(0), m(0))
    j084 = Point(m(-14), m(0), m(0))
    j085 = Point(m(14), m(0), m(0))
    j086 = Point(m(-2.54), m(0), m(-2.61))
    j087 = Point(m(2.54), m(0), m(-2.61))
    j088 = Point(m(-2.69), m(0), m(-5.31))
    j089 = Point(m(2.69), m(0), m(-5.31))
    j090 = Point(m(-2.86), m(0), m(-8.31))
    j091 = Point(m(2.86), m(0), m(-8.31))
    j092 = Point(m(-1.43), m(0), m(-9.65))
    j093 = Point(m(1.44), m(0), m(-9.65))
    j094 = Point(m(-3.01), m(0), m(-11.01))
    j095 = Point(m(0.01), m(0), m(-11.01))
    j096 = Point(m(3.01), m(0), m(-11.01))
    j097 = Point(m(-1.51), m(0), m(-12.43))
    j098 = Point(m(1.59), m(0), m(-12.5))
    j099 = Point(m(-3.18), m(0), m(-14))
    j100 = Point(m(3.18), m(0), m(-14))
    j101 = Point(m(-3.38), m(0), m(-15.03))
    j102 = Point(m(-1.59), m(0), m(-15.03))
    j103 = Point(m(1.59), m(0), m(-15.03))
    j104 = Point(m(3.38), m(0), m(-15.03))
    j105 = Point(m(-3.58), m(0), m(-16.05))
    j106 = Point(m(0.01), m(0), m(-16.05))
    j107 = Point(m(3.58), m(0), m(-16.05))
    j108 = Point(m(-3.83), m(0), m(-17.34))
    j109 = Point(m(-1.98), m(0), m(-17.34))
    j110 = Point(m(1.98), m(0), m(-17.34))
    j111 = Point(m(3.83), m(0), m(-17.34))
    j112 = Point(m(-3.97), m(0), m(-18.62))
    j113 = Point(m(3.97), m(0), m(-18.62))
    j114 = Point(m(-4.41), m(0), m(-20.34))
    j115 = Point(m(-1.98), m(0), m(-20.34))
    j116 = Point(m(1.98), m(0), m(-20.34))
    j117 = Point(m(4.41), m(0), m(-20.34))
    j118 = Point(m(-4.73), m(0), m(-21.99))
    j119 = Point(m(4.73), m(0), m(-21.99))
    j120 = Point(m(-5.04), m(0), m(-23.57))
    j121 = Point(m(-1.75), m(0), m(-23.57))
    j122 = Point(m(1.75), m(0), m(-23.57))
    j123 = Point(m(5.04), m(0), m(-23.57))
    j124 = Point(m(-5.3), m(0), m(-24.89))
    j125 = Point(m(-3.28), m(0), m(-24.89))
    j126 = Point(m(3.28), m(0), m(-24.89))
    j127 = Point(m(5.3), m(0), m(-24.89))
    j128 = Point(m(-5.71), m(0), m(-27))
    j129 = Point(m(5.71), m(0), m(-27))
    return Tower(
        name="D-2-D-2018.3 WA160",
        datum=LowestCrossarm((m(27), m(30), m(36), m(42), m(48))),
        voltages=(kv(380),),
        line_angles=(),
        attachments=(
            Mount(Wire.SHIELD, Point(m(-8.6), m(0), m(20)), Hold.CLAMP),
            Mount(Wire.SHIELD, Point(m(8.6), m(0), m(20)), Hold.CLAMP),
            Mount(Wire.PHASE, Point(m(-11.25), m(0), m(10)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(11.25), m(0), m(10)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-14), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-8), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(8), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(14), m(0), m(0)), Hold.STRAIN),
        ),
        bases=(),
        body=(
            Body(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j121, j116, role=Role.DIAGONAL_BRACE),
                        Bar(j122, j115, role=Role.DIAGONAL_BRACE),
                        Bar(j119, j118, role=Role.TRANSVERSE_BRACE),
                        Bar(j020, j021, role=Role.TRANSVERSE_BRACE),
                        Bar(j044, j045, role=Role.TRANSVERSE_BRACE),
                        Bar(j076, j077, role=Role.TRANSVERSE_BRACE),
                        Bar(j056, j057, role=Role.TRANSVERSE_BRACE),
                        Bar(j077, j086, role=Role.DIAGONAL_BRACE),
                        Bar(j086, j089, role=Role.DIAGONAL_BRACE),
                        Bar(j089, j090, role=Role.DIAGONAL_BRACE),
                        Bar(j091, j088, role=Role.DIAGONAL_BRACE),
                        Bar(j088, j087, role=Role.DIAGONAL_BRACE),
                        Bar(j087, j076, role=Role.DIAGONAL_BRACE),
                        Bar(j094, j095, role=Role.TRANSVERSE_BRACE),
                        Bar(j095, j096, role=Role.TRANSVERSE_BRACE),
                        Bar(j100, j098, role=Role.DIAGONAL_BRACE),
                        Bar(j098, j095, role=Role.DIAGONAL_BRACE),
                        Bar(j095, j092, role=Role.DIAGONAL_BRACE),
                        Bar(j092, j090, role=Role.DIAGONAL_BRACE),
                        Bar(j099, j097, role=Role.DIAGONAL_BRACE),
                        Bar(j097, j095, role=Role.DIAGONAL_BRACE),
                        Bar(j095, j093, role=Role.DIAGONAL_BRACE),
                        Bar(j093, j091, role=Role.DIAGONAL_BRACE),
                        Bar(j092, j094, role=Role.DIAGONAL_BRACE),
                        Bar(j094, j097, role=Role.DIAGONAL_BRACE),
                        Bar(j093, j096, role=Role.DIAGONAL_BRACE),
                        Bar(j096, j098, role=Role.DIAGONAL_BRACE),
                        Bar(j106, j102, role=Role.DIAGONAL_BRACE),
                        Bar(j109, j106, role=Role.DIAGONAL_BRACE),
                        Bar(j106, j105, role=Role.TRANSVERSE_BRACE),
                        Bar(j099, j094, role=Role.CHORD),
                        Bar(j094, j090, role=Role.CHORD),
                        Bar(j090, j088, role=Role.CHORD),
                        Bar(j088, j086, role=Role.CHORD),
                        Bar(j086, j076, role=Role.CHORD),
                        Bar(j076, j061, role=Role.CHORD),
                        Bar(j061, j056, role=Role.CHORD),
                        Bar(j057, j061, role=Role.DIAGONAL_BRACE),
                        Bar(j061, j077, role=Role.DIAGONAL_BRACE),
                        Bar(j077, j087, role=Role.CHORD),
                        Bar(j087, j089, role=Role.CHORD),
                        Bar(j089, j091, role=Role.CHORD),
                        Bar(j091, j096, role=Role.CHORD),
                        Bar(j096, j100, role=Role.CHORD),
                        Bar(j056, j062, role=Role.DIAGONAL_BRACE),
                        Bar(j062, j076, role=Role.DIAGONAL_BRACE),
                        Bar(j056, j054, role=Role.CHORD),
                        Bar(j054, j052, role=Role.CHORD),
                        Bar(j052, j044, role=Role.CHORD),
                        Bar(j044, j026, role=Role.CHORD),
                        Bar(j026, j020, role=Role.CHORD),
                        Bar(j045, j026, role=Role.DIAGONAL_BRACE),
                        Bar(j026, j021, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j027, role=Role.CHORD),
                        Bar(j027, j045, role=Role.CHORD),
                        Bar(j045, j053, role=Role.CHORD),
                        Bar(j053, j055, role=Role.CHORD),
                        Bar(j055, j057, role=Role.CHORD),
                        Bar(j057, j062, role=Role.CHORD),
                        Bar(j062, j077, role=Role.CHORD),
                        Bar(j057, j054, role=Role.DIAGONAL_BRACE),
                        Bar(j054, j053, role=Role.DIAGONAL_BRACE),
                        Bar(j053, j044, role=Role.DIAGONAL_BRACE),
                        Bar(j044, j027, role=Role.DIAGONAL_BRACE),
                        Bar(j027, j020, role=Role.DIAGONAL_BRACE),
                        Bar(j056, j055, role=Role.DIAGONAL_BRACE),
                        Bar(j055, j052, role=Role.DIAGONAL_BRACE),
                        Bar(j052, j045, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        legs=(
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j128, j124, role=Role.CHORD),
                        Bar(j124, j120, role=Role.CHORD),
                        Bar(j120, j118, role=Role.CHORD),
                        Bar(j118, j114, role=Role.CHORD),
                        Bar(j114, j108, role=Role.CHORD),
                        Bar(j108, j105, role=Role.CHORD),
                        Bar(j105, j101, role=Role.CHORD),
                        Bar(j101, j099, role=Role.CHORD),
                        Bar(j128, j125, role=Role.DIAGONAL_BRACE),
                        Bar(j125, j121, role=Role.DIAGONAL_BRACE),
                        Bar(j115, j112, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j120, role=Role.TRANSVERSE_BRACE),
                        Bar(j125, j124, role=Role.TRANSVERSE_BRACE),
                        Bar(j115, j114, role=Role.TRANSVERSE_BRACE),
                        Bar(j125, j120, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j118, role=Role.DIAGONAL_BRACE),
                        Bar(j118, j115, role=Role.DIAGONAL_BRACE),
                        Bar(j102, j099, role=Role.DIAGONAL_BRACE),
                        Bar(j112, j109, role=Role.DIAGONAL_BRACE),
                        Bar(j105, j102, role=Role.DIAGONAL_BRACE),
                        Bar(j105, j109, role=Role.DIAGONAL_BRACE),
                        Bar(j108, j109, role=Role.TRANSVERSE_BRACE),
                        Bar(j101, j102, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j100, j104, role=Role.CHORD),
                        Bar(j104, j107, role=Role.CHORD),
                        Bar(j107, j111, role=Role.CHORD),
                        Bar(j111, j117, role=Role.CHORD),
                        Bar(j117, j119, role=Role.CHORD),
                        Bar(j119, j123, role=Role.CHORD),
                        Bar(j123, j127, role=Role.CHORD),
                        Bar(j127, j129, role=Role.CHORD),
                        Bar(j116, j113, role=Role.DIAGONAL_BRACE),
                        Bar(j129, j126, role=Role.DIAGONAL_BRACE),
                        Bar(j126, j122, role=Role.DIAGONAL_BRACE),
                        Bar(j122, j123, role=Role.TRANSVERSE_BRACE),
                        Bar(j126, j127, role=Role.TRANSVERSE_BRACE),
                        Bar(j116, j117, role=Role.TRANSVERSE_BRACE),
                        Bar(j126, j123, role=Role.DIAGONAL_BRACE),
                        Bar(j122, j119, role=Role.DIAGONAL_BRACE),
                        Bar(j119, j116, role=Role.DIAGONAL_BRACE),
                        Bar(j113, j110, role=Role.DIAGONAL_BRACE),
                        Bar(j110, j106, role=Role.DIAGONAL_BRACE),
                        Bar(j106, j103, role=Role.DIAGONAL_BRACE),
                        Bar(j103, j100, role=Role.DIAGONAL_BRACE),
                        Bar(j107, j106, role=Role.TRANSVERSE_BRACE),
                        Bar(j103, j107, role=Role.DIAGONAL_BRACE),
                        Bar(j107, j110, role=Role.DIAGONAL_BRACE),
                        Bar(j103, j104, role=Role.TRANSVERSE_BRACE),
                        Bar(j110, j111, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        head=(
            Head(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j021, j017, role=Role.DIAGONAL_BRACE),
                        Bar(j017, j020, role=Role.DIAGONAL_BRACE),
                        Bar(j015, j017, role=Role.DIAGONAL_BRACE),
                        Bar(j017, j016, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j016, role=Role.CHORD),
                        Bar(j020, j015, role=Role.CHORD),
                    ),
                )
            ),
        ),
        crossarms=(
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j038, j036, role=Role.CHORD),
                        Bar(j036, j039, role=Role.CHORD),
                        Bar(j039, j034, role=Role.CHORD),
                        Bar(j034, j040, role=Role.CHORD),
                        Bar(j040, j041, role=Role.CHORD),
                        Bar(j041, j042, role=Role.CHORD),
                        Bar(j042, j043, role=Role.CHORD),
                        Bar(j043, j044, role=Role.CHORD),
                        Bar(j032, j030, role=Role.CHORD),
                        Bar(j030, j024, role=Role.CHORD),
                        Bar(j024, j022, role=Role.CHORD),
                        Bar(j022, j020, role=Role.CHORD),
                        Bar(j032, j038, role=Role.CHORD),
                        Bar(j044, j028, role=Role.DIAGONAL_BRACE),
                        Bar(j028, j043, role=Role.TRANSVERSE_BRACE),
                        Bar(j022, j042, role=Role.TRANSVERSE_BRACE),
                        Bar(j042, j028, role=Role.DIAGONAL_BRACE),
                        Bar(j028, j020, role=Role.DIAGONAL_BRACE),
                        Bar(j041, j024, role=Role.TRANSVERSE_BRACE),
                        Bar(j024, j042, role=Role.DIAGONAL_BRACE),
                        Bar(j024, j034, role=Role.DIAGONAL_BRACE),
                        Bar(j039, j030, role=Role.TRANSVERSE_BRACE),
                        Bar(j030, j040, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j045, j046, role=Role.CHORD),
                        Bar(j046, j047, role=Role.CHORD),
                        Bar(j047, j048, role=Role.CHORD),
                        Bar(j048, j049, role=Role.CHORD),
                        Bar(j049, j035, role=Role.CHORD),
                        Bar(j035, j050, role=Role.CHORD),
                        Bar(j050, j037, role=Role.CHORD),
                        Bar(j037, j051, role=Role.CHORD),
                        Bar(j051, j033, role=Role.CHORD),
                        Bar(j033, j031, role=Role.CHORD),
                        Bar(j031, j025, role=Role.CHORD),
                        Bar(j025, j023, role=Role.CHORD),
                        Bar(j023, j021, role=Role.CHORD),
                        Bar(j031, j050, role=Role.TRANSVERSE_BRACE),
                        Bar(j031, j049, role=Role.DIAGONAL_BRACE),
                        Bar(j048, j025, role=Role.TRANSVERSE_BRACE),
                        Bar(j025, j047, role=Role.DIAGONAL_BRACE),
                        Bar(j025, j035, role=Role.DIAGONAL_BRACE),
                        Bar(j023, j047, role=Role.TRANSVERSE_BRACE),
                        Bar(j047, j029, role=Role.DIAGONAL_BRACE),
                        Bar(j029, j021, role=Role.DIAGONAL_BRACE),
                        Bar(j045, j029, role=Role.DIAGONAL_BRACE),
                        Bar(j029, j046, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j070, j084, role=Role.CHORD),
                        Bar(j084, j071, role=Role.CHORD),
                        Bar(j071, j072, role=Role.CHORD),
                        Bar(j072, j073, role=Role.CHORD),
                        Bar(j073, j074, role=Role.CHORD),
                        Bar(j074, j075, role=Role.CHORD),
                        Bar(j075, j076, role=Role.CHORD),
                        Bar(j070, j068, role=Role.CHORD),
                        Bar(j068, j066, role=Role.CHORD),
                        Bar(j066, j064, role=Role.CHORD),
                        Bar(j064, j058, role=Role.CHORD),
                        Bar(j058, j056, role=Role.CHORD),
                        Bar(j066, j071, role=Role.TRANSVERSE_BRACE),
                        Bar(j056, j060, role=Role.DIAGONAL_BRACE),
                        Bar(j060, j074, role=Role.DIAGONAL_BRACE),
                        Bar(j074, j058, role=Role.TRANSVERSE_BRACE),
                        Bar(j066, j072, role=Role.DIAGONAL_BRACE),
                        Bar(j072, j064, role=Role.DIAGONAL_BRACE),
                        Bar(j064, j074, role=Role.DIAGONAL_BRACE),
                        Bar(j073, j064, role=Role.TRANSVERSE_BRACE),
                        Bar(j076, j060, role=Role.DIAGONAL_BRACE),
                        Bar(j060, j075, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j077, j078, role=Role.CHORD),
                        Bar(j078, j079, role=Role.CHORD),
                        Bar(j079, j080, role=Role.CHORD),
                        Bar(j080, j081, role=Role.CHORD),
                        Bar(j081, j082, role=Role.CHORD),
                        Bar(j082, j085, role=Role.CHORD),
                        Bar(j085, j083, role=Role.CHORD),
                        Bar(j083, j069, role=Role.CHORD),
                        Bar(j069, j067, role=Role.CHORD),
                        Bar(j067, j065, role=Role.CHORD),
                        Bar(j065, j059, role=Role.CHORD),
                        Bar(j059, j057, role=Role.CHORD),
                        Bar(j067, j082, role=Role.TRANSVERSE_BRACE),
                        Bar(j067, j081, role=Role.DIAGONAL_BRACE),
                        Bar(j081, j065, role=Role.DIAGONAL_BRACE),
                        Bar(j065, j079, role=Role.DIAGONAL_BRACE),
                        Bar(j079, j059, role=Role.TRANSVERSE_BRACE),
                        Bar(j080, j065, role=Role.TRANSVERSE_BRACE),
                        Bar(j077, j063, role=Role.DIAGONAL_BRACE),
                        Bar(j063, j078, role=Role.TRANSVERSE_BRACE),
                        Bar(j057, j063, role=Role.DIAGONAL_BRACE),
                        Bar(j063, j079, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        peaks=(
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j001, j003, role=Role.CHORD),
                        Bar(j003, j009, role=Role.CHORD),
                        Bar(j009, j013, role=Role.CHORD),
                        Bar(j013, j018, role=Role.CHORD),
                        Bar(j018, j020, role=Role.CHORD),
                        Bar(j001, j005, role=Role.CHORD),
                        Bar(j005, j007, role=Role.CHORD),
                        Bar(j007, j011, role=Role.CHORD),
                        Bar(j011, j015, role=Role.CHORD),
                        Bar(j015, j018, role=Role.DIAGONAL_BRACE),
                        Bar(j018, j011, role=Role.TRANSVERSE_BRACE),
                        Bar(j011, j013, role=Role.DIAGONAL_BRACE),
                        Bar(j013, j007, role=Role.DIAGONAL_BRACE),
                        Bar(j007, j009, role=Role.DIAGONAL_BRACE),
                        Bar(j009, j005, role=Role.DIAGONAL_BRACE),
                        Bar(j005, j003, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j002, j004, role=Role.CHORD),
                        Bar(j004, j010, role=Role.CHORD),
                        Bar(j010, j014, role=Role.CHORD),
                        Bar(j014, j019, role=Role.CHORD),
                        Bar(j019, j021, role=Role.CHORD),
                        Bar(j016, j012, role=Role.CHORD),
                        Bar(j012, j008, role=Role.CHORD),
                        Bar(j008, j006, role=Role.CHORD),
                        Bar(j006, j002, role=Role.CHORD),
                        Bar(j016, j019, role=Role.DIAGONAL_BRACE),
                        Bar(j019, j012, role=Role.TRANSVERSE_BRACE),
                        Bar(j012, j014, role=Role.DIAGONAL_BRACE),
                        Bar(j014, j008, role=Role.DIAGONAL_BRACE),
                        Bar(j008, j010, role=Role.DIAGONAL_BRACE),
                        Bar(j010, j006, role=Role.DIAGONAL_BRACE),
                        Bar(j006, j004, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
    )


D_2_D_2018_3_WA160 = _d_2_d_2018_3_wa160()


def _d_2_d_2018_3_we_wadiff140() -> Tower[LowestCrossarm]:
    """D-2-D-2018.3 WE WAdiff140: each joint written once, by its key."""
    j001 = Point(m(-8.6), m(0), m(20.5))
    j002 = Point(m(8.6), m(0), m(20.5))
    j003 = Point(m(-8.39), m(0), m(20.05))
    j004 = Point(m(8.41), m(0), m(20))
    j005 = Point(m(-7.58), m(0), m(19.8))
    j006 = Point(m(7.61), m(0), m(19.75))
    j007 = Point(m(-6), m(0), m(18.85))
    j008 = Point(m(6.02), m(0), m(18.82))
    j009 = Point(m(-7.53), m(0), m(18.57))
    j010 = Point(m(7.55), m(0), m(18.52))
    j011 = Point(m(-4.11), m(0), m(17.88))
    j012 = Point(m(4.13), m(0), m(17.87))
    j013 = Point(m(-6.21), m(0), m(16.95))
    j014 = Point(m(6.23), m(0), m(16.92))
    j015 = Point(m(-1.54), m(0), m(16.8))
    j016 = Point(m(1.58), m(0), m(16.8))
    j017 = Point(m(0.01), m(0), m(16.34))
    j018 = Point(m(-4.47), m(0), m(15.31))
    j019 = Point(m(4.48), m(0), m(15.29))
    j020 = Point(m(-1.97), m(0), m(13.4))
    j021 = Point(m(1.99), m(0), m(13.4))
    j022 = Point(m(-6.67), m(0), m(12.24))
    j023 = Point(m(6.66), m(0), m(12.24))
    j024 = Point(m(-8.71), m(0), m(11.73))
    j025 = Point(m(8.7), m(0), m(11.73))
    j026 = Point(m(-2.07), m(0), m(11.69))
    j027 = Point(m(2.08), m(0), m(11.69))
    j028 = Point(m(-4.42), m(0), m(11.64))
    j029 = Point(m(4.42), m(0), m(11.64))
    j030 = Point(m(-12.1), m(0), m(10.88))
    j031 = Point(m(12.08), m(0), m(10.88))
    j032 = Point(m(-12.91), m(0), m(10.68))
    j033 = Point(m(12.9), m(0), m(10.68))
    j034 = Point(m(-10.83), m(0), m(10.01))
    j035 = Point(m(10.82), m(0), m(10.01))
    j036 = Point(m(-12.5), m(0), m(10))
    j037 = Point(m(12.5), m(0), m(10))
    j038 = Point(m(-12.91), m(0), m(10))
    j039 = Point(m(-12.1), m(0), m(10))
    j040 = Point(m(-10.75), m(0), m(10))
    j041 = Point(m(-8.71), m(0), m(10))
    j042 = Point(m(-6.68), m(0), m(10))
    j043 = Point(m(-4.43), m(0), m(10))
    j044 = Point(m(-2.17), m(0), m(10))
    j045 = Point(m(2.17), m(0), m(10))
    j046 = Point(m(4.43), m(0), m(10))
    j047 = Point(m(6.67), m(0), m(10))
    j048 = Point(m(8.7), m(0), m(10))
    j049 = Point(m(10.73), m(0), m(10))
    j050 = Point(m(12.08), m(0), m(10))
    j051 = Point(m(12.9), m(0), m(10))
    j052 = Point(m(-2.3), m(0), m(8))
    j053 = Point(m(2.3), m(0), m(8))
    j054 = Point(m(-2.44), m(0), m(6))
    j055 = Point(m(2.43), m(0), m(6))
    j056 = Point(m(-2.57), m(0), m(4))
    j057 = Point(m(2.57), m(0), m(4))
    j058 = Point(m(-9.51), m(0), m(2.6))
    j059 = Point(m(9.49), m(0), m(2.6))
    j060 = Point(m(-6.04), m(0), m(2))
    j061 = Point(m(-2.7), m(0), m(2))
    j062 = Point(m(2.7), m(0), m(2))
    j063 = Point(m(6.03), m(0), m(2))
    j064 = Point(m(-11.79), m(0), m(1.94))
    j065 = Point(m(11.79), m(0), m(1.94))
    j066 = Point(m(-15.68), m(0), m(0.79))
    j067 = Point(m(15.67), m(0), m(0.79))
    j068 = Point(m(-16.33), m(0), m(0.6))
    j069 = Point(m(16.32), m(0), m(0.6))
    j070 = Point(m(-16.33), m(0), m(0))
    j071 = Point(m(-15.68), m(0), m(0))
    j072 = Point(m(-14.6), m(0), m(0))
    j073 = Point(m(-11.79), m(0), m(0))
    j074 = Point(m(-9.5), m(0), m(0))
    j075 = Point(m(-6.04), m(0), m(0))
    j076 = Point(m(-2.83), m(0), m(0))
    j077 = Point(m(2.83), m(0), m(0))
    j078 = Point(m(6.03), m(0), m(0))
    j079 = Point(m(9.5), m(0), m(0))
    j080 = Point(m(11.79), m(0), m(0))
    j081 = Point(m(14.59), m(0), m(0))
    j082 = Point(m(15.67), m(0), m(0))
    j083 = Point(m(16.32), m(0), m(0))
    j084 = Point(m(-16), m(0), m(0))
    j085 = Point(m(16), m(0), m(0))
    j086 = Point(m(-3.01), m(0), m(-2.6))
    j087 = Point(m(3.01), m(0), m(-2.6))
    j088 = Point(m(-3.19), m(0), m(-5.3))
    j089 = Point(m(3.19), m(0), m(-5.3))
    j090 = Point(m(-3.39), m(0), m(-8.3))
    j091 = Point(m(3.39), m(0), m(-8.3))
    j092 = Point(m(-1.69), m(0), m(-9.66))
    j093 = Point(m(1.71), m(0), m(-9.66))
    j094 = Point(m(-3.58), m(0), m(-11))
    j095 = Point(m(0.01), m(0), m(-11))
    j096 = Point(m(3.58), m(0), m(-11))
    j097 = Point(m(-1.79), m(0), m(-12.42))
    j098 = Point(m(1.89), m(0), m(-12.5))
    j099 = Point(m(-3.78), m(0), m(-14.01))
    j100 = Point(m(3.78), m(0), m(-14.01))
    j101 = Point(m(-4.02), m(0), m(-15.03))
    j102 = Point(m(-1.89), m(0), m(-15.03))
    j103 = Point(m(1.89), m(0), m(-15.03))
    j104 = Point(m(4.02), m(0), m(-15.03))
    j105 = Point(m(-4.25), m(0), m(-16.06))
    j106 = Point(m(0.01), m(0), m(-16.06))
    j107 = Point(m(4.25), m(0), m(-16.06))
    j108 = Point(m(-4.55), m(0), m(-17.34))
    j109 = Point(m(-2.35), m(0), m(-17.34))
    j110 = Point(m(2.35), m(0), m(-17.34))
    j111 = Point(m(4.55), m(0), m(-17.34))
    j112 = Point(m(-4.72), m(0), m(-18.63))
    j113 = Point(m(4.72), m(0), m(-18.63))
    j114 = Point(m(-5.24), m(0), m(-20.34))
    j115 = Point(m(-2.35), m(0), m(-20.34))
    j116 = Point(m(2.35), m(0), m(-20.34))
    j117 = Point(m(5.24), m(0), m(-20.34))
    j118 = Point(m(-5.62), m(0), m(-21.99))
    j119 = Point(m(5.62), m(0), m(-21.99))
    j120 = Point(m(-5.99), m(0), m(-23.57))
    j121 = Point(m(-2.07), m(0), m(-23.57))
    j122 = Point(m(2.07), m(0), m(-23.57))
    j123 = Point(m(5.99), m(0), m(-23.57))
    j124 = Point(m(-6.29), m(0), m(-24.89))
    j125 = Point(m(-3.89), m(0), m(-24.89))
    j126 = Point(m(3.89), m(0), m(-24.89))
    j127 = Point(m(6.29), m(0), m(-24.89))
    j128 = Point(m(-6.78), m(0), m(-27))
    j129 = Point(m(6.78), m(0), m(-27))
    return Tower(
        name="D-2-D-2018.3 WE WAdiff140",
        datum=LowestCrossarm((m(27),)),
        voltages=(kv(380),),
        line_angles=(),
        attachments=(
            Mount(Wire.SHIELD, Point(m(-8.6), m(0), m(20.5)), Hold.CLAMP),
            Mount(Wire.SHIELD, Point(m(8.6), m(0), m(20.5)), Hold.CLAMP),
            Mount(Wire.PHASE, Point(m(-12.5), m(0), m(10)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(12.5), m(0), m(10)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-16), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-9.5), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(9.5), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(16), m(0), m(0)), Hold.STRAIN),
        ),
        bases=(),
        body=(
            Body(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j121, j116, role=Role.DIAGONAL_BRACE),
                        Bar(j122, j115, role=Role.DIAGONAL_BRACE),
                        Bar(j119, j118, role=Role.TRANSVERSE_BRACE),
                        Bar(j020, j021, role=Role.TRANSVERSE_BRACE),
                        Bar(j044, j045, role=Role.TRANSVERSE_BRACE),
                        Bar(j076, j077, role=Role.TRANSVERSE_BRACE),
                        Bar(j056, j057, role=Role.TRANSVERSE_BRACE),
                        Bar(j077, j086, role=Role.DIAGONAL_BRACE),
                        Bar(j086, j089, role=Role.DIAGONAL_BRACE),
                        Bar(j089, j090, role=Role.DIAGONAL_BRACE),
                        Bar(j091, j088, role=Role.DIAGONAL_BRACE),
                        Bar(j088, j087, role=Role.DIAGONAL_BRACE),
                        Bar(j087, j076, role=Role.DIAGONAL_BRACE),
                        Bar(j094, j095, role=Role.TRANSVERSE_BRACE),
                        Bar(j095, j096, role=Role.TRANSVERSE_BRACE),
                        Bar(j100, j098, role=Role.DIAGONAL_BRACE),
                        Bar(j098, j095, role=Role.DIAGONAL_BRACE),
                        Bar(j095, j092, role=Role.DIAGONAL_BRACE),
                        Bar(j092, j090, role=Role.DIAGONAL_BRACE),
                        Bar(j099, j097, role=Role.DIAGONAL_BRACE),
                        Bar(j097, j095, role=Role.DIAGONAL_BRACE),
                        Bar(j095, j093, role=Role.DIAGONAL_BRACE),
                        Bar(j093, j091, role=Role.DIAGONAL_BRACE),
                        Bar(j092, j094, role=Role.DIAGONAL_BRACE),
                        Bar(j094, j097, role=Role.DIAGONAL_BRACE),
                        Bar(j093, j096, role=Role.DIAGONAL_BRACE),
                        Bar(j096, j098, role=Role.DIAGONAL_BRACE),
                        Bar(j106, j102, role=Role.DIAGONAL_BRACE),
                        Bar(j109, j106, role=Role.DIAGONAL_BRACE),
                        Bar(j106, j105, role=Role.TRANSVERSE_BRACE),
                        Bar(j099, j094, role=Role.CHORD),
                        Bar(j094, j090, role=Role.CHORD),
                        Bar(j090, j088, role=Role.CHORD),
                        Bar(j088, j086, role=Role.CHORD),
                        Bar(j086, j076, role=Role.CHORD),
                        Bar(j076, j061, role=Role.CHORD),
                        Bar(j061, j056, role=Role.CHORD),
                        Bar(j057, j061, role=Role.DIAGONAL_BRACE),
                        Bar(j061, j077, role=Role.DIAGONAL_BRACE),
                        Bar(j077, j087, role=Role.CHORD),
                        Bar(j087, j089, role=Role.CHORD),
                        Bar(j089, j091, role=Role.CHORD),
                        Bar(j091, j096, role=Role.CHORD),
                        Bar(j096, j100, role=Role.CHORD),
                        Bar(j056, j062, role=Role.DIAGONAL_BRACE),
                        Bar(j062, j076, role=Role.DIAGONAL_BRACE),
                        Bar(j056, j054, role=Role.CHORD),
                        Bar(j054, j052, role=Role.CHORD),
                        Bar(j052, j044, role=Role.CHORD),
                        Bar(j044, j026, role=Role.CHORD),
                        Bar(j026, j020, role=Role.CHORD),
                        Bar(j045, j026, role=Role.DIAGONAL_BRACE),
                        Bar(j026, j021, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j027, role=Role.CHORD),
                        Bar(j027, j045, role=Role.CHORD),
                        Bar(j045, j053, role=Role.CHORD),
                        Bar(j053, j055, role=Role.CHORD),
                        Bar(j055, j057, role=Role.CHORD),
                        Bar(j057, j062, role=Role.CHORD),
                        Bar(j062, j077, role=Role.CHORD),
                        Bar(j057, j054, role=Role.DIAGONAL_BRACE),
                        Bar(j054, j053, role=Role.DIAGONAL_BRACE),
                        Bar(j053, j044, role=Role.DIAGONAL_BRACE),
                        Bar(j044, j027, role=Role.DIAGONAL_BRACE),
                        Bar(j027, j020, role=Role.DIAGONAL_BRACE),
                        Bar(j056, j055, role=Role.DIAGONAL_BRACE),
                        Bar(j055, j052, role=Role.DIAGONAL_BRACE),
                        Bar(j052, j045, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        legs=(
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j128, j124, role=Role.CHORD),
                        Bar(j124, j120, role=Role.CHORD),
                        Bar(j120, j118, role=Role.CHORD),
                        Bar(j118, j114, role=Role.CHORD),
                        Bar(j114, j108, role=Role.CHORD),
                        Bar(j108, j105, role=Role.CHORD),
                        Bar(j105, j101, role=Role.CHORD),
                        Bar(j101, j099, role=Role.CHORD),
                        Bar(j128, j125, role=Role.DIAGONAL_BRACE),
                        Bar(j125, j121, role=Role.DIAGONAL_BRACE),
                        Bar(j115, j112, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j120, role=Role.TRANSVERSE_BRACE),
                        Bar(j125, j124, role=Role.TRANSVERSE_BRACE),
                        Bar(j115, j114, role=Role.TRANSVERSE_BRACE),
                        Bar(j125, j120, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j118, role=Role.DIAGONAL_BRACE),
                        Bar(j118, j115, role=Role.DIAGONAL_BRACE),
                        Bar(j102, j099, role=Role.DIAGONAL_BRACE),
                        Bar(j112, j109, role=Role.DIAGONAL_BRACE),
                        Bar(j105, j102, role=Role.DIAGONAL_BRACE),
                        Bar(j105, j109, role=Role.DIAGONAL_BRACE),
                        Bar(j108, j109, role=Role.TRANSVERSE_BRACE),
                        Bar(j101, j102, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j100, j104, role=Role.CHORD),
                        Bar(j104, j107, role=Role.CHORD),
                        Bar(j107, j111, role=Role.CHORD),
                        Bar(j111, j117, role=Role.CHORD),
                        Bar(j117, j119, role=Role.CHORD),
                        Bar(j119, j123, role=Role.CHORD),
                        Bar(j123, j127, role=Role.CHORD),
                        Bar(j127, j129, role=Role.CHORD),
                        Bar(j116, j113, role=Role.DIAGONAL_BRACE),
                        Bar(j129, j126, role=Role.DIAGONAL_BRACE),
                        Bar(j126, j122, role=Role.DIAGONAL_BRACE),
                        Bar(j122, j123, role=Role.TRANSVERSE_BRACE),
                        Bar(j126, j127, role=Role.TRANSVERSE_BRACE),
                        Bar(j116, j117, role=Role.TRANSVERSE_BRACE),
                        Bar(j126, j123, role=Role.DIAGONAL_BRACE),
                        Bar(j122, j119, role=Role.DIAGONAL_BRACE),
                        Bar(j119, j116, role=Role.DIAGONAL_BRACE),
                        Bar(j113, j110, role=Role.DIAGONAL_BRACE),
                        Bar(j110, j106, role=Role.DIAGONAL_BRACE),
                        Bar(j106, j103, role=Role.DIAGONAL_BRACE),
                        Bar(j103, j100, role=Role.DIAGONAL_BRACE),
                        Bar(j107, j106, role=Role.TRANSVERSE_BRACE),
                        Bar(j103, j107, role=Role.DIAGONAL_BRACE),
                        Bar(j107, j110, role=Role.DIAGONAL_BRACE),
                        Bar(j103, j104, role=Role.TRANSVERSE_BRACE),
                        Bar(j110, j111, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        head=(
            Head(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j015, j017, role=Role.DIAGONAL_BRACE),
                        Bar(j017, j016, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j017, role=Role.DIAGONAL_BRACE),
                        Bar(j017, j020, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j016, role=Role.CHORD),
                        Bar(j020, j015, role=Role.CHORD),
                    ),
                )
            ),
        ),
        crossarms=(
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j038, j036, role=Role.CHORD),
                        Bar(j036, j039, role=Role.CHORD),
                        Bar(j039, j034, role=Role.CHORD),
                        Bar(j034, j040, role=Role.CHORD),
                        Bar(j040, j041, role=Role.CHORD),
                        Bar(j041, j042, role=Role.CHORD),
                        Bar(j042, j043, role=Role.CHORD),
                        Bar(j043, j044, role=Role.CHORD),
                        Bar(j032, j030, role=Role.CHORD),
                        Bar(j030, j024, role=Role.CHORD),
                        Bar(j024, j022, role=Role.CHORD),
                        Bar(j022, j020, role=Role.CHORD),
                        Bar(j032, j038, role=Role.CHORD),
                        Bar(j044, j028, role=Role.DIAGONAL_BRACE),
                        Bar(j028, j043, role=Role.TRANSVERSE_BRACE),
                        Bar(j022, j042, role=Role.TRANSVERSE_BRACE),
                        Bar(j042, j028, role=Role.DIAGONAL_BRACE),
                        Bar(j028, j020, role=Role.DIAGONAL_BRACE),
                        Bar(j041, j024, role=Role.TRANSVERSE_BRACE),
                        Bar(j024, j042, role=Role.DIAGONAL_BRACE),
                        Bar(j024, j034, role=Role.DIAGONAL_BRACE),
                        Bar(j039, j030, role=Role.TRANSVERSE_BRACE),
                        Bar(j030, j040, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j045, j046, role=Role.CHORD),
                        Bar(j046, j047, role=Role.CHORD),
                        Bar(j047, j048, role=Role.CHORD),
                        Bar(j048, j049, role=Role.CHORD),
                        Bar(j049, j035, role=Role.CHORD),
                        Bar(j035, j050, role=Role.CHORD),
                        Bar(j050, j037, role=Role.CHORD),
                        Bar(j037, j051, role=Role.CHORD),
                        Bar(j051, j033, role=Role.CHORD),
                        Bar(j033, j031, role=Role.CHORD),
                        Bar(j031, j025, role=Role.CHORD),
                        Bar(j025, j023, role=Role.CHORD),
                        Bar(j023, j021, role=Role.CHORD),
                        Bar(j031, j050, role=Role.TRANSVERSE_BRACE),
                        Bar(j031, j049, role=Role.DIAGONAL_BRACE),
                        Bar(j048, j025, role=Role.TRANSVERSE_BRACE),
                        Bar(j025, j047, role=Role.DIAGONAL_BRACE),
                        Bar(j025, j035, role=Role.DIAGONAL_BRACE),
                        Bar(j023, j047, role=Role.TRANSVERSE_BRACE),
                        Bar(j047, j029, role=Role.DIAGONAL_BRACE),
                        Bar(j029, j021, role=Role.DIAGONAL_BRACE),
                        Bar(j045, j029, role=Role.DIAGONAL_BRACE),
                        Bar(j029, j046, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j070, j084, role=Role.CHORD),
                        Bar(j084, j071, role=Role.CHORD),
                        Bar(j071, j072, role=Role.CHORD),
                        Bar(j072, j073, role=Role.CHORD),
                        Bar(j073, j074, role=Role.CHORD),
                        Bar(j074, j075, role=Role.CHORD),
                        Bar(j075, j076, role=Role.CHORD),
                        Bar(j070, j068, role=Role.CHORD),
                        Bar(j068, j066, role=Role.CHORD),
                        Bar(j066, j064, role=Role.CHORD),
                        Bar(j064, j058, role=Role.CHORD),
                        Bar(j058, j056, role=Role.CHORD),
                        Bar(j066, j071, role=Role.TRANSVERSE_BRACE),
                        Bar(j056, j060, role=Role.DIAGONAL_BRACE),
                        Bar(j060, j074, role=Role.DIAGONAL_BRACE),
                        Bar(j074, j058, role=Role.TRANSVERSE_BRACE),
                        Bar(j066, j072, role=Role.DIAGONAL_BRACE),
                        Bar(j072, j064, role=Role.DIAGONAL_BRACE),
                        Bar(j064, j074, role=Role.DIAGONAL_BRACE),
                        Bar(j073, j064, role=Role.TRANSVERSE_BRACE),
                        Bar(j076, j060, role=Role.DIAGONAL_BRACE),
                        Bar(j060, j075, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j077, j078, role=Role.CHORD),
                        Bar(j078, j079, role=Role.CHORD),
                        Bar(j079, j080, role=Role.CHORD),
                        Bar(j080, j081, role=Role.CHORD),
                        Bar(j081, j082, role=Role.CHORD),
                        Bar(j082, j085, role=Role.CHORD),
                        Bar(j085, j083, role=Role.CHORD),
                        Bar(j083, j069, role=Role.CHORD),
                        Bar(j069, j067, role=Role.CHORD),
                        Bar(j067, j065, role=Role.CHORD),
                        Bar(j065, j059, role=Role.CHORD),
                        Bar(j059, j057, role=Role.CHORD),
                        Bar(j067, j082, role=Role.TRANSVERSE_BRACE),
                        Bar(j067, j081, role=Role.DIAGONAL_BRACE),
                        Bar(j081, j065, role=Role.DIAGONAL_BRACE),
                        Bar(j065, j079, role=Role.DIAGONAL_BRACE),
                        Bar(j079, j059, role=Role.TRANSVERSE_BRACE),
                        Bar(j080, j065, role=Role.TRANSVERSE_BRACE),
                        Bar(j077, j063, role=Role.DIAGONAL_BRACE),
                        Bar(j063, j078, role=Role.TRANSVERSE_BRACE),
                        Bar(j057, j063, role=Role.DIAGONAL_BRACE),
                        Bar(j063, j079, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        peaks=(
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j001, j003, role=Role.CHORD),
                        Bar(j003, j009, role=Role.CHORD),
                        Bar(j009, j013, role=Role.CHORD),
                        Bar(j013, j018, role=Role.CHORD),
                        Bar(j018, j020, role=Role.CHORD),
                        Bar(j001, j005, role=Role.CHORD),
                        Bar(j005, j007, role=Role.CHORD),
                        Bar(j007, j011, role=Role.CHORD),
                        Bar(j011, j015, role=Role.CHORD),
                        Bar(j015, j018, role=Role.DIAGONAL_BRACE),
                        Bar(j018, j011, role=Role.TRANSVERSE_BRACE),
                        Bar(j011, j013, role=Role.DIAGONAL_BRACE),
                        Bar(j013, j007, role=Role.DIAGONAL_BRACE),
                        Bar(j007, j009, role=Role.DIAGONAL_BRACE),
                        Bar(j009, j005, role=Role.DIAGONAL_BRACE),
                        Bar(j005, j003, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j016, j012, role=Role.CHORD),
                        Bar(j012, j008, role=Role.CHORD),
                        Bar(j008, j006, role=Role.CHORD),
                        Bar(j006, j002, role=Role.CHORD),
                        Bar(j002, j004, role=Role.CHORD),
                        Bar(j004, j010, role=Role.CHORD),
                        Bar(j010, j014, role=Role.CHORD),
                        Bar(j014, j019, role=Role.CHORD),
                        Bar(j019, j021, role=Role.CHORD),
                        Bar(j016, j019, role=Role.DIAGONAL_BRACE),
                        Bar(j019, j012, role=Role.TRANSVERSE_BRACE),
                        Bar(j012, j014, role=Role.DIAGONAL_BRACE),
                        Bar(j014, j008, role=Role.DIAGONAL_BRACE),
                        Bar(j008, j010, role=Role.DIAGONAL_BRACE),
                        Bar(j010, j006, role=Role.DIAGONAL_BRACE),
                        Bar(j006, j004, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
    )


D_2_D_2018_3_WE_WADIFF140 = _d_2_d_2018_3_we_wadiff140()


def _d_2_t_2019_1_t1() -> Tower[LowestCrossarm]:
    """D-2-T-2019.1 T1: each joint written once, by its key."""
    j001 = Point(m(-4.5), m(0), m(26.5))
    j002 = Point(m(-4.28), m(0), m(26.5))
    j003 = Point(m(4.27), m(0), m(26.5))
    j004 = Point(m(4.5), m(0), m(26.5))
    j005 = Point(m(-3.97), m(0), m(25.6))
    j006 = Point(m(-2.93), m(0), m(25.6))
    j007 = Point(m(2.93), m(0), m(25.6))
    j008 = Point(m(3.96), m(0), m(25.6))
    j009 = Point(m(-1.47), m(0), m(24.73))
    j010 = Point(m(1.47), m(0), m(24.73))
    j011 = Point(m(-3.06), m(0), m(24.33))
    j012 = Point(m(3.06), m(0), m(24.33))
    j013 = Point(m(0), m(0), m(23.98))
    j014 = Point(m(-2.06), m(0), m(23.14))
    j015 = Point(m(2.06), m(0), m(23.14))
    j016 = Point(m(-1.42), m(0), m(22.46))
    j017 = Point(m(0), m(0), m(22.46))
    j018 = Point(m(1.42), m(0), m(22.46))
    j019 = Point(m(-4.1), m(0), m(21.77))
    j020 = Point(m(4.09), m(0), m(21.77))
    j021 = Point(m(-1.45), m(0), m(21.31))
    j022 = Point(m(1.45), m(0), m(21.31))
    j023 = Point(m(-2.76), m(0), m(21.23))
    j024 = Point(m(2.77), m(0), m(21.23))
    j025 = Point(m(-6.92), m(0), m(21.05))
    j026 = Point(m(6.92), m(0), m(21.05))
    j027 = Point(m(-9.75), m(0), m(20.33))
    j028 = Point(m(9.73), m(0), m(20.33))
    j029 = Point(m(-9.75), m(0), m(20))
    j030 = Point(m(-6.92), m(0), m(20))
    j031 = Point(m(-4.11), m(0), m(20))
    j032 = Point(m(-1.49), m(0), m(20))
    j033 = Point(m(1.49), m(0), m(20))
    j034 = Point(m(4.1), m(0), m(20))
    j035 = Point(m(6.92), m(0), m(20))
    j036 = Point(m(9.73), m(0), m(20))
    j037 = Point(m(-1.55), m(0), m(18.21))
    j038 = Point(m(1.55), m(0), m(18.21))
    j039 = Point(m(-1.59), m(0), m(16.73))
    j040 = Point(m(1.59), m(0), m(16.73))
    j041 = Point(m(-1.66), m(0), m(14.5))
    j042 = Point(m(1.66), m(0), m(14.5))
    j043 = Point(m(-6.51), m(0), m(12.7))
    j044 = Point(m(6.5), m(0), m(12.7))
    j045 = Point(m(-1.73), m(0), m(12.35))
    j046 = Point(m(1.73), m(0), m(12.35))
    j047 = Point(m(-4.1), m(0), m(12.24))
    j048 = Point(m(4.1), m(0), m(12.24))
    j049 = Point(m(-9.43), m(0), m(11.62))
    j050 = Point(m(9.42), m(0), m(11.62))
    j051 = Point(m(-12.35), m(0), m(10.52))
    j052 = Point(m(12.33), m(0), m(10.52))
    j053 = Point(m(-12.35), m(0), m(10))
    j054 = Point(m(-9.43), m(0), m(10))
    j055 = Point(m(-6.51), m(0), m(10))
    j056 = Point(m(-1.8), m(0), m(10))
    j057 = Point(m(1.8), m(0), m(10))
    j058 = Point(m(6.5), m(0), m(10))
    j059 = Point(m(9.42), m(0), m(10))
    j060 = Point(m(12.33), m(0), m(10))
    j061 = Point(m(-1.86), m(0), m(8.07))
    j062 = Point(m(1.86), m(0), m(8.07))
    j063 = Point(m(-1.91), m(0), m(6.13))
    j064 = Point(m(1.91), m(0), m(6.13))
    j065 = Point(m(-1.98), m(0), m(3.99))
    j066 = Point(m(1.98), m(0), m(3.99))
    j067 = Point(m(-4.69), m(0), m(2.86))
    j068 = Point(m(4.68), m(0), m(2.86))
    j069 = Point(m(-2.04), m(0), m(2.14))
    j070 = Point(m(2.04), m(0), m(2.14))
    j071 = Point(m(-3.34), m(0), m(2))
    j072 = Point(m(3.34), m(0), m(2))
    j073 = Point(m(-7.44), m(0), m(1.7))
    j074 = Point(m(7.43), m(0), m(1.7))
    j075 = Point(m(-10.17), m(0), m(0.54))
    j076 = Point(m(10.15), m(0), m(0.54))
    j077 = Point(m(-10.17), m(0), m(0))
    j078 = Point(m(-7.43), m(0), m(0))
    j079 = Point(m(-4.69), m(0), m(0))
    j080 = Point(m(-2.1), m(0), m(0))
    j081 = Point(m(-0.28), m(0), m(0))
    j082 = Point(m(0.28), m(0), m(0))
    j083 = Point(m(2.1), m(0), m(0))
    j084 = Point(m(4.68), m(0), m(0))
    j085 = Point(m(7.43), m(0), m(0))
    j086 = Point(m(10.15), m(0), m(0))
    j087 = Point(m(-2.14), m(0), m(-1.86))
    j088 = Point(m(2.14), m(0), m(-1.86))
    j089 = Point(m(-2.21), m(0), m(-4.83))
    j090 = Point(m(2.21), m(0), m(-4.83))
    j091 = Point(m(-2.3), m(0), m(-8.81))
    j092 = Point(m(2.3), m(0), m(-8.81))
    j093 = Point(m(-2.4), m(0), m(-13.27))
    j094 = Point(m(2.4), m(0), m(-13.27))
    j095 = Point(m(-2.51), m(0), m(-18.28))
    j096 = Point(m(2.51), m(0), m(-18.28))
    j097 = Point(m(-2.66), m(0), m(-19.5))
    j098 = Point(m(-1.15), m(0), m(-19.5))
    j099 = Point(m(1.15), m(0), m(-19.5))
    j100 = Point(m(2.66), m(0), m(-19.5))
    j101 = Point(m(-2.78), m(0), m(-20.53))
    j102 = Point(m(2.78), m(0), m(-20.53))
    j103 = Point(m(-2.9), m(0), m(-21.52))
    j104 = Point(m(-1.09), m(0), m(-21.52))
    j105 = Point(m(1.09), m(0), m(-21.52))
    j106 = Point(m(2.9), m(0), m(-21.52))
    j107 = Point(m(-3.03), m(0), m(-22.55))
    j108 = Point(m(-2.24), m(0), m(-22.55))
    j109 = Point(m(2.24), m(0), m(-22.55))
    j110 = Point(m(3.03), m(0), m(-22.55))
    j111 = Point(m(-3.13), m(0), m(-23.36))
    j112 = Point(m(3.13), m(0), m(-23.36))
    j113 = Point(m(-3.36), m(0), m(-25.24))
    j114 = Point(m(-1.53), m(0), m(-25.24))
    j115 = Point(m(1.53), m(0), m(-25.24))
    j116 = Point(m(3.36), m(0), m(-25.24))
    j117 = Point(m(-3.58), m(0), m(-27.05))
    j118 = Point(m(3.58), m(0), m(-27.05))
    j119 = Point(m(-3.79), m(0), m(-28.78))
    j120 = Point(m(-1.46), m(0), m(-28.78))
    j121 = Point(m(1.47), m(0), m(-28.78))
    j122 = Point(m(3.79), m(0), m(-28.78))
    j123 = Point(m(-3.97), m(0), m(-30.24))
    j124 = Point(m(-2.7), m(0), m(-30.24))
    j125 = Point(m(2.7), m(0), m(-30.24))
    j126 = Point(m(3.97), m(0), m(-30.24))
    j127 = Point(m(-4.18), m(0), m(-32))
    j128 = Point(m(4.18), m(0), m(-32))
    return Tower(
        name="D-2-T-2019.1 T1",
        datum=LowestCrossarm((m(32), m(35), m(38), m(41), m(50))),
        voltages=(kv(380),),
        line_angles=(),
        attachments=(
            Mount(Wire.SHIELD, Point(m(-4.5), m(0), m(26.5)), Hold.CLAMP),
            Mount(Wire.SHIELD, Point(m(4.5), m(0), m(26.5)), Hold.CLAMP),
            WirePosition(
                Wire.PHASE,
                Point(m(-7), m(0), m(16.35)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j029),
                    InsulatorString(mount=j031),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(7), m(0), m(16.35)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j036),
                    InsulatorString(mount=j034),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(-9.5), m(0), m(6.34)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j053),
                    InsulatorString(mount=j055),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(9.5), m(0), m(6.34)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j060),
                    InsulatorString(mount=j058),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(-7.5), m(0), m(-3.62)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j077),
                    InsulatorString(mount=j079),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(7.5), m(0), m(-3.62)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j086),
                    InsulatorString(mount=j084),
                ),
            ),
        ),
        bases=(),
        body=(
            Body(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j065, j066, role=Role.TRANSVERSE_BRACE),
                        Bar(j080, j069, role=Role.CHORD),
                        Bar(j069, j065, role=Role.CHORD),
                        Bar(j065, j063, role=Role.CHORD),
                        Bar(j063, j061, role=Role.CHORD),
                        Bar(j061, j056, role=Role.CHORD),
                        Bar(j056, j045, role=Role.CHORD),
                        Bar(j045, j041, role=Role.CHORD),
                        Bar(j041, j039, role=Role.CHORD),
                        Bar(j039, j037, role=Role.CHORD),
                        Bar(j037, j032, role=Role.CHORD),
                        Bar(j032, j021, role=Role.CHORD),
                        Bar(j021, j016, role=Role.CHORD),
                        Bar(j018, j022, role=Role.CHORD),
                        Bar(j022, j033, role=Role.CHORD),
                        Bar(j033, j038, role=Role.CHORD),
                        Bar(j038, j040, role=Role.CHORD),
                        Bar(j040, j042, role=Role.CHORD),
                        Bar(j042, j046, role=Role.CHORD),
                        Bar(j046, j057, role=Role.CHORD),
                        Bar(j057, j062, role=Role.CHORD),
                        Bar(j062, j064, role=Role.CHORD),
                        Bar(j064, j066, role=Role.CHORD),
                        Bar(j066, j070, role=Role.CHORD),
                        Bar(j070, j083, role=Role.CHORD),
                        Bar(j080, j087, role=Role.CHORD),
                        Bar(j087, j089, role=Role.CHORD),
                        Bar(j089, j091, role=Role.CHORD),
                        Bar(j091, j093, role=Role.CHORD),
                        Bar(j093, j095, role=Role.CHORD),
                        Bar(j083, j088, role=Role.CHORD),
                        Bar(j088, j090, role=Role.CHORD),
                        Bar(j090, j092, role=Role.CHORD),
                        Bar(j092, j094, role=Role.CHORD),
                        Bar(j094, j096, role=Role.CHORD),
                        Bar(j041, j042, role=Role.TRANSVERSE_BRACE),
                        Bar(j080, j070, role=Role.DIAGONAL_BRACE),
                        Bar(j070, j065, role=Role.DIAGONAL_BRACE),
                        Bar(j056, j046, role=Role.DIAGONAL_BRACE),
                        Bar(j046, j041, role=Role.DIAGONAL_BRACE),
                        Bar(j032, j022, role=Role.DIAGONAL_BRACE),
                        Bar(j022, j016, role=Role.DIAGONAL_BRACE),
                        Bar(j083, j069, role=Role.DIAGONAL_BRACE),
                        Bar(j069, j066, role=Role.DIAGONAL_BRACE),
                        Bar(j057, j045, role=Role.DIAGONAL_BRACE),
                        Bar(j045, j042, role=Role.DIAGONAL_BRACE),
                        Bar(j033, j021, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j018, role=Role.DIAGONAL_BRACE),
                        Bar(j065, j064, role=Role.DIAGONAL_BRACE),
                        Bar(j064, j061, role=Role.DIAGONAL_BRACE),
                        Bar(j061, j057, role=Role.DIAGONAL_BRACE),
                        Bar(j066, j063, role=Role.DIAGONAL_BRACE),
                        Bar(j063, j062, role=Role.DIAGONAL_BRACE),
                        Bar(j062, j056, role=Role.DIAGONAL_BRACE),
                        Bar(j041, j040, role=Role.DIAGONAL_BRACE),
                        Bar(j040, j037, role=Role.DIAGONAL_BRACE),
                        Bar(j037, j033, role=Role.DIAGONAL_BRACE),
                        Bar(j042, j039, role=Role.DIAGONAL_BRACE),
                        Bar(j039, j038, role=Role.DIAGONAL_BRACE),
                        Bar(j038, j032, role=Role.DIAGONAL_BRACE),
                        Bar(j120, j115, role=Role.DIAGONAL_BRACE),
                        Bar(j105, j098, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j114, role=Role.DIAGONAL_BRACE),
                        Bar(j104, j099, role=Role.DIAGONAL_BRACE),
                        Bar(j095, j094, role=Role.DIAGONAL_BRACE),
                        Bar(j094, j091, role=Role.DIAGONAL_BRACE),
                        Bar(j091, j090, role=Role.DIAGONAL_BRACE),
                        Bar(j090, j087, role=Role.DIAGONAL_BRACE),
                        Bar(j087, j083, role=Role.DIAGONAL_BRACE),
                        Bar(j096, j093, role=Role.DIAGONAL_BRACE),
                        Bar(j093, j092, role=Role.DIAGONAL_BRACE),
                        Bar(j092, j089, role=Role.DIAGONAL_BRACE),
                        Bar(j089, j088, role=Role.DIAGONAL_BRACE),
                        Bar(j088, j080, role=Role.DIAGONAL_BRACE),
                        Bar(j118, j117, role=Role.TRANSVERSE_BRACE),
                        Bar(j102, j101, role=Role.TRANSVERSE_BRACE),
                        Bar(j095, j096, role=Role.TRANSVERSE_BRACE),
                        Bar(j032, j033, role=Role.TRANSVERSE_BRACE),
                        Bar(j056, j057, role=Role.TRANSVERSE_BRACE),
                        Bar(j080, j081, role=Role.TRANSVERSE_BRACE),
                        Bar(j081, j082, role=Role.TRANSVERSE_BRACE),
                        Bar(j082, j083, role=Role.TRANSVERSE_BRACE),
                        Bar(j018, j017, role=Role.TRANSVERSE_BRACE),
                        Bar(j017, j016, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        legs=(
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j127, j123, role=Role.CHORD),
                        Bar(j123, j119, role=Role.CHORD),
                        Bar(j119, j117, role=Role.CHORD),
                        Bar(j117, j113, role=Role.CHORD),
                        Bar(j113, j111, role=Role.CHORD),
                        Bar(j111, j107, role=Role.CHORD),
                        Bar(j107, j103, role=Role.CHORD),
                        Bar(j103, j101, role=Role.CHORD),
                        Bar(j101, j097, role=Role.CHORD),
                        Bar(j097, j095, role=Role.CHORD),
                        Bar(j127, j124, role=Role.DIAGONAL_BRACE),
                        Bar(j124, j120, role=Role.DIAGONAL_BRACE),
                        Bar(j098, j095, role=Role.DIAGONAL_BRACE),
                        Bar(j114, j111, role=Role.DIAGONAL_BRACE),
                        Bar(j111, j108, role=Role.DIAGONAL_BRACE),
                        Bar(j108, j104, role=Role.DIAGONAL_BRACE),
                        Bar(j120, j119, role=Role.TRANSVERSE_BRACE),
                        Bar(j124, j123, role=Role.TRANSVERSE_BRACE),
                        Bar(j114, j113, role=Role.TRANSVERSE_BRACE),
                        Bar(j124, j119, role=Role.DIAGONAL_BRACE),
                        Bar(j120, j117, role=Role.DIAGONAL_BRACE),
                        Bar(j117, j114, role=Role.DIAGONAL_BRACE),
                        Bar(j098, j097, role=Role.TRANSVERSE_BRACE),
                        Bar(j104, j103, role=Role.TRANSVERSE_BRACE),
                        Bar(j103, j108, role=Role.DIAGONAL_BRACE),
                        Bar(j108, j107, role=Role.TRANSVERSE_BRACE),
                        Bar(j104, j101, role=Role.DIAGONAL_BRACE),
                        Bar(j101, j098, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j096, j100, role=Role.CHORD),
                        Bar(j100, j102, role=Role.CHORD),
                        Bar(j102, j106, role=Role.CHORD),
                        Bar(j106, j110, role=Role.CHORD),
                        Bar(j110, j112, role=Role.CHORD),
                        Bar(j112, j116, role=Role.CHORD),
                        Bar(j116, j118, role=Role.CHORD),
                        Bar(j118, j122, role=Role.CHORD),
                        Bar(j122, j126, role=Role.CHORD),
                        Bar(j126, j128, role=Role.CHORD),
                        Bar(j115, j112, role=Role.DIAGONAL_BRACE),
                        Bar(j112, j109, role=Role.DIAGONAL_BRACE),
                        Bar(j109, j105, role=Role.DIAGONAL_BRACE),
                        Bar(j128, j125, role=Role.DIAGONAL_BRACE),
                        Bar(j125, j121, role=Role.DIAGONAL_BRACE),
                        Bar(j099, j096, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j122, role=Role.TRANSVERSE_BRACE),
                        Bar(j125, j126, role=Role.TRANSVERSE_BRACE),
                        Bar(j115, j116, role=Role.TRANSVERSE_BRACE),
                        Bar(j125, j122, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j118, role=Role.DIAGONAL_BRACE),
                        Bar(j118, j115, role=Role.DIAGONAL_BRACE),
                        Bar(j099, j100, role=Role.TRANSVERSE_BRACE),
                        Bar(j105, j106, role=Role.TRANSVERSE_BRACE),
                        Bar(j106, j109, role=Role.DIAGONAL_BRACE),
                        Bar(j109, j110, role=Role.TRANSVERSE_BRACE),
                        Bar(j105, j102, role=Role.DIAGONAL_BRACE),
                        Bar(j102, j099, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        head=(
            Head(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j017, j013, role=Role.TRANSVERSE_BRACE),
                        Bar(j013, j016, role=Role.CHORD),
                        Bar(j013, j018, role=Role.CHORD),
                    ),
                )
            ),
        ),
        crossarms=(
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j029, j030, role=Role.CHORD),
                        Bar(j030, j031, role=Role.CHORD),
                        Bar(j031, j032, role=Role.CHORD),
                        Bar(j016, j019, role=Role.CHORD),
                        Bar(j019, j025, role=Role.CHORD),
                        Bar(j025, j027, role=Role.CHORD),
                        Bar(j019, j031, role=Role.TRANSVERSE_BRACE),
                        Bar(j031, j025, role=Role.DIAGONAL_BRACE),
                        Bar(j025, j030, role=Role.TRANSVERSE_BRACE),
                        Bar(j029, j027, role=Role.CHORD),
                        Bar(j016, j023, role=Role.DIAGONAL_BRACE),
                        Bar(j023, j031, role=Role.DIAGONAL_BRACE),
                        Bar(j023, j032, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j036, j035, role=Role.CHORD),
                        Bar(j035, j034, role=Role.CHORD),
                        Bar(j034, j033, role=Role.CHORD),
                        Bar(j018, j020, role=Role.CHORD),
                        Bar(j020, j026, role=Role.CHORD),
                        Bar(j026, j028, role=Role.CHORD),
                        Bar(j020, j034, role=Role.TRANSVERSE_BRACE),
                        Bar(j034, j026, role=Role.DIAGONAL_BRACE),
                        Bar(j026, j035, role=Role.TRANSVERSE_BRACE),
                        Bar(j036, j028, role=Role.CHORD),
                        Bar(j018, j024, role=Role.DIAGONAL_BRACE),
                        Bar(j024, j034, role=Role.DIAGONAL_BRACE),
                        Bar(j024, j033, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j053, j054, role=Role.CHORD),
                        Bar(j054, j055, role=Role.CHORD),
                        Bar(j055, j056, role=Role.CHORD),
                        Bar(j041, j043, role=Role.CHORD),
                        Bar(j043, j049, role=Role.CHORD),
                        Bar(j049, j051, role=Role.CHORD),
                        Bar(j043, j055, role=Role.TRANSVERSE_BRACE),
                        Bar(j055, j049, role=Role.DIAGONAL_BRACE),
                        Bar(j049, j054, role=Role.TRANSVERSE_BRACE),
                        Bar(j053, j051, role=Role.CHORD),
                        Bar(j041, j047, role=Role.DIAGONAL_BRACE),
                        Bar(j047, j055, role=Role.DIAGONAL_BRACE),
                        Bar(j047, j056, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j060, j059, role=Role.CHORD),
                        Bar(j059, j058, role=Role.CHORD),
                        Bar(j058, j057, role=Role.CHORD),
                        Bar(j042, j044, role=Role.CHORD),
                        Bar(j044, j050, role=Role.CHORD),
                        Bar(j050, j052, role=Role.CHORD),
                        Bar(j044, j058, role=Role.TRANSVERSE_BRACE),
                        Bar(j058, j050, role=Role.DIAGONAL_BRACE),
                        Bar(j050, j059, role=Role.TRANSVERSE_BRACE),
                        Bar(j060, j052, role=Role.CHORD),
                        Bar(j042, j048, role=Role.DIAGONAL_BRACE),
                        Bar(j048, j058, role=Role.DIAGONAL_BRACE),
                        Bar(j048, j057, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j077, j078, role=Role.CHORD),
                        Bar(j078, j079, role=Role.CHORD),
                        Bar(j079, j080, role=Role.CHORD),
                        Bar(j065, j067, role=Role.CHORD),
                        Bar(j067, j073, role=Role.CHORD),
                        Bar(j073, j075, role=Role.CHORD),
                        Bar(j067, j079, role=Role.TRANSVERSE_BRACE),
                        Bar(j079, j073, role=Role.DIAGONAL_BRACE),
                        Bar(j073, j078, role=Role.TRANSVERSE_BRACE),
                        Bar(j077, j075, role=Role.CHORD),
                        Bar(j065, j071, role=Role.DIAGONAL_BRACE),
                        Bar(j071, j079, role=Role.DIAGONAL_BRACE),
                        Bar(j071, j080, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j086, j085, role=Role.CHORD),
                        Bar(j085, j084, role=Role.CHORD),
                        Bar(j084, j083, role=Role.CHORD),
                        Bar(j066, j068, role=Role.CHORD),
                        Bar(j068, j074, role=Role.CHORD),
                        Bar(j074, j076, role=Role.CHORD),
                        Bar(j068, j084, role=Role.TRANSVERSE_BRACE),
                        Bar(j084, j074, role=Role.DIAGONAL_BRACE),
                        Bar(j074, j085, role=Role.TRANSVERSE_BRACE),
                        Bar(j086, j076, role=Role.CHORD),
                        Bar(j066, j072, role=Role.DIAGONAL_BRACE),
                        Bar(j072, j084, role=Role.DIAGONAL_BRACE),
                        Bar(j072, j083, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        peaks=(
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j002, j005, role=Role.DIAGONAL_BRACE),
                        Bar(j005, j006, role=Role.TRANSVERSE_BRACE),
                        Bar(j006, j011, role=Role.TRANSVERSE_BRACE),
                        Bar(j011, j009, role=Role.DIAGONAL_BRACE),
                        Bar(j009, j014, role=Role.DIAGONAL_BRACE),
                        Bar(j014, j013, role=Role.DIAGONAL_BRACE),
                        Bar(j013, j009, role=Role.CHORD),
                        Bar(j009, j006, role=Role.CHORD),
                        Bar(j006, j002, role=Role.CHORD),
                        Bar(j002, j001, role=Role.CHORD),
                        Bar(j001, j005, role=Role.CHORD),
                        Bar(j005, j011, role=Role.CHORD),
                        Bar(j011, j014, role=Role.CHORD),
                        Bar(j014, j016, role=Role.CHORD),
                    ),
                )
            ),
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j003, j008, role=Role.DIAGONAL_BRACE),
                        Bar(j008, j007, role=Role.TRANSVERSE_BRACE),
                        Bar(j007, j012, role=Role.TRANSVERSE_BRACE),
                        Bar(j012, j010, role=Role.DIAGONAL_BRACE),
                        Bar(j010, j015, role=Role.DIAGONAL_BRACE),
                        Bar(j015, j013, role=Role.DIAGONAL_BRACE),
                        Bar(j018, j015, role=Role.CHORD),
                        Bar(j015, j012, role=Role.CHORD),
                        Bar(j012, j008, role=Role.CHORD),
                        Bar(j008, j004, role=Role.CHORD),
                        Bar(j004, j003, role=Role.CHORD),
                        Bar(j003, j007, role=Role.CHORD),
                        Bar(j007, j010, role=Role.CHORD),
                        Bar(j010, j013, role=Role.CHORD),
                    ),
                )
            ),
        ),
    )


D_2_T_2019_1_T1 = _d_2_t_2019_1_t1()


def _d_2_t_2019_1_t2() -> Tower[LowestCrossarm]:
    """D-2-T-2019.1 T2: each joint written once, by its key."""
    j001 = Point(m(-4.5), m(0), m(26.5))
    j002 = Point(m(-4.28), m(0), m(26.5))
    j003 = Point(m(4.27), m(0), m(26.5))
    j004 = Point(m(4.5), m(0), m(26.5))
    j005 = Point(m(-3.97), m(0), m(25.6))
    j006 = Point(m(-2.93), m(0), m(25.6))
    j007 = Point(m(2.93), m(0), m(25.6))
    j008 = Point(m(3.97), m(0), m(25.6))
    j009 = Point(m(-1.47), m(0), m(24.73))
    j010 = Point(m(1.47), m(0), m(24.73))
    j011 = Point(m(-3.06), m(0), m(24.33))
    j012 = Point(m(3.06), m(0), m(24.33))
    j013 = Point(m(0), m(0), m(23.98))
    j014 = Point(m(-2.06), m(0), m(23.14))
    j015 = Point(m(2.06), m(0), m(23.14))
    j016 = Point(m(0), m(0), m(22.47))
    j017 = Point(m(1.42), m(0), m(22.47))
    j018 = Point(m(-1.42), m(0), m(22.46))
    j019 = Point(m(-4.1), m(0), m(21.79))
    j020 = Point(m(4.1), m(0), m(21.79))
    j021 = Point(m(-1.45), m(0), m(21.33))
    j022 = Point(m(1.45), m(0), m(21.33))
    j023 = Point(m(-2.76), m(0), m(21.23))
    j024 = Point(m(2.77), m(0), m(21.23))
    j025 = Point(m(-6.92), m(0), m(21.06))
    j026 = Point(m(6.94), m(0), m(21.06))
    j027 = Point(m(-9.75), m(0), m(20.33))
    j028 = Point(m(9.75), m(0), m(20.33))
    j029 = Point(m(-9.75), m(0), m(20))
    j030 = Point(m(-6.92), m(0), m(20))
    j031 = Point(m(-4.11), m(0), m(20))
    j032 = Point(m(-1.49), m(0), m(20))
    j033 = Point(m(1.49), m(0), m(20))
    j034 = Point(m(4.11), m(0), m(20))
    j035 = Point(m(6.94), m(0), m(20))
    j036 = Point(m(9.75), m(0), m(20))
    j037 = Point(m(-1.55), m(0), m(18.21))
    j038 = Point(m(1.55), m(0), m(18.21))
    j039 = Point(m(-1.59), m(0), m(16.73))
    j040 = Point(m(1.59), m(0), m(16.73))
    j041 = Point(m(-1.66), m(0), m(14.5))
    j042 = Point(m(1.66), m(0), m(14.5))
    j043 = Point(m(-6.5), m(0), m(12.71))
    j044 = Point(m(6.5), m(0), m(12.71))
    j045 = Point(m(-1.73), m(0), m(12.37))
    j046 = Point(m(1.73), m(0), m(12.37))
    j047 = Point(m(-4.1), m(0), m(12.24))
    j048 = Point(m(4.1), m(0), m(12.24))
    j049 = Point(m(-9.42), m(0), m(11.62))
    j050 = Point(m(9.42), m(0), m(11.62))
    j051 = Point(m(-12.33), m(0), m(10.54))
    j052 = Point(m(12.33), m(0), m(10.54))
    j053 = Point(m(-12.33), m(0), m(10))
    j054 = Point(m(-9.42), m(0), m(10))
    j055 = Point(m(-6.5), m(0), m(10))
    j056 = Point(m(-1.8), m(0), m(10))
    j057 = Point(m(1.8), m(0), m(10))
    j058 = Point(m(6.5), m(0), m(10))
    j059 = Point(m(9.42), m(0), m(10))
    j060 = Point(m(12.33), m(0), m(10))
    j061 = Point(m(-1.86), m(0), m(8.07))
    j062 = Point(m(1.86), m(0), m(8.07))
    j063 = Point(m(-1.91), m(0), m(6.12))
    j064 = Point(m(1.91), m(0), m(6.12))
    j065 = Point(m(-1.98), m(0), m(4))
    j066 = Point(m(1.98), m(0), m(4))
    j067 = Point(m(-4.69), m(0), m(2.85))
    j068 = Point(m(4.68), m(0), m(2.85))
    j069 = Point(m(-2.04), m(0), m(2.14))
    j070 = Point(m(2.04), m(0), m(2.14))
    j071 = Point(m(-3.34), m(0), m(2))
    j072 = Point(m(3.34), m(0), m(2))
    j073 = Point(m(-7.44), m(0), m(1.69))
    j074 = Point(m(7.43), m(0), m(1.69))
    j075 = Point(m(-10.17), m(0), m(0.52))
    j076 = Point(m(10.15), m(0), m(0.52))
    j077 = Point(m(-10.17), m(0), m(0))
    j078 = Point(m(-7.44), m(0), m(0))
    j079 = Point(m(-4.69), m(0), m(0))
    j080 = Point(m(-2.1), m(0), m(0))
    j081 = Point(m(-0.28), m(0), m(0))
    j082 = Point(m(0.28), m(0), m(0))
    j083 = Point(m(2.1), m(0), m(0))
    j084 = Point(m(4.68), m(0), m(0))
    j085 = Point(m(7.43), m(0), m(0))
    j086 = Point(m(10.15), m(0), m(0))
    j087 = Point(m(-2.14), m(0), m(-1.87))
    j088 = Point(m(2.14), m(0), m(-1.87))
    j089 = Point(m(-2.19), m(0), m(-4.88))
    j090 = Point(m(2.19), m(0), m(-4.88))
    j091 = Point(m(-2.29), m(0), m(-9.71))
    j092 = Point(m(2.29), m(0), m(-9.71))
    j093 = Point(m(-2.39), m(0), m(-15.17))
    j094 = Point(m(2.39), m(0), m(-15.17))
    j095 = Point(m(-2.51), m(0), m(-21.26))
    j096 = Point(m(2.51), m(0), m(-21.26))
    j097 = Point(m(-2.66), m(0), m(-22.76))
    j098 = Point(m(-1.15), m(0), m(-22.76))
    j099 = Point(m(1.15), m(0), m(-22.76))
    j100 = Point(m(2.66), m(0), m(-22.76))
    j101 = Point(m(-2.79), m(0), m(-24.02))
    j102 = Point(m(2.79), m(0), m(-24.02))
    j103 = Point(m(-2.9), m(0), m(-25.21))
    j104 = Point(m(-1.09), m(0), m(-25.21))
    j105 = Point(m(1.09), m(0), m(-25.21))
    j106 = Point(m(2.9), m(0), m(-25.21))
    j107 = Point(m(-3.03), m(0), m(-26.47))
    j108 = Point(m(-2.24), m(0), m(-26.47))
    j109 = Point(m(2.24), m(0), m(-26.47))
    j110 = Point(m(3.03), m(0), m(-26.47))
    j111 = Point(m(-3.13), m(0), m(-27.45))
    j112 = Point(m(3.13), m(0), m(-27.45))
    j113 = Point(m(-3.36), m(0), m(-29.74))
    j114 = Point(m(-1.53), m(0), m(-29.74))
    j115 = Point(m(1.53), m(0), m(-29.74))
    j116 = Point(m(3.36), m(0), m(-29.74))
    j117 = Point(m(-3.58), m(0), m(-31.96))
    j118 = Point(m(3.58), m(0), m(-31.96))
    j119 = Point(m(-3.79), m(0), m(-34.07))
    j120 = Point(m(-1.46), m(0), m(-34.07))
    j121 = Point(m(1.46), m(0), m(-34.07))
    j122 = Point(m(3.79), m(0), m(-34.07))
    j123 = Point(m(-3.97), m(0), m(-35.85))
    j124 = Point(m(-2.7), m(0), m(-35.85))
    j125 = Point(m(2.7), m(0), m(-35.85))
    j126 = Point(m(3.97), m(0), m(-35.85))
    j127 = Point(m(-4.18), m(0), m(-38))
    j128 = Point(m(4.18), m(0), m(-38))
    return Tower(
        name="D-2-T-2019.1 T2",
        datum=LowestCrossarm((m(38),)),
        voltages=(kv(380),),
        line_angles=(),
        attachments=(
            Mount(Wire.SHIELD, Point(m(-4.5), m(0), m(26.5)), Hold.CLAMP),
            Mount(Wire.SHIELD, Point(m(4.5), m(0), m(26.5)), Hold.CLAMP),
            WirePosition(
                Wire.PHASE,
                Point(m(-7), m(0), m(16.35)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j029),
                    InsulatorString(mount=j031),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(7), m(0), m(16.35)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j036),
                    InsulatorString(mount=j034),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(-9.5), m(0), m(6.35)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j053),
                    InsulatorString(mount=j055),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(9.5), m(0), m(6.35)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j060),
                    InsulatorString(mount=j058),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(-7.5), m(0), m(-3.62)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j077),
                    InsulatorString(mount=j079),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(7.5), m(0), m(-3.62)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j086),
                    InsulatorString(mount=j084),
                ),
            ),
        ),
        bases=(),
        body=(
            Body(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j065, j066, role=Role.TRANSVERSE_BRACE),
                        Bar(j080, j069, role=Role.CHORD),
                        Bar(j069, j065, role=Role.CHORD),
                        Bar(j065, j063, role=Role.CHORD),
                        Bar(j063, j061, role=Role.CHORD),
                        Bar(j061, j056, role=Role.CHORD),
                        Bar(j056, j045, role=Role.CHORD),
                        Bar(j045, j041, role=Role.CHORD),
                        Bar(j041, j039, role=Role.CHORD),
                        Bar(j039, j037, role=Role.CHORD),
                        Bar(j037, j032, role=Role.CHORD),
                        Bar(j032, j021, role=Role.CHORD),
                        Bar(j021, j018, role=Role.CHORD),
                        Bar(j017, j022, role=Role.CHORD),
                        Bar(j022, j033, role=Role.CHORD),
                        Bar(j033, j038, role=Role.CHORD),
                        Bar(j038, j040, role=Role.CHORD),
                        Bar(j040, j042, role=Role.CHORD),
                        Bar(j042, j046, role=Role.CHORD),
                        Bar(j046, j057, role=Role.CHORD),
                        Bar(j057, j062, role=Role.CHORD),
                        Bar(j062, j064, role=Role.CHORD),
                        Bar(j064, j066, role=Role.CHORD),
                        Bar(j066, j070, role=Role.CHORD),
                        Bar(j070, j083, role=Role.CHORD),
                        Bar(j080, j087, role=Role.CHORD),
                        Bar(j087, j089, role=Role.CHORD),
                        Bar(j089, j091, role=Role.CHORD),
                        Bar(j091, j093, role=Role.CHORD),
                        Bar(j093, j095, role=Role.CHORD),
                        Bar(j083, j088, role=Role.CHORD),
                        Bar(j088, j090, role=Role.CHORD),
                        Bar(j090, j092, role=Role.CHORD),
                        Bar(j092, j094, role=Role.CHORD),
                        Bar(j094, j096, role=Role.CHORD),
                        Bar(j041, j042, role=Role.TRANSVERSE_BRACE),
                        Bar(j080, j070, role=Role.DIAGONAL_BRACE),
                        Bar(j070, j065, role=Role.DIAGONAL_BRACE),
                        Bar(j056, j046, role=Role.DIAGONAL_BRACE),
                        Bar(j046, j041, role=Role.DIAGONAL_BRACE),
                        Bar(j032, j022, role=Role.DIAGONAL_BRACE),
                        Bar(j022, j018, role=Role.DIAGONAL_BRACE),
                        Bar(j083, j069, role=Role.DIAGONAL_BRACE),
                        Bar(j069, j066, role=Role.DIAGONAL_BRACE),
                        Bar(j057, j045, role=Role.DIAGONAL_BRACE),
                        Bar(j045, j042, role=Role.DIAGONAL_BRACE),
                        Bar(j033, j021, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j017, role=Role.DIAGONAL_BRACE),
                        Bar(j065, j064, role=Role.DIAGONAL_BRACE),
                        Bar(j064, j061, role=Role.DIAGONAL_BRACE),
                        Bar(j061, j057, role=Role.DIAGONAL_BRACE),
                        Bar(j066, j063, role=Role.DIAGONAL_BRACE),
                        Bar(j063, j062, role=Role.DIAGONAL_BRACE),
                        Bar(j062, j056, role=Role.DIAGONAL_BRACE),
                        Bar(j041, j040, role=Role.DIAGONAL_BRACE),
                        Bar(j040, j037, role=Role.DIAGONAL_BRACE),
                        Bar(j037, j033, role=Role.DIAGONAL_BRACE),
                        Bar(j042, j039, role=Role.DIAGONAL_BRACE),
                        Bar(j039, j038, role=Role.DIAGONAL_BRACE),
                        Bar(j038, j032, role=Role.DIAGONAL_BRACE),
                        Bar(j120, j115, role=Role.DIAGONAL_BRACE),
                        Bar(j105, j098, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j114, role=Role.DIAGONAL_BRACE),
                        Bar(j104, j099, role=Role.DIAGONAL_BRACE),
                        Bar(j095, j094, role=Role.DIAGONAL_BRACE),
                        Bar(j094, j091, role=Role.DIAGONAL_BRACE),
                        Bar(j091, j090, role=Role.DIAGONAL_BRACE),
                        Bar(j090, j087, role=Role.DIAGONAL_BRACE),
                        Bar(j087, j083, role=Role.DIAGONAL_BRACE),
                        Bar(j096, j093, role=Role.DIAGONAL_BRACE),
                        Bar(j093, j092, role=Role.DIAGONAL_BRACE),
                        Bar(j092, j089, role=Role.DIAGONAL_BRACE),
                        Bar(j089, j088, role=Role.DIAGONAL_BRACE),
                        Bar(j088, j080, role=Role.DIAGONAL_BRACE),
                        Bar(j118, j117, role=Role.TRANSVERSE_BRACE),
                        Bar(j102, j101, role=Role.TRANSVERSE_BRACE),
                        Bar(j095, j096, role=Role.TRANSVERSE_BRACE),
                        Bar(j032, j033, role=Role.TRANSVERSE_BRACE),
                        Bar(j056, j057, role=Role.TRANSVERSE_BRACE),
                        Bar(j080, j081, role=Role.TRANSVERSE_BRACE),
                        Bar(j081, j082, role=Role.TRANSVERSE_BRACE),
                        Bar(j082, j083, role=Role.TRANSVERSE_BRACE),
                        Bar(j017, j016, role=Role.TRANSVERSE_BRACE),
                        Bar(j016, j018, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        legs=(
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j127, j123, role=Role.CHORD),
                        Bar(j123, j119, role=Role.CHORD),
                        Bar(j119, j117, role=Role.CHORD),
                        Bar(j117, j113, role=Role.CHORD),
                        Bar(j113, j111, role=Role.CHORD),
                        Bar(j111, j107, role=Role.CHORD),
                        Bar(j107, j103, role=Role.CHORD),
                        Bar(j103, j101, role=Role.CHORD),
                        Bar(j101, j097, role=Role.CHORD),
                        Bar(j097, j095, role=Role.CHORD),
                        Bar(j127, j124, role=Role.DIAGONAL_BRACE),
                        Bar(j124, j120, role=Role.DIAGONAL_BRACE),
                        Bar(j098, j095, role=Role.DIAGONAL_BRACE),
                        Bar(j114, j111, role=Role.DIAGONAL_BRACE),
                        Bar(j111, j108, role=Role.DIAGONAL_BRACE),
                        Bar(j108, j104, role=Role.DIAGONAL_BRACE),
                        Bar(j120, j119, role=Role.TRANSVERSE_BRACE),
                        Bar(j124, j123, role=Role.TRANSVERSE_BRACE),
                        Bar(j114, j113, role=Role.TRANSVERSE_BRACE),
                        Bar(j124, j119, role=Role.DIAGONAL_BRACE),
                        Bar(j120, j117, role=Role.DIAGONAL_BRACE),
                        Bar(j117, j114, role=Role.DIAGONAL_BRACE),
                        Bar(j098, j097, role=Role.TRANSVERSE_BRACE),
                        Bar(j104, j103, role=Role.TRANSVERSE_BRACE),
                        Bar(j103, j108, role=Role.DIAGONAL_BRACE),
                        Bar(j108, j107, role=Role.TRANSVERSE_BRACE),
                        Bar(j104, j101, role=Role.DIAGONAL_BRACE),
                        Bar(j101, j098, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j096, j100, role=Role.CHORD),
                        Bar(j100, j102, role=Role.CHORD),
                        Bar(j102, j106, role=Role.CHORD),
                        Bar(j106, j110, role=Role.CHORD),
                        Bar(j110, j112, role=Role.CHORD),
                        Bar(j112, j116, role=Role.CHORD),
                        Bar(j116, j118, role=Role.CHORD),
                        Bar(j118, j122, role=Role.CHORD),
                        Bar(j122, j126, role=Role.CHORD),
                        Bar(j126, j128, role=Role.CHORD),
                        Bar(j115, j112, role=Role.DIAGONAL_BRACE),
                        Bar(j112, j109, role=Role.DIAGONAL_BRACE),
                        Bar(j109, j105, role=Role.DIAGONAL_BRACE),
                        Bar(j128, j125, role=Role.DIAGONAL_BRACE),
                        Bar(j125, j121, role=Role.DIAGONAL_BRACE),
                        Bar(j099, j096, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j122, role=Role.TRANSVERSE_BRACE),
                        Bar(j125, j126, role=Role.TRANSVERSE_BRACE),
                        Bar(j115, j116, role=Role.TRANSVERSE_BRACE),
                        Bar(j125, j122, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j118, role=Role.DIAGONAL_BRACE),
                        Bar(j118, j115, role=Role.DIAGONAL_BRACE),
                        Bar(j099, j100, role=Role.TRANSVERSE_BRACE),
                        Bar(j105, j106, role=Role.TRANSVERSE_BRACE),
                        Bar(j106, j109, role=Role.DIAGONAL_BRACE),
                        Bar(j109, j110, role=Role.TRANSVERSE_BRACE),
                        Bar(j105, j102, role=Role.DIAGONAL_BRACE),
                        Bar(j102, j099, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        head=(
            Head(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j016, j013, role=Role.TRANSVERSE_BRACE),
                        Bar(j013, j018, role=Role.CHORD),
                        Bar(j013, j017, role=Role.CHORD),
                    ),
                )
            ),
        ),
        crossarms=(
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j029, j030, role=Role.CHORD),
                        Bar(j030, j031, role=Role.CHORD),
                        Bar(j031, j032, role=Role.CHORD),
                        Bar(j018, j019, role=Role.CHORD),
                        Bar(j019, j025, role=Role.CHORD),
                        Bar(j025, j027, role=Role.CHORD),
                        Bar(j019, j031, role=Role.TRANSVERSE_BRACE),
                        Bar(j031, j025, role=Role.DIAGONAL_BRACE),
                        Bar(j025, j030, role=Role.TRANSVERSE_BRACE),
                        Bar(j029, j027, role=Role.CHORD),
                        Bar(j018, j023, role=Role.DIAGONAL_BRACE),
                        Bar(j023, j031, role=Role.DIAGONAL_BRACE),
                        Bar(j023, j032, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j036, j035, role=Role.CHORD),
                        Bar(j035, j034, role=Role.CHORD),
                        Bar(j034, j033, role=Role.CHORD),
                        Bar(j017, j020, role=Role.CHORD),
                        Bar(j020, j026, role=Role.CHORD),
                        Bar(j026, j028, role=Role.CHORD),
                        Bar(j020, j034, role=Role.TRANSVERSE_BRACE),
                        Bar(j034, j026, role=Role.DIAGONAL_BRACE),
                        Bar(j026, j035, role=Role.TRANSVERSE_BRACE),
                        Bar(j036, j028, role=Role.CHORD),
                        Bar(j017, j024, role=Role.DIAGONAL_BRACE),
                        Bar(j024, j034, role=Role.DIAGONAL_BRACE),
                        Bar(j024, j033, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j053, j054, role=Role.CHORD),
                        Bar(j054, j055, role=Role.CHORD),
                        Bar(j055, j056, role=Role.CHORD),
                        Bar(j041, j043, role=Role.CHORD),
                        Bar(j043, j049, role=Role.CHORD),
                        Bar(j049, j051, role=Role.CHORD),
                        Bar(j043, j055, role=Role.TRANSVERSE_BRACE),
                        Bar(j055, j049, role=Role.DIAGONAL_BRACE),
                        Bar(j049, j054, role=Role.TRANSVERSE_BRACE),
                        Bar(j053, j051, role=Role.CHORD),
                        Bar(j041, j047, role=Role.DIAGONAL_BRACE),
                        Bar(j047, j055, role=Role.DIAGONAL_BRACE),
                        Bar(j047, j056, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j060, j059, role=Role.CHORD),
                        Bar(j059, j058, role=Role.CHORD),
                        Bar(j058, j057, role=Role.CHORD),
                        Bar(j042, j044, role=Role.CHORD),
                        Bar(j044, j050, role=Role.CHORD),
                        Bar(j050, j052, role=Role.CHORD),
                        Bar(j044, j058, role=Role.TRANSVERSE_BRACE),
                        Bar(j058, j050, role=Role.DIAGONAL_BRACE),
                        Bar(j050, j059, role=Role.TRANSVERSE_BRACE),
                        Bar(j060, j052, role=Role.CHORD),
                        Bar(j042, j048, role=Role.DIAGONAL_BRACE),
                        Bar(j048, j058, role=Role.DIAGONAL_BRACE),
                        Bar(j048, j057, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j077, j078, role=Role.CHORD),
                        Bar(j078, j079, role=Role.CHORD),
                        Bar(j079, j080, role=Role.CHORD),
                        Bar(j065, j067, role=Role.CHORD),
                        Bar(j067, j073, role=Role.CHORD),
                        Bar(j073, j075, role=Role.CHORD),
                        Bar(j067, j079, role=Role.TRANSVERSE_BRACE),
                        Bar(j079, j073, role=Role.DIAGONAL_BRACE),
                        Bar(j073, j078, role=Role.TRANSVERSE_BRACE),
                        Bar(j077, j075, role=Role.CHORD),
                        Bar(j065, j071, role=Role.DIAGONAL_BRACE),
                        Bar(j071, j079, role=Role.DIAGONAL_BRACE),
                        Bar(j071, j080, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j086, j085, role=Role.CHORD),
                        Bar(j085, j084, role=Role.CHORD),
                        Bar(j084, j083, role=Role.CHORD),
                        Bar(j066, j068, role=Role.CHORD),
                        Bar(j068, j074, role=Role.CHORD),
                        Bar(j074, j076, role=Role.CHORD),
                        Bar(j068, j084, role=Role.TRANSVERSE_BRACE),
                        Bar(j084, j074, role=Role.DIAGONAL_BRACE),
                        Bar(j074, j085, role=Role.TRANSVERSE_BRACE),
                        Bar(j086, j076, role=Role.CHORD),
                        Bar(j066, j072, role=Role.DIAGONAL_BRACE),
                        Bar(j072, j084, role=Role.DIAGONAL_BRACE),
                        Bar(j072, j083, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        peaks=(
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j002, j005, role=Role.DIAGONAL_BRACE),
                        Bar(j005, j006, role=Role.TRANSVERSE_BRACE),
                        Bar(j006, j011, role=Role.TRANSVERSE_BRACE),
                        Bar(j011, j009, role=Role.DIAGONAL_BRACE),
                        Bar(j009, j014, role=Role.DIAGONAL_BRACE),
                        Bar(j014, j013, role=Role.DIAGONAL_BRACE),
                        Bar(j013, j009, role=Role.CHORD),
                        Bar(j009, j006, role=Role.CHORD),
                        Bar(j006, j002, role=Role.CHORD),
                        Bar(j002, j001, role=Role.CHORD),
                        Bar(j001, j005, role=Role.CHORD),
                        Bar(j005, j011, role=Role.CHORD),
                        Bar(j011, j014, role=Role.CHORD),
                        Bar(j014, j018, role=Role.CHORD),
                    ),
                )
            ),
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j003, j008, role=Role.DIAGONAL_BRACE),
                        Bar(j008, j007, role=Role.TRANSVERSE_BRACE),
                        Bar(j007, j012, role=Role.TRANSVERSE_BRACE),
                        Bar(j012, j010, role=Role.DIAGONAL_BRACE),
                        Bar(j010, j015, role=Role.DIAGONAL_BRACE),
                        Bar(j015, j013, role=Role.DIAGONAL_BRACE),
                        Bar(j017, j015, role=Role.CHORD),
                        Bar(j015, j012, role=Role.CHORD),
                        Bar(j012, j008, role=Role.CHORD),
                        Bar(j008, j004, role=Role.CHORD),
                        Bar(j004, j003, role=Role.CHORD),
                        Bar(j003, j007, role=Role.CHORD),
                        Bar(j007, j010, role=Role.CHORD),
                        Bar(j010, j013, role=Role.CHORD),
                    ),
                )
            ),
        ),
    )


D_2_T_2019_1_T2 = _d_2_t_2019_1_t2()


def _d_2_t_2019_1_wa120() -> Tower[LowestCrossarm]:
    """D-2-T-2019.1 WA120: each joint written once, by its key."""
    j001 = Point(m(-6), m(0), m(26.5))
    j002 = Point(m(-5.72), m(0), m(26.5))
    j003 = Point(m(5.72), m(0), m(26.5))
    j004 = Point(m(6), m(0), m(26.5))
    j005 = Point(m(-5.1), m(0), m(26.26))
    j006 = Point(m(5.11), m(0), m(26.26))
    j007 = Point(m(-5.63), m(0), m(26.18))
    j008 = Point(m(5.64), m(0), m(26.18))
    j009 = Point(m(-4.13), m(0), m(25.87))
    j010 = Point(m(4.14), m(0), m(25.87))
    j011 = Point(m(-5.08), m(0), m(25.67))
    j012 = Point(m(5.07), m(0), m(25.67))
    j013 = Point(m(-2.88), m(0), m(25.39))
    j014 = Point(m(2.89), m(0), m(25.39))
    j015 = Point(m(-4.18), m(0), m(24.9))
    j016 = Point(m(4.19), m(0), m(24.9))
    j017 = Point(m(-1.46), m(0), m(24.84))
    j018 = Point(m(1.48), m(0), m(24.84))
    j019 = Point(m(0), m(0), m(24.31))
    j020 = Point(m(-3.17), m(0), m(24.04))
    j021 = Point(m(3.18), m(0), m(24.04))
    j022 = Point(m(-2.3), m(0), m(23.34))
    j023 = Point(m(2.31), m(0), m(23.34))
    j024 = Point(m(0), m(0), m(22.68))
    j025 = Point(m(1.48), m(0), m(22.68))
    j026 = Point(m(-1.48), m(0), m(22.66))
    j027 = Point(m(-4.17), m(0), m(21.93))
    j028 = Point(m(4.17), m(0), m(21.93))
    j029 = Point(m(-1.52), m(0), m(21.44))
    j030 = Point(m(1.52), m(0), m(21.44))
    j031 = Point(m(-2.82), m(0), m(21.33))
    j032 = Point(m(2.83), m(0), m(21.33))
    j033 = Point(m(-7.01), m(0), m(21.15))
    j034 = Point(m(7.02), m(0), m(21.15))
    j035 = Point(m(-9.86), m(0), m(20.36))
    j036 = Point(m(9.85), m(0), m(20.36))
    j037 = Point(m(-9.86), m(0), m(20))
    j038 = Point(m(-7.01), m(0), m(20))
    j039 = Point(m(-4.17), m(0), m(20))
    j040 = Point(m(-1.56), m(0), m(20))
    j041 = Point(m(1.57), m(0), m(20))
    j042 = Point(m(4.18), m(0), m(20))
    j043 = Point(m(7.02), m(0), m(20))
    j044 = Point(m(9.85), m(0), m(20))
    j045 = Point(m(-9.5), m(0), m(20))
    j046 = Point(m(9.5), m(0), m(20))
    j047 = Point(m(-1.62), m(0), m(18.21))
    j048 = Point(m(1.62), m(0), m(18.21))
    j049 = Point(m(-1.66), m(0), m(16.73))
    j050 = Point(m(1.67), m(0), m(16.73))
    j051 = Point(m(-1.73), m(0), m(14.5))
    j052 = Point(m(1.74), m(0), m(14.5))
    j053 = Point(m(-6.63), m(0), m(12.71))
    j054 = Point(m(6.65), m(0), m(12.71))
    j055 = Point(m(-1.8), m(0), m(12.37))
    j056 = Point(m(1.81), m(0), m(12.37))
    j057 = Point(m(-4.2), m(0), m(12.24))
    j058 = Point(m(4.2), m(0), m(12.24))
    j059 = Point(m(-9.6), m(0), m(11.62))
    j060 = Point(m(9.61), m(0), m(11.62))
    j061 = Point(m(-12.56), m(0), m(10.54))
    j062 = Point(m(12.58), m(0), m(10.54))
    j063 = Point(m(-12.56), m(0), m(10))
    j064 = Point(m(-9.6), m(0), m(10))
    j065 = Point(m(-6.64), m(0), m(10))
    j066 = Point(m(-1.87), m(0), m(10))
    j067 = Point(m(1.88), m(0), m(10))
    j068 = Point(m(6.65), m(0), m(10))
    j069 = Point(m(9.61), m(0), m(10))
    j070 = Point(m(12.58), m(0), m(10))
    j071 = Point(m(-12.2), m(0), m(10))
    j072 = Point(m(12.2), m(0), m(10))
    j073 = Point(m(-1.93), m(0), m(8.07))
    j074 = Point(m(1.94), m(0), m(8.07))
    j075 = Point(m(-1.99), m(0), m(6.12))
    j076 = Point(m(2.01), m(0), m(6.12))
    j077 = Point(m(-2.06), m(0), m(4))
    j078 = Point(m(2.07), m(0), m(4))
    j079 = Point(m(-4.87), m(0), m(2.85))
    j080 = Point(m(4.86), m(0), m(2.85))
    j081 = Point(m(-2.11), m(0), m(2.14))
    j082 = Point(m(2.13), m(0), m(2.14))
    j083 = Point(m(-3.47), m(0), m(2))
    j084 = Point(m(3.46), m(0), m(2))
    j085 = Point(m(-7.7), m(0), m(1.69))
    j086 = Point(m(7.71), m(0), m(1.69))
    j087 = Point(m(-10.55), m(0), m(0.52))
    j088 = Point(m(10.55), m(0), m(0.52))
    j089 = Point(m(-10.2), m(0), m(0))
    j090 = Point(m(10.2), m(0), m(0))
    j091 = Point(m(-10.55), m(0), m(0))
    j092 = Point(m(-7.7), m(0), m(0))
    j093 = Point(m(-4.87), m(0), m(0))
    j094 = Point(m(-2.18), m(0), m(0))
    j095 = Point(m(-0.3), m(0), m(0))
    j096 = Point(m(0.31), m(0), m(0))
    j097 = Point(m(2.2), m(0), m(0))
    j098 = Point(m(4.86), m(0), m(0))
    j099 = Point(m(7.71), m(0), m(0))
    j100 = Point(m(10.55), m(0), m(0))
    j101 = Point(m(-2.22), m(0), m(-1.58))
    j102 = Point(m(2.24), m(0), m(-1.58))
    j103 = Point(m(-2.28), m(0), m(-4.1))
    j104 = Point(m(2.3), m(0), m(-4.1))
    j105 = Point(m(-2.37), m(0), m(-7.88))
    j106 = Point(m(2.39), m(0), m(-7.88))
    j107 = Point(m(-2.47), m(0), m(-12.15))
    j108 = Point(m(2.49), m(0), m(-12.15))
    j109 = Point(m(-2.59), m(0), m(-16.91))
    j110 = Point(m(2.61), m(0), m(-16.91))
    j111 = Point(m(-2.75), m(0), m(-18.08))
    j112 = Point(m(-1.19), m(0), m(-18.08))
    j113 = Point(m(1.21), m(0), m(-18.08))
    j114 = Point(m(2.77), m(0), m(-18.08))
    j115 = Point(m(-2.88), m(0), m(-19.07))
    j116 = Point(m(2.9), m(0), m(-19.07))
    j117 = Point(m(-3), m(0), m(-20))
    j118 = Point(m(-1.13), m(0), m(-20))
    j119 = Point(m(1.13), m(0), m(-20))
    j120 = Point(m(3.02), m(0), m(-20))
    j121 = Point(m(-3.13), m(0), m(-20.98))
    j122 = Point(m(-2.31), m(0), m(-20.98))
    j123 = Point(m(2.32), m(0), m(-20.98))
    j124 = Point(m(3.15), m(0), m(-20.98))
    j125 = Point(m(-3.24), m(0), m(-21.75))
    j126 = Point(m(3.25), m(0), m(-21.75))
    j127 = Point(m(-3.48), m(0), m(-23.54))
    j128 = Point(m(-1.59), m(0), m(-23.54))
    j129 = Point(m(1.59), m(0), m(-23.54))
    j130 = Point(m(3.49), m(0), m(-23.54))
    j131 = Point(m(-3.71), m(0), m(-25.28))
    j132 = Point(m(3.72), m(0), m(-25.28))
    j133 = Point(m(-3.93), m(0), m(-26.93))
    j134 = Point(m(-1.51), m(0), m(-26.93))
    j135 = Point(m(1.53), m(0), m(-26.93))
    j136 = Point(m(3.94), m(0), m(-26.93))
    j137 = Point(m(-4.12), m(0), m(-28.32))
    j138 = Point(m(-2.79), m(0), m(-28.32))
    j139 = Point(m(2.8), m(0), m(-28.32))
    j140 = Point(m(4.13), m(0), m(-28.32))
    j141 = Point(m(-4.34), m(0), m(-30))
    j142 = Point(m(4.35), m(0), m(-30))
    return Tower(
        name="D-2-T-2019.1 WA120",
        datum=LowestCrossarm((m(30),)),
        voltages=(kv(380),),
        line_angles=(),
        attachments=(
            Mount(Wire.SHIELD, Point(m(-6), m(0), m(26.5)), Hold.CLAMP),
            Mount(Wire.SHIELD, Point(m(6), m(0), m(26.5)), Hold.CLAMP),
            Mount(Wire.PHASE, Point(m(-9.5), m(0), m(20)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(9.5), m(0), m(20)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-12.2), m(0), m(10)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(12.2), m(0), m(10)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-10.2), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(10.2), m(0), m(0)), Hold.STRAIN),
        ),
        bases=(),
        body=(
            Body(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j077, j078, role=Role.TRANSVERSE_BRACE),
                        Bar(j094, j081, role=Role.CHORD),
                        Bar(j081, j077, role=Role.CHORD),
                        Bar(j077, j075, role=Role.CHORD),
                        Bar(j075, j073, role=Role.CHORD),
                        Bar(j073, j066, role=Role.CHORD),
                        Bar(j066, j055, role=Role.CHORD),
                        Bar(j055, j051, role=Role.CHORD),
                        Bar(j051, j049, role=Role.CHORD),
                        Bar(j049, j047, role=Role.CHORD),
                        Bar(j047, j040, role=Role.CHORD),
                        Bar(j040, j029, role=Role.CHORD),
                        Bar(j029, j026, role=Role.CHORD),
                        Bar(j025, j030, role=Role.CHORD),
                        Bar(j030, j041, role=Role.CHORD),
                        Bar(j041, j048, role=Role.CHORD),
                        Bar(j048, j050, role=Role.CHORD),
                        Bar(j050, j052, role=Role.CHORD),
                        Bar(j052, j056, role=Role.CHORD),
                        Bar(j056, j067, role=Role.CHORD),
                        Bar(j067, j074, role=Role.CHORD),
                        Bar(j074, j076, role=Role.CHORD),
                        Bar(j076, j078, role=Role.CHORD),
                        Bar(j078, j082, role=Role.CHORD),
                        Bar(j082, j097, role=Role.CHORD),
                        Bar(j094, j101, role=Role.CHORD),
                        Bar(j101, j103, role=Role.CHORD),
                        Bar(j103, j105, role=Role.CHORD),
                        Bar(j105, j107, role=Role.CHORD),
                        Bar(j107, j109, role=Role.CHORD),
                        Bar(j097, j102, role=Role.CHORD),
                        Bar(j102, j104, role=Role.CHORD),
                        Bar(j104, j106, role=Role.CHORD),
                        Bar(j106, j108, role=Role.CHORD),
                        Bar(j108, j110, role=Role.CHORD),
                        Bar(j026, j024, role=Role.TRANSVERSE_BRACE),
                        Bar(j024, j025, role=Role.TRANSVERSE_BRACE),
                        Bar(j051, j052, role=Role.TRANSVERSE_BRACE),
                        Bar(j094, j082, role=Role.DIAGONAL_BRACE),
                        Bar(j082, j077, role=Role.DIAGONAL_BRACE),
                        Bar(j066, j056, role=Role.DIAGONAL_BRACE),
                        Bar(j056, j051, role=Role.DIAGONAL_BRACE),
                        Bar(j040, j030, role=Role.DIAGONAL_BRACE),
                        Bar(j030, j026, role=Role.DIAGONAL_BRACE),
                        Bar(j097, j081, role=Role.DIAGONAL_BRACE),
                        Bar(j081, j078, role=Role.DIAGONAL_BRACE),
                        Bar(j067, j055, role=Role.DIAGONAL_BRACE),
                        Bar(j055, j052, role=Role.DIAGONAL_BRACE),
                        Bar(j041, j029, role=Role.DIAGONAL_BRACE),
                        Bar(j029, j025, role=Role.DIAGONAL_BRACE),
                        Bar(j077, j076, role=Role.DIAGONAL_BRACE),
                        Bar(j076, j073, role=Role.DIAGONAL_BRACE),
                        Bar(j073, j067, role=Role.DIAGONAL_BRACE),
                        Bar(j078, j075, role=Role.DIAGONAL_BRACE),
                        Bar(j075, j074, role=Role.DIAGONAL_BRACE),
                        Bar(j074, j066, role=Role.DIAGONAL_BRACE),
                        Bar(j051, j050, role=Role.DIAGONAL_BRACE),
                        Bar(j050, j047, role=Role.DIAGONAL_BRACE),
                        Bar(j047, j041, role=Role.DIAGONAL_BRACE),
                        Bar(j052, j049, role=Role.DIAGONAL_BRACE),
                        Bar(j049, j048, role=Role.DIAGONAL_BRACE),
                        Bar(j048, j040, role=Role.DIAGONAL_BRACE),
                        Bar(j134, j129, role=Role.DIAGONAL_BRACE),
                        Bar(j119, j112, role=Role.DIAGONAL_BRACE),
                        Bar(j135, j128, role=Role.DIAGONAL_BRACE),
                        Bar(j118, j113, role=Role.DIAGONAL_BRACE),
                        Bar(j109, j108, role=Role.DIAGONAL_BRACE),
                        Bar(j108, j105, role=Role.DIAGONAL_BRACE),
                        Bar(j105, j104, role=Role.DIAGONAL_BRACE),
                        Bar(j104, j101, role=Role.DIAGONAL_BRACE),
                        Bar(j101, j097, role=Role.DIAGONAL_BRACE),
                        Bar(j110, j107, role=Role.DIAGONAL_BRACE),
                        Bar(j107, j106, role=Role.DIAGONAL_BRACE),
                        Bar(j106, j103, role=Role.DIAGONAL_BRACE),
                        Bar(j103, j102, role=Role.DIAGONAL_BRACE),
                        Bar(j102, j094, role=Role.DIAGONAL_BRACE),
                        Bar(j132, j131, role=Role.TRANSVERSE_BRACE),
                        Bar(j116, j115, role=Role.TRANSVERSE_BRACE),
                        Bar(j109, j110, role=Role.TRANSVERSE_BRACE),
                        Bar(j040, j041, role=Role.TRANSVERSE_BRACE),
                        Bar(j066, j067, role=Role.TRANSVERSE_BRACE),
                        Bar(j094, j095, role=Role.TRANSVERSE_BRACE),
                        Bar(j095, j096, role=Role.TRANSVERSE_BRACE),
                        Bar(j096, j097, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        legs=(
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j141, j137, role=Role.CHORD),
                        Bar(j137, j133, role=Role.CHORD),
                        Bar(j133, j131, role=Role.CHORD),
                        Bar(j131, j127, role=Role.CHORD),
                        Bar(j127, j125, role=Role.CHORD),
                        Bar(j125, j121, role=Role.CHORD),
                        Bar(j121, j117, role=Role.CHORD),
                        Bar(j117, j115, role=Role.CHORD),
                        Bar(j115, j111, role=Role.CHORD),
                        Bar(j111, j109, role=Role.CHORD),
                        Bar(j141, j138, role=Role.DIAGONAL_BRACE),
                        Bar(j138, j134, role=Role.DIAGONAL_BRACE),
                        Bar(j112, j109, role=Role.DIAGONAL_BRACE),
                        Bar(j128, j125, role=Role.DIAGONAL_BRACE),
                        Bar(j125, j122, role=Role.DIAGONAL_BRACE),
                        Bar(j122, j118, role=Role.DIAGONAL_BRACE),
                        Bar(j134, j133, role=Role.TRANSVERSE_BRACE),
                        Bar(j138, j137, role=Role.TRANSVERSE_BRACE),
                        Bar(j128, j127, role=Role.TRANSVERSE_BRACE),
                        Bar(j138, j133, role=Role.DIAGONAL_BRACE),
                        Bar(j134, j131, role=Role.DIAGONAL_BRACE),
                        Bar(j131, j128, role=Role.DIAGONAL_BRACE),
                        Bar(j112, j111, role=Role.TRANSVERSE_BRACE),
                        Bar(j118, j117, role=Role.TRANSVERSE_BRACE),
                        Bar(j117, j122, role=Role.DIAGONAL_BRACE),
                        Bar(j122, j121, role=Role.TRANSVERSE_BRACE),
                        Bar(j118, j115, role=Role.DIAGONAL_BRACE),
                        Bar(j115, j112, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j110, j114, role=Role.CHORD),
                        Bar(j114, j116, role=Role.CHORD),
                        Bar(j116, j120, role=Role.CHORD),
                        Bar(j120, j124, role=Role.CHORD),
                        Bar(j124, j126, role=Role.CHORD),
                        Bar(j126, j130, role=Role.CHORD),
                        Bar(j130, j132, role=Role.CHORD),
                        Bar(j132, j136, role=Role.CHORD),
                        Bar(j136, j140, role=Role.CHORD),
                        Bar(j140, j142, role=Role.CHORD),
                        Bar(j129, j126, role=Role.DIAGONAL_BRACE),
                        Bar(j126, j123, role=Role.DIAGONAL_BRACE),
                        Bar(j123, j119, role=Role.DIAGONAL_BRACE),
                        Bar(j142, j139, role=Role.DIAGONAL_BRACE),
                        Bar(j139, j135, role=Role.DIAGONAL_BRACE),
                        Bar(j113, j110, role=Role.DIAGONAL_BRACE),
                        Bar(j135, j136, role=Role.TRANSVERSE_BRACE),
                        Bar(j139, j140, role=Role.TRANSVERSE_BRACE),
                        Bar(j129, j130, role=Role.TRANSVERSE_BRACE),
                        Bar(j139, j136, role=Role.DIAGONAL_BRACE),
                        Bar(j135, j132, role=Role.DIAGONAL_BRACE),
                        Bar(j132, j129, role=Role.DIAGONAL_BRACE),
                        Bar(j113, j114, role=Role.TRANSVERSE_BRACE),
                        Bar(j119, j120, role=Role.TRANSVERSE_BRACE),
                        Bar(j120, j123, role=Role.DIAGONAL_BRACE),
                        Bar(j123, j124, role=Role.TRANSVERSE_BRACE),
                        Bar(j119, j116, role=Role.DIAGONAL_BRACE),
                        Bar(j116, j113, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        head=(
            Head(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j024, j019, role=Role.TRANSVERSE_BRACE),
                        Bar(j019, j026, role=Role.DIAGONAL_BRACE),
                        Bar(j019, j025, role=Role.DIAGONAL_BRACE),
                        Bar(j018, j019, role=Role.DIAGONAL_BRACE),
                        Bar(j019, j017, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        crossarms=(
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j037, j045, role=Role.CHORD),
                        Bar(j045, j038, role=Role.CHORD),
                        Bar(j038, j039, role=Role.CHORD),
                        Bar(j039, j040, role=Role.CHORD),
                        Bar(j026, j027, role=Role.CHORD),
                        Bar(j027, j033, role=Role.CHORD),
                        Bar(j033, j035, role=Role.CHORD),
                        Bar(j027, j039, role=Role.TRANSVERSE_BRACE),
                        Bar(j039, j033, role=Role.DIAGONAL_BRACE),
                        Bar(j033, j038, role=Role.TRANSVERSE_BRACE),
                        Bar(j037, j035, role=Role.CHORD),
                        Bar(j026, j031, role=Role.DIAGONAL_BRACE),
                        Bar(j031, j039, role=Role.DIAGONAL_BRACE),
                        Bar(j031, j040, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j044, j046, role=Role.CHORD),
                        Bar(j046, j043, role=Role.CHORD),
                        Bar(j043, j042, role=Role.CHORD),
                        Bar(j042, j041, role=Role.CHORD),
                        Bar(j025, j028, role=Role.CHORD),
                        Bar(j028, j034, role=Role.CHORD),
                        Bar(j034, j036, role=Role.CHORD),
                        Bar(j028, j042, role=Role.TRANSVERSE_BRACE),
                        Bar(j042, j034, role=Role.DIAGONAL_BRACE),
                        Bar(j034, j043, role=Role.TRANSVERSE_BRACE),
                        Bar(j044, j036, role=Role.CHORD),
                        Bar(j025, j032, role=Role.DIAGONAL_BRACE),
                        Bar(j032, j042, role=Role.DIAGONAL_BRACE),
                        Bar(j032, j041, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j063, j071, role=Role.CHORD),
                        Bar(j071, j064, role=Role.CHORD),
                        Bar(j064, j065, role=Role.CHORD),
                        Bar(j065, j066, role=Role.CHORD),
                        Bar(j051, j053, role=Role.CHORD),
                        Bar(j053, j059, role=Role.CHORD),
                        Bar(j059, j061, role=Role.CHORD),
                        Bar(j053, j065, role=Role.TRANSVERSE_BRACE),
                        Bar(j065, j059, role=Role.DIAGONAL_BRACE),
                        Bar(j059, j064, role=Role.TRANSVERSE_BRACE),
                        Bar(j063, j061, role=Role.CHORD),
                        Bar(j051, j057, role=Role.DIAGONAL_BRACE),
                        Bar(j057, j065, role=Role.DIAGONAL_BRACE),
                        Bar(j057, j066, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j070, j072, role=Role.CHORD),
                        Bar(j072, j069, role=Role.CHORD),
                        Bar(j069, j068, role=Role.CHORD),
                        Bar(j068, j067, role=Role.CHORD),
                        Bar(j052, j054, role=Role.CHORD),
                        Bar(j054, j060, role=Role.CHORD),
                        Bar(j060, j062, role=Role.CHORD),
                        Bar(j054, j068, role=Role.TRANSVERSE_BRACE),
                        Bar(j068, j060, role=Role.DIAGONAL_BRACE),
                        Bar(j060, j069, role=Role.TRANSVERSE_BRACE),
                        Bar(j070, j062, role=Role.CHORD),
                        Bar(j052, j058, role=Role.DIAGONAL_BRACE),
                        Bar(j058, j068, role=Role.DIAGONAL_BRACE),
                        Bar(j058, j067, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j091, j089, role=Role.CHORD),
                        Bar(j089, j092, role=Role.CHORD),
                        Bar(j092, j093, role=Role.CHORD),
                        Bar(j093, j094, role=Role.CHORD),
                        Bar(j077, j079, role=Role.CHORD),
                        Bar(j079, j085, role=Role.CHORD),
                        Bar(j085, j087, role=Role.CHORD),
                        Bar(j079, j093, role=Role.TRANSVERSE_BRACE),
                        Bar(j093, j085, role=Role.DIAGONAL_BRACE),
                        Bar(j085, j092, role=Role.TRANSVERSE_BRACE),
                        Bar(j091, j087, role=Role.CHORD),
                        Bar(j077, j083, role=Role.DIAGONAL_BRACE),
                        Bar(j083, j093, role=Role.DIAGONAL_BRACE),
                        Bar(j083, j094, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j100, j090, role=Role.CHORD),
                        Bar(j090, j099, role=Role.CHORD),
                        Bar(j099, j098, role=Role.CHORD),
                        Bar(j098, j097, role=Role.CHORD),
                        Bar(j078, j080, role=Role.CHORD),
                        Bar(j080, j086, role=Role.CHORD),
                        Bar(j086, j088, role=Role.CHORD),
                        Bar(j080, j098, role=Role.TRANSVERSE_BRACE),
                        Bar(j098, j086, role=Role.DIAGONAL_BRACE),
                        Bar(j086, j099, role=Role.TRANSVERSE_BRACE),
                        Bar(j100, j088, role=Role.CHORD),
                        Bar(j078, j084, role=Role.DIAGONAL_BRACE),
                        Bar(j084, j098, role=Role.DIAGONAL_BRACE),
                        Bar(j084, j097, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        peaks=(
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j002, j007, role=Role.DIAGONAL_BRACE),
                        Bar(j007, j005, role=Role.DIAGONAL_BRACE),
                        Bar(j005, j011, role=Role.DIAGONAL_BRACE),
                        Bar(j011, j009, role=Role.DIAGONAL_BRACE),
                        Bar(j009, j015, role=Role.TRANSVERSE_BRACE),
                        Bar(j015, j013, role=Role.DIAGONAL_BRACE),
                        Bar(j013, j020, role=Role.DIAGONAL_BRACE),
                        Bar(j020, j017, role=Role.DIAGONAL_BRACE),
                        Bar(j017, j022, role=Role.DIAGONAL_BRACE),
                        Bar(j022, j019, role=Role.DIAGONAL_BRACE),
                        Bar(j017, j013, role=Role.CHORD),
                        Bar(j013, j009, role=Role.CHORD),
                        Bar(j009, j005, role=Role.CHORD),
                        Bar(j005, j002, role=Role.CHORD),
                        Bar(j002, j001, role=Role.CHORD),
                        Bar(j001, j007, role=Role.CHORD),
                        Bar(j007, j011, role=Role.CHORD),
                        Bar(j011, j015, role=Role.CHORD),
                        Bar(j015, j020, role=Role.CHORD),
                        Bar(j020, j022, role=Role.CHORD),
                        Bar(j022, j026, role=Role.CHORD),
                    ),
                )
            ),
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j003, j008, role=Role.DIAGONAL_BRACE),
                        Bar(j008, j006, role=Role.DIAGONAL_BRACE),
                        Bar(j006, j012, role=Role.DIAGONAL_BRACE),
                        Bar(j012, j010, role=Role.DIAGONAL_BRACE),
                        Bar(j010, j016, role=Role.TRANSVERSE_BRACE),
                        Bar(j016, j014, role=Role.DIAGONAL_BRACE),
                        Bar(j014, j021, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j018, role=Role.DIAGONAL_BRACE),
                        Bar(j018, j023, role=Role.DIAGONAL_BRACE),
                        Bar(j023, j019, role=Role.DIAGONAL_BRACE),
                        Bar(j025, j023, role=Role.CHORD),
                        Bar(j023, j021, role=Role.CHORD),
                        Bar(j021, j016, role=Role.CHORD),
                        Bar(j016, j012, role=Role.CHORD),
                        Bar(j012, j008, role=Role.CHORD),
                        Bar(j008, j004, role=Role.CHORD),
                        Bar(j004, j003, role=Role.CHORD),
                        Bar(j003, j006, role=Role.CHORD),
                        Bar(j006, j010, role=Role.CHORD),
                        Bar(j010, j014, role=Role.CHORD),
                        Bar(j014, j018, role=Role.CHORD),
                    ),
                )
            ),
        ),
    )


D_2_T_2019_1_WA120 = _d_2_t_2019_1_wa120()


def _d_2_t_2019_1_wa140() -> Tower[LowestCrossarm]:
    """D-2-T-2019.1 WA140: each joint written once, by its key."""
    j001 = Point(m(-5), m(0), m(26.5))
    j002 = Point(m(-4.76), m(0), m(26.5))
    j003 = Point(m(4.75), m(0), m(26.5))
    j004 = Point(m(5), m(0), m(26.5))
    j005 = Point(m(-4.61), m(0), m(26.06))
    j006 = Point(m(4.59), m(0), m(26.06))
    j007 = Point(m(-3.7), m(0), m(25.93))
    j008 = Point(m(3.69), m(0), m(25.93))
    j009 = Point(m(-3.56), m(0), m(24.92))
    j010 = Point(m(-1.8), m(0), m(24.92))
    j011 = Point(m(1.81), m(0), m(24.92))
    j012 = Point(m(3.55), m(0), m(24.92))
    j013 = Point(m(0), m(0), m(23.98))
    j014 = Point(m(-1.96), m(0), m(23.2))
    j015 = Point(m(1.97), m(0), m(23.2))
    j016 = Point(m(1.26), m(0), m(22.47))
    j017 = Point(m(-1.26), m(0), m(22.46))
    j018 = Point(m(-3.52), m(0), m(21.79))
    j019 = Point(m(3.52), m(0), m(21.79))
    j020 = Point(m(-1.29), m(0), m(21.33))
    j021 = Point(m(1.29), m(0), m(21.33))
    j022 = Point(m(-2.39), m(0), m(21.23))
    j023 = Point(m(2.4), m(0), m(21.23))
    j024 = Point(m(-5.91), m(0), m(21.06))
    j025 = Point(m(5.92), m(0), m(21.06))
    j026 = Point(m(-8.3), m(0), m(20.33))
    j027 = Point(m(8.3), m(0), m(20.33))
    j028 = Point(m(-8.3), m(0), m(20))
    j029 = Point(m(-5.91), m(0), m(20))
    j030 = Point(m(-3.53), m(0), m(20))
    j031 = Point(m(-1.33), m(0), m(20))
    j032 = Point(m(1.33), m(0), m(20))
    j033 = Point(m(3.53), m(0), m(20))
    j034 = Point(m(5.92), m(0), m(20))
    j035 = Point(m(8.3), m(0), m(20))
    j036 = Point(m(-8), m(0), m(20))
    j037 = Point(m(8), m(0), m(20))
    j038 = Point(m(-1.37), m(0), m(18.21))
    j039 = Point(m(1.38), m(0), m(18.21))
    j040 = Point(m(-1.41), m(0), m(16.73))
    j041 = Point(m(1.42), m(0), m(16.73))
    j042 = Point(m(-1.47), m(0), m(14.5))
    j043 = Point(m(1.48), m(0), m(14.5))
    j044 = Point(m(-5.8), m(0), m(12.71))
    j045 = Point(m(5.81), m(0), m(12.71))
    j046 = Point(m(-1.53), m(0), m(12.37))
    j047 = Point(m(1.53), m(0), m(12.37))
    j048 = Point(m(-3.65), m(0), m(12.24))
    j049 = Point(m(3.65), m(0), m(12.24))
    j050 = Point(m(-8.4), m(0), m(11.62))
    j051 = Point(m(8.42), m(0), m(11.62))
    j052 = Point(m(-11.02), m(0), m(10.54))
    j053 = Point(m(11.04), m(0), m(10.54))
    j054 = Point(m(-11.02), m(0), m(10))
    j055 = Point(m(-8.4), m(0), m(10))
    j056 = Point(m(-5.8), m(0), m(10))
    j057 = Point(m(-1.59), m(0), m(10))
    j058 = Point(m(1.6), m(0), m(10))
    j059 = Point(m(5.8), m(0), m(10))
    j060 = Point(m(8.42), m(0), m(10))
    j061 = Point(m(11.04), m(0), m(10))
    j062 = Point(m(-10.7), m(0), m(10))
    j063 = Point(m(10.7), m(0), m(10))
    j064 = Point(m(-1.64), m(0), m(8.07))
    j065 = Point(m(1.65), m(0), m(8.07))
    j066 = Point(m(-1.7), m(0), m(6.12))
    j067 = Point(m(1.7), m(0), m(6.12))
    j068 = Point(m(-1.75), m(0), m(4))
    j069 = Point(m(1.76), m(0), m(4))
    j070 = Point(m(-4.15), m(0), m(2.85))
    j071 = Point(m(4.15), m(0), m(2.85))
    j072 = Point(m(-1.8), m(0), m(2.14))
    j073 = Point(m(1.81), m(0), m(2.14))
    j074 = Point(m(-2.96), m(0), m(2))
    j075 = Point(m(2.95), m(0), m(2))
    j076 = Point(m(-6.57), m(0), m(1.69))
    j077 = Point(m(6.57), m(0), m(1.69))
    j078 = Point(m(-9), m(0), m(0.52))
    j079 = Point(m(9), m(0), m(0.52))
    j080 = Point(m(-8.7), m(0), m(0))
    j081 = Point(m(8.7), m(0), m(0))
    j082 = Point(m(-9), m(0), m(0))
    j083 = Point(m(-6.57), m(0), m(0))
    j084 = Point(m(-4.15), m(0), m(0))
    j085 = Point(m(-1.86), m(0), m(0))
    j086 = Point(m(-0.25), m(0), m(0))
    j087 = Point(m(0.26), m(0), m(0))
    j088 = Point(m(1.87), m(0), m(0))
    j089 = Point(m(4.15), m(0), m(0))
    j090 = Point(m(6.57), m(0), m(0))
    j091 = Point(m(9), m(0), m(0))
    j092 = Point(m(-1.89), m(0), m(-2.53))
    j093 = Point(m(1.9), m(0), m(-2.53))
    j094 = Point(m(-1.94), m(0), m(-6.56))
    j095 = Point(m(1.95), m(0), m(-6.56))
    j096 = Point(m(-2.02), m(0), m(-12.6))
    j097 = Point(m(2.03), m(0), m(-12.6))
    j098 = Point(m(-2.11), m(0), m(-19.44))
    j099 = Point(m(2.12), m(0), m(-19.44))
    j100 = Point(m(-2.21), m(0), m(-27.06))
    j101 = Point(m(2.22), m(0), m(-27.06))
    j102 = Point(m(-2.34), m(0), m(-28.93))
    j103 = Point(m(-1.02), m(0), m(-28.93))
    j104 = Point(m(1.02), m(0), m(-28.93))
    j105 = Point(m(2.35), m(0), m(-28.93))
    j106 = Point(m(-2.46), m(0), m(-30.51))
    j107 = Point(m(2.46), m(0), m(-30.51))
    j108 = Point(m(-2.56), m(0), m(-31.99))
    j109 = Point(m(-0.96), m(0), m(-31.99))
    j110 = Point(m(0.96), m(0), m(-31.99))
    j111 = Point(m(2.57), m(0), m(-31.99))
    j112 = Point(m(-2.67), m(0), m(-33.57))
    j113 = Point(m(-1.97), m(0), m(-33.57))
    j114 = Point(m(1.98), m(0), m(-33.57))
    j115 = Point(m(2.68), m(0), m(-33.57))
    j116 = Point(m(-2.76), m(0), m(-34.8))
    j117 = Point(m(2.77), m(0), m(-34.8))
    j118 = Point(m(-2.96), m(0), m(-37.67))
    j119 = Point(m(-1.36), m(0), m(-37.67))
    j120 = Point(m(1.36), m(0), m(-37.67))
    j121 = Point(m(2.97), m(0), m(-37.67))
    j122 = Point(m(-3.16), m(0), m(-40.45))
    j123 = Point(m(3.17), m(0), m(-40.45))
    j124 = Point(m(-3.35), m(0), m(-43.09))
    j125 = Point(m(-1.29), m(0), m(-43.09))
    j126 = Point(m(1.3), m(0), m(-43.09))
    j127 = Point(m(3.35), m(0), m(-43.09))
    j128 = Point(m(-3.51), m(0), m(-45.31))
    j129 = Point(m(-2.38), m(0), m(-45.31))
    j130 = Point(m(2.39), m(0), m(-45.31))
    j131 = Point(m(3.51), m(0), m(-45.31))
    j132 = Point(m(-3.7), m(0), m(-48))
    j133 = Point(m(3.7), m(0), m(-48))
    return Tower(
        name="D-2-T-2019.1 WA140",
        datum=LowestCrossarm((m(48),)),
        voltages=(kv(380),),
        line_angles=(),
        attachments=(
            Mount(Wire.SHIELD, Point(m(-5), m(0), m(26.5)), Hold.CLAMP),
            Mount(Wire.SHIELD, Point(m(5), m(0), m(26.5)), Hold.CLAMP),
            Mount(Wire.PHASE, Point(m(-8), m(0), m(20)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(8), m(0), m(20)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-10.7), m(0), m(10)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(10.7), m(0), m(10)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-8.7), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(8.7), m(0), m(0)), Hold.STRAIN),
        ),
        bases=(),
        body=(
            Body(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j068, j069, role=Role.TRANSVERSE_BRACE),
                        Bar(j085, j072, role=Role.CHORD),
                        Bar(j072, j068, role=Role.CHORD),
                        Bar(j068, j066, role=Role.CHORD),
                        Bar(j066, j064, role=Role.CHORD),
                        Bar(j064, j057, role=Role.CHORD),
                        Bar(j057, j046, role=Role.CHORD),
                        Bar(j046, j042, role=Role.CHORD),
                        Bar(j042, j040, role=Role.CHORD),
                        Bar(j040, j038, role=Role.CHORD),
                        Bar(j038, j031, role=Role.CHORD),
                        Bar(j031, j020, role=Role.CHORD),
                        Bar(j020, j017, role=Role.CHORD),
                        Bar(j016, j021, role=Role.CHORD),
                        Bar(j021, j032, role=Role.CHORD),
                        Bar(j032, j039, role=Role.CHORD),
                        Bar(j039, j041, role=Role.CHORD),
                        Bar(j041, j043, role=Role.CHORD),
                        Bar(j043, j047, role=Role.CHORD),
                        Bar(j047, j058, role=Role.CHORD),
                        Bar(j058, j065, role=Role.CHORD),
                        Bar(j065, j067, role=Role.CHORD),
                        Bar(j067, j069, role=Role.CHORD),
                        Bar(j069, j073, role=Role.CHORD),
                        Bar(j073, j088, role=Role.CHORD),
                        Bar(j085, j092, role=Role.CHORD),
                        Bar(j092, j094, role=Role.CHORD),
                        Bar(j094, j096, role=Role.CHORD),
                        Bar(j096, j098, role=Role.CHORD),
                        Bar(j098, j100, role=Role.CHORD),
                        Bar(j088, j093, role=Role.CHORD),
                        Bar(j093, j095, role=Role.CHORD),
                        Bar(j095, j097, role=Role.CHORD),
                        Bar(j097, j099, role=Role.CHORD),
                        Bar(j099, j101, role=Role.CHORD),
                        Bar(j042, j043, role=Role.TRANSVERSE_BRACE),
                        Bar(j085, j073, role=Role.DIAGONAL_BRACE),
                        Bar(j073, j068, role=Role.DIAGONAL_BRACE),
                        Bar(j057, j047, role=Role.DIAGONAL_BRACE),
                        Bar(j047, j042, role=Role.DIAGONAL_BRACE),
                        Bar(j031, j021, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j017, role=Role.DIAGONAL_BRACE),
                        Bar(j088, j072, role=Role.DIAGONAL_BRACE),
                        Bar(j072, j069, role=Role.DIAGONAL_BRACE),
                        Bar(j058, j046, role=Role.DIAGONAL_BRACE),
                        Bar(j046, j043, role=Role.DIAGONAL_BRACE),
                        Bar(j032, j020, role=Role.DIAGONAL_BRACE),
                        Bar(j020, j016, role=Role.DIAGONAL_BRACE),
                        Bar(j068, j067, role=Role.DIAGONAL_BRACE),
                        Bar(j067, j064, role=Role.DIAGONAL_BRACE),
                        Bar(j064, j058, role=Role.DIAGONAL_BRACE),
                        Bar(j069, j066, role=Role.DIAGONAL_BRACE),
                        Bar(j066, j065, role=Role.DIAGONAL_BRACE),
                        Bar(j065, j057, role=Role.DIAGONAL_BRACE),
                        Bar(j042, j041, role=Role.DIAGONAL_BRACE),
                        Bar(j041, j038, role=Role.DIAGONAL_BRACE),
                        Bar(j038, j032, role=Role.DIAGONAL_BRACE),
                        Bar(j043, j040, role=Role.DIAGONAL_BRACE),
                        Bar(j040, j039, role=Role.DIAGONAL_BRACE),
                        Bar(j039, j031, role=Role.DIAGONAL_BRACE),
                        Bar(j125, j120, role=Role.DIAGONAL_BRACE),
                        Bar(j110, j103, role=Role.DIAGONAL_BRACE),
                        Bar(j126, j119, role=Role.DIAGONAL_BRACE),
                        Bar(j109, j104, role=Role.DIAGONAL_BRACE),
                        Bar(j100, j099, role=Role.DIAGONAL_BRACE),
                        Bar(j099, j096, role=Role.DIAGONAL_BRACE),
                        Bar(j096, j095, role=Role.DIAGONAL_BRACE),
                        Bar(j095, j092, role=Role.DIAGONAL_BRACE),
                        Bar(j092, j088, role=Role.DIAGONAL_BRACE),
                        Bar(j101, j098, role=Role.DIAGONAL_BRACE),
                        Bar(j098, j097, role=Role.DIAGONAL_BRACE),
                        Bar(j097, j094, role=Role.DIAGONAL_BRACE),
                        Bar(j094, j093, role=Role.DIAGONAL_BRACE),
                        Bar(j093, j085, role=Role.DIAGONAL_BRACE),
                        Bar(j123, j122, role=Role.TRANSVERSE_BRACE),
                        Bar(j107, j106, role=Role.TRANSVERSE_BRACE),
                        Bar(j100, j101, role=Role.TRANSVERSE_BRACE),
                        Bar(j031, j032, role=Role.TRANSVERSE_BRACE),
                        Bar(j057, j058, role=Role.TRANSVERSE_BRACE),
                        Bar(j085, j086, role=Role.TRANSVERSE_BRACE),
                        Bar(j086, j087, role=Role.TRANSVERSE_BRACE),
                        Bar(j087, j088, role=Role.TRANSVERSE_BRACE),
                        Bar(j017, j016, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        legs=(
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j132, j128, role=Role.CHORD),
                        Bar(j128, j124, role=Role.CHORD),
                        Bar(j124, j122, role=Role.CHORD),
                        Bar(j122, j118, role=Role.CHORD),
                        Bar(j118, j116, role=Role.CHORD),
                        Bar(j116, j112, role=Role.CHORD),
                        Bar(j112, j108, role=Role.CHORD),
                        Bar(j108, j106, role=Role.CHORD),
                        Bar(j106, j102, role=Role.CHORD),
                        Bar(j102, j100, role=Role.CHORD),
                        Bar(j132, j129, role=Role.DIAGONAL_BRACE),
                        Bar(j129, j125, role=Role.DIAGONAL_BRACE),
                        Bar(j103, j100, role=Role.DIAGONAL_BRACE),
                        Bar(j119, j116, role=Role.DIAGONAL_BRACE),
                        Bar(j116, j113, role=Role.DIAGONAL_BRACE),
                        Bar(j113, j109, role=Role.DIAGONAL_BRACE),
                        Bar(j125, j124, role=Role.TRANSVERSE_BRACE),
                        Bar(j129, j128, role=Role.TRANSVERSE_BRACE),
                        Bar(j119, j118, role=Role.TRANSVERSE_BRACE),
                        Bar(j129, j124, role=Role.DIAGONAL_BRACE),
                        Bar(j125, j122, role=Role.DIAGONAL_BRACE),
                        Bar(j122, j119, role=Role.DIAGONAL_BRACE),
                        Bar(j103, j102, role=Role.TRANSVERSE_BRACE),
                        Bar(j109, j108, role=Role.TRANSVERSE_BRACE),
                        Bar(j108, j113, role=Role.DIAGONAL_BRACE),
                        Bar(j113, j112, role=Role.TRANSVERSE_BRACE),
                        Bar(j109, j106, role=Role.DIAGONAL_BRACE),
                        Bar(j106, j103, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j101, j105, role=Role.CHORD),
                        Bar(j105, j107, role=Role.CHORD),
                        Bar(j107, j111, role=Role.CHORD),
                        Bar(j111, j115, role=Role.CHORD),
                        Bar(j115, j117, role=Role.CHORD),
                        Bar(j117, j121, role=Role.CHORD),
                        Bar(j121, j123, role=Role.CHORD),
                        Bar(j123, j127, role=Role.CHORD),
                        Bar(j127, j131, role=Role.CHORD),
                        Bar(j131, j133, role=Role.CHORD),
                        Bar(j120, j117, role=Role.DIAGONAL_BRACE),
                        Bar(j117, j114, role=Role.DIAGONAL_BRACE),
                        Bar(j114, j110, role=Role.DIAGONAL_BRACE),
                        Bar(j133, j130, role=Role.DIAGONAL_BRACE),
                        Bar(j130, j126, role=Role.DIAGONAL_BRACE),
                        Bar(j104, j101, role=Role.DIAGONAL_BRACE),
                        Bar(j126, j127, role=Role.TRANSVERSE_BRACE),
                        Bar(j130, j131, role=Role.TRANSVERSE_BRACE),
                        Bar(j120, j121, role=Role.TRANSVERSE_BRACE),
                        Bar(j130, j127, role=Role.DIAGONAL_BRACE),
                        Bar(j126, j123, role=Role.DIAGONAL_BRACE),
                        Bar(j123, j120, role=Role.DIAGONAL_BRACE),
                        Bar(j104, j105, role=Role.TRANSVERSE_BRACE),
                        Bar(j110, j111, role=Role.TRANSVERSE_BRACE),
                        Bar(j111, j114, role=Role.DIAGONAL_BRACE),
                        Bar(j114, j115, role=Role.TRANSVERSE_BRACE),
                        Bar(j110, j107, role=Role.DIAGONAL_BRACE),
                        Bar(j107, j104, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        head=(
            Head(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j016, j013, role=Role.CHORD),
                        Bar(j013, j017, role=Role.CHORD),
                    ),
                )
            ),
        ),
        crossarms=(
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j028, j036, role=Role.CHORD),
                        Bar(j036, j029, role=Role.CHORD),
                        Bar(j029, j030, role=Role.CHORD),
                        Bar(j030, j031, role=Role.CHORD),
                        Bar(j017, j018, role=Role.CHORD),
                        Bar(j018, j024, role=Role.CHORD),
                        Bar(j024, j026, role=Role.CHORD),
                        Bar(j018, j030, role=Role.TRANSVERSE_BRACE),
                        Bar(j030, j024, role=Role.DIAGONAL_BRACE),
                        Bar(j024, j029, role=Role.TRANSVERSE_BRACE),
                        Bar(j028, j026, role=Role.CHORD),
                        Bar(j017, j022, role=Role.DIAGONAL_BRACE),
                        Bar(j022, j030, role=Role.DIAGONAL_BRACE),
                        Bar(j022, j031, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j035, j037, role=Role.CHORD),
                        Bar(j037, j034, role=Role.CHORD),
                        Bar(j034, j033, role=Role.CHORD),
                        Bar(j033, j032, role=Role.CHORD),
                        Bar(j016, j019, role=Role.CHORD),
                        Bar(j019, j025, role=Role.CHORD),
                        Bar(j025, j027, role=Role.CHORD),
                        Bar(j019, j033, role=Role.TRANSVERSE_BRACE),
                        Bar(j033, j025, role=Role.DIAGONAL_BRACE),
                        Bar(j025, j034, role=Role.TRANSVERSE_BRACE),
                        Bar(j035, j027, role=Role.CHORD),
                        Bar(j016, j023, role=Role.DIAGONAL_BRACE),
                        Bar(j023, j033, role=Role.DIAGONAL_BRACE),
                        Bar(j023, j032, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j054, j062, role=Role.CHORD),
                        Bar(j062, j055, role=Role.CHORD),
                        Bar(j055, j056, role=Role.CHORD),
                        Bar(j056, j057, role=Role.CHORD),
                        Bar(j042, j044, role=Role.CHORD),
                        Bar(j044, j050, role=Role.CHORD),
                        Bar(j050, j052, role=Role.CHORD),
                        Bar(j044, j056, role=Role.TRANSVERSE_BRACE),
                        Bar(j056, j050, role=Role.DIAGONAL_BRACE),
                        Bar(j050, j055, role=Role.TRANSVERSE_BRACE),
                        Bar(j054, j052, role=Role.CHORD),
                        Bar(j042, j048, role=Role.DIAGONAL_BRACE),
                        Bar(j048, j056, role=Role.DIAGONAL_BRACE),
                        Bar(j048, j057, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j061, j063, role=Role.CHORD),
                        Bar(j063, j060, role=Role.CHORD),
                        Bar(j060, j059, role=Role.CHORD),
                        Bar(j059, j058, role=Role.CHORD),
                        Bar(j043, j045, role=Role.CHORD),
                        Bar(j045, j051, role=Role.CHORD),
                        Bar(j051, j053, role=Role.CHORD),
                        Bar(j045, j059, role=Role.TRANSVERSE_BRACE),
                        Bar(j059, j051, role=Role.DIAGONAL_BRACE),
                        Bar(j051, j060, role=Role.TRANSVERSE_BRACE),
                        Bar(j061, j053, role=Role.CHORD),
                        Bar(j043, j049, role=Role.DIAGONAL_BRACE),
                        Bar(j049, j059, role=Role.DIAGONAL_BRACE),
                        Bar(j049, j058, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j082, j080, role=Role.CHORD),
                        Bar(j080, j083, role=Role.CHORD),
                        Bar(j083, j084, role=Role.CHORD),
                        Bar(j084, j085, role=Role.CHORD),
                        Bar(j068, j070, role=Role.CHORD),
                        Bar(j070, j076, role=Role.CHORD),
                        Bar(j076, j078, role=Role.CHORD),
                        Bar(j070, j084, role=Role.TRANSVERSE_BRACE),
                        Bar(j084, j076, role=Role.DIAGONAL_BRACE),
                        Bar(j076, j083, role=Role.TRANSVERSE_BRACE),
                        Bar(j082, j078, role=Role.CHORD),
                        Bar(j068, j074, role=Role.DIAGONAL_BRACE),
                        Bar(j074, j084, role=Role.DIAGONAL_BRACE),
                        Bar(j074, j085, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j091, j081, role=Role.CHORD),
                        Bar(j081, j090, role=Role.CHORD),
                        Bar(j090, j089, role=Role.CHORD),
                        Bar(j089, j088, role=Role.CHORD),
                        Bar(j069, j071, role=Role.CHORD),
                        Bar(j071, j077, role=Role.CHORD),
                        Bar(j077, j079, role=Role.CHORD),
                        Bar(j071, j089, role=Role.TRANSVERSE_BRACE),
                        Bar(j089, j077, role=Role.DIAGONAL_BRACE),
                        Bar(j077, j090, role=Role.TRANSVERSE_BRACE),
                        Bar(j091, j079, role=Role.CHORD),
                        Bar(j069, j075, role=Role.DIAGONAL_BRACE),
                        Bar(j075, j089, role=Role.DIAGONAL_BRACE),
                        Bar(j075, j088, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        peaks=(
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j002, j005, role=Role.DIAGONAL_BRACE),
                        Bar(j005, j007, role=Role.DIAGONAL_BRACE),
                        Bar(j007, j009, role=Role.DIAGONAL_BRACE),
                        Bar(j009, j010, role=Role.TRANSVERSE_BRACE),
                        Bar(j010, j014, role=Role.DIAGONAL_BRACE),
                        Bar(j014, j013, role=Role.DIAGONAL_BRACE),
                        Bar(j013, j010, role=Role.CHORD),
                        Bar(j010, j007, role=Role.CHORD),
                        Bar(j007, j002, role=Role.CHORD),
                        Bar(j002, j001, role=Role.CHORD),
                        Bar(j001, j005, role=Role.CHORD),
                        Bar(j005, j009, role=Role.CHORD),
                        Bar(j009, j014, role=Role.CHORD),
                        Bar(j014, j017, role=Role.CHORD),
                    ),
                )
            ),
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j003, j006, role=Role.DIAGONAL_BRACE),
                        Bar(j006, j008, role=Role.DIAGONAL_BRACE),
                        Bar(j008, j012, role=Role.DIAGONAL_BRACE),
                        Bar(j012, j011, role=Role.TRANSVERSE_BRACE),
                        Bar(j011, j015, role=Role.DIAGONAL_BRACE),
                        Bar(j015, j013, role=Role.DIAGONAL_BRACE),
                        Bar(j013, j011, role=Role.CHORD),
                        Bar(j011, j008, role=Role.CHORD),
                        Bar(j008, j003, role=Role.CHORD),
                        Bar(j003, j004, role=Role.CHORD),
                        Bar(j004, j006, role=Role.CHORD),
                        Bar(j006, j012, role=Role.CHORD),
                        Bar(j012, j015, role=Role.CHORD),
                        Bar(j015, j016, role=Role.CHORD),
                    ),
                )
            ),
        ),
    )


D_2_T_2019_1_WA140 = _d_2_t_2019_1_wa140()


def _d_2_t_2019_1_wa160() -> Tower[LowestCrossarm]:
    """D-2-T-2019.1 WA160: each joint written once, by its key."""
    j001 = Point(m(-5), m(0), m(27))
    j002 = Point(m(-4.71), m(0), m(27))
    j003 = Point(m(4.72), m(0), m(27))
    j004 = Point(m(5), m(0), m(27))
    j005 = Point(m(-4.04), m(0), m(26.03))
    j006 = Point(m(-2.88), m(0), m(26.03))
    j007 = Point(m(2.89), m(0), m(26.03))
    j008 = Point(m(4.03), m(0), m(26.03))
    j009 = Point(m(-1.23), m(0), m(25.09))
    j010 = Point(m(1.23), m(0), m(25.09))
    j011 = Point(m(-2.78), m(0), m(24.66))
    j012 = Point(m(2.79), m(0), m(24.66))
    j013 = Point(m(0), m(0), m(24.28))
    j014 = Point(m(-1.73), m(0), m(23.38))
    j015 = Point(m(1.74), m(0), m(23.38))
    j016 = Point(m(0), m(0), m(22.66))
    j017 = Point(m(1.19), m(0), m(22.66))
    j018 = Point(m(-1.19), m(0), m(22.65))
    j019 = Point(m(-3.3), m(0), m(21.92))
    j020 = Point(m(3.3), m(0), m(21.92))
    j021 = Point(m(-1.22), m(0), m(21.43))
    j022 = Point(m(1.22), m(0), m(21.43))
    j023 = Point(m(-2.25), m(0), m(21.32))
    j024 = Point(m(2.26), m(0), m(21.32))
    j025 = Point(m(-5.54), m(0), m(21.14))
    j026 = Point(m(5.55), m(0), m(21.14))
    j027 = Point(m(-7.78), m(0), m(20.36))
    j028 = Point(m(7.78), m(0), m(20.36))
    j029 = Point(m(-7.78), m(0), m(20))
    j030 = Point(m(-5.54), m(0), m(20))
    j031 = Point(m(-3.31), m(0), m(20))
    j032 = Point(m(-1.26), m(0), m(20))
    j033 = Point(m(1.26), m(0), m(20))
    j034 = Point(m(3.31), m(0), m(20))
    j035 = Point(m(5.55), m(0), m(20))
    j036 = Point(m(7.78), m(0), m(20))
    j037 = Point(m(-7.5), m(0), m(20))
    j038 = Point(m(7.5), m(0), m(20))
    j039 = Point(m(-1.3), m(0), m(18.21))
    j040 = Point(m(1.3), m(0), m(18.21))
    j041 = Point(m(-1.34), m(0), m(16.73))
    j042 = Point(m(1.34), m(0), m(16.73))
    j043 = Point(m(-1.39), m(0), m(14.5))
    j044 = Point(m(1.4), m(0), m(14.5))
    j045 = Point(m(-5.52), m(0), m(12.71))
    j046 = Point(m(5.53), m(0), m(12.71))
    j047 = Point(m(-1.44), m(0), m(12.37))
    j048 = Point(m(1.45), m(0), m(12.37))
    j049 = Point(m(-3.47), m(0), m(12.24))
    j050 = Point(m(3.47), m(0), m(12.24))
    j051 = Point(m(-8.01), m(0), m(11.62))
    j052 = Point(m(8.02), m(0), m(11.62))
    j053 = Point(m(-10.5), m(0), m(10.54))
    j054 = Point(m(10.52), m(0), m(10.54))
    j055 = Point(m(-10.5), m(0), m(10))
    j056 = Point(m(-8.01), m(0), m(10))
    j057 = Point(m(-5.52), m(0), m(10))
    j058 = Point(m(-1.5), m(0), m(10))
    j059 = Point(m(1.51), m(0), m(10))
    j060 = Point(m(5.52), m(0), m(10))
    j061 = Point(m(8.02), m(0), m(10))
    j062 = Point(m(10.52), m(0), m(10))
    j063 = Point(m(-10.2), m(0), m(10))
    j064 = Point(m(10.2), m(0), m(10))
    j065 = Point(m(-1.55), m(0), m(8.07))
    j066 = Point(m(1.56), m(0), m(8.07))
    j067 = Point(m(-1.6), m(0), m(6.12))
    j068 = Point(m(1.61), m(0), m(6.12))
    j069 = Point(m(-1.65), m(0), m(4))
    j070 = Point(m(1.66), m(0), m(4))
    j071 = Point(m(-3.91), m(0), m(2.85))
    j072 = Point(m(3.91), m(0), m(2.85))
    j073 = Point(m(-1.7), m(0), m(2.14))
    j074 = Point(m(1.71), m(0), m(2.14))
    j075 = Point(m(-2.79), m(0), m(2))
    j076 = Point(m(2.78), m(0), m(2))
    j077 = Point(m(-6.19), m(0), m(1.69))
    j078 = Point(m(6.2), m(0), m(1.69))
    j079 = Point(m(-8.48), m(0), m(0.52))
    j080 = Point(m(8.47), m(0), m(0.52))
    j081 = Point(m(-8.2), m(0), m(0))
    j082 = Point(m(8.2), m(0), m(0))
    j083 = Point(m(-8.48), m(0), m(0))
    j084 = Point(m(-6.19), m(0), m(0))
    j085 = Point(m(-3.91), m(0), m(0))
    j086 = Point(m(-1.75), m(0), m(0))
    j087 = Point(m(-0.24), m(0), m(0))
    j088 = Point(m(0.24), m(0), m(0))
    j089 = Point(m(1.76), m(0), m(0))
    j090 = Point(m(3.91), m(0), m(0))
    j091 = Point(m(6.2), m(0), m(0))
    j092 = Point(m(8.47), m(0), m(0))
    j093 = Point(m(-1.78), m(0), m(-1.58))
    j094 = Point(m(1.79), m(0), m(-1.58))
    j095 = Point(m(-1.83), m(0), m(-4.1))
    j096 = Point(m(1.84), m(0), m(-4.1))
    j097 = Point(m(-1.9), m(0), m(-7.88))
    j098 = Point(m(1.92), m(0), m(-7.88))
    j099 = Point(m(-1.99), m(0), m(-12.15))
    j100 = Point(m(2), m(0), m(-12.15))
    j101 = Point(m(-2.08), m(0), m(-16.91))
    j102 = Point(m(2.1), m(0), m(-16.91))
    j103 = Point(m(-2.21), m(0), m(-18.08))
    j104 = Point(m(-0.96), m(0), m(-18.08))
    j105 = Point(m(0.96), m(0), m(-18.08))
    j106 = Point(m(2.22), m(0), m(-18.08))
    j107 = Point(m(-2.31), m(0), m(-19.07))
    j108 = Point(m(2.33), m(0), m(-19.07))
    j109 = Point(m(-2.41), m(0), m(-20))
    j110 = Point(m(-0.91), m(0), m(-20))
    j111 = Point(m(0.91), m(0), m(-20))
    j112 = Point(m(2.43), m(0), m(-20))
    j113 = Point(m(-2.52), m(0), m(-20.98))
    j114 = Point(m(-1.86), m(0), m(-20.98))
    j115 = Point(m(1.87), m(0), m(-20.98))
    j116 = Point(m(2.53), m(0), m(-20.98))
    j117 = Point(m(-2.6), m(0), m(-21.75))
    j118 = Point(m(2.61), m(0), m(-21.75))
    j119 = Point(m(-2.79), m(0), m(-23.54))
    j120 = Point(m(-1.28), m(0), m(-23.54))
    j121 = Point(m(1.28), m(0), m(-23.54))
    j122 = Point(m(2.8), m(0), m(-23.54))
    j123 = Point(m(-2.98), m(0), m(-25.28))
    j124 = Point(m(2.99), m(0), m(-25.28))
    j125 = Point(m(-3.16), m(0), m(-26.93))
    j126 = Point(m(-1.22), m(0), m(-26.93))
    j127 = Point(m(1.23), m(0), m(-26.93))
    j128 = Point(m(3.16), m(0), m(-26.93))
    j129 = Point(m(-3.31), m(0), m(-28.32))
    j130 = Point(m(-2.25), m(0), m(-28.32))
    j131 = Point(m(2.25), m(0), m(-28.32))
    j132 = Point(m(3.31), m(0), m(-28.32))
    j133 = Point(m(-3.49), m(0), m(-30))
    j134 = Point(m(3.49), m(0), m(-30))
    return Tower(
        name="D-2-T-2019.1 WA160",
        datum=LowestCrossarm((m(30),)),
        voltages=(kv(380),),
        line_angles=(),
        attachments=(
            Mount(Wire.SHIELD, Point(m(-5), m(0), m(27)), Hold.CLAMP),
            Mount(Wire.SHIELD, Point(m(5), m(0), m(27)), Hold.CLAMP),
            Mount(Wire.PHASE, Point(m(-7.5), m(0), m(20)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(7.5), m(0), m(20)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-10.2), m(0), m(10)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(10.2), m(0), m(10)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-8.2), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(8.2), m(0), m(0)), Hold.STRAIN),
        ),
        bases=(),
        body=(
            Body(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j069, j070, role=Role.TRANSVERSE_BRACE),
                        Bar(j086, j073, role=Role.CHORD),
                        Bar(j073, j069, role=Role.CHORD),
                        Bar(j069, j067, role=Role.CHORD),
                        Bar(j067, j065, role=Role.CHORD),
                        Bar(j065, j058, role=Role.CHORD),
                        Bar(j058, j047, role=Role.CHORD),
                        Bar(j047, j043, role=Role.CHORD),
                        Bar(j043, j041, role=Role.CHORD),
                        Bar(j041, j039, role=Role.CHORD),
                        Bar(j039, j032, role=Role.CHORD),
                        Bar(j032, j021, role=Role.CHORD),
                        Bar(j021, j018, role=Role.CHORD),
                        Bar(j017, j022, role=Role.CHORD),
                        Bar(j022, j033, role=Role.CHORD),
                        Bar(j033, j040, role=Role.CHORD),
                        Bar(j040, j042, role=Role.CHORD),
                        Bar(j042, j044, role=Role.CHORD),
                        Bar(j044, j048, role=Role.CHORD),
                        Bar(j048, j059, role=Role.CHORD),
                        Bar(j059, j066, role=Role.CHORD),
                        Bar(j066, j068, role=Role.CHORD),
                        Bar(j068, j070, role=Role.CHORD),
                        Bar(j070, j074, role=Role.CHORD),
                        Bar(j074, j089, role=Role.CHORD),
                        Bar(j086, j093, role=Role.CHORD),
                        Bar(j093, j095, role=Role.CHORD),
                        Bar(j095, j097, role=Role.CHORD),
                        Bar(j097, j099, role=Role.CHORD),
                        Bar(j099, j101, role=Role.CHORD),
                        Bar(j089, j094, role=Role.CHORD),
                        Bar(j094, j096, role=Role.CHORD),
                        Bar(j096, j098, role=Role.CHORD),
                        Bar(j098, j100, role=Role.CHORD),
                        Bar(j100, j102, role=Role.CHORD),
                        Bar(j043, j044, role=Role.TRANSVERSE_BRACE),
                        Bar(j086, j074, role=Role.DIAGONAL_BRACE),
                        Bar(j074, j069, role=Role.DIAGONAL_BRACE),
                        Bar(j058, j048, role=Role.DIAGONAL_BRACE),
                        Bar(j048, j043, role=Role.DIAGONAL_BRACE),
                        Bar(j032, j022, role=Role.DIAGONAL_BRACE),
                        Bar(j022, j018, role=Role.DIAGONAL_BRACE),
                        Bar(j089, j073, role=Role.DIAGONAL_BRACE),
                        Bar(j073, j070, role=Role.DIAGONAL_BRACE),
                        Bar(j059, j047, role=Role.DIAGONAL_BRACE),
                        Bar(j047, j044, role=Role.DIAGONAL_BRACE),
                        Bar(j033, j021, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j017, role=Role.DIAGONAL_BRACE),
                        Bar(j069, j068, role=Role.DIAGONAL_BRACE),
                        Bar(j068, j065, role=Role.DIAGONAL_BRACE),
                        Bar(j065, j059, role=Role.DIAGONAL_BRACE),
                        Bar(j070, j067, role=Role.DIAGONAL_BRACE),
                        Bar(j067, j066, role=Role.DIAGONAL_BRACE),
                        Bar(j066, j058, role=Role.DIAGONAL_BRACE),
                        Bar(j043, j042, role=Role.DIAGONAL_BRACE),
                        Bar(j042, j039, role=Role.DIAGONAL_BRACE),
                        Bar(j039, j033, role=Role.DIAGONAL_BRACE),
                        Bar(j044, j041, role=Role.DIAGONAL_BRACE),
                        Bar(j041, j040, role=Role.DIAGONAL_BRACE),
                        Bar(j040, j032, role=Role.DIAGONAL_BRACE),
                        Bar(j126, j121, role=Role.DIAGONAL_BRACE),
                        Bar(j111, j104, role=Role.DIAGONAL_BRACE),
                        Bar(j127, j120, role=Role.DIAGONAL_BRACE),
                        Bar(j110, j105, role=Role.DIAGONAL_BRACE),
                        Bar(j101, j100, role=Role.DIAGONAL_BRACE),
                        Bar(j100, j097, role=Role.DIAGONAL_BRACE),
                        Bar(j097, j096, role=Role.DIAGONAL_BRACE),
                        Bar(j096, j093, role=Role.DIAGONAL_BRACE),
                        Bar(j093, j089, role=Role.DIAGONAL_BRACE),
                        Bar(j102, j099, role=Role.DIAGONAL_BRACE),
                        Bar(j099, j098, role=Role.DIAGONAL_BRACE),
                        Bar(j098, j095, role=Role.DIAGONAL_BRACE),
                        Bar(j095, j094, role=Role.DIAGONAL_BRACE),
                        Bar(j094, j086, role=Role.DIAGONAL_BRACE),
                        Bar(j124, j123, role=Role.TRANSVERSE_BRACE),
                        Bar(j108, j107, role=Role.TRANSVERSE_BRACE),
                        Bar(j101, j102, role=Role.TRANSVERSE_BRACE),
                        Bar(j032, j033, role=Role.TRANSVERSE_BRACE),
                        Bar(j058, j059, role=Role.TRANSVERSE_BRACE),
                        Bar(j086, j087, role=Role.TRANSVERSE_BRACE),
                        Bar(j087, j088, role=Role.TRANSVERSE_BRACE),
                        Bar(j088, j089, role=Role.TRANSVERSE_BRACE),
                        Bar(j018, j016, role=Role.TRANSVERSE_BRACE),
                        Bar(j016, j017, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        legs=(
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j133, j129, role=Role.CHORD),
                        Bar(j129, j125, role=Role.CHORD),
                        Bar(j125, j123, role=Role.CHORD),
                        Bar(j123, j119, role=Role.CHORD),
                        Bar(j119, j117, role=Role.CHORD),
                        Bar(j117, j113, role=Role.CHORD),
                        Bar(j113, j109, role=Role.CHORD),
                        Bar(j109, j107, role=Role.CHORD),
                        Bar(j107, j103, role=Role.CHORD),
                        Bar(j103, j101, role=Role.CHORD),
                        Bar(j133, j130, role=Role.DIAGONAL_BRACE),
                        Bar(j130, j126, role=Role.DIAGONAL_BRACE),
                        Bar(j104, j101, role=Role.DIAGONAL_BRACE),
                        Bar(j120, j117, role=Role.DIAGONAL_BRACE),
                        Bar(j117, j114, role=Role.DIAGONAL_BRACE),
                        Bar(j114, j110, role=Role.DIAGONAL_BRACE),
                        Bar(j126, j125, role=Role.TRANSVERSE_BRACE),
                        Bar(j130, j129, role=Role.TRANSVERSE_BRACE),
                        Bar(j120, j119, role=Role.TRANSVERSE_BRACE),
                        Bar(j130, j125, role=Role.DIAGONAL_BRACE),
                        Bar(j126, j123, role=Role.DIAGONAL_BRACE),
                        Bar(j123, j120, role=Role.DIAGONAL_BRACE),
                        Bar(j104, j103, role=Role.TRANSVERSE_BRACE),
                        Bar(j110, j109, role=Role.TRANSVERSE_BRACE),
                        Bar(j109, j114, role=Role.DIAGONAL_BRACE),
                        Bar(j114, j113, role=Role.TRANSVERSE_BRACE),
                        Bar(j110, j107, role=Role.DIAGONAL_BRACE),
                        Bar(j107, j104, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j102, j106, role=Role.CHORD),
                        Bar(j106, j108, role=Role.CHORD),
                        Bar(j108, j112, role=Role.CHORD),
                        Bar(j112, j116, role=Role.CHORD),
                        Bar(j116, j118, role=Role.CHORD),
                        Bar(j118, j122, role=Role.CHORD),
                        Bar(j122, j124, role=Role.CHORD),
                        Bar(j124, j128, role=Role.CHORD),
                        Bar(j128, j132, role=Role.CHORD),
                        Bar(j132, j134, role=Role.CHORD),
                        Bar(j121, j118, role=Role.DIAGONAL_BRACE),
                        Bar(j118, j115, role=Role.DIAGONAL_BRACE),
                        Bar(j115, j111, role=Role.DIAGONAL_BRACE),
                        Bar(j134, j131, role=Role.DIAGONAL_BRACE),
                        Bar(j131, j127, role=Role.DIAGONAL_BRACE),
                        Bar(j105, j102, role=Role.DIAGONAL_BRACE),
                        Bar(j127, j128, role=Role.TRANSVERSE_BRACE),
                        Bar(j131, j132, role=Role.TRANSVERSE_BRACE),
                        Bar(j121, j122, role=Role.TRANSVERSE_BRACE),
                        Bar(j131, j128, role=Role.DIAGONAL_BRACE),
                        Bar(j127, j124, role=Role.DIAGONAL_BRACE),
                        Bar(j124, j121, role=Role.DIAGONAL_BRACE),
                        Bar(j105, j106, role=Role.TRANSVERSE_BRACE),
                        Bar(j111, j112, role=Role.TRANSVERSE_BRACE),
                        Bar(j112, j115, role=Role.DIAGONAL_BRACE),
                        Bar(j115, j116, role=Role.TRANSVERSE_BRACE),
                        Bar(j111, j108, role=Role.DIAGONAL_BRACE),
                        Bar(j108, j105, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        head=(
            Head(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j016, j013, role=Role.TRANSVERSE_BRACE),
                        Bar(j013, j018, role=Role.CHORD),
                        Bar(j013, j017, role=Role.CHORD),
                    ),
                )
            ),
        ),
        crossarms=(
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j029, j037, role=Role.CHORD),
                        Bar(j037, j030, role=Role.CHORD),
                        Bar(j030, j031, role=Role.CHORD),
                        Bar(j031, j032, role=Role.CHORD),
                        Bar(j018, j019, role=Role.CHORD),
                        Bar(j019, j025, role=Role.CHORD),
                        Bar(j025, j027, role=Role.CHORD),
                        Bar(j019, j031, role=Role.TRANSVERSE_BRACE),
                        Bar(j031, j025, role=Role.DIAGONAL_BRACE),
                        Bar(j025, j030, role=Role.TRANSVERSE_BRACE),
                        Bar(j029, j027, role=Role.CHORD),
                        Bar(j018, j023, role=Role.DIAGONAL_BRACE),
                        Bar(j023, j031, role=Role.DIAGONAL_BRACE),
                        Bar(j023, j032, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j036, j038, role=Role.CHORD),
                        Bar(j038, j035, role=Role.CHORD),
                        Bar(j035, j034, role=Role.CHORD),
                        Bar(j034, j033, role=Role.CHORD),
                        Bar(j017, j020, role=Role.CHORD),
                        Bar(j020, j026, role=Role.CHORD),
                        Bar(j026, j028, role=Role.CHORD),
                        Bar(j020, j034, role=Role.TRANSVERSE_BRACE),
                        Bar(j034, j026, role=Role.DIAGONAL_BRACE),
                        Bar(j026, j035, role=Role.TRANSVERSE_BRACE),
                        Bar(j036, j028, role=Role.CHORD),
                        Bar(j017, j024, role=Role.DIAGONAL_BRACE),
                        Bar(j024, j034, role=Role.DIAGONAL_BRACE),
                        Bar(j024, j033, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j055, j063, role=Role.CHORD),
                        Bar(j063, j056, role=Role.CHORD),
                        Bar(j056, j057, role=Role.CHORD),
                        Bar(j057, j058, role=Role.CHORD),
                        Bar(j043, j045, role=Role.CHORD),
                        Bar(j045, j051, role=Role.CHORD),
                        Bar(j051, j053, role=Role.CHORD),
                        Bar(j045, j057, role=Role.TRANSVERSE_BRACE),
                        Bar(j057, j051, role=Role.DIAGONAL_BRACE),
                        Bar(j051, j056, role=Role.TRANSVERSE_BRACE),
                        Bar(j055, j053, role=Role.CHORD),
                        Bar(j043, j049, role=Role.DIAGONAL_BRACE),
                        Bar(j049, j057, role=Role.DIAGONAL_BRACE),
                        Bar(j049, j058, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j062, j064, role=Role.CHORD),
                        Bar(j064, j061, role=Role.CHORD),
                        Bar(j061, j060, role=Role.CHORD),
                        Bar(j060, j059, role=Role.CHORD),
                        Bar(j044, j046, role=Role.CHORD),
                        Bar(j046, j052, role=Role.CHORD),
                        Bar(j052, j054, role=Role.CHORD),
                        Bar(j046, j060, role=Role.TRANSVERSE_BRACE),
                        Bar(j060, j052, role=Role.DIAGONAL_BRACE),
                        Bar(j052, j061, role=Role.TRANSVERSE_BRACE),
                        Bar(j062, j054, role=Role.CHORD),
                        Bar(j044, j050, role=Role.DIAGONAL_BRACE),
                        Bar(j050, j060, role=Role.DIAGONAL_BRACE),
                        Bar(j050, j059, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j083, j081, role=Role.CHORD),
                        Bar(j081, j084, role=Role.CHORD),
                        Bar(j084, j085, role=Role.CHORD),
                        Bar(j085, j086, role=Role.CHORD),
                        Bar(j069, j071, role=Role.CHORD),
                        Bar(j071, j077, role=Role.CHORD),
                        Bar(j077, j079, role=Role.CHORD),
                        Bar(j071, j085, role=Role.TRANSVERSE_BRACE),
                        Bar(j085, j077, role=Role.DIAGONAL_BRACE),
                        Bar(j077, j084, role=Role.TRANSVERSE_BRACE),
                        Bar(j083, j079, role=Role.CHORD),
                        Bar(j069, j075, role=Role.DIAGONAL_BRACE),
                        Bar(j075, j085, role=Role.DIAGONAL_BRACE),
                        Bar(j075, j086, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j092, j082, role=Role.CHORD),
                        Bar(j082, j091, role=Role.CHORD),
                        Bar(j091, j090, role=Role.CHORD),
                        Bar(j090, j089, role=Role.CHORD),
                        Bar(j070, j072, role=Role.CHORD),
                        Bar(j072, j078, role=Role.CHORD),
                        Bar(j078, j080, role=Role.CHORD),
                        Bar(j072, j090, role=Role.TRANSVERSE_BRACE),
                        Bar(j090, j078, role=Role.DIAGONAL_BRACE),
                        Bar(j078, j091, role=Role.TRANSVERSE_BRACE),
                        Bar(j092, j080, role=Role.CHORD),
                        Bar(j070, j076, role=Role.DIAGONAL_BRACE),
                        Bar(j076, j090, role=Role.DIAGONAL_BRACE),
                        Bar(j076, j089, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        peaks=(
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j002, j005, role=Role.DIAGONAL_BRACE),
                        Bar(j005, j006, role=Role.TRANSVERSE_BRACE),
                        Bar(j006, j011, role=Role.TRANSVERSE_BRACE),
                        Bar(j011, j009, role=Role.DIAGONAL_BRACE),
                        Bar(j009, j014, role=Role.DIAGONAL_BRACE),
                        Bar(j014, j013, role=Role.DIAGONAL_BRACE),
                        Bar(j013, j009, role=Role.CHORD),
                        Bar(j009, j006, role=Role.CHORD),
                        Bar(j006, j002, role=Role.CHORD),
                        Bar(j002, j001, role=Role.CHORD),
                        Bar(j001, j005, role=Role.CHORD),
                        Bar(j005, j011, role=Role.CHORD),
                        Bar(j011, j014, role=Role.CHORD),
                        Bar(j014, j018, role=Role.CHORD),
                    ),
                )
            ),
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j003, j008, role=Role.DIAGONAL_BRACE),
                        Bar(j008, j007, role=Role.TRANSVERSE_BRACE),
                        Bar(j007, j012, role=Role.TRANSVERSE_BRACE),
                        Bar(j012, j010, role=Role.DIAGONAL_BRACE),
                        Bar(j010, j015, role=Role.DIAGONAL_BRACE),
                        Bar(j015, j013, role=Role.DIAGONAL_BRACE),
                        Bar(j017, j015, role=Role.CHORD),
                        Bar(j015, j012, role=Role.CHORD),
                        Bar(j012, j008, role=Role.CHORD),
                        Bar(j008, j004, role=Role.CHORD),
                        Bar(j004, j003, role=Role.CHORD),
                        Bar(j003, j007, role=Role.CHORD),
                        Bar(j007, j010, role=Role.CHORD),
                        Bar(j010, j013, role=Role.CHORD),
                    ),
                )
            ),
        ),
    )


D_2_T_2019_1_WA160 = _d_2_t_2019_1_wa160()


def _da_4_de_2018_1_t1() -> Tower[LowestCrossarm]:
    """DA-4-DE-2018.1 T1: each joint written once, by its key."""
    j001 = Point(m(-6.5), m(0), m(29.5))
    j002 = Point(m(6.5), m(0), m(29.5))
    j003 = Point(m(-6.35), m(0), m(29.43))
    j004 = Point(m(6.34), m(0), m(29.43))
    j005 = Point(m(-6.07), m(0), m(28.97))
    j006 = Point(m(-5.3), m(0), m(28.97))
    j007 = Point(m(5.3), m(0), m(28.97))
    j008 = Point(m(6.07), m(0), m(28.97))
    j009 = Point(m(-3.91), m(0), m(28.42))
    j010 = Point(m(3.91), m(0), m(28.42))
    j011 = Point(m(-5.34), m(0), m(28.19))
    j012 = Point(m(5.34), m(0), m(28.19))
    j013 = Point(m(-2.2), m(0), m(27.79))
    j014 = Point(m(2.19), m(0), m(27.79))
    j015 = Point(m(-4.16), m(0), m(27.13))
    j016 = Point(m(4.16), m(0), m(27.13))
    j017 = Point(m(-0.01), m(0), m(27.02))
    j018 = Point(m(-2.52), m(0), m(25.89))
    j019 = Point(m(2.52), m(0), m(25.89))
    j020 = Point(m(-1.2), m(0), m(25.03))
    j021 = Point(m(-0.01), m(0), m(25.03))
    j022 = Point(m(1.2), m(0), m(25.03))
    j023 = Point(m(-6.42), m(0), m(23.94))
    j024 = Point(m(6.42), m(0), m(23.94))
    j025 = Point(m(-3.71), m(0), m(23.57))
    j026 = Point(m(3.71), m(0), m(23.57))
    j027 = Point(m(-1.27), m(0), m(23.51))
    j028 = Point(m(1.26), m(0), m(23.51))
    j029 = Point(m(-9.95), m(0), m(23.22))
    j030 = Point(m(9.95), m(0), m(23.22))
    j031 = Point(m(-13.48), m(0), m(22.5))
    j032 = Point(m(13.48), m(0), m(22.5))
    j033 = Point(m(-13.49), m(0), m(22))
    j034 = Point(m(-11.72), m(0), m(22))
    j035 = Point(m(-9.95), m(0), m(22))
    j036 = Point(m(-8.18), m(0), m(22))
    j037 = Point(m(-6.41), m(0), m(22))
    j038 = Point(m(-3.69), m(0), m(22))
    j039 = Point(m(-1.33), m(0), m(22))
    j040 = Point(m(1.32), m(0), m(22))
    j041 = Point(m(3.69), m(0), m(22))
    j042 = Point(m(6.42), m(0), m(22))
    j043 = Point(m(8.18), m(0), m(22))
    j044 = Point(m(9.95), m(0), m(22))
    j045 = Point(m(11.72), m(0), m(22))
    j046 = Point(m(13.48), m(0), m(22))
    j047 = Point(m(-1.41), m(0), m(20))
    j048 = Point(m(1.4), m(0), m(20))
    j049 = Point(m(-1.48), m(0), m(18.01))
    j050 = Point(m(1.48), m(0), m(18.01))
    j051 = Point(m(-1.56), m(0), m(16))
    j052 = Point(m(1.56), m(0), m(16))
    j053 = Point(m(-9.95), m(0), m(14.09))
    j054 = Point(m(9.95), m(0), m(14.09))
    j055 = Point(m(-1.64), m(0), m(14))
    j056 = Point(m(1.64), m(0), m(14))
    j057 = Point(m(-7.2), m(0), m(13.49))
    j058 = Point(m(7.2), m(0), m(13.49))
    j059 = Point(m(-12.7), m(0), m(13.31))
    j060 = Point(m(12.7), m(0), m(13.31))
    j061 = Point(m(-15.6), m(0), m(12.5))
    j062 = Point(m(15.6), m(0), m(12.5))
    j063 = Point(m(-15.6), m(0), m(12))
    j064 = Point(m(-14.12), m(0), m(12))
    j065 = Point(m(-12.7), m(0), m(12))
    j066 = Point(m(-10.28), m(0), m(12))
    j067 = Point(m(-9.62), m(0), m(12))
    j068 = Point(m(-7.2), m(0), m(12))
    j069 = Point(m(-2.92), m(0), m(12))
    j070 = Point(m(-1.72), m(0), m(12))
    j071 = Point(m(1.72), m(0), m(12))
    j072 = Point(m(2.92), m(0), m(12))
    j073 = Point(m(7.2), m(0), m(12))
    j074 = Point(m(9.62), m(0), m(12))
    j075 = Point(m(10.27), m(0), m(12))
    j076 = Point(m(12.7), m(0), m(12))
    j077 = Point(m(14.12), m(0), m(12))
    j078 = Point(m(15.6), m(0), m(12))
    j079 = Point(m(-9.95), m(0), m(11.55))
    j080 = Point(m(9.95), m(0), m(11.55))
    j081 = Point(m(-1.84), m(0), m(9.12))
    j082 = Point(m(1.84), m(0), m(9.12))
    j083 = Point(m(-1.96), m(0), m(6.4))
    j084 = Point(m(1.96), m(0), m(6.4))
    j085 = Point(m(-2.07), m(0), m(3.75))
    j086 = Point(m(2.07), m(0), m(3.75))
    j087 = Point(m(-5.7), m(0), m(2.82))
    j088 = Point(m(5.7), m(0), m(2.82))
    j089 = Point(m(-3.88), m(0), m(1.88))
    j090 = Point(m(3.88), m(0), m(1.88))
    j091 = Point(m(-10), m(0), m(1.7))
    j092 = Point(m(10), m(0), m(1.7))
    j093 = Point(m(-7.85), m(0), m(1.41))
    j094 = Point(m(7.86), m(0), m(1.41))
    j095 = Point(m(-2.18), m(0), m(1.23))
    j096 = Point(m(2.18), m(0), m(1.23))
    j097 = Point(m(-12.17), m(0), m(1.12))
    j098 = Point(m(12.17), m(0), m(1.12))
    j099 = Point(m(-14.43), m(0), m(0.53))
    j100 = Point(m(14.43), m(0), m(0.53))
    j101 = Point(m(-14.43), m(0), m(0))
    j102 = Point(m(-14.3), m(0), m(0))
    j103 = Point(m(-12.17), m(0), m(0))
    j104 = Point(m(-10), m(0), m(0))
    j105 = Point(m(-5.7), m(0), m(0))
    j106 = Point(m(-2.23), m(0), m(0))
    j107 = Point(m(2.23), m(0), m(0))
    j108 = Point(m(5.7), m(0), m(0))
    j109 = Point(m(10), m(0), m(0))
    j110 = Point(m(12.17), m(0), m(0))
    j111 = Point(m(14.3), m(0), m(0))
    j112 = Point(m(14.43), m(0), m(0))
    j113 = Point(m(0), m(0), m(0))
    j114 = Point(m(-2.29), m(0), m(-1.3))
    j115 = Point(m(2.29), m(0), m(-1.3))
    j116 = Point(m(-2.36), m(0), m(-2.27))
    j117 = Point(m(-1.15), m(0), m(-2.27))
    j118 = Point(m(1.15), m(0), m(-2.27))
    j119 = Point(m(2.36), m(0), m(-2.27))
    j120 = Point(m(-2.51), m(0), m(-4.32))
    j121 = Point(m(-0.01), m(0), m(-4.32))
    j122 = Point(m(2.51), m(0), m(-4.32))
    j123 = Point(m(-2.7), m(0), m(-6.86))
    j124 = Point(m(-1.43), m(0), m(-6.86))
    j125 = Point(m(1.43), m(0), m(-6.86))
    j126 = Point(m(2.7), m(0), m(-6.86))
    j127 = Point(m(-2.86), m(0), m(-9.4))
    j128 = Point(m(2.86), m(0), m(-9.4))
    j129 = Point(m(-3.14), m(0), m(-12.79))
    j130 = Point(m(-1.43), m(0), m(-12.79))
    j131 = Point(m(1.43), m(0), m(-12.79))
    j132 = Point(m(3.14), m(0), m(-12.79))
    j133 = Point(m(-3.38), m(0), m(-16.08))
    j134 = Point(m(3.38), m(0), m(-16.08))
    j135 = Point(m(-3.61), m(0), m(-19.2))
    j136 = Point(m(-1.26), m(0), m(-19.2))
    j137 = Point(m(1.26), m(0), m(-19.2))
    j138 = Point(m(3.61), m(0), m(-19.2))
    j139 = Point(m(-3.8), m(0), m(-21.83))
    j140 = Point(m(-2.36), m(0), m(-21.83))
    j141 = Point(m(2.36), m(0), m(-21.83))
    j142 = Point(m(3.8), m(0), m(-21.83))
    j143 = Point(m(-4.11), m(0), m(-26))
    j144 = Point(m(4.11), m(0), m(-26))
    return Tower(
        name="DA-4-DE-2018.1 T1",
        datum=LowestCrossarm((m(26), m(29), m(32), m(35), m(38), m(41))),
        voltages=(kv(380),),
        line_angles=(),
        attachments=(
            Mount(Wire.SHIELD, Point(m(-6.5), m(0), m(29.5)), Hold.CLAMP),
            Mount(Wire.SHIELD, Point(m(6.5), m(0), m(29.5)), Hold.CLAMP),
            WirePosition(
                Wire.PHASE,
                Point(m(-9.95), m(0), m(18.55)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j033),
                    InsulatorString(mount=j037),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(9.95), m(0), m(18.55)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j042),
                    InsulatorString(mount=j046),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(-12.7), m(0), m(8.17)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j063),
                    InsulatorString(mount=j079),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(-7.2), m(0), m(8.17)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j079),
                    InsulatorString(mount=j069),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(7.2), m(0), m(8.17)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j080),
                    InsulatorString(mount=j072),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(12.7), m(0), m(8.17)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j078),
                    InsulatorString(mount=j080),
                ),
            ),
            Mount(Wire.SHIELD, Point(m(0), m(0), m(0)), Hold.CLAMP),
            WirePosition(
                Wire.PHASE,
                Point(m(-14.3), m(0), m(-2.15)),
                Hold.SUSPENSION,
                strings=(InsulatorString(mount=j102),),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(-10), m(0), m(-2.15)),
                Hold.SUSPENSION,
                strings=(InsulatorString(mount=j104),),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(-5.7), m(0), m(-2.15)),
                Hold.SUSPENSION,
                strings=(InsulatorString(mount=j105),),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(5.7), m(0), m(-2.15)),
                Hold.SUSPENSION,
                strings=(InsulatorString(mount=j108),),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(10), m(0), m(-2.15)),
                Hold.SUSPENSION,
                strings=(InsulatorString(mount=j109),),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(14.3), m(0), m(-2.15)),
                Hold.SUSPENSION,
                strings=(InsulatorString(mount=j111),),
            ),
        ),
        bases=(),
        body=(
            Body(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j136, j131, role=Role.DIAGONAL_BRACE),
                        Bar(j137, j130, role=Role.DIAGONAL_BRACE),
                        Bar(j134, j133, role=Role.TRANSVERSE_BRACE),
                        Bar(j020, j021, role=Role.TRANSVERSE_BRACE),
                        Bar(j021, j022, role=Role.TRANSVERSE_BRACE),
                        Bar(j051, j052, role=Role.TRANSVERSE_BRACE),
                        Bar(j071, j081, role=Role.DIAGONAL_BRACE),
                        Bar(j081, j084, role=Role.DIAGONAL_BRACE),
                        Bar(j084, j085, role=Role.DIAGONAL_BRACE),
                        Bar(j086, j083, role=Role.DIAGONAL_BRACE),
                        Bar(j083, j082, role=Role.DIAGONAL_BRACE),
                        Bar(j082, j070, role=Role.DIAGONAL_BRACE),
                        Bar(j115, j113, role=Role.DIAGONAL_BRACE),
                        Bar(j113, j095, role=Role.DIAGONAL_BRACE),
                        Bar(j114, j113, role=Role.DIAGONAL_BRACE),
                        Bar(j113, j096, role=Role.DIAGONAL_BRACE),
                        Bar(j096, j085, role=Role.DIAGONAL_BRACE),
                        Bar(j095, j086, role=Role.DIAGONAL_BRACE),
                        Bar(j125, j121, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j118, role=Role.DIAGONAL_BRACE),
                        Bar(j122, j121, role=Role.TRANSVERSE_BRACE),
                        Bar(j114, j106, role=Role.CHORD),
                        Bar(j106, j095, role=Role.CHORD),
                        Bar(j095, j085, role=Role.CHORD),
                        Bar(j085, j083, role=Role.CHORD),
                        Bar(j083, j081, role=Role.CHORD),
                        Bar(j081, j070, role=Role.CHORD),
                        Bar(j070, j055, role=Role.CHORD),
                        Bar(j055, j051, role=Role.CHORD),
                        Bar(j052, j055, role=Role.DIAGONAL_BRACE),
                        Bar(j055, j071, role=Role.DIAGONAL_BRACE),
                        Bar(j071, j082, role=Role.CHORD),
                        Bar(j082, j084, role=Role.CHORD),
                        Bar(j084, j086, role=Role.CHORD),
                        Bar(j086, j096, role=Role.CHORD),
                        Bar(j096, j107, role=Role.CHORD),
                        Bar(j107, j115, role=Role.CHORD),
                        Bar(j051, j056, role=Role.DIAGONAL_BRACE),
                        Bar(j056, j070, role=Role.DIAGONAL_BRACE),
                        Bar(j051, j049, role=Role.CHORD),
                        Bar(j049, j047, role=Role.CHORD),
                        Bar(j047, j039, role=Role.CHORD),
                        Bar(j039, j027, role=Role.CHORD),
                        Bar(j027, j020, role=Role.CHORD),
                        Bar(j040, j027, role=Role.DIAGONAL_BRACE),
                        Bar(j027, j022, role=Role.DIAGONAL_BRACE),
                        Bar(j022, j028, role=Role.CHORD),
                        Bar(j028, j040, role=Role.CHORD),
                        Bar(j040, j048, role=Role.CHORD),
                        Bar(j048, j050, role=Role.CHORD),
                        Bar(j050, j052, role=Role.CHORD),
                        Bar(j052, j056, role=Role.CHORD),
                        Bar(j056, j071, role=Role.CHORD),
                        Bar(j039, j028, role=Role.DIAGONAL_BRACE),
                        Bar(j028, j020, role=Role.DIAGONAL_BRACE),
                        Bar(j039, j048, role=Role.DIAGONAL_BRACE),
                        Bar(j048, j049, role=Role.DIAGONAL_BRACE),
                        Bar(j049, j052, role=Role.DIAGONAL_BRACE),
                        Bar(j051, j050, role=Role.DIAGONAL_BRACE),
                        Bar(j050, j047, role=Role.DIAGONAL_BRACE),
                        Bar(j047, j040, role=Role.DIAGONAL_BRACE),
                        Bar(j106, j113, role=Role.TRANSVERSE_BRACE),
                        Bar(j113, j107, role=Role.TRANSVERSE_BRACE),
                        Bar(j085, j086, role=Role.TRANSVERSE_BRACE),
                        Bar(j071, j070, role=Role.TRANSVERSE_BRACE),
                        Bar(j040, j039, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        legs=(
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j143, j139, role=Role.CHORD),
                        Bar(j139, j135, role=Role.CHORD),
                        Bar(j135, j133, role=Role.CHORD),
                        Bar(j133, j129, role=Role.CHORD),
                        Bar(j129, j123, role=Role.CHORD),
                        Bar(j123, j120, role=Role.CHORD),
                        Bar(j120, j116, role=Role.CHORD),
                        Bar(j116, j114, role=Role.CHORD),
                        Bar(j143, j140, role=Role.DIAGONAL_BRACE),
                        Bar(j140, j136, role=Role.DIAGONAL_BRACE),
                        Bar(j130, j127, role=Role.DIAGONAL_BRACE),
                        Bar(j136, j135, role=Role.TRANSVERSE_BRACE),
                        Bar(j140, j139, role=Role.TRANSVERSE_BRACE),
                        Bar(j130, j129, role=Role.TRANSVERSE_BRACE),
                        Bar(j140, j135, role=Role.DIAGONAL_BRACE),
                        Bar(j136, j133, role=Role.DIAGONAL_BRACE),
                        Bar(j133, j130, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j117, role=Role.DIAGONAL_BRACE),
                        Bar(j117, j114, role=Role.DIAGONAL_BRACE),
                        Bar(j127, j124, role=Role.DIAGONAL_BRACE),
                        Bar(j124, j121, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j120, role=Role.TRANSVERSE_BRACE),
                        Bar(j120, j117, role=Role.DIAGONAL_BRACE),
                        Bar(j120, j124, role=Role.DIAGONAL_BRACE),
                        Bar(j123, j124, role=Role.TRANSVERSE_BRACE),
                        Bar(j116, j117, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j115, j119, role=Role.CHORD),
                        Bar(j119, j122, role=Role.CHORD),
                        Bar(j122, j126, role=Role.CHORD),
                        Bar(j126, j132, role=Role.CHORD),
                        Bar(j132, j134, role=Role.CHORD),
                        Bar(j134, j138, role=Role.CHORD),
                        Bar(j138, j142, role=Role.CHORD),
                        Bar(j142, j144, role=Role.CHORD),
                        Bar(j131, j128, role=Role.DIAGONAL_BRACE),
                        Bar(j144, j141, role=Role.DIAGONAL_BRACE),
                        Bar(j141, j137, role=Role.DIAGONAL_BRACE),
                        Bar(j137, j138, role=Role.TRANSVERSE_BRACE),
                        Bar(j141, j142, role=Role.TRANSVERSE_BRACE),
                        Bar(j131, j132, role=Role.TRANSVERSE_BRACE),
                        Bar(j141, j138, role=Role.DIAGONAL_BRACE),
                        Bar(j137, j134, role=Role.DIAGONAL_BRACE),
                        Bar(j134, j131, role=Role.DIAGONAL_BRACE),
                        Bar(j128, j125, role=Role.DIAGONAL_BRACE),
                        Bar(j118, j115, role=Role.DIAGONAL_BRACE),
                        Bar(j118, j122, role=Role.DIAGONAL_BRACE),
                        Bar(j122, j125, role=Role.DIAGONAL_BRACE),
                        Bar(j118, j119, role=Role.TRANSVERSE_BRACE),
                        Bar(j125, j126, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        head=(
            Head(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j021, j017, role=Role.TRANSVERSE_BRACE),
                        Bar(j017, j020, role=Role.CHORD),
                        Bar(j017, j022, role=Role.CHORD),
                    ),
                )
            ),
        ),
        crossarms=(
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j039, j038, role=Role.CHORD),
                        Bar(j038, j037, role=Role.CHORD),
                        Bar(j037, j036, role=Role.CHORD),
                        Bar(j036, j035, role=Role.CHORD),
                        Bar(j035, j034, role=Role.CHORD),
                        Bar(j034, j033, role=Role.CHORD),
                        Bar(j020, j023, role=Role.CHORD),
                        Bar(j023, j029, role=Role.CHORD),
                        Bar(j029, j031, role=Role.CHORD),
                        Bar(j031, j033, role=Role.CHORD),
                        Bar(j020, j025, role=Role.DIAGONAL_BRACE),
                        Bar(j025, j037, role=Role.DIAGONAL_BRACE),
                        Bar(j037, j023, role=Role.TRANSVERSE_BRACE),
                        Bar(j039, j025, role=Role.DIAGONAL_BRACE),
                        Bar(j025, j038, role=Role.TRANSVERSE_BRACE),
                        Bar(j035, j029, role=Role.TRANSVERSE_BRACE),
                        Bar(j023, j036, role=Role.DIAGONAL_BRACE),
                        Bar(j036, j029, role=Role.DIAGONAL_BRACE),
                        Bar(j029, j034, role=Role.DIAGONAL_BRACE),
                        Bar(j034, j031, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j046, j045, role=Role.CHORD),
                        Bar(j045, j044, role=Role.CHORD),
                        Bar(j044, j043, role=Role.CHORD),
                        Bar(j043, j042, role=Role.CHORD),
                        Bar(j042, j041, role=Role.CHORD),
                        Bar(j041, j040, role=Role.CHORD),
                        Bar(j022, j024, role=Role.CHORD),
                        Bar(j024, j030, role=Role.CHORD),
                        Bar(j030, j032, role=Role.CHORD),
                        Bar(j032, j046, role=Role.CHORD),
                        Bar(j022, j026, role=Role.DIAGONAL_BRACE),
                        Bar(j026, j042, role=Role.DIAGONAL_BRACE),
                        Bar(j042, j024, role=Role.TRANSVERSE_BRACE),
                        Bar(j040, j026, role=Role.DIAGONAL_BRACE),
                        Bar(j026, j041, role=Role.TRANSVERSE_BRACE),
                        Bar(j044, j030, role=Role.TRANSVERSE_BRACE),
                        Bar(j024, j043, role=Role.DIAGONAL_BRACE),
                        Bar(j043, j030, role=Role.DIAGONAL_BRACE),
                        Bar(j030, j045, role=Role.DIAGONAL_BRACE),
                        Bar(j045, j032, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j070, j069, role=Role.TRANSVERSE_BRACE),
                        Bar(j069, j068, role=Role.TRANSVERSE_BRACE),
                        Bar(j068, j067, role=Role.TRANSVERSE_BRACE),
                        Bar(j067, j066, role=Role.TRANSVERSE_BRACE),
                        Bar(j066, j065, role=Role.TRANSVERSE_BRACE),
                        Bar(j065, j064, role=Role.TRANSVERSE_BRACE),
                        Bar(j064, j063, role=Role.TRANSVERSE_BRACE),
                        Bar(j051, j059, role=Role.CHORD),
                        Bar(j059, j061, role=Role.CHORD),
                        Bar(j061, j063, role=Role.CHORD),
                        Bar(j079, j066, role=Role.DIAGONAL_BRACE),
                        Bar(j066, j053, role=Role.DIAGONAL_BRACE),
                        Bar(j053, j067, role=Role.DIAGONAL_BRACE),
                        Bar(j067, j079, role=Role.DIAGONAL_BRACE),
                        Bar(j065, j059, role=Role.TRANSVERSE_BRACE),
                        Bar(j068, j057, role=Role.TRANSVERSE_BRACE),
                        Bar(j057, j069, role=Role.DIAGONAL_BRACE),
                        Bar(j069, j051, role=Role.DIAGONAL_BRACE),
                        Bar(j051, j067, role=Role.DIAGONAL_BRACE),
                        Bar(j066, j059, role=Role.DIAGONAL_BRACE),
                        Bar(j059, j064, role=Role.DIAGONAL_BRACE),
                        Bar(j064, j061, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j078, j077, role=Role.TRANSVERSE_BRACE),
                        Bar(j077, j076, role=Role.TRANSVERSE_BRACE),
                        Bar(j076, j075, role=Role.TRANSVERSE_BRACE),
                        Bar(j075, j074, role=Role.TRANSVERSE_BRACE),
                        Bar(j074, j073, role=Role.TRANSVERSE_BRACE),
                        Bar(j073, j072, role=Role.TRANSVERSE_BRACE),
                        Bar(j072, j071, role=Role.TRANSVERSE_BRACE),
                        Bar(j062, j078, role=Role.CHORD),
                        Bar(j080, j075, role=Role.DIAGONAL_BRACE),
                        Bar(j075, j054, role=Role.DIAGONAL_BRACE),
                        Bar(j054, j074, role=Role.DIAGONAL_BRACE),
                        Bar(j074, j080, role=Role.DIAGONAL_BRACE),
                        Bar(j076, j060, role=Role.TRANSVERSE_BRACE),
                        Bar(j073, j058, role=Role.TRANSVERSE_BRACE),
                        Bar(j075, j060, role=Role.DIAGONAL_BRACE),
                        Bar(j060, j077, role=Role.DIAGONAL_BRACE),
                        Bar(j077, j062, role=Role.DIAGONAL_BRACE),
                        Bar(j062, j060, role=Role.CHORD),
                        Bar(j060, j052, role=Role.CHORD),
                        Bar(j052, j074, role=Role.DIAGONAL_BRACE),
                        Bar(j058, j072, role=Role.DIAGONAL_BRACE),
                        Bar(j072, j052, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j085, j087, role=Role.CHORD),
                        Bar(j087, j091, role=Role.CHORD),
                        Bar(j091, j097, role=Role.CHORD),
                        Bar(j097, j099, role=Role.CHORD),
                        Bar(j099, j101, role=Role.CHORD),
                        Bar(j101, j102, role=Role.CHORD),
                        Bar(j102, j103, role=Role.CHORD),
                        Bar(j103, j104, role=Role.CHORD),
                        Bar(j104, j105, role=Role.CHORD),
                        Bar(j105, j106, role=Role.CHORD),
                        Bar(j087, j093, role=Role.DIAGONAL_BRACE),
                        Bar(j093, j104, role=Role.DIAGONAL_BRACE),
                        Bar(j104, j097, role=Role.DIAGONAL_BRACE),
                        Bar(j105, j089, role=Role.DIAGONAL_BRACE),
                        Bar(j089, j085, role=Role.DIAGONAL_BRACE),
                        Bar(j089, j106, role=Role.DIAGONAL_BRACE),
                        Bar(j097, j103, role=Role.TRANSVERSE_BRACE),
                        Bar(j087, j105, role=Role.TRANSVERSE_BRACE),
                        Bar(j091, j104, role=Role.TRANSVERSE_BRACE),
                        Bar(j105, j093, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j107, j108, role=Role.CHORD),
                        Bar(j108, j109, role=Role.CHORD),
                        Bar(j109, j110, role=Role.CHORD),
                        Bar(j110, j111, role=Role.CHORD),
                        Bar(j111, j112, role=Role.CHORD),
                        Bar(j112, j100, role=Role.CHORD),
                        Bar(j100, j098, role=Role.CHORD),
                        Bar(j098, j092, role=Role.CHORD),
                        Bar(j092, j088, role=Role.CHORD),
                        Bar(j088, j086, role=Role.CHORD),
                        Bar(j088, j094, role=Role.DIAGONAL_BRACE),
                        Bar(j094, j109, role=Role.DIAGONAL_BRACE),
                        Bar(j109, j098, role=Role.DIAGONAL_BRACE),
                        Bar(j108, j090, role=Role.DIAGONAL_BRACE),
                        Bar(j090, j086, role=Role.DIAGONAL_BRACE),
                        Bar(j090, j107, role=Role.DIAGONAL_BRACE),
                        Bar(j098, j110, role=Role.TRANSVERSE_BRACE),
                        Bar(j088, j108, role=Role.TRANSVERSE_BRACE),
                        Bar(j092, j109, role=Role.TRANSVERSE_BRACE),
                        Bar(j108, j094, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        peaks=(
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j003, j005, role=Role.DIAGONAL_BRACE),
                        Bar(j005, j006, role=Role.TRANSVERSE_BRACE),
                        Bar(j006, j011, role=Role.DIAGONAL_BRACE),
                        Bar(j011, j009, role=Role.DIAGONAL_BRACE),
                        Bar(j009, j015, role=Role.TRANSVERSE_BRACE),
                        Bar(j015, j013, role=Role.DIAGONAL_BRACE),
                        Bar(j013, j018, role=Role.DIAGONAL_BRACE),
                        Bar(j018, j017, role=Role.DIAGONAL_BRACE),
                        Bar(j017, j013, role=Role.CHORD),
                        Bar(j013, j009, role=Role.CHORD),
                        Bar(j009, j006, role=Role.CHORD),
                        Bar(j006, j003, role=Role.CHORD),
                        Bar(j003, j001, role=Role.CHORD),
                        Bar(j001, j005, role=Role.CHORD),
                        Bar(j005, j011, role=Role.CHORD),
                        Bar(j011, j015, role=Role.CHORD),
                        Bar(j015, j018, role=Role.CHORD),
                        Bar(j018, j020, role=Role.CHORD),
                    ),
                )
            ),
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j004, j008, role=Role.DIAGONAL_BRACE),
                        Bar(j008, j007, role=Role.TRANSVERSE_BRACE),
                        Bar(j007, j012, role=Role.DIAGONAL_BRACE),
                        Bar(j012, j010, role=Role.DIAGONAL_BRACE),
                        Bar(j010, j016, role=Role.TRANSVERSE_BRACE),
                        Bar(j016, j014, role=Role.DIAGONAL_BRACE),
                        Bar(j014, j019, role=Role.DIAGONAL_BRACE),
                        Bar(j019, j017, role=Role.DIAGONAL_BRACE),
                        Bar(j022, j019, role=Role.CHORD),
                        Bar(j019, j016, role=Role.CHORD),
                        Bar(j016, j012, role=Role.CHORD),
                        Bar(j012, j008, role=Role.CHORD),
                        Bar(j008, j002, role=Role.CHORD),
                        Bar(j002, j004, role=Role.CHORD),
                        Bar(j004, j007, role=Role.CHORD),
                        Bar(j007, j010, role=Role.CHORD),
                        Bar(j010, j014, role=Role.CHORD),
                        Bar(j014, j017, role=Role.CHORD),
                    ),
                )
            ),
        ),
    )


DA_4_DE_2018_1_T1 = _da_4_de_2018_1_t1()


def _da_4_de_2018_1_t2() -> Tower[LowestCrossarm]:
    """DA-4-DE-2018.1 T2: each joint written once, by its key."""
    j001 = Point(m(-6.5), m(0), m(29.5))
    j002 = Point(m(6.5), m(0), m(29.5))
    j003 = Point(m(-6.35), m(0), m(29.43))
    j004 = Point(m(6.35), m(0), m(29.43))
    j005 = Point(m(-6.11), m(0), m(28.97))
    j006 = Point(m(-5.32), m(0), m(28.97))
    j007 = Point(m(5.33), m(0), m(28.97))
    j008 = Point(m(6.1), m(0), m(28.97))
    j009 = Point(m(-3.94), m(0), m(28.42))
    j010 = Point(m(3.94), m(0), m(28.42))
    j011 = Point(m(-5.4), m(0), m(28.2))
    j012 = Point(m(5.4), m(0), m(28.2))
    j013 = Point(m(-2.21), m(0), m(27.8))
    j014 = Point(m(2.22), m(0), m(27.8))
    j015 = Point(m(-4.24), m(0), m(27.13))
    j016 = Point(m(4.23), m(0), m(27.13))
    j017 = Point(m(0), m(0), m(27.02))
    j018 = Point(m(-2.56), m(0), m(25.89))
    j019 = Point(m(2.57), m(0), m(25.89))
    j020 = Point(m(-1.2), m(0), m(25.03))
    j021 = Point(m(0), m(0), m(25.03))
    j022 = Point(m(1.2), m(0), m(25.03))
    j023 = Point(m(-6.66), m(0), m(23.94))
    j024 = Point(m(6.66), m(0), m(23.94))
    j025 = Point(m(-3.83), m(0), m(23.57))
    j026 = Point(m(3.82), m(0), m(23.57))
    j027 = Point(m(-1.26), m(0), m(23.51))
    j028 = Point(m(1.26), m(0), m(23.51))
    j029 = Point(m(-10.35), m(0), m(23.22))
    j030 = Point(m(10.35), m(0), m(23.22))
    j031 = Point(m(-14.05), m(0), m(22.5))
    j032 = Point(m(14.04), m(0), m(22.5))
    j033 = Point(m(-14.05), m(0), m(22))
    j034 = Point(m(-12.2), m(0), m(22))
    j035 = Point(m(-10.35), m(0), m(22))
    j036 = Point(m(-8.5), m(0), m(22))
    j037 = Point(m(-6.65), m(0), m(22))
    j038 = Point(m(-3.81), m(0), m(22))
    j039 = Point(m(-1.32), m(0), m(22))
    j040 = Point(m(1.32), m(0), m(22))
    j041 = Point(m(3.81), m(0), m(22))
    j042 = Point(m(6.65), m(0), m(22))
    j043 = Point(m(8.5), m(0), m(22))
    j044 = Point(m(10.35), m(0), m(22))
    j045 = Point(m(12.2), m(0), m(22))
    j046 = Point(m(14.05), m(0), m(22))
    j047 = Point(m(-1.4), m(0), m(20.01))
    j048 = Point(m(1.4), m(0), m(20.01))
    j049 = Point(m(-1.47), m(0), m(18))
    j050 = Point(m(1.48), m(0), m(18))
    j051 = Point(m(-1.55), m(0), m(16))
    j052 = Point(m(1.56), m(0), m(16))
    j053 = Point(m(-10.35), m(0), m(14.09))
    j054 = Point(m(10.36), m(0), m(14.09))
    j055 = Point(m(-1.63), m(0), m(13.99))
    j056 = Point(m(1.64), m(0), m(13.99))
    j057 = Point(m(-7.2), m(0), m(13.49))
    j058 = Point(m(7.2), m(0), m(13.49))
    j059 = Point(m(-13.5), m(0), m(13.32))
    j060 = Point(m(13.5), m(0), m(13.32))
    j061 = Point(m(-16.82), m(0), m(12.5))
    j062 = Point(m(16.84), m(0), m(12.5))
    j063 = Point(m(-16.82), m(0), m(12))
    j064 = Point(m(-15.13), m(0), m(12))
    j065 = Point(m(-13.5), m(0), m(12))
    j066 = Point(m(-10.73), m(0), m(12))
    j067 = Point(m(-9.97), m(0), m(12))
    j068 = Point(m(-7.2), m(0), m(12))
    j069 = Point(m(-2.91), m(0), m(12))
    j070 = Point(m(-1.71), m(0), m(12))
    j071 = Point(m(1.72), m(0), m(12))
    j072 = Point(m(2.92), m(0), m(12))
    j073 = Point(m(7.2), m(0), m(12))
    j074 = Point(m(9.97), m(0), m(12))
    j075 = Point(m(10.73), m(0), m(12))
    j076 = Point(m(13.5), m(0), m(12))
    j077 = Point(m(15.14), m(0), m(12))
    j078 = Point(m(16.84), m(0), m(12))
    j079 = Point(m(-10.35), m(0), m(11.54))
    j080 = Point(m(10.36), m(0), m(11.54))
    j081 = Point(m(-1.84), m(0), m(9.11))
    j082 = Point(m(1.84), m(0), m(9.11))
    j083 = Point(m(-1.95), m(0), m(6.39))
    j084 = Point(m(1.96), m(0), m(6.39))
    j085 = Point(m(-2.07), m(0), m(3.75))
    j086 = Point(m(2.07), m(0), m(3.75))
    j087 = Point(m(-5.7), m(0), m(2.82))
    j088 = Point(m(5.7), m(0), m(2.82))
    j089 = Point(m(-3.88), m(0), m(1.87))
    j090 = Point(m(3.88), m(0), m(1.87))
    j091 = Point(m(-10.8), m(0), m(1.69))
    j092 = Point(m(10.8), m(0), m(1.69))
    j093 = Point(m(-8.25), m(0), m(1.41))
    j094 = Point(m(8.26), m(0), m(1.41))
    j095 = Point(m(-2.18), m(0), m(1.23))
    j096 = Point(m(2.18), m(0), m(1.23))
    j097 = Point(m(-13.37), m(0), m(1.12))
    j098 = Point(m(13.38), m(0), m(1.12))
    j099 = Point(m(-16.06), m(0), m(0.53))
    j100 = Point(m(16.05), m(0), m(0.53))
    j101 = Point(m(-16.06), m(0), m(0))
    j102 = Point(m(-15.9), m(0), m(0))
    j103 = Point(m(-13.37), m(0), m(0))
    j104 = Point(m(-10.8), m(0), m(0))
    j105 = Point(m(-5.7), m(0), m(0))
    j106 = Point(m(-2.23), m(0), m(0))
    j107 = Point(m(0), m(0), m(0))
    j108 = Point(m(2.23), m(0), m(0))
    j109 = Point(m(5.7), m(0), m(0))
    j110 = Point(m(10.8), m(0), m(0))
    j111 = Point(m(13.38), m(0), m(0))
    j112 = Point(m(15.9), m(0), m(0))
    j113 = Point(m(16.05), m(0), m(0))
    j114 = Point(m(-2.29), m(0), m(-1.3))
    j115 = Point(m(2.29), m(0), m(-1.3))
    j116 = Point(m(-2.35), m(0), m(-2.33))
    j117 = Point(m(-1.14), m(0), m(-2.33))
    j118 = Point(m(1.15), m(0), m(-2.33))
    j119 = Point(m(2.35), m(0), m(-2.33))
    j120 = Point(m(-2.5), m(0), m(-4.87))
    j121 = Point(m(0), m(0), m(-4.87))
    j122 = Point(m(2.5), m(0), m(-4.87))
    j123 = Point(m(-2.69), m(0), m(-8.05))
    j124 = Point(m(-1.42), m(0), m(-8.05))
    j125 = Point(m(1.43), m(0), m(-8.05))
    j126 = Point(m(2.69), m(0), m(-8.05))
    j127 = Point(m(-2.85), m(0), m(-11.23))
    j128 = Point(m(2.86), m(0), m(-11.23))
    j129 = Point(m(-3.13), m(0), m(-15.5))
    j130 = Point(m(-1.42), m(0), m(-15.5))
    j131 = Point(m(1.43), m(0), m(-15.5))
    j132 = Point(m(3.13), m(0), m(-15.5))
    j133 = Point(m(-3.37), m(0), m(-19.58))
    j134 = Point(m(3.37), m(0), m(-19.58))
    j135 = Point(m(-3.6), m(0), m(-23.49))
    j136 = Point(m(-1.25), m(0), m(-23.49))
    j137 = Point(m(1.26), m(0), m(-23.49))
    j138 = Point(m(3.61), m(0), m(-23.49))
    j139 = Point(m(-3.79), m(0), m(-26.77))
    j140 = Point(m(-2.35), m(0), m(-26.77))
    j141 = Point(m(2.36), m(0), m(-26.77))
    j142 = Point(m(3.8), m(0), m(-26.77))
    j143 = Point(m(-4.1), m(0), m(-32))
    j144 = Point(m(4.11), m(0), m(-32))
    return Tower(
        name="DA-4-DE-2018.1 T2",
        datum=LowestCrossarm((m(32),)),
        voltages=(kv(380),),
        line_angles=(),
        attachments=(
            Mount(Wire.SHIELD, Point(m(-6.5), m(0), m(29.5)), Hold.CLAMP),
            Mount(Wire.SHIELD, Point(m(6.5), m(0), m(29.5)), Hold.CLAMP),
            WirePosition(
                Wire.PHASE,
                Point(m(-10.35), m(0), m(18.54)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j033),
                    InsulatorString(mount=j037),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(10.35), m(0), m(18.54)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j042),
                    InsulatorString(mount=j046),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(-13.5), m(0), m(8.16)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j063),
                    InsulatorString(mount=j079),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(-7.2), m(0), m(8.16)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j079),
                    InsulatorString(mount=j069),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(7.2), m(0), m(8.16)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j080),
                    InsulatorString(mount=j072),
                ),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(13.5), m(0), m(8.16)),
                Hold.V_STRING,
                strings=(
                    InsulatorString(mount=j078),
                    InsulatorString(mount=j080),
                ),
            ),
            Mount(Wire.SHIELD, Point(m(0), m(0), m(0)), Hold.CLAMP),
            WirePosition(
                Wire.PHASE,
                Point(m(-15.9), m(0), m(-2.15)),
                Hold.SUSPENSION,
                strings=(InsulatorString(mount=j102),),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(-10.8), m(0), m(-2.15)),
                Hold.SUSPENSION,
                strings=(InsulatorString(mount=j104),),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(-5.7), m(0), m(-2.15)),
                Hold.SUSPENSION,
                strings=(InsulatorString(mount=j105),),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(5.7), m(0), m(-2.15)),
                Hold.SUSPENSION,
                strings=(InsulatorString(mount=j109),),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(10.8), m(0), m(-2.15)),
                Hold.SUSPENSION,
                strings=(InsulatorString(mount=j110),),
            ),
            WirePosition(
                Wire.PHASE,
                Point(m(15.9), m(0), m(-2.15)),
                Hold.SUSPENSION,
                strings=(InsulatorString(mount=j112),),
            ),
        ),
        bases=(),
        body=(
            Body(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j136, j131, role=Role.DIAGONAL_BRACE),
                        Bar(j137, j130, role=Role.DIAGONAL_BRACE),
                        Bar(j134, j133, role=Role.TRANSVERSE_BRACE),
                        Bar(j020, j021, role=Role.TRANSVERSE_BRACE),
                        Bar(j021, j022, role=Role.TRANSVERSE_BRACE),
                        Bar(j051, j052, role=Role.TRANSVERSE_BRACE),
                        Bar(j071, j081, role=Role.DIAGONAL_BRACE),
                        Bar(j081, j084, role=Role.DIAGONAL_BRACE),
                        Bar(j084, j085, role=Role.DIAGONAL_BRACE),
                        Bar(j086, j083, role=Role.DIAGONAL_BRACE),
                        Bar(j083, j082, role=Role.DIAGONAL_BRACE),
                        Bar(j082, j070, role=Role.DIAGONAL_BRACE),
                        Bar(j115, j107, role=Role.DIAGONAL_BRACE),
                        Bar(j107, j095, role=Role.DIAGONAL_BRACE),
                        Bar(j114, j107, role=Role.DIAGONAL_BRACE),
                        Bar(j107, j096, role=Role.DIAGONAL_BRACE),
                        Bar(j096, j085, role=Role.DIAGONAL_BRACE),
                        Bar(j095, j086, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j117, role=Role.DIAGONAL_BRACE),
                        Bar(j124, j121, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j120, role=Role.TRANSVERSE_BRACE),
                        Bar(j114, j106, role=Role.CHORD),
                        Bar(j106, j095, role=Role.CHORD),
                        Bar(j095, j085, role=Role.CHORD),
                        Bar(j085, j083, role=Role.CHORD),
                        Bar(j083, j081, role=Role.CHORD),
                        Bar(j081, j070, role=Role.CHORD),
                        Bar(j070, j055, role=Role.CHORD),
                        Bar(j055, j051, role=Role.CHORD),
                        Bar(j052, j055, role=Role.DIAGONAL_BRACE),
                        Bar(j055, j071, role=Role.DIAGONAL_BRACE),
                        Bar(j071, j082, role=Role.CHORD),
                        Bar(j082, j084, role=Role.CHORD),
                        Bar(j084, j086, role=Role.CHORD),
                        Bar(j086, j096, role=Role.CHORD),
                        Bar(j096, j108, role=Role.CHORD),
                        Bar(j108, j115, role=Role.CHORD),
                        Bar(j051, j056, role=Role.DIAGONAL_BRACE),
                        Bar(j056, j070, role=Role.DIAGONAL_BRACE),
                        Bar(j051, j049, role=Role.CHORD),
                        Bar(j049, j047, role=Role.CHORD),
                        Bar(j047, j039, role=Role.CHORD),
                        Bar(j039, j027, role=Role.CHORD),
                        Bar(j027, j020, role=Role.CHORD),
                        Bar(j040, j027, role=Role.DIAGONAL_BRACE),
                        Bar(j027, j022, role=Role.DIAGONAL_BRACE),
                        Bar(j022, j028, role=Role.CHORD),
                        Bar(j028, j040, role=Role.CHORD),
                        Bar(j040, j048, role=Role.CHORD),
                        Bar(j048, j050, role=Role.CHORD),
                        Bar(j050, j052, role=Role.CHORD),
                        Bar(j052, j056, role=Role.CHORD),
                        Bar(j056, j071, role=Role.CHORD),
                        Bar(j052, j049, role=Role.DIAGONAL_BRACE),
                        Bar(j049, j048, role=Role.DIAGONAL_BRACE),
                        Bar(j048, j039, role=Role.DIAGONAL_BRACE),
                        Bar(j039, j028, role=Role.DIAGONAL_BRACE),
                        Bar(j028, j020, role=Role.DIAGONAL_BRACE),
                        Bar(j051, j050, role=Role.DIAGONAL_BRACE),
                        Bar(j050, j047, role=Role.DIAGONAL_BRACE),
                        Bar(j047, j040, role=Role.DIAGONAL_BRACE),
                        Bar(j106, j107, role=Role.TRANSVERSE_BRACE),
                        Bar(j107, j108, role=Role.TRANSVERSE_BRACE),
                        Bar(j085, j086, role=Role.TRANSVERSE_BRACE),
                        Bar(j071, j070, role=Role.TRANSVERSE_BRACE),
                        Bar(j040, j039, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        legs=(
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j143, j139, role=Role.CHORD),
                        Bar(j139, j135, role=Role.CHORD),
                        Bar(j135, j133, role=Role.CHORD),
                        Bar(j133, j129, role=Role.CHORD),
                        Bar(j129, j123, role=Role.CHORD),
                        Bar(j123, j120, role=Role.CHORD),
                        Bar(j120, j116, role=Role.CHORD),
                        Bar(j116, j114, role=Role.CHORD),
                        Bar(j143, j140, role=Role.DIAGONAL_BRACE),
                        Bar(j140, j136, role=Role.DIAGONAL_BRACE),
                        Bar(j130, j127, role=Role.DIAGONAL_BRACE),
                        Bar(j136, j135, role=Role.TRANSVERSE_BRACE),
                        Bar(j140, j139, role=Role.TRANSVERSE_BRACE),
                        Bar(j130, j129, role=Role.TRANSVERSE_BRACE),
                        Bar(j140, j135, role=Role.DIAGONAL_BRACE),
                        Bar(j136, j133, role=Role.DIAGONAL_BRACE),
                        Bar(j133, j130, role=Role.DIAGONAL_BRACE),
                        Bar(j117, j114, role=Role.DIAGONAL_BRACE),
                        Bar(j127, j124, role=Role.DIAGONAL_BRACE),
                        Bar(j120, j117, role=Role.DIAGONAL_BRACE),
                        Bar(j120, j124, role=Role.DIAGONAL_BRACE),
                        Bar(j123, j124, role=Role.TRANSVERSE_BRACE),
                        Bar(j116, j117, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j115, j119, role=Role.CHORD),
                        Bar(j119, j122, role=Role.CHORD),
                        Bar(j122, j126, role=Role.CHORD),
                        Bar(j126, j132, role=Role.CHORD),
                        Bar(j132, j134, role=Role.CHORD),
                        Bar(j134, j138, role=Role.CHORD),
                        Bar(j138, j142, role=Role.CHORD),
                        Bar(j142, j144, role=Role.CHORD),
                        Bar(j131, j128, role=Role.DIAGONAL_BRACE),
                        Bar(j144, j141, role=Role.DIAGONAL_BRACE),
                        Bar(j141, j137, role=Role.DIAGONAL_BRACE),
                        Bar(j137, j138, role=Role.TRANSVERSE_BRACE),
                        Bar(j141, j142, role=Role.TRANSVERSE_BRACE),
                        Bar(j131, j132, role=Role.TRANSVERSE_BRACE),
                        Bar(j141, j138, role=Role.DIAGONAL_BRACE),
                        Bar(j137, j134, role=Role.DIAGONAL_BRACE),
                        Bar(j134, j131, role=Role.DIAGONAL_BRACE),
                        Bar(j128, j125, role=Role.DIAGONAL_BRACE),
                        Bar(j125, j121, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j118, role=Role.DIAGONAL_BRACE),
                        Bar(j118, j115, role=Role.DIAGONAL_BRACE),
                        Bar(j122, j121, role=Role.TRANSVERSE_BRACE),
                        Bar(j118, j122, role=Role.DIAGONAL_BRACE),
                        Bar(j122, j125, role=Role.DIAGONAL_BRACE),
                        Bar(j118, j119, role=Role.TRANSVERSE_BRACE),
                        Bar(j125, j126, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        head=(
            Head(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j021, j017, role=Role.TRANSVERSE_BRACE),
                        Bar(j017, j020, role=Role.CHORD),
                        Bar(j017, j022, role=Role.CHORD),
                    ),
                )
            ),
        ),
        crossarms=(
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j039, j038, role=Role.CHORD),
                        Bar(j038, j037, role=Role.CHORD),
                        Bar(j037, j036, role=Role.CHORD),
                        Bar(j036, j035, role=Role.CHORD),
                        Bar(j035, j034, role=Role.CHORD),
                        Bar(j034, j033, role=Role.CHORD),
                        Bar(j020, j023, role=Role.CHORD),
                        Bar(j023, j029, role=Role.CHORD),
                        Bar(j029, j031, role=Role.CHORD),
                        Bar(j031, j033, role=Role.CHORD),
                        Bar(j020, j025, role=Role.DIAGONAL_BRACE),
                        Bar(j025, j037, role=Role.DIAGONAL_BRACE),
                        Bar(j037, j023, role=Role.TRANSVERSE_BRACE),
                        Bar(j039, j025, role=Role.DIAGONAL_BRACE),
                        Bar(j025, j038, role=Role.TRANSVERSE_BRACE),
                        Bar(j035, j029, role=Role.TRANSVERSE_BRACE),
                        Bar(j023, j036, role=Role.DIAGONAL_BRACE),
                        Bar(j036, j029, role=Role.DIAGONAL_BRACE),
                        Bar(j029, j034, role=Role.DIAGONAL_BRACE),
                        Bar(j034, j031, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j046, j045, role=Role.CHORD),
                        Bar(j045, j044, role=Role.CHORD),
                        Bar(j044, j043, role=Role.CHORD),
                        Bar(j043, j042, role=Role.CHORD),
                        Bar(j042, j041, role=Role.CHORD),
                        Bar(j041, j040, role=Role.CHORD),
                        Bar(j022, j024, role=Role.CHORD),
                        Bar(j024, j030, role=Role.CHORD),
                        Bar(j030, j032, role=Role.CHORD),
                        Bar(j032, j046, role=Role.CHORD),
                        Bar(j022, j026, role=Role.DIAGONAL_BRACE),
                        Bar(j026, j042, role=Role.DIAGONAL_BRACE),
                        Bar(j042, j024, role=Role.TRANSVERSE_BRACE),
                        Bar(j040, j026, role=Role.DIAGONAL_BRACE),
                        Bar(j026, j041, role=Role.TRANSVERSE_BRACE),
                        Bar(j044, j030, role=Role.TRANSVERSE_BRACE),
                        Bar(j024, j043, role=Role.DIAGONAL_BRACE),
                        Bar(j043, j030, role=Role.DIAGONAL_BRACE),
                        Bar(j030, j045, role=Role.DIAGONAL_BRACE),
                        Bar(j045, j032, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j070, j069, role=Role.TRANSVERSE_BRACE),
                        Bar(j069, j068, role=Role.TRANSVERSE_BRACE),
                        Bar(j068, j067, role=Role.TRANSVERSE_BRACE),
                        Bar(j067, j066, role=Role.TRANSVERSE_BRACE),
                        Bar(j066, j065, role=Role.TRANSVERSE_BRACE),
                        Bar(j065, j064, role=Role.TRANSVERSE_BRACE),
                        Bar(j064, j063, role=Role.TRANSVERSE_BRACE),
                        Bar(j051, j053, role=Role.CHORD),
                        Bar(j053, j059, role=Role.CHORD),
                        Bar(j059, j061, role=Role.CHORD),
                        Bar(j061, j063, role=Role.CHORD),
                        Bar(j079, j066, role=Role.DIAGONAL_BRACE),
                        Bar(j066, j053, role=Role.DIAGONAL_BRACE),
                        Bar(j053, j067, role=Role.DIAGONAL_BRACE),
                        Bar(j067, j079, role=Role.DIAGONAL_BRACE),
                        Bar(j065, j059, role=Role.TRANSVERSE_BRACE),
                        Bar(j068, j057, role=Role.TRANSVERSE_BRACE),
                        Bar(j057, j069, role=Role.DIAGONAL_BRACE),
                        Bar(j069, j051, role=Role.DIAGONAL_BRACE),
                        Bar(j051, j067, role=Role.DIAGONAL_BRACE),
                        Bar(j066, j059, role=Role.DIAGONAL_BRACE),
                        Bar(j059, j064, role=Role.DIAGONAL_BRACE),
                        Bar(j064, j061, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j078, j077, role=Role.TRANSVERSE_BRACE),
                        Bar(j077, j076, role=Role.TRANSVERSE_BRACE),
                        Bar(j076, j075, role=Role.TRANSVERSE_BRACE),
                        Bar(j075, j074, role=Role.TRANSVERSE_BRACE),
                        Bar(j074, j073, role=Role.TRANSVERSE_BRACE),
                        Bar(j073, j072, role=Role.TRANSVERSE_BRACE),
                        Bar(j072, j071, role=Role.TRANSVERSE_BRACE),
                        Bar(j062, j078, role=Role.CHORD),
                        Bar(j080, j075, role=Role.DIAGONAL_BRACE),
                        Bar(j075, j054, role=Role.DIAGONAL_BRACE),
                        Bar(j054, j074, role=Role.DIAGONAL_BRACE),
                        Bar(j074, j080, role=Role.DIAGONAL_BRACE),
                        Bar(j076, j060, role=Role.TRANSVERSE_BRACE),
                        Bar(j073, j058, role=Role.TRANSVERSE_BRACE),
                        Bar(j075, j060, role=Role.DIAGONAL_BRACE),
                        Bar(j060, j077, role=Role.DIAGONAL_BRACE),
                        Bar(j077, j062, role=Role.DIAGONAL_BRACE),
                        Bar(j062, j060, role=Role.CHORD),
                        Bar(j060, j054, role=Role.CHORD),
                        Bar(j054, j052, role=Role.CHORD),
                        Bar(j052, j074, role=Role.DIAGONAL_BRACE),
                        Bar(j058, j072, role=Role.DIAGONAL_BRACE),
                        Bar(j072, j052, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j085, j087, role=Role.CHORD),
                        Bar(j087, j091, role=Role.CHORD),
                        Bar(j091, j097, role=Role.CHORD),
                        Bar(j097, j099, role=Role.CHORD),
                        Bar(j099, j101, role=Role.CHORD),
                        Bar(j101, j102, role=Role.CHORD),
                        Bar(j102, j103, role=Role.CHORD),
                        Bar(j103, j104, role=Role.CHORD),
                        Bar(j104, j105, role=Role.CHORD),
                        Bar(j105, j106, role=Role.CHORD),
                        Bar(j087, j093, role=Role.DIAGONAL_BRACE),
                        Bar(j093, j104, role=Role.DIAGONAL_BRACE),
                        Bar(j104, j097, role=Role.DIAGONAL_BRACE),
                        Bar(j105, j089, role=Role.DIAGONAL_BRACE),
                        Bar(j089, j085, role=Role.DIAGONAL_BRACE),
                        Bar(j089, j106, role=Role.DIAGONAL_BRACE),
                        Bar(j097, j103, role=Role.TRANSVERSE_BRACE),
                        Bar(j087, j105, role=Role.TRANSVERSE_BRACE),
                        Bar(j091, j104, role=Role.TRANSVERSE_BRACE),
                        Bar(j105, j093, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j108, j109, role=Role.CHORD),
                        Bar(j109, j110, role=Role.CHORD),
                        Bar(j110, j111, role=Role.CHORD),
                        Bar(j111, j112, role=Role.CHORD),
                        Bar(j112, j113, role=Role.CHORD),
                        Bar(j113, j100, role=Role.CHORD),
                        Bar(j100, j098, role=Role.CHORD),
                        Bar(j098, j092, role=Role.CHORD),
                        Bar(j092, j088, role=Role.CHORD),
                        Bar(j088, j086, role=Role.CHORD),
                        Bar(j088, j094, role=Role.DIAGONAL_BRACE),
                        Bar(j094, j110, role=Role.DIAGONAL_BRACE),
                        Bar(j110, j098, role=Role.DIAGONAL_BRACE),
                        Bar(j109, j090, role=Role.DIAGONAL_BRACE),
                        Bar(j090, j086, role=Role.DIAGONAL_BRACE),
                        Bar(j090, j108, role=Role.DIAGONAL_BRACE),
                        Bar(j098, j111, role=Role.TRANSVERSE_BRACE),
                        Bar(j088, j109, role=Role.TRANSVERSE_BRACE),
                        Bar(j092, j110, role=Role.TRANSVERSE_BRACE),
                        Bar(j109, j094, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        peaks=(
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j003, j005, role=Role.DIAGONAL_BRACE),
                        Bar(j005, j006, role=Role.TRANSVERSE_BRACE),
                        Bar(j006, j011, role=Role.DIAGONAL_BRACE),
                        Bar(j011, j009, role=Role.DIAGONAL_BRACE),
                        Bar(j009, j015, role=Role.TRANSVERSE_BRACE),
                        Bar(j015, j013, role=Role.DIAGONAL_BRACE),
                        Bar(j013, j018, role=Role.DIAGONAL_BRACE),
                        Bar(j018, j017, role=Role.DIAGONAL_BRACE),
                        Bar(j017, j013, role=Role.CHORD),
                        Bar(j013, j009, role=Role.CHORD),
                        Bar(j009, j006, role=Role.CHORD),
                        Bar(j006, j003, role=Role.CHORD),
                        Bar(j003, j001, role=Role.CHORD),
                        Bar(j001, j005, role=Role.CHORD),
                        Bar(j005, j011, role=Role.CHORD),
                        Bar(j011, j015, role=Role.CHORD),
                        Bar(j015, j018, role=Role.CHORD),
                        Bar(j018, j020, role=Role.CHORD),
                    ),
                )
            ),
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j004, j008, role=Role.DIAGONAL_BRACE),
                        Bar(j008, j007, role=Role.TRANSVERSE_BRACE),
                        Bar(j007, j012, role=Role.DIAGONAL_BRACE),
                        Bar(j012, j010, role=Role.DIAGONAL_BRACE),
                        Bar(j010, j016, role=Role.TRANSVERSE_BRACE),
                        Bar(j016, j014, role=Role.DIAGONAL_BRACE),
                        Bar(j014, j019, role=Role.DIAGONAL_BRACE),
                        Bar(j019, j017, role=Role.DIAGONAL_BRACE),
                        Bar(j022, j019, role=Role.CHORD),
                        Bar(j019, j016, role=Role.CHORD),
                        Bar(j016, j012, role=Role.CHORD),
                        Bar(j012, j008, role=Role.CHORD),
                        Bar(j008, j002, role=Role.CHORD),
                        Bar(j002, j004, role=Role.CHORD),
                        Bar(j004, j007, role=Role.CHORD),
                        Bar(j007, j010, role=Role.CHORD),
                        Bar(j010, j014, role=Role.CHORD),
                        Bar(j014, j017, role=Role.CHORD),
                    ),
                )
            ),
        ),
    )


DA_4_DE_2018_1_T2 = _da_4_de_2018_1_t2()


def _da_4_de_2018_1_wa120() -> Tower[LowestCrossarm]:
    """DA-4-DE-2018.1 WA120: each joint written once, by its key."""
    j001 = Point(m(-8.45), m(0), m(32.5))
    j002 = Point(m(8.45), m(0), m(32.5))
    j003 = Point(m(-8.35), m(0), m(32.4))
    j004 = Point(m(8.34), m(0), m(32.4))
    j005 = Point(m(-8.12), m(0), m(31.79))
    j006 = Point(m(8.12), m(0), m(31.79))
    j007 = Point(m(-7.37), m(0), m(31.54))
    j008 = Point(m(7.35), m(0), m(31.54))
    j009 = Point(m(-7.37), m(0), m(30.56))
    j010 = Point(m(-6.01), m(0), m(30.56))
    j011 = Point(m(6.01), m(0), m(30.56))
    j012 = Point(m(7.37), m(0), m(30.56))
    j013 = Point(m(-4.1), m(0), m(29.38))
    j014 = Point(m(4.1), m(0), m(29.38))
    j015 = Point(m(-6.15), m(0), m(29.01))
    j016 = Point(m(6.14), m(0), m(29.01))
    j017 = Point(m(-1.64), m(0), m(28.07))
    j018 = Point(m(1.64), m(0), m(28.07))
    j019 = Point(m(-0.01), m(0), m(27.28))
    j020 = Point(m(-4.28), m(0), m(27.22))
    j021 = Point(m(4.28), m(0), m(27.22))
    j022 = Point(m(-1.64), m(0), m(25.19))
    j023 = Point(m(1.64), m(0), m(25.19))
    j024 = Point(m(-6.91), m(0), m(24.09))
    j025 = Point(m(6.91), m(0), m(24.09))
    j026 = Point(m(-9.21), m(0), m(23.62))
    j027 = Point(m(9.21), m(0), m(23.62))
    j028 = Point(m(-1.72), m(0), m(23.59))
    j029 = Point(m(1.72), m(0), m(23.59))
    j030 = Point(m(-4.37), m(0), m(23.54))
    j031 = Point(m(4.37), m(0), m(23.54))
    j032 = Point(m(-13.04), m(0), m(22.83))
    j033 = Point(m(13.04), m(0), m(22.83))
    j034 = Point(m(-13.97), m(0), m(22.64))
    j035 = Point(m(13.95), m(0), m(22.64))
    j036 = Point(m(-11.61), m(0), m(22.02))
    j037 = Point(m(11.6), m(0), m(22.02))
    j038 = Point(m(-13.97), m(0), m(22))
    j039 = Point(m(-13.04), m(0), m(22))
    j040 = Point(m(-11.51), m(0), m(22))
    j041 = Point(m(-9.21), m(0), m(22))
    j042 = Point(m(-6.9), m(0), m(22))
    j043 = Point(m(-4.36), m(0), m(22))
    j044 = Point(m(-1.8), m(0), m(22))
    j045 = Point(m(1.8), m(0), m(22))
    j046 = Point(m(4.36), m(0), m(22))
    j047 = Point(m(6.9), m(0), m(22))
    j048 = Point(m(9.2), m(0), m(22))
    j049 = Point(m(11.5), m(0), m(22))
    j050 = Point(m(13.04), m(0), m(22))
    j051 = Point(m(13.95), m(0), m(22))
    j052 = Point(m(-13.5), m(0), m(22))
    j053 = Point(m(13.5), m(0), m(22))
    j054 = Point(m(-1.91), m(0), m(20))
    j055 = Point(m(1.91), m(0), m(20))
    j056 = Point(m(-2.02), m(0), m(18.01))
    j057 = Point(m(2.02), m(0), m(18.01))
    j058 = Point(m(-2.13), m(0), m(16))
    j059 = Point(m(2.13), m(0), m(16))
    j060 = Point(m(-10.01), m(0), m(14.61))
    j061 = Point(m(9.99), m(0), m(14.61))
    j062 = Point(m(-6.05), m(0), m(14))
    j063 = Point(m(-2.24), m(0), m(14))
    j064 = Point(m(2.24), m(0), m(14))
    j065 = Point(m(6.04), m(0), m(14))
    j066 = Point(m(-12.48), m(0), m(13.94))
    j067 = Point(m(12.45), m(0), m(13.94))
    j068 = Point(m(-16.66), m(0), m(12.79))
    j069 = Point(m(16.64), m(0), m(12.79))
    j070 = Point(m(-17.35), m(0), m(12.6))
    j071 = Point(m(17.35), m(0), m(12.6))
    j072 = Point(m(-17.35), m(0), m(12))
    j073 = Point(m(-17), m(0), m(12))
    j074 = Point(m(-16.66), m(0), m(12))
    j075 = Point(m(-15.49), m(0), m(12))
    j076 = Point(m(-12.48), m(0), m(12))
    j077 = Point(m(-10), m(0), m(12))
    j078 = Point(m(-6.03), m(0), m(12))
    j079 = Point(m(-2.35), m(0), m(12))
    j080 = Point(m(2.35), m(0), m(12))
    j081 = Point(m(6.02), m(0), m(12))
    j082 = Point(m(10), m(0), m(12))
    j083 = Point(m(12.45), m(0), m(12))
    j084 = Point(m(15.48), m(0), m(12))
    j085 = Point(m(16.64), m(0), m(12))
    j086 = Point(m(17), m(0), m(12))
    j087 = Point(m(17.35), m(0), m(12))
    j088 = Point(m(-2.48), m(0), m(9.51))
    j089 = Point(m(2.48), m(0), m(9.51))
    j090 = Point(m(-2.62), m(0), m(6.93))
    j091 = Point(m(2.62), m(0), m(6.93))
    j092 = Point(m(-2.77), m(0), m(4.05))
    j093 = Point(m(2.77), m(0), m(4.05))
    j094 = Point(m(-7.81), m(0), m(3.04))
    j095 = Point(m(7.79), m(0), m(3.04))
    j096 = Point(m(-5.31), m(0), m(2.03))
    j097 = Point(m(5.31), m(0), m(2.03))
    j098 = Point(m(-13.26), m(0), m(1.83))
    j099 = Point(m(13.24), m(0), m(1.83))
    j100 = Point(m(-10.54), m(0), m(1.53))
    j101 = Point(m(10.53), m(0), m(1.53))
    j102 = Point(m(-2.91), m(0), m(1.33))
    j103 = Point(m(2.91), m(0), m(1.33))
    j104 = Point(m(-16.01), m(0), m(1.21))
    j105 = Point(m(15.99), m(0), m(1.21))
    j106 = Point(m(-18.87), m(0), m(0.57))
    j107 = Point(m(18.85), m(0), m(0.57))
    j108 = Point(m(-18.87), m(0), m(0))
    j109 = Point(m(-16.01), m(0), m(0))
    j110 = Point(m(-13.25), m(0), m(0))
    j111 = Point(m(-7.8), m(0), m(0))
    j112 = Point(m(-2.99), m(0), m(0))
    j113 = Point(m(2.99), m(0), m(0))
    j114 = Point(m(7.8), m(0), m(0))
    j115 = Point(m(13.25), m(0), m(0))
    j116 = Point(m(15.99), m(0), m(0))
    j117 = Point(m(18.85), m(0), m(0))
    j118 = Point(m(-18.7), m(0), m(0))
    j119 = Point(m(0), m(0), m(0))
    j120 = Point(m(18.7), m(0), m(0))
    j121 = Point(m(-3.13), m(0), m(-2.74))
    j122 = Point(m(3.13), m(0), m(-2.74))
    j123 = Point(m(-3.33), m(0), m(-4.65))
    j124 = Point(m(-1.57), m(0), m(-4.65))
    j125 = Point(m(1.57), m(0), m(-4.65))
    j126 = Point(m(3.33), m(0), m(-4.65))
    j127 = Point(m(-3.53), m(0), m(-6.58))
    j128 = Point(m(-0.01), m(0), m(-6.58))
    j129 = Point(m(3.53), m(0), m(-6.58))
    j130 = Point(m(-3.77), m(0), m(-8.97))
    j131 = Point(m(-1.95), m(0), m(-8.97))
    j132 = Point(m(1.95), m(0), m(-8.97))
    j133 = Point(m(3.77), m(0), m(-8.97))
    j134 = Point(m(-3.91), m(0), m(-11.35))
    j135 = Point(m(3.91), m(0), m(-11.35))
    j136 = Point(m(-4.35), m(0), m(-14.56))
    j137 = Point(m(-1.95), m(0), m(-14.56))
    j138 = Point(m(1.95), m(0), m(-14.56))
    j139 = Point(m(4.35), m(0), m(-14.56))
    j140 = Point(m(-4.67), m(0), m(-17.66))
    j141 = Point(m(4.67), m(0), m(-17.66))
    j142 = Point(m(-4.97), m(0), m(-20.6))
    j143 = Point(m(-1.72), m(0), m(-20.6))
    j144 = Point(m(1.72), m(0), m(-20.6))
    j145 = Point(m(4.97), m(0), m(-20.6))
    j146 = Point(m(-5.23), m(0), m(-23.07))
    j147 = Point(m(-3.23), m(0), m(-23.07))
    j148 = Point(m(3.23), m(0), m(-23.07))
    j149 = Point(m(5.23), m(0), m(-23.07))
    j150 = Point(m(-5.63), m(0), m(-27))
    j151 = Point(m(5.63), m(0), m(-27))
    return Tower(
        name="DA-4-DE-2018.1 WA120",
        datum=LowestCrossarm((m(27), m(33))),
        voltages=(kv(380),),
        line_angles=(),
        attachments=(
            Mount(Wire.SHIELD, Point(m(-8.45), m(0), m(32.5)), Hold.CLAMP),
            Mount(Wire.SHIELD, Point(m(8.45), m(0), m(32.5)), Hold.CLAMP),
            Mount(Wire.PHASE, Point(m(-13.5), m(0), m(22)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(13.5), m(0), m(22)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-17), m(0), m(12)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-10), m(0), m(12)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(10), m(0), m(12)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(17), m(0), m(12)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-18.7), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-13.25), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-7.8), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.SHIELD, Point(m(0), m(0), m(0)), Hold.CLAMP),
            Mount(Wire.PHASE, Point(m(7.8), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(13.25), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(18.7), m(0), m(0)), Hold.STRAIN),
        ),
        bases=(),
        body=(
            Body(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j143, j138, role=Role.DIAGONAL_BRACE),
                        Bar(j144, j137, role=Role.DIAGONAL_BRACE),
                        Bar(j141, j140, role=Role.TRANSVERSE_BRACE),
                        Bar(j022, j023, role=Role.TRANSVERSE_BRACE),
                        Bar(j044, j045, role=Role.TRANSVERSE_BRACE),
                        Bar(j079, j080, role=Role.TRANSVERSE_BRACE),
                        Bar(j058, j059, role=Role.TRANSVERSE_BRACE),
                        Bar(j080, j088, role=Role.DIAGONAL_BRACE),
                        Bar(j088, j091, role=Role.DIAGONAL_BRACE),
                        Bar(j091, j092, role=Role.DIAGONAL_BRACE),
                        Bar(j093, j090, role=Role.DIAGONAL_BRACE),
                        Bar(j090, j089, role=Role.DIAGONAL_BRACE),
                        Bar(j089, j079, role=Role.DIAGONAL_BRACE),
                        Bar(j122, j119, role=Role.DIAGONAL_BRACE),
                        Bar(j119, j102, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j119, role=Role.DIAGONAL_BRACE),
                        Bar(j119, j103, role=Role.DIAGONAL_BRACE),
                        Bar(j103, j092, role=Role.DIAGONAL_BRACE),
                        Bar(j102, j093, role=Role.DIAGONAL_BRACE),
                        Bar(j132, j128, role=Role.DIAGONAL_BRACE),
                        Bar(j128, j125, role=Role.DIAGONAL_BRACE),
                        Bar(j129, j128, role=Role.TRANSVERSE_BRACE),
                        Bar(j121, j112, role=Role.CHORD),
                        Bar(j112, j102, role=Role.CHORD),
                        Bar(j102, j092, role=Role.CHORD),
                        Bar(j092, j090, role=Role.CHORD),
                        Bar(j090, j088, role=Role.CHORD),
                        Bar(j088, j079, role=Role.CHORD),
                        Bar(j079, j063, role=Role.CHORD),
                        Bar(j063, j058, role=Role.CHORD),
                        Bar(j059, j063, role=Role.DIAGONAL_BRACE),
                        Bar(j063, j080, role=Role.DIAGONAL_BRACE),
                        Bar(j080, j089, role=Role.CHORD),
                        Bar(j089, j091, role=Role.CHORD),
                        Bar(j091, j093, role=Role.CHORD),
                        Bar(j093, j103, role=Role.CHORD),
                        Bar(j103, j113, role=Role.CHORD),
                        Bar(j113, j122, role=Role.CHORD),
                        Bar(j058, j064, role=Role.DIAGONAL_BRACE),
                        Bar(j064, j079, role=Role.DIAGONAL_BRACE),
                        Bar(j058, j056, role=Role.CHORD),
                        Bar(j056, j054, role=Role.CHORD),
                        Bar(j054, j044, role=Role.CHORD),
                        Bar(j044, j028, role=Role.CHORD),
                        Bar(j028, j022, role=Role.CHORD),
                        Bar(j045, j028, role=Role.DIAGONAL_BRACE),
                        Bar(j028, j023, role=Role.DIAGONAL_BRACE),
                        Bar(j023, j029, role=Role.CHORD),
                        Bar(j029, j045, role=Role.CHORD),
                        Bar(j045, j055, role=Role.CHORD),
                        Bar(j055, j057, role=Role.CHORD),
                        Bar(j057, j059, role=Role.CHORD),
                        Bar(j059, j064, role=Role.CHORD),
                        Bar(j064, j080, role=Role.CHORD),
                        Bar(j044, j029, role=Role.DIAGONAL_BRACE),
                        Bar(j029, j022, role=Role.DIAGONAL_BRACE),
                        Bar(j044, j055, role=Role.DIAGONAL_BRACE),
                        Bar(j055, j056, role=Role.DIAGONAL_BRACE),
                        Bar(j056, j059, role=Role.DIAGONAL_BRACE),
                        Bar(j058, j057, role=Role.DIAGONAL_BRACE),
                        Bar(j057, j054, role=Role.DIAGONAL_BRACE),
                        Bar(j054, j045, role=Role.DIAGONAL_BRACE),
                        Bar(j112, j119, role=Role.TRANSVERSE_BRACE),
                        Bar(j119, j113, role=Role.TRANSVERSE_BRACE),
                        Bar(j092, j093, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        legs=(
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j150, j146, role=Role.CHORD),
                        Bar(j146, j142, role=Role.CHORD),
                        Bar(j142, j140, role=Role.CHORD),
                        Bar(j140, j136, role=Role.CHORD),
                        Bar(j136, j130, role=Role.CHORD),
                        Bar(j130, j127, role=Role.CHORD),
                        Bar(j127, j123, role=Role.CHORD),
                        Bar(j123, j121, role=Role.CHORD),
                        Bar(j150, j147, role=Role.DIAGONAL_BRACE),
                        Bar(j147, j143, role=Role.DIAGONAL_BRACE),
                        Bar(j137, j134, role=Role.DIAGONAL_BRACE),
                        Bar(j143, j142, role=Role.TRANSVERSE_BRACE),
                        Bar(j147, j146, role=Role.TRANSVERSE_BRACE),
                        Bar(j137, j136, role=Role.TRANSVERSE_BRACE),
                        Bar(j147, j142, role=Role.DIAGONAL_BRACE),
                        Bar(j143, j140, role=Role.DIAGONAL_BRACE),
                        Bar(j140, j137, role=Role.DIAGONAL_BRACE),
                        Bar(j128, j124, role=Role.DIAGONAL_BRACE),
                        Bar(j124, j121, role=Role.DIAGONAL_BRACE),
                        Bar(j134, j131, role=Role.DIAGONAL_BRACE),
                        Bar(j131, j128, role=Role.DIAGONAL_BRACE),
                        Bar(j128, j127, role=Role.TRANSVERSE_BRACE),
                        Bar(j127, j124, role=Role.DIAGONAL_BRACE),
                        Bar(j127, j131, role=Role.DIAGONAL_BRACE),
                        Bar(j130, j131, role=Role.TRANSVERSE_BRACE),
                        Bar(j123, j124, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j122, j126, role=Role.CHORD),
                        Bar(j126, j129, role=Role.CHORD),
                        Bar(j129, j133, role=Role.CHORD),
                        Bar(j133, j139, role=Role.CHORD),
                        Bar(j139, j141, role=Role.CHORD),
                        Bar(j141, j145, role=Role.CHORD),
                        Bar(j145, j149, role=Role.CHORD),
                        Bar(j149, j151, role=Role.CHORD),
                        Bar(j138, j135, role=Role.DIAGONAL_BRACE),
                        Bar(j151, j148, role=Role.DIAGONAL_BRACE),
                        Bar(j148, j144, role=Role.DIAGONAL_BRACE),
                        Bar(j144, j145, role=Role.TRANSVERSE_BRACE),
                        Bar(j148, j149, role=Role.TRANSVERSE_BRACE),
                        Bar(j138, j139, role=Role.TRANSVERSE_BRACE),
                        Bar(j148, j145, role=Role.DIAGONAL_BRACE),
                        Bar(j144, j141, role=Role.DIAGONAL_BRACE),
                        Bar(j141, j138, role=Role.DIAGONAL_BRACE),
                        Bar(j135, j132, role=Role.DIAGONAL_BRACE),
                        Bar(j125, j122, role=Role.DIAGONAL_BRACE),
                        Bar(j125, j129, role=Role.DIAGONAL_BRACE),
                        Bar(j129, j132, role=Role.DIAGONAL_BRACE),
                        Bar(j125, j126, role=Role.TRANSVERSE_BRACE),
                        Bar(j132, j133, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        head=(
            Head(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j018, j023, role=Role.CHORD),
                        Bar(j023, j019, role=Role.DIAGONAL_BRACE),
                        Bar(j019, j022, role=Role.DIAGONAL_BRACE),
                        Bar(j018, j019, role=Role.DIAGONAL_BRACE),
                        Bar(j019, j017, role=Role.DIAGONAL_BRACE),
                        Bar(j022, j017, role=Role.CHORD),
                    ),
                )
            ),
        ),
        crossarms=(
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j038, j052, role=Role.CHORD),
                        Bar(j052, j039, role=Role.CHORD),
                        Bar(j039, j036, role=Role.CHORD),
                        Bar(j036, j040, role=Role.CHORD),
                        Bar(j040, j041, role=Role.CHORD),
                        Bar(j041, j042, role=Role.CHORD),
                        Bar(j042, j043, role=Role.CHORD),
                        Bar(j043, j044, role=Role.CHORD),
                        Bar(j034, j032, role=Role.CHORD),
                        Bar(j032, j026, role=Role.CHORD),
                        Bar(j026, j024, role=Role.CHORD),
                        Bar(j024, j022, role=Role.CHORD),
                        Bar(j034, j038, role=Role.CHORD),
                        Bar(j044, j030, role=Role.DIAGONAL_BRACE),
                        Bar(j030, j043, role=Role.TRANSVERSE_BRACE),
                        Bar(j024, j042, role=Role.TRANSVERSE_BRACE),
                        Bar(j042, j030, role=Role.DIAGONAL_BRACE),
                        Bar(j030, j022, role=Role.DIAGONAL_BRACE),
                        Bar(j041, j026, role=Role.TRANSVERSE_BRACE),
                        Bar(j026, j042, role=Role.DIAGONAL_BRACE),
                        Bar(j026, j036, role=Role.DIAGONAL_BRACE),
                        Bar(j039, j032, role=Role.TRANSVERSE_BRACE),
                        Bar(j032, j036, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j045, j046, role=Role.CHORD),
                        Bar(j046, j047, role=Role.CHORD),
                        Bar(j047, j048, role=Role.CHORD),
                        Bar(j048, j049, role=Role.CHORD),
                        Bar(j049, j037, role=Role.CHORD),
                        Bar(j037, j050, role=Role.CHORD),
                        Bar(j050, j053, role=Role.CHORD),
                        Bar(j053, j051, role=Role.CHORD),
                        Bar(j051, j035, role=Role.CHORD),
                        Bar(j035, j033, role=Role.CHORD),
                        Bar(j033, j027, role=Role.CHORD),
                        Bar(j027, j025, role=Role.CHORD),
                        Bar(j025, j023, role=Role.CHORD),
                        Bar(j033, j050, role=Role.TRANSVERSE_BRACE),
                        Bar(j033, j037, role=Role.DIAGONAL_BRACE),
                        Bar(j048, j027, role=Role.TRANSVERSE_BRACE),
                        Bar(j027, j047, role=Role.DIAGONAL_BRACE),
                        Bar(j027, j037, role=Role.DIAGONAL_BRACE),
                        Bar(j025, j047, role=Role.TRANSVERSE_BRACE),
                        Bar(j047, j031, role=Role.DIAGONAL_BRACE),
                        Bar(j031, j023, role=Role.DIAGONAL_BRACE),
                        Bar(j045, j031, role=Role.DIAGONAL_BRACE),
                        Bar(j031, j046, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j072, j073, role=Role.CHORD),
                        Bar(j073, j074, role=Role.CHORD),
                        Bar(j074, j075, role=Role.CHORD),
                        Bar(j075, j076, role=Role.CHORD),
                        Bar(j076, j077, role=Role.CHORD),
                        Bar(j077, j078, role=Role.CHORD),
                        Bar(j078, j079, role=Role.CHORD),
                        Bar(j072, j070, role=Role.CHORD),
                        Bar(j070, j068, role=Role.CHORD),
                        Bar(j068, j066, role=Role.CHORD),
                        Bar(j066, j060, role=Role.CHORD),
                        Bar(j060, j058, role=Role.CHORD),
                        Bar(j068, j074, role=Role.TRANSVERSE_BRACE),
                        Bar(j058, j062, role=Role.DIAGONAL_BRACE),
                        Bar(j062, j077, role=Role.DIAGONAL_BRACE),
                        Bar(j077, j060, role=Role.TRANSVERSE_BRACE),
                        Bar(j068, j075, role=Role.DIAGONAL_BRACE),
                        Bar(j075, j066, role=Role.DIAGONAL_BRACE),
                        Bar(j066, j077, role=Role.DIAGONAL_BRACE),
                        Bar(j076, j066, role=Role.TRANSVERSE_BRACE),
                        Bar(j079, j062, role=Role.DIAGONAL_BRACE),
                        Bar(j062, j078, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j080, j081, role=Role.CHORD),
                        Bar(j081, j082, role=Role.CHORD),
                        Bar(j082, j083, role=Role.CHORD),
                        Bar(j083, j084, role=Role.CHORD),
                        Bar(j084, j085, role=Role.CHORD),
                        Bar(j085, j086, role=Role.CHORD),
                        Bar(j086, j087, role=Role.CHORD),
                        Bar(j087, j071, role=Role.CHORD),
                        Bar(j071, j069, role=Role.CHORD),
                        Bar(j069, j067, role=Role.CHORD),
                        Bar(j067, j061, role=Role.CHORD),
                        Bar(j061, j059, role=Role.CHORD),
                        Bar(j069, j085, role=Role.TRANSVERSE_BRACE),
                        Bar(j069, j084, role=Role.DIAGONAL_BRACE),
                        Bar(j084, j067, role=Role.DIAGONAL_BRACE),
                        Bar(j067, j082, role=Role.DIAGONAL_BRACE),
                        Bar(j082, j061, role=Role.TRANSVERSE_BRACE),
                        Bar(j083, j067, role=Role.TRANSVERSE_BRACE),
                        Bar(j080, j065, role=Role.DIAGONAL_BRACE),
                        Bar(j065, j081, role=Role.TRANSVERSE_BRACE),
                        Bar(j059, j065, role=Role.DIAGONAL_BRACE),
                        Bar(j065, j082, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j092, j094, role=Role.CHORD),
                        Bar(j094, j098, role=Role.CHORD),
                        Bar(j098, j104, role=Role.CHORD),
                        Bar(j104, j106, role=Role.CHORD),
                        Bar(j106, j108, role=Role.CHORD),
                        Bar(j108, j118, role=Role.CHORD),
                        Bar(j118, j109, role=Role.CHORD),
                        Bar(j109, j110, role=Role.CHORD),
                        Bar(j110, j111, role=Role.CHORD),
                        Bar(j111, j112, role=Role.CHORD),
                        Bar(j094, j100, role=Role.DIAGONAL_BRACE),
                        Bar(j100, j110, role=Role.DIAGONAL_BRACE),
                        Bar(j110, j104, role=Role.DIAGONAL_BRACE),
                        Bar(j111, j096, role=Role.DIAGONAL_BRACE),
                        Bar(j096, j092, role=Role.DIAGONAL_BRACE),
                        Bar(j096, j112, role=Role.DIAGONAL_BRACE),
                        Bar(j104, j109, role=Role.TRANSVERSE_BRACE),
                        Bar(j094, j111, role=Role.TRANSVERSE_BRACE),
                        Bar(j098, j110, role=Role.TRANSVERSE_BRACE),
                        Bar(j111, j100, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j113, j114, role=Role.CHORD),
                        Bar(j114, j115, role=Role.CHORD),
                        Bar(j115, j116, role=Role.CHORD),
                        Bar(j116, j120, role=Role.CHORD),
                        Bar(j120, j117, role=Role.CHORD),
                        Bar(j117, j107, role=Role.CHORD),
                        Bar(j107, j105, role=Role.CHORD),
                        Bar(j105, j099, role=Role.CHORD),
                        Bar(j099, j095, role=Role.CHORD),
                        Bar(j095, j093, role=Role.CHORD),
                        Bar(j095, j101, role=Role.DIAGONAL_BRACE),
                        Bar(j101, j115, role=Role.DIAGONAL_BRACE),
                        Bar(j115, j105, role=Role.DIAGONAL_BRACE),
                        Bar(j114, j097, role=Role.DIAGONAL_BRACE),
                        Bar(j097, j093, role=Role.DIAGONAL_BRACE),
                        Bar(j097, j113, role=Role.DIAGONAL_BRACE),
                        Bar(j105, j116, role=Role.TRANSVERSE_BRACE),
                        Bar(j095, j114, role=Role.TRANSVERSE_BRACE),
                        Bar(j099, j115, role=Role.TRANSVERSE_BRACE),
                        Bar(j114, j101, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        peaks=(
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j017, j013, role=Role.CHORD),
                        Bar(j013, j010, role=Role.CHORD),
                        Bar(j010, j007, role=Role.CHORD),
                        Bar(j007, j003, role=Role.CHORD),
                        Bar(j003, j001, role=Role.CHORD),
                        Bar(j001, j005, role=Role.CHORD),
                        Bar(j005, j009, role=Role.CHORD),
                        Bar(j009, j015, role=Role.CHORD),
                        Bar(j015, j020, role=Role.CHORD),
                        Bar(j020, j022, role=Role.CHORD),
                        Bar(j017, j020, role=Role.DIAGONAL_BRACE),
                        Bar(j020, j013, role=Role.DIAGONAL_BRACE),
                        Bar(j013, j015, role=Role.DIAGONAL_BRACE),
                        Bar(j015, j010, role=Role.DIAGONAL_BRACE),
                        Bar(j010, j009, role=Role.TRANSVERSE_BRACE),
                        Bar(j009, j007, role=Role.DIAGONAL_BRACE),
                        Bar(j007, j005, role=Role.DIAGONAL_BRACE),
                        Bar(j005, j003, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j008, j012, role=Role.DIAGONAL_BRACE),
                        Bar(j012, j011, role=Role.TRANSVERSE_BRACE),
                        Bar(j011, j016, role=Role.DIAGONAL_BRACE),
                        Bar(j016, j014, role=Role.DIAGONAL_BRACE),
                        Bar(j014, j021, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j018, role=Role.DIAGONAL_BRACE),
                        Bar(j023, j021, role=Role.CHORD),
                        Bar(j021, j016, role=Role.CHORD),
                        Bar(j016, j012, role=Role.CHORD),
                        Bar(j012, j006, role=Role.CHORD),
                        Bar(j006, j002, role=Role.CHORD),
                        Bar(j002, j004, role=Role.CHORD),
                        Bar(j004, j008, role=Role.CHORD),
                        Bar(j008, j011, role=Role.CHORD),
                        Bar(j011, j014, role=Role.CHORD),
                        Bar(j014, j018, role=Role.CHORD),
                        Bar(j008, j006, role=Role.DIAGONAL_BRACE),
                        Bar(j006, j004, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
    )


DA_4_DE_2018_1_WA120 = _da_4_de_2018_1_wa120()


def _da_4_de_2018_1_wa140() -> Tower[LowestCrossarm]:
    """DA-4-DE-2018.1 WA140: each joint written once, by its key."""
    j001 = Point(m(-8.6), m(0), m(32))
    j002 = Point(m(8.6), m(0), m(32))
    j003 = Point(m(-8.47), m(0), m(31.91))
    j004 = Point(m(8.47), m(0), m(31.91))
    j005 = Point(m(-8.1), m(0), m(31.34))
    j006 = Point(m(8.11), m(0), m(31.34))
    j007 = Point(m(-7.29), m(0), m(31.09))
    j008 = Point(m(7.29), m(0), m(31.09))
    j009 = Point(m(-7.15), m(0), m(30.16))
    j010 = Point(m(-5.81), m(0), m(30.16))
    j011 = Point(m(5.8), m(0), m(30.16))
    j012 = Point(m(7.15), m(0), m(30.16))
    j013 = Point(m(-3.85), m(0), m(29.03))
    j014 = Point(m(3.84), m(0), m(29.03))
    j015 = Point(m(-5.76), m(0), m(28.68))
    j016 = Point(m(5.76), m(0), m(28.68))
    j017 = Point(m(-1.47), m(0), m(27.8))
    j018 = Point(m(1.47), m(0), m(27.8))
    j019 = Point(m(0), m(0), m(27.03))
    j020 = Point(m(-3.9), m(0), m(26.97))
    j021 = Point(m(3.91), m(0), m(26.97))
    j022 = Point(m(-1.47), m(0), m(25.03))
    j023 = Point(m(1.47), m(0), m(25.03))
    j024 = Point(m(-6.16), m(0), m(24))
    j025 = Point(m(6.15), m(0), m(24))
    j026 = Point(m(-8.2), m(0), m(23.55))
    j027 = Point(m(8.19), m(0), m(23.55))
    j028 = Point(m(-1.54), m(0), m(23.52))
    j029 = Point(m(1.54), m(0), m(23.52))
    j030 = Point(m(-3.9), m(0), m(23.46))
    j031 = Point(m(3.9), m(0), m(23.46))
    j032 = Point(m(-11.6), m(0), m(22.79))
    j033 = Point(m(11.59), m(0), m(22.79))
    j034 = Point(m(-12.42), m(0), m(22.61))
    j035 = Point(m(12.4), m(0), m(22.61))
    j036 = Point(m(-10.32), m(0), m(22.02))
    j037 = Point(m(10.3), m(0), m(22.02))
    j038 = Point(m(-12.42), m(0), m(22))
    j039 = Point(m(-11.6), m(0), m(22))
    j040 = Point(m(-10.23), m(0), m(22))
    j041 = Point(m(-8.2), m(0), m(22))
    j042 = Point(m(-6.15), m(0), m(22))
    j043 = Point(m(-3.9), m(0), m(22))
    j044 = Point(m(-1.62), m(0), m(22))
    j045 = Point(m(1.62), m(0), m(22))
    j046 = Point(m(3.89), m(0), m(22))
    j047 = Point(m(6.14), m(0), m(22))
    j048 = Point(m(8.19), m(0), m(22))
    j049 = Point(m(10.23), m(0), m(22))
    j050 = Point(m(11.59), m(0), m(22))
    j051 = Point(m(12.4), m(0), m(22))
    j052 = Point(m(-12), m(0), m(22))
    j053 = Point(m(12), m(0), m(22))
    j054 = Point(m(-1.72), m(0), m(20.01))
    j055 = Point(m(1.72), m(0), m(20.01))
    j056 = Point(m(-1.81), m(0), m(18))
    j057 = Point(m(1.81), m(0), m(18))
    j058 = Point(m(-1.91), m(0), m(16))
    j059 = Point(m(1.91), m(0), m(16))
    j060 = Point(m(-9), m(0), m(14.6))
    j061 = Point(m(9), m(0), m(14.6))
    j062 = Point(m(-5.45), m(0), m(13.99))
    j063 = Point(m(-2.01), m(0), m(13.99))
    j064 = Point(m(2), m(0), m(13.99))
    j065 = Point(m(5.44), m(0), m(13.99))
    j066 = Point(m(-11.29), m(0), m(13.93))
    j067 = Point(m(11.28), m(0), m(13.93))
    j068 = Point(m(-15.18), m(0), m(12.78))
    j069 = Point(m(15.17), m(0), m(12.78))
    j070 = Point(m(-15.83), m(0), m(12.59))
    j071 = Point(m(15.82), m(0), m(12.59))
    j072 = Point(m(-15.83), m(0), m(12))
    j073 = Point(m(-15.18), m(0), m(12))
    j074 = Point(m(-14.09), m(0), m(12))
    j075 = Point(m(-11.29), m(0), m(12))
    j076 = Point(m(-9), m(0), m(12))
    j077 = Point(m(-5.43), m(0), m(12))
    j078 = Point(m(-2.1), m(0), m(12))
    j079 = Point(m(2.1), m(0), m(12))
    j080 = Point(m(5.42), m(0), m(12))
    j081 = Point(m(9), m(0), m(12))
    j082 = Point(m(11.28), m(0), m(12))
    j083 = Point(m(14.08), m(0), m(12))
    j084 = Point(m(15.17), m(0), m(12))
    j085 = Point(m(15.82), m(0), m(12))
    j086 = Point(m(-15.5), m(0), m(12))
    j087 = Point(m(15.5), m(0), m(12))
    j088 = Point(m(-2.22), m(0), m(9.51))
    j089 = Point(m(2.22), m(0), m(9.51))
    j090 = Point(m(-2.34), m(0), m(6.92))
    j091 = Point(m(2.34), m(0), m(6.92))
    j092 = Point(m(-2.48), m(0), m(4.06))
    j093 = Point(m(2.48), m(0), m(4.06))
    j094 = Point(m(-7.01), m(0), m(3.05))
    j095 = Point(m(6.99), m(0), m(3.05))
    j096 = Point(m(-4.77), m(0), m(2.02))
    j097 = Point(m(4.76), m(0), m(2.02))
    j098 = Point(m(-11.86), m(0), m(1.83))
    j099 = Point(m(11.84), m(0), m(1.83))
    j100 = Point(m(-9.43), m(0), m(1.53))
    j101 = Point(m(9.42), m(0), m(1.53))
    j102 = Point(m(-2.61), m(0), m(1.33))
    j103 = Point(m(2.61), m(0), m(1.33))
    j104 = Point(m(-14.3), m(0), m(1.22))
    j105 = Point(m(14.29), m(0), m(1.22))
    j106 = Point(m(-16.85), m(0), m(0.58))
    j107 = Point(m(16.84), m(0), m(0.58))
    j108 = Point(m(-16.85), m(0), m(0))
    j109 = Point(m(-16.7), m(0), m(0))
    j110 = Point(m(-14.3), m(0), m(0))
    j111 = Point(m(-11.85), m(0), m(0))
    j112 = Point(m(-7), m(0), m(0))
    j113 = Point(m(-2.68), m(0), m(0))
    j114 = Point(m(0), m(0), m(0))
    j115 = Point(m(2.68), m(0), m(0))
    j116 = Point(m(7), m(0), m(0))
    j117 = Point(m(11.85), m(0), m(0))
    j118 = Point(m(14.29), m(0), m(0))
    j119 = Point(m(16.7), m(0), m(0))
    j120 = Point(m(16.84), m(0), m(0))
    j121 = Point(m(-2.81), m(0), m(-2.73))
    j122 = Point(m(2.81), m(0), m(-2.73))
    j123 = Point(m(-2.99), m(0), m(-4.66))
    j124 = Point(m(-1.4), m(0), m(-4.66))
    j125 = Point(m(1.4), m(0), m(-4.66))
    j126 = Point(m(2.96), m(0), m(-4.66))
    j127 = Point(m(-3.16), m(0), m(-6.56))
    j128 = Point(m(0), m(0), m(-6.56))
    j129 = Point(m(3.16), m(0), m(-6.56))
    j130 = Point(m(-3.38), m(0), m(-8.96))
    j131 = Point(m(-1.76), m(0), m(-8.96))
    j132 = Point(m(1.76), m(0), m(-8.96))
    j133 = Point(m(3.38), m(0), m(-8.96))
    j134 = Point(m(-3.5), m(0), m(-11.36))
    j135 = Point(m(3.5), m(0), m(-11.36))
    j136 = Point(m(-3.9), m(0), m(-14.57))
    j137 = Point(m(-1.76), m(0), m(-14.57))
    j138 = Point(m(1.76), m(0), m(-14.57))
    j139 = Point(m(3.9), m(0), m(-14.57))
    j140 = Point(m(-4.18), m(0), m(-17.65))
    j141 = Point(m(4.19), m(0), m(-17.65))
    j142 = Point(m(-4.45), m(0), m(-20.59))
    j143 = Point(m(-1.55), m(0), m(-20.59))
    j144 = Point(m(1.55), m(0), m(-20.59))
    j145 = Point(m(4.46), m(0), m(-20.59))
    j146 = Point(m(-4.68), m(0), m(-23.06))
    j147 = Point(m(-2.9), m(0), m(-23.06))
    j148 = Point(m(2.9), m(0), m(-23.06))
    j149 = Point(m(4.69), m(0), m(-23.06))
    j150 = Point(m(-5.04), m(0), m(-27))
    j151 = Point(m(5.05), m(0), m(-27))
    return Tower(
        name="DA-4-DE-2018.1 WA140",
        datum=LowestCrossarm((m(27), m(33))),
        voltages=(kv(380),),
        line_angles=(),
        attachments=(
            Mount(Wire.SHIELD, Point(m(-8.6), m(0), m(32)), Hold.CLAMP),
            Mount(Wire.SHIELD, Point(m(8.6), m(0), m(32)), Hold.CLAMP),
            Mount(Wire.PHASE, Point(m(-12), m(0), m(22)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(12), m(0), m(22)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-15.5), m(0), m(12)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-9), m(0), m(12)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(9), m(0), m(12)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(15.5), m(0), m(12)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-16.7), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-11.85), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-7), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.SHIELD, Point(m(0), m(0), m(0)), Hold.CLAMP),
            Mount(Wire.PHASE, Point(m(7), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(11.85), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(16.7), m(0), m(0)), Hold.STRAIN),
        ),
        bases=(),
        body=(
            Body(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j143, j138, role=Role.DIAGONAL_BRACE),
                        Bar(j144, j137, role=Role.DIAGONAL_BRACE),
                        Bar(j141, j140, role=Role.TRANSVERSE_BRACE),
                        Bar(j022, j023, role=Role.TRANSVERSE_BRACE),
                        Bar(j044, j045, role=Role.TRANSVERSE_BRACE),
                        Bar(j078, j079, role=Role.TRANSVERSE_BRACE),
                        Bar(j058, j059, role=Role.TRANSVERSE_BRACE),
                        Bar(j079, j088, role=Role.DIAGONAL_BRACE),
                        Bar(j088, j091, role=Role.DIAGONAL_BRACE),
                        Bar(j091, j092, role=Role.DIAGONAL_BRACE),
                        Bar(j093, j090, role=Role.DIAGONAL_BRACE),
                        Bar(j090, j089, role=Role.DIAGONAL_BRACE),
                        Bar(j089, j078, role=Role.DIAGONAL_BRACE),
                        Bar(j122, j114, role=Role.DIAGONAL_BRACE),
                        Bar(j114, j102, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j114, role=Role.DIAGONAL_BRACE),
                        Bar(j114, j103, role=Role.DIAGONAL_BRACE),
                        Bar(j103, j092, role=Role.DIAGONAL_BRACE),
                        Bar(j102, j093, role=Role.DIAGONAL_BRACE),
                        Bar(j132, j128, role=Role.DIAGONAL_BRACE),
                        Bar(j128, j125, role=Role.DIAGONAL_BRACE),
                        Bar(j129, j128, role=Role.TRANSVERSE_BRACE),
                        Bar(j121, j113, role=Role.CHORD),
                        Bar(j113, j102, role=Role.CHORD),
                        Bar(j102, j092, role=Role.CHORD),
                        Bar(j092, j090, role=Role.CHORD),
                        Bar(j090, j088, role=Role.CHORD),
                        Bar(j088, j078, role=Role.CHORD),
                        Bar(j078, j063, role=Role.CHORD),
                        Bar(j063, j058, role=Role.CHORD),
                        Bar(j059, j063, role=Role.DIAGONAL_BRACE),
                        Bar(j063, j079, role=Role.DIAGONAL_BRACE),
                        Bar(j079, j089, role=Role.CHORD),
                        Bar(j089, j091, role=Role.CHORD),
                        Bar(j091, j093, role=Role.CHORD),
                        Bar(j093, j103, role=Role.CHORD),
                        Bar(j103, j115, role=Role.CHORD),
                        Bar(j115, j122, role=Role.CHORD),
                        Bar(j058, j064, role=Role.DIAGONAL_BRACE),
                        Bar(j064, j078, role=Role.DIAGONAL_BRACE),
                        Bar(j058, j056, role=Role.CHORD),
                        Bar(j056, j054, role=Role.CHORD),
                        Bar(j054, j044, role=Role.CHORD),
                        Bar(j044, j028, role=Role.CHORD),
                        Bar(j028, j022, role=Role.CHORD),
                        Bar(j045, j028, role=Role.DIAGONAL_BRACE),
                        Bar(j028, j023, role=Role.DIAGONAL_BRACE),
                        Bar(j023, j029, role=Role.CHORD),
                        Bar(j029, j045, role=Role.CHORD),
                        Bar(j045, j055, role=Role.CHORD),
                        Bar(j055, j057, role=Role.CHORD),
                        Bar(j057, j059, role=Role.CHORD),
                        Bar(j059, j064, role=Role.CHORD),
                        Bar(j064, j079, role=Role.CHORD),
                        Bar(j059, j056, role=Role.DIAGONAL_BRACE),
                        Bar(j056, j055, role=Role.DIAGONAL_BRACE),
                        Bar(j055, j044, role=Role.DIAGONAL_BRACE),
                        Bar(j044, j029, role=Role.DIAGONAL_BRACE),
                        Bar(j029, j022, role=Role.DIAGONAL_BRACE),
                        Bar(j058, j057, role=Role.DIAGONAL_BRACE),
                        Bar(j057, j054, role=Role.DIAGONAL_BRACE),
                        Bar(j054, j045, role=Role.DIAGONAL_BRACE),
                        Bar(j113, j114, role=Role.TRANSVERSE_BRACE),
                        Bar(j114, j115, role=Role.TRANSVERSE_BRACE),
                        Bar(j092, j093, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        legs=(
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j150, j146, role=Role.CHORD),
                        Bar(j146, j142, role=Role.CHORD),
                        Bar(j142, j140, role=Role.CHORD),
                        Bar(j140, j136, role=Role.CHORD),
                        Bar(j136, j130, role=Role.CHORD),
                        Bar(j130, j127, role=Role.CHORD),
                        Bar(j127, j123, role=Role.CHORD),
                        Bar(j123, j121, role=Role.CHORD),
                        Bar(j150, j147, role=Role.DIAGONAL_BRACE),
                        Bar(j147, j143, role=Role.DIAGONAL_BRACE),
                        Bar(j137, j134, role=Role.DIAGONAL_BRACE),
                        Bar(j143, j142, role=Role.TRANSVERSE_BRACE),
                        Bar(j147, j146, role=Role.TRANSVERSE_BRACE),
                        Bar(j137, j136, role=Role.TRANSVERSE_BRACE),
                        Bar(j147, j142, role=Role.DIAGONAL_BRACE),
                        Bar(j143, j140, role=Role.DIAGONAL_BRACE),
                        Bar(j140, j137, role=Role.DIAGONAL_BRACE),
                        Bar(j128, j124, role=Role.DIAGONAL_BRACE),
                        Bar(j124, j121, role=Role.DIAGONAL_BRACE),
                        Bar(j134, j131, role=Role.DIAGONAL_BRACE),
                        Bar(j131, j128, role=Role.DIAGONAL_BRACE),
                        Bar(j128, j127, role=Role.TRANSVERSE_BRACE),
                        Bar(j127, j124, role=Role.DIAGONAL_BRACE),
                        Bar(j127, j131, role=Role.DIAGONAL_BRACE),
                        Bar(j130, j131, role=Role.TRANSVERSE_BRACE),
                        Bar(j123, j124, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j122, j129, role=Role.CHORD),
                        Bar(j129, j133, role=Role.CHORD),
                        Bar(j133, j139, role=Role.CHORD),
                        Bar(j139, j141, role=Role.CHORD),
                        Bar(j141, j145, role=Role.CHORD),
                        Bar(j145, j149, role=Role.CHORD),
                        Bar(j149, j151, role=Role.CHORD),
                        Bar(j138, j135, role=Role.DIAGONAL_BRACE),
                        Bar(j151, j148, role=Role.DIAGONAL_BRACE),
                        Bar(j148, j144, role=Role.DIAGONAL_BRACE),
                        Bar(j144, j145, role=Role.TRANSVERSE_BRACE),
                        Bar(j148, j149, role=Role.TRANSVERSE_BRACE),
                        Bar(j138, j139, role=Role.TRANSVERSE_BRACE),
                        Bar(j148, j145, role=Role.DIAGONAL_BRACE),
                        Bar(j144, j141, role=Role.DIAGONAL_BRACE),
                        Bar(j141, j138, role=Role.DIAGONAL_BRACE),
                        Bar(j135, j132, role=Role.DIAGONAL_BRACE),
                        Bar(j125, j122, role=Role.DIAGONAL_BRACE),
                        Bar(j125, j129, role=Role.DIAGONAL_BRACE),
                        Bar(j129, j132, role=Role.DIAGONAL_BRACE),
                        Bar(j125, j126, role=Role.TRANSVERSE_BRACE),
                        Bar(j132, j133, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        head=(
            Head(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j018, j023, role=Role.CHORD),
                        Bar(j023, j019, role=Role.DIAGONAL_BRACE),
                        Bar(j019, j022, role=Role.DIAGONAL_BRACE),
                        Bar(j018, j019, role=Role.DIAGONAL_BRACE),
                        Bar(j019, j017, role=Role.DIAGONAL_BRACE),
                        Bar(j022, j017, role=Role.CHORD),
                    ),
                )
            ),
        ),
        crossarms=(
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j038, j052, role=Role.CHORD),
                        Bar(j052, j039, role=Role.CHORD),
                        Bar(j039, j036, role=Role.CHORD),
                        Bar(j036, j040, role=Role.CHORD),
                        Bar(j040, j041, role=Role.CHORD),
                        Bar(j041, j042, role=Role.CHORD),
                        Bar(j042, j043, role=Role.CHORD),
                        Bar(j043, j044, role=Role.CHORD),
                        Bar(j034, j032, role=Role.CHORD),
                        Bar(j032, j026, role=Role.CHORD),
                        Bar(j026, j024, role=Role.CHORD),
                        Bar(j024, j022, role=Role.CHORD),
                        Bar(j034, j038, role=Role.CHORD),
                        Bar(j044, j030, role=Role.DIAGONAL_BRACE),
                        Bar(j030, j043, role=Role.TRANSVERSE_BRACE),
                        Bar(j024, j042, role=Role.TRANSVERSE_BRACE),
                        Bar(j042, j030, role=Role.DIAGONAL_BRACE),
                        Bar(j030, j022, role=Role.DIAGONAL_BRACE),
                        Bar(j041, j026, role=Role.TRANSVERSE_BRACE),
                        Bar(j026, j042, role=Role.DIAGONAL_BRACE),
                        Bar(j026, j036, role=Role.DIAGONAL_BRACE),
                        Bar(j039, j032, role=Role.TRANSVERSE_BRACE),
                        Bar(j032, j036, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j045, j046, role=Role.CHORD),
                        Bar(j046, j047, role=Role.CHORD),
                        Bar(j047, j048, role=Role.CHORD),
                        Bar(j048, j049, role=Role.CHORD),
                        Bar(j049, j037, role=Role.CHORD),
                        Bar(j037, j050, role=Role.CHORD),
                        Bar(j050, j053, role=Role.CHORD),
                        Bar(j053, j051, role=Role.CHORD),
                        Bar(j051, j035, role=Role.CHORD),
                        Bar(j035, j033, role=Role.CHORD),
                        Bar(j033, j027, role=Role.CHORD),
                        Bar(j027, j025, role=Role.CHORD),
                        Bar(j025, j023, role=Role.CHORD),
                        Bar(j033, j050, role=Role.TRANSVERSE_BRACE),
                        Bar(j033, j037, role=Role.DIAGONAL_BRACE),
                        Bar(j048, j027, role=Role.TRANSVERSE_BRACE),
                        Bar(j027, j047, role=Role.DIAGONAL_BRACE),
                        Bar(j027, j037, role=Role.DIAGONAL_BRACE),
                        Bar(j025, j047, role=Role.TRANSVERSE_BRACE),
                        Bar(j047, j031, role=Role.DIAGONAL_BRACE),
                        Bar(j031, j023, role=Role.DIAGONAL_BRACE),
                        Bar(j045, j031, role=Role.DIAGONAL_BRACE),
                        Bar(j031, j046, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j072, j086, role=Role.CHORD),
                        Bar(j086, j073, role=Role.CHORD),
                        Bar(j073, j074, role=Role.CHORD),
                        Bar(j074, j075, role=Role.CHORD),
                        Bar(j075, j076, role=Role.CHORD),
                        Bar(j076, j077, role=Role.CHORD),
                        Bar(j077, j078, role=Role.CHORD),
                        Bar(j072, j070, role=Role.CHORD),
                        Bar(j070, j068, role=Role.CHORD),
                        Bar(j068, j066, role=Role.CHORD),
                        Bar(j066, j060, role=Role.CHORD),
                        Bar(j060, j058, role=Role.CHORD),
                        Bar(j068, j073, role=Role.TRANSVERSE_BRACE),
                        Bar(j058, j062, role=Role.DIAGONAL_BRACE),
                        Bar(j062, j076, role=Role.DIAGONAL_BRACE),
                        Bar(j076, j060, role=Role.TRANSVERSE_BRACE),
                        Bar(j068, j074, role=Role.DIAGONAL_BRACE),
                        Bar(j074, j066, role=Role.DIAGONAL_BRACE),
                        Bar(j066, j076, role=Role.DIAGONAL_BRACE),
                        Bar(j075, j066, role=Role.TRANSVERSE_BRACE),
                        Bar(j078, j062, role=Role.DIAGONAL_BRACE),
                        Bar(j062, j077, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j079, j080, role=Role.CHORD),
                        Bar(j080, j081, role=Role.CHORD),
                        Bar(j081, j082, role=Role.CHORD),
                        Bar(j082, j083, role=Role.CHORD),
                        Bar(j083, j084, role=Role.CHORD),
                        Bar(j084, j087, role=Role.CHORD),
                        Bar(j087, j085, role=Role.CHORD),
                        Bar(j085, j071, role=Role.CHORD),
                        Bar(j071, j069, role=Role.CHORD),
                        Bar(j069, j067, role=Role.CHORD),
                        Bar(j067, j061, role=Role.CHORD),
                        Bar(j061, j059, role=Role.CHORD),
                        Bar(j069, j084, role=Role.TRANSVERSE_BRACE),
                        Bar(j069, j083, role=Role.DIAGONAL_BRACE),
                        Bar(j083, j067, role=Role.DIAGONAL_BRACE),
                        Bar(j067, j081, role=Role.DIAGONAL_BRACE),
                        Bar(j081, j061, role=Role.TRANSVERSE_BRACE),
                        Bar(j082, j067, role=Role.TRANSVERSE_BRACE),
                        Bar(j079, j065, role=Role.DIAGONAL_BRACE),
                        Bar(j065, j080, role=Role.TRANSVERSE_BRACE),
                        Bar(j059, j065, role=Role.DIAGONAL_BRACE),
                        Bar(j065, j081, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j092, j094, role=Role.CHORD),
                        Bar(j094, j098, role=Role.CHORD),
                        Bar(j098, j104, role=Role.CHORD),
                        Bar(j104, j106, role=Role.CHORD),
                        Bar(j106, j108, role=Role.CHORD),
                        Bar(j108, j109, role=Role.CHORD),
                        Bar(j109, j110, role=Role.CHORD),
                        Bar(j110, j111, role=Role.CHORD),
                        Bar(j111, j112, role=Role.CHORD),
                        Bar(j112, j113, role=Role.CHORD),
                        Bar(j094, j100, role=Role.DIAGONAL_BRACE),
                        Bar(j100, j111, role=Role.DIAGONAL_BRACE),
                        Bar(j111, j104, role=Role.DIAGONAL_BRACE),
                        Bar(j112, j096, role=Role.DIAGONAL_BRACE),
                        Bar(j096, j092, role=Role.DIAGONAL_BRACE),
                        Bar(j096, j113, role=Role.DIAGONAL_BRACE),
                        Bar(j104, j110, role=Role.TRANSVERSE_BRACE),
                        Bar(j094, j112, role=Role.TRANSVERSE_BRACE),
                        Bar(j098, j111, role=Role.TRANSVERSE_BRACE),
                        Bar(j112, j100, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j115, j116, role=Role.CHORD),
                        Bar(j116, j117, role=Role.CHORD),
                        Bar(j117, j118, role=Role.CHORD),
                        Bar(j118, j119, role=Role.CHORD),
                        Bar(j119, j120, role=Role.CHORD),
                        Bar(j120, j107, role=Role.CHORD),
                        Bar(j107, j105, role=Role.CHORD),
                        Bar(j105, j099, role=Role.CHORD),
                        Bar(j099, j095, role=Role.CHORD),
                        Bar(j095, j093, role=Role.CHORD),
                        Bar(j095, j101, role=Role.DIAGONAL_BRACE),
                        Bar(j101, j117, role=Role.DIAGONAL_BRACE),
                        Bar(j117, j105, role=Role.DIAGONAL_BRACE),
                        Bar(j116, j097, role=Role.DIAGONAL_BRACE),
                        Bar(j097, j093, role=Role.DIAGONAL_BRACE),
                        Bar(j097, j115, role=Role.DIAGONAL_BRACE),
                        Bar(j105, j118, role=Role.TRANSVERSE_BRACE),
                        Bar(j095, j116, role=Role.TRANSVERSE_BRACE),
                        Bar(j099, j117, role=Role.TRANSVERSE_BRACE),
                        Bar(j116, j101, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        peaks=(
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j017, j013, role=Role.CHORD),
                        Bar(j013, j010, role=Role.CHORD),
                        Bar(j010, j007, role=Role.CHORD),
                        Bar(j007, j003, role=Role.CHORD),
                        Bar(j003, j001, role=Role.CHORD),
                        Bar(j001, j005, role=Role.CHORD),
                        Bar(j005, j009, role=Role.CHORD),
                        Bar(j009, j015, role=Role.CHORD),
                        Bar(j015, j020, role=Role.CHORD),
                        Bar(j020, j022, role=Role.CHORD),
                        Bar(j017, j020, role=Role.DIAGONAL_BRACE),
                        Bar(j020, j013, role=Role.DIAGONAL_BRACE),
                        Bar(j013, j015, role=Role.DIAGONAL_BRACE),
                        Bar(j015, j010, role=Role.DIAGONAL_BRACE),
                        Bar(j010, j009, role=Role.TRANSVERSE_BRACE),
                        Bar(j009, j007, role=Role.DIAGONAL_BRACE),
                        Bar(j007, j005, role=Role.DIAGONAL_BRACE),
                        Bar(j005, j003, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j004, j006, role=Role.DIAGONAL_BRACE),
                        Bar(j006, j008, role=Role.DIAGONAL_BRACE),
                        Bar(j008, j012, role=Role.DIAGONAL_BRACE),
                        Bar(j012, j011, role=Role.TRANSVERSE_BRACE),
                        Bar(j011, j016, role=Role.DIAGONAL_BRACE),
                        Bar(j016, j014, role=Role.DIAGONAL_BRACE),
                        Bar(j014, j021, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j018, role=Role.DIAGONAL_BRACE),
                        Bar(j023, j021, role=Role.CHORD),
                        Bar(j021, j016, role=Role.CHORD),
                        Bar(j016, j012, role=Role.CHORD),
                        Bar(j012, j006, role=Role.CHORD),
                        Bar(j006, j002, role=Role.CHORD),
                        Bar(j002, j004, role=Role.CHORD),
                        Bar(j004, j008, role=Role.CHORD),
                        Bar(j008, j011, role=Role.CHORD),
                        Bar(j011, j014, role=Role.CHORD),
                        Bar(j014, j018, role=Role.CHORD),
                    ),
                )
            ),
        ),
    )


DA_4_DE_2018_1_WA140 = _da_4_de_2018_1_wa140()


def _da_4_de_2018_1_wa160() -> Tower[LowestCrossarm]:
    """DA-4-DE-2018.1 WA160: each joint written once, by its key."""
    j001 = Point(m(-8.6), m(0), m(32))
    j002 = Point(m(8.6), m(0), m(32))
    j003 = Point(m(-8.46), m(0), m(31.91))
    j004 = Point(m(8.45), m(0), m(31.91))
    j005 = Point(m(-8.04), m(0), m(31.33))
    j006 = Point(m(8.04), m(0), m(31.33))
    j007 = Point(m(-7.2), m(0), m(31.08))
    j008 = Point(m(7.19), m(0), m(31.08))
    j009 = Point(m(-6.98), m(0), m(30.16))
    j010 = Point(m(-5.66), m(0), m(30.16))
    j011 = Point(m(5.65), m(0), m(30.16))
    j012 = Point(m(6.98), m(0), m(30.16))
    j013 = Point(m(-3.68), m(0), m(29.03))
    j014 = Point(m(3.68), m(0), m(29.03))
    j015 = Point(m(-5.55), m(0), m(28.68))
    j016 = Point(m(5.54), m(0), m(28.68))
    j017 = Point(m(-1.37), m(0), m(27.79))
    j018 = Point(m(1.37), m(0), m(27.79))
    j019 = Point(m(0), m(0), m(27.03))
    j020 = Point(m(-3.68), m(0), m(26.96))
    j021 = Point(m(3.69), m(0), m(26.96))
    j022 = Point(m(-1.37), m(0), m(25.03))
    j023 = Point(m(1.37), m(0), m(25.03))
    j024 = Point(m(-5.77), m(0), m(23.99))
    j025 = Point(m(5.76), m(0), m(23.99))
    j026 = Point(m(-7.67), m(0), m(23.54))
    j027 = Point(m(7.67), m(0), m(23.54))
    j028 = Point(m(-1.44), m(0), m(23.52))
    j029 = Point(m(1.44), m(0), m(23.52))
    j030 = Point(m(-3.64), m(0), m(23.45))
    j031 = Point(m(3.64), m(0), m(23.45))
    j032 = Point(m(-10.87), m(0), m(22.79))
    j033 = Point(m(10.86), m(0), m(22.79))
    j034 = Point(m(-11.64), m(0), m(22.61))
    j035 = Point(m(11.62), m(0), m(22.61))
    j036 = Point(m(-9.67), m(0), m(22.02))
    j037 = Point(m(9.65), m(0), m(22.02))
    j038 = Point(m(-11.64), m(0), m(22))
    j039 = Point(m(-10.87), m(0), m(22))
    j040 = Point(m(-9.59), m(0), m(22))
    j041 = Point(m(-7.67), m(0), m(22))
    j042 = Point(m(-5.76), m(0), m(22))
    j043 = Point(m(-3.63), m(0), m(22))
    j044 = Point(m(-1.51), m(0), m(22))
    j045 = Point(m(1.51), m(0), m(22))
    j046 = Point(m(3.64), m(0), m(22))
    j047 = Point(m(5.75), m(0), m(22))
    j048 = Point(m(7.67), m(0), m(22))
    j049 = Point(m(9.59), m(0), m(22))
    j050 = Point(m(10.86), m(0), m(22))
    j051 = Point(m(11.62), m(0), m(22))
    j052 = Point(m(-11.25), m(0), m(22))
    j053 = Point(m(11.25), m(0), m(22))
    j054 = Point(m(-1.6), m(0), m(20))
    j055 = Point(m(1.6), m(0), m(20))
    j056 = Point(m(-1.68), m(0), m(18))
    j057 = Point(m(1.69), m(0), m(18))
    j058 = Point(m(-1.77), m(0), m(16))
    j059 = Point(m(1.78), m(0), m(16))
    j060 = Point(m(-8.01), m(0), m(14.61))
    j061 = Point(m(8), m(0), m(14.61))
    j062 = Point(m(-4.89), m(0), m(14))
    j063 = Point(m(-1.86), m(0), m(14))
    j064 = Point(m(1.87), m(0), m(14))
    j065 = Point(m(4.88), m(0), m(14))
    j066 = Point(m(-10.12), m(0), m(13.93))
    j067 = Point(m(10.11), m(0), m(13.93))
    j068 = Point(m(-13.7), m(0), m(12.79))
    j069 = Point(m(13.69), m(0), m(12.79))
    j070 = Point(m(-14.31), m(0), m(12.6))
    j071 = Point(m(14.3), m(0), m(12.6))
    j072 = Point(m(-14), m(0), m(12))
    j073 = Point(m(14), m(0), m(12))
    j074 = Point(m(-14.31), m(0), m(12))
    j075 = Point(m(-13.7), m(0), m(12))
    j076 = Point(m(-12.7), m(0), m(12))
    j077 = Point(m(-10.12), m(0), m(12))
    j078 = Point(m(-8), m(0), m(12))
    j079 = Point(m(-4.87), m(0), m(12))
    j080 = Point(m(-1.95), m(0), m(12))
    j081 = Point(m(1.96), m(0), m(12))
    j082 = Point(m(4.86), m(0), m(12))
    j083 = Point(m(8), m(0), m(12))
    j084 = Point(m(10.11), m(0), m(12))
    j085 = Point(m(12.69), m(0), m(12))
    j086 = Point(m(13.69), m(0), m(12))
    j087 = Point(m(14.3), m(0), m(12))
    j088 = Point(m(-2.06), m(0), m(9.52))
    j089 = Point(m(2.07), m(0), m(9.52))
    j090 = Point(m(-2.18), m(0), m(6.93))
    j091 = Point(m(2.18), m(0), m(6.93))
    j092 = Point(m(-2.31), m(0), m(4.06))
    j093 = Point(m(2.31), m(0), m(4.06))
    j094 = Point(m(-6.51), m(0), m(3.05))
    j095 = Point(m(6.49), m(0), m(3.05))
    j096 = Point(m(-4.43), m(0), m(2.03))
    j097 = Point(m(4.42), m(0), m(2.03))
    j098 = Point(m(-11.01), m(0), m(1.84))
    j099 = Point(m(10.99), m(0), m(1.84))
    j100 = Point(m(-8.76), m(0), m(1.53))
    j101 = Point(m(8.76), m(0), m(1.53))
    j102 = Point(m(-2.43), m(0), m(1.33))
    j103 = Point(m(2.43), m(0), m(1.33))
    j104 = Point(m(-13.27), m(0), m(1.22))
    j105 = Point(m(13.26), m(0), m(1.22))
    j106 = Point(m(-15.64), m(0), m(0.58))
    j107 = Point(m(15.63), m(0), m(0.58))
    j108 = Point(m(-15.64), m(0), m(0))
    j109 = Point(m(-13.27), m(0), m(0))
    j110 = Point(m(-11), m(0), m(0))
    j111 = Point(m(-6.5), m(0), m(0))
    j112 = Point(m(-2.49), m(0), m(0))
    j113 = Point(m(2.49), m(0), m(0))
    j114 = Point(m(6.5), m(0), m(0))
    j115 = Point(m(11), m(0), m(0))
    j116 = Point(m(13.26), m(0), m(0))
    j117 = Point(m(15.63), m(0), m(0))
    j118 = Point(m(-15.5), m(0), m(0))
    j119 = Point(m(0), m(0), m(0))
    j120 = Point(m(15.5), m(0), m(0))
    j121 = Point(m(-2.61), m(0), m(-2.73))
    j122 = Point(m(2.61), m(0), m(-2.73))
    j123 = Point(m(-2.77), m(0), m(-4.65))
    j124 = Point(m(-1.3), m(0), m(-4.65))
    j125 = Point(m(1.31), m(0), m(-4.65))
    j126 = Point(m(2.77), m(0), m(-4.65))
    j127 = Point(m(-2.94), m(0), m(-6.56))
    j128 = Point(m(0), m(0), m(-6.56))
    j129 = Point(m(2.94), m(0), m(-6.56))
    j130 = Point(m(-3.14), m(0), m(-8.95))
    j131 = Point(m(-1.62), m(0), m(-8.95))
    j132 = Point(m(1.63), m(0), m(-8.95))
    j133 = Point(m(3.14), m(0), m(-8.95))
    j134 = Point(m(-3.25), m(0), m(-11.35))
    j135 = Point(m(3.25), m(0), m(-11.35))
    j136 = Point(m(-3.62), m(0), m(-14.56))
    j137 = Point(m(-1.62), m(0), m(-14.56))
    j138 = Point(m(1.63), m(0), m(-14.56))
    j139 = Point(m(3.62), m(0), m(-14.56))
    j140 = Point(m(-3.88), m(0), m(-17.64))
    j141 = Point(m(3.89), m(0), m(-17.64))
    j142 = Point(m(-4.13), m(0), m(-20.6))
    j143 = Point(m(-1.43), m(0), m(-20.6))
    j144 = Point(m(1.44), m(0), m(-20.6))
    j145 = Point(m(4.14), m(0), m(-20.6))
    j146 = Point(m(-4.34), m(0), m(-23.07))
    j147 = Point(m(-2.68), m(0), m(-23.07))
    j148 = Point(m(2.69), m(0), m(-23.07))
    j149 = Point(m(4.35), m(0), m(-23.07))
    j150 = Point(m(-4.68), m(0), m(-27))
    j151 = Point(m(4.69), m(0), m(-27))
    return Tower(
        name="DA-4-DE-2018.1 WA160",
        datum=LowestCrossarm((m(27), m(33))),
        voltages=(kv(380),),
        line_angles=(),
        attachments=(
            Mount(Wire.SHIELD, Point(m(-8.6), m(0), m(32)), Hold.CLAMP),
            Mount(Wire.SHIELD, Point(m(8.6), m(0), m(32)), Hold.CLAMP),
            Mount(Wire.PHASE, Point(m(-11.25), m(0), m(22)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(11.25), m(0), m(22)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-14), m(0), m(12)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-8), m(0), m(12)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(8), m(0), m(12)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(14), m(0), m(12)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-15.5), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-11), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-6.5), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.SHIELD, Point(m(0), m(0), m(0)), Hold.CLAMP),
            Mount(Wire.PHASE, Point(m(6.5), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(11), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(15.5), m(0), m(0)), Hold.STRAIN),
        ),
        bases=(),
        body=(
            Body(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j143, j138, role=Role.DIAGONAL_BRACE),
                        Bar(j144, j137, role=Role.DIAGONAL_BRACE),
                        Bar(j141, j140, role=Role.TRANSVERSE_BRACE),
                        Bar(j022, j023, role=Role.TRANSVERSE_BRACE),
                        Bar(j044, j045, role=Role.TRANSVERSE_BRACE),
                        Bar(j080, j081, role=Role.TRANSVERSE_BRACE),
                        Bar(j058, j059, role=Role.TRANSVERSE_BRACE),
                        Bar(j081, j088, role=Role.DIAGONAL_BRACE),
                        Bar(j088, j091, role=Role.DIAGONAL_BRACE),
                        Bar(j091, j092, role=Role.DIAGONAL_BRACE),
                        Bar(j093, j090, role=Role.DIAGONAL_BRACE),
                        Bar(j090, j089, role=Role.DIAGONAL_BRACE),
                        Bar(j089, j080, role=Role.DIAGONAL_BRACE),
                        Bar(j122, j119, role=Role.DIAGONAL_BRACE),
                        Bar(j119, j102, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j119, role=Role.DIAGONAL_BRACE),
                        Bar(j119, j103, role=Role.DIAGONAL_BRACE),
                        Bar(j103, j092, role=Role.DIAGONAL_BRACE),
                        Bar(j102, j093, role=Role.DIAGONAL_BRACE),
                        Bar(j132, j128, role=Role.DIAGONAL_BRACE),
                        Bar(j128, j125, role=Role.DIAGONAL_BRACE),
                        Bar(j129, j128, role=Role.TRANSVERSE_BRACE),
                        Bar(j121, j112, role=Role.CHORD),
                        Bar(j112, j102, role=Role.CHORD),
                        Bar(j102, j092, role=Role.CHORD),
                        Bar(j092, j090, role=Role.CHORD),
                        Bar(j090, j088, role=Role.CHORD),
                        Bar(j088, j080, role=Role.CHORD),
                        Bar(j080, j063, role=Role.CHORD),
                        Bar(j063, j058, role=Role.CHORD),
                        Bar(j059, j063, role=Role.DIAGONAL_BRACE),
                        Bar(j063, j081, role=Role.DIAGONAL_BRACE),
                        Bar(j081, j089, role=Role.CHORD),
                        Bar(j089, j091, role=Role.CHORD),
                        Bar(j091, j093, role=Role.CHORD),
                        Bar(j093, j103, role=Role.CHORD),
                        Bar(j103, j113, role=Role.CHORD),
                        Bar(j113, j122, role=Role.CHORD),
                        Bar(j058, j064, role=Role.DIAGONAL_BRACE),
                        Bar(j064, j080, role=Role.DIAGONAL_BRACE),
                        Bar(j058, j056, role=Role.CHORD),
                        Bar(j056, j054, role=Role.CHORD),
                        Bar(j054, j044, role=Role.CHORD),
                        Bar(j044, j028, role=Role.CHORD),
                        Bar(j028, j022, role=Role.CHORD),
                        Bar(j045, j028, role=Role.DIAGONAL_BRACE),
                        Bar(j028, j023, role=Role.DIAGONAL_BRACE),
                        Bar(j023, j029, role=Role.CHORD),
                        Bar(j029, j045, role=Role.CHORD),
                        Bar(j045, j055, role=Role.CHORD),
                        Bar(j055, j057, role=Role.CHORD),
                        Bar(j057, j059, role=Role.CHORD),
                        Bar(j059, j064, role=Role.CHORD),
                        Bar(j064, j081, role=Role.CHORD),
                        Bar(j059, j056, role=Role.DIAGONAL_BRACE),
                        Bar(j056, j055, role=Role.DIAGONAL_BRACE),
                        Bar(j055, j044, role=Role.DIAGONAL_BRACE),
                        Bar(j044, j029, role=Role.DIAGONAL_BRACE),
                        Bar(j029, j022, role=Role.DIAGONAL_BRACE),
                        Bar(j058, j057, role=Role.DIAGONAL_BRACE),
                        Bar(j057, j054, role=Role.DIAGONAL_BRACE),
                        Bar(j054, j045, role=Role.DIAGONAL_BRACE),
                        Bar(j112, j119, role=Role.TRANSVERSE_BRACE),
                        Bar(j119, j113, role=Role.TRANSVERSE_BRACE),
                        Bar(j092, j093, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        legs=(
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j150, j146, role=Role.CHORD),
                        Bar(j146, j142, role=Role.CHORD),
                        Bar(j142, j140, role=Role.CHORD),
                        Bar(j140, j136, role=Role.CHORD),
                        Bar(j136, j130, role=Role.CHORD),
                        Bar(j130, j127, role=Role.CHORD),
                        Bar(j127, j123, role=Role.CHORD),
                        Bar(j123, j121, role=Role.CHORD),
                        Bar(j150, j147, role=Role.DIAGONAL_BRACE),
                        Bar(j147, j143, role=Role.DIAGONAL_BRACE),
                        Bar(j137, j134, role=Role.DIAGONAL_BRACE),
                        Bar(j143, j142, role=Role.TRANSVERSE_BRACE),
                        Bar(j147, j146, role=Role.TRANSVERSE_BRACE),
                        Bar(j137, j136, role=Role.TRANSVERSE_BRACE),
                        Bar(j147, j142, role=Role.DIAGONAL_BRACE),
                        Bar(j143, j140, role=Role.DIAGONAL_BRACE),
                        Bar(j140, j137, role=Role.DIAGONAL_BRACE),
                        Bar(j128, j124, role=Role.DIAGONAL_BRACE),
                        Bar(j124, j121, role=Role.DIAGONAL_BRACE),
                        Bar(j134, j131, role=Role.DIAGONAL_BRACE),
                        Bar(j131, j128, role=Role.DIAGONAL_BRACE),
                        Bar(j128, j127, role=Role.TRANSVERSE_BRACE),
                        Bar(j127, j124, role=Role.DIAGONAL_BRACE),
                        Bar(j127, j131, role=Role.DIAGONAL_BRACE),
                        Bar(j130, j131, role=Role.TRANSVERSE_BRACE),
                        Bar(j123, j124, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j122, j126, role=Role.CHORD),
                        Bar(j126, j129, role=Role.CHORD),
                        Bar(j129, j133, role=Role.CHORD),
                        Bar(j133, j139, role=Role.CHORD),
                        Bar(j139, j141, role=Role.CHORD),
                        Bar(j141, j145, role=Role.CHORD),
                        Bar(j145, j149, role=Role.CHORD),
                        Bar(j149, j151, role=Role.CHORD),
                        Bar(j138, j135, role=Role.DIAGONAL_BRACE),
                        Bar(j151, j148, role=Role.DIAGONAL_BRACE),
                        Bar(j148, j144, role=Role.DIAGONAL_BRACE),
                        Bar(j144, j145, role=Role.TRANSVERSE_BRACE),
                        Bar(j148, j149, role=Role.TRANSVERSE_BRACE),
                        Bar(j138, j139, role=Role.TRANSVERSE_BRACE),
                        Bar(j148, j145, role=Role.DIAGONAL_BRACE),
                        Bar(j144, j141, role=Role.DIAGONAL_BRACE),
                        Bar(j141, j138, role=Role.DIAGONAL_BRACE),
                        Bar(j135, j132, role=Role.DIAGONAL_BRACE),
                        Bar(j125, j122, role=Role.DIAGONAL_BRACE),
                        Bar(j125, j129, role=Role.DIAGONAL_BRACE),
                        Bar(j129, j132, role=Role.DIAGONAL_BRACE),
                        Bar(j125, j126, role=Role.TRANSVERSE_BRACE),
                        Bar(j132, j133, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        head=(
            Head(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j018, j023, role=Role.CHORD),
                        Bar(j023, j019, role=Role.DIAGONAL_BRACE),
                        Bar(j019, j022, role=Role.DIAGONAL_BRACE),
                        Bar(j018, j019, role=Role.DIAGONAL_BRACE),
                        Bar(j019, j017, role=Role.DIAGONAL_BRACE),
                        Bar(j022, j017, role=Role.CHORD),
                    ),
                )
            ),
        ),
        crossarms=(
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j038, j052, role=Role.CHORD),
                        Bar(j052, j039, role=Role.CHORD),
                        Bar(j039, j036, role=Role.CHORD),
                        Bar(j036, j040, role=Role.CHORD),
                        Bar(j040, j041, role=Role.CHORD),
                        Bar(j041, j042, role=Role.CHORD),
                        Bar(j042, j043, role=Role.CHORD),
                        Bar(j043, j044, role=Role.CHORD),
                        Bar(j034, j032, role=Role.CHORD),
                        Bar(j032, j026, role=Role.CHORD),
                        Bar(j026, j024, role=Role.CHORD),
                        Bar(j024, j022, role=Role.CHORD),
                        Bar(j034, j038, role=Role.CHORD),
                        Bar(j044, j030, role=Role.DIAGONAL_BRACE),
                        Bar(j030, j043, role=Role.TRANSVERSE_BRACE),
                        Bar(j024, j042, role=Role.TRANSVERSE_BRACE),
                        Bar(j042, j030, role=Role.DIAGONAL_BRACE),
                        Bar(j030, j022, role=Role.DIAGONAL_BRACE),
                        Bar(j041, j026, role=Role.TRANSVERSE_BRACE),
                        Bar(j026, j042, role=Role.DIAGONAL_BRACE),
                        Bar(j026, j036, role=Role.DIAGONAL_BRACE),
                        Bar(j039, j032, role=Role.TRANSVERSE_BRACE),
                        Bar(j032, j036, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j045, j046, role=Role.CHORD),
                        Bar(j046, j047, role=Role.CHORD),
                        Bar(j047, j048, role=Role.CHORD),
                        Bar(j048, j049, role=Role.CHORD),
                        Bar(j049, j037, role=Role.CHORD),
                        Bar(j037, j050, role=Role.CHORD),
                        Bar(j050, j053, role=Role.CHORD),
                        Bar(j053, j051, role=Role.CHORD),
                        Bar(j051, j035, role=Role.CHORD),
                        Bar(j035, j033, role=Role.CHORD),
                        Bar(j033, j027, role=Role.CHORD),
                        Bar(j027, j025, role=Role.CHORD),
                        Bar(j025, j023, role=Role.CHORD),
                        Bar(j033, j050, role=Role.TRANSVERSE_BRACE),
                        Bar(j033, j037, role=Role.DIAGONAL_BRACE),
                        Bar(j048, j027, role=Role.TRANSVERSE_BRACE),
                        Bar(j027, j047, role=Role.DIAGONAL_BRACE),
                        Bar(j027, j037, role=Role.DIAGONAL_BRACE),
                        Bar(j025, j047, role=Role.TRANSVERSE_BRACE),
                        Bar(j047, j031, role=Role.DIAGONAL_BRACE),
                        Bar(j031, j023, role=Role.DIAGONAL_BRACE),
                        Bar(j045, j031, role=Role.DIAGONAL_BRACE),
                        Bar(j031, j046, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j074, j072, role=Role.CHORD),
                        Bar(j072, j075, role=Role.CHORD),
                        Bar(j075, j076, role=Role.CHORD),
                        Bar(j076, j077, role=Role.CHORD),
                        Bar(j077, j078, role=Role.CHORD),
                        Bar(j078, j079, role=Role.CHORD),
                        Bar(j079, j080, role=Role.CHORD),
                        Bar(j074, j070, role=Role.CHORD),
                        Bar(j070, j068, role=Role.CHORD),
                        Bar(j068, j066, role=Role.CHORD),
                        Bar(j066, j060, role=Role.CHORD),
                        Bar(j060, j058, role=Role.CHORD),
                        Bar(j068, j075, role=Role.TRANSVERSE_BRACE),
                        Bar(j058, j062, role=Role.DIAGONAL_BRACE),
                        Bar(j062, j078, role=Role.DIAGONAL_BRACE),
                        Bar(j078, j060, role=Role.TRANSVERSE_BRACE),
                        Bar(j068, j076, role=Role.DIAGONAL_BRACE),
                        Bar(j076, j066, role=Role.DIAGONAL_BRACE),
                        Bar(j066, j078, role=Role.DIAGONAL_BRACE),
                        Bar(j077, j066, role=Role.TRANSVERSE_BRACE),
                        Bar(j080, j062, role=Role.DIAGONAL_BRACE),
                        Bar(j062, j079, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j081, j082, role=Role.CHORD),
                        Bar(j082, j083, role=Role.CHORD),
                        Bar(j083, j084, role=Role.CHORD),
                        Bar(j084, j085, role=Role.CHORD),
                        Bar(j085, j086, role=Role.CHORD),
                        Bar(j086, j073, role=Role.CHORD),
                        Bar(j073, j087, role=Role.CHORD),
                        Bar(j087, j071, role=Role.CHORD),
                        Bar(j071, j069, role=Role.CHORD),
                        Bar(j069, j067, role=Role.CHORD),
                        Bar(j067, j061, role=Role.CHORD),
                        Bar(j061, j059, role=Role.CHORD),
                        Bar(j069, j086, role=Role.TRANSVERSE_BRACE),
                        Bar(j069, j085, role=Role.DIAGONAL_BRACE),
                        Bar(j085, j067, role=Role.DIAGONAL_BRACE),
                        Bar(j067, j083, role=Role.DIAGONAL_BRACE),
                        Bar(j083, j061, role=Role.TRANSVERSE_BRACE),
                        Bar(j084, j067, role=Role.TRANSVERSE_BRACE),
                        Bar(j081, j065, role=Role.DIAGONAL_BRACE),
                        Bar(j065, j082, role=Role.TRANSVERSE_BRACE),
                        Bar(j059, j065, role=Role.DIAGONAL_BRACE),
                        Bar(j065, j083, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j092, j094, role=Role.CHORD),
                        Bar(j094, j098, role=Role.CHORD),
                        Bar(j098, j104, role=Role.CHORD),
                        Bar(j104, j106, role=Role.CHORD),
                        Bar(j106, j108, role=Role.CHORD),
                        Bar(j108, j118, role=Role.CHORD),
                        Bar(j118, j109, role=Role.CHORD),
                        Bar(j109, j110, role=Role.CHORD),
                        Bar(j110, j111, role=Role.CHORD),
                        Bar(j111, j112, role=Role.CHORD),
                        Bar(j094, j100, role=Role.DIAGONAL_BRACE),
                        Bar(j100, j110, role=Role.DIAGONAL_BRACE),
                        Bar(j110, j104, role=Role.DIAGONAL_BRACE),
                        Bar(j111, j096, role=Role.DIAGONAL_BRACE),
                        Bar(j096, j092, role=Role.DIAGONAL_BRACE),
                        Bar(j096, j112, role=Role.DIAGONAL_BRACE),
                        Bar(j104, j109, role=Role.TRANSVERSE_BRACE),
                        Bar(j094, j111, role=Role.TRANSVERSE_BRACE),
                        Bar(j098, j110, role=Role.TRANSVERSE_BRACE),
                        Bar(j111, j100, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j113, j114, role=Role.CHORD),
                        Bar(j114, j115, role=Role.CHORD),
                        Bar(j115, j116, role=Role.CHORD),
                        Bar(j116, j120, role=Role.CHORD),
                        Bar(j120, j117, role=Role.CHORD),
                        Bar(j117, j107, role=Role.CHORD),
                        Bar(j107, j105, role=Role.CHORD),
                        Bar(j105, j099, role=Role.CHORD),
                        Bar(j099, j095, role=Role.CHORD),
                        Bar(j095, j093, role=Role.CHORD),
                        Bar(j095, j101, role=Role.DIAGONAL_BRACE),
                        Bar(j101, j115, role=Role.DIAGONAL_BRACE),
                        Bar(j115, j105, role=Role.DIAGONAL_BRACE),
                        Bar(j114, j097, role=Role.DIAGONAL_BRACE),
                        Bar(j097, j093, role=Role.DIAGONAL_BRACE),
                        Bar(j097, j113, role=Role.DIAGONAL_BRACE),
                        Bar(j105, j116, role=Role.TRANSVERSE_BRACE),
                        Bar(j095, j114, role=Role.TRANSVERSE_BRACE),
                        Bar(j099, j115, role=Role.TRANSVERSE_BRACE),
                        Bar(j114, j101, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        peaks=(
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j017, j013, role=Role.CHORD),
                        Bar(j013, j010, role=Role.CHORD),
                        Bar(j010, j007, role=Role.CHORD),
                        Bar(j007, j003, role=Role.CHORD),
                        Bar(j003, j001, role=Role.CHORD),
                        Bar(j001, j005, role=Role.CHORD),
                        Bar(j005, j009, role=Role.CHORD),
                        Bar(j009, j015, role=Role.CHORD),
                        Bar(j015, j020, role=Role.CHORD),
                        Bar(j020, j022, role=Role.CHORD),
                        Bar(j017, j020, role=Role.DIAGONAL_BRACE),
                        Bar(j020, j013, role=Role.DIAGONAL_BRACE),
                        Bar(j013, j015, role=Role.DIAGONAL_BRACE),
                        Bar(j015, j010, role=Role.DIAGONAL_BRACE),
                        Bar(j010, j009, role=Role.TRANSVERSE_BRACE),
                        Bar(j009, j007, role=Role.DIAGONAL_BRACE),
                        Bar(j007, j005, role=Role.DIAGONAL_BRACE),
                        Bar(j005, j003, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j008, j012, role=Role.DIAGONAL_BRACE),
                        Bar(j012, j011, role=Role.TRANSVERSE_BRACE),
                        Bar(j011, j016, role=Role.DIAGONAL_BRACE),
                        Bar(j016, j014, role=Role.DIAGONAL_BRACE),
                        Bar(j014, j021, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j018, role=Role.DIAGONAL_BRACE),
                        Bar(j023, j021, role=Role.CHORD),
                        Bar(j021, j016, role=Role.CHORD),
                        Bar(j016, j012, role=Role.CHORD),
                        Bar(j012, j006, role=Role.CHORD),
                        Bar(j006, j002, role=Role.CHORD),
                        Bar(j002, j004, role=Role.CHORD),
                        Bar(j004, j008, role=Role.CHORD),
                        Bar(j008, j011, role=Role.CHORD),
                        Bar(j011, j014, role=Role.CHORD),
                        Bar(j014, j018, role=Role.CHORD),
                        Bar(j008, j006, role=Role.DIAGONAL_BRACE),
                        Bar(j006, j004, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
    )


DA_4_DE_2018_1_WA160 = _da_4_de_2018_1_wa160()


def _da_4_de_2018_1_we_wadiff_140() -> Tower[LowestCrossarm]:
    """DA-4-DE-2018.1 WE WAdiff 140: each joint written once, by its key."""
    j001 = Point(m(-8.6), m(0), m(32.5))
    j002 = Point(m(8.6), m(0), m(32.5))
    j003 = Point(m(-8.48), m(0), m(32.4))
    j004 = Point(m(8.46), m(0), m(32.4))
    j005 = Point(m(-8.15), m(0), m(31.79))
    j006 = Point(m(8.15), m(0), m(31.79))
    j007 = Point(m(-7.35), m(0), m(31.54))
    j008 = Point(m(7.34), m(0), m(31.54))
    j009 = Point(m(-7.24), m(0), m(30.56))
    j010 = Point(m(-5.88), m(0), m(30.56))
    j011 = Point(m(5.88), m(0), m(30.56))
    j012 = Point(m(7.24), m(0), m(30.56))
    j013 = Point(m(-3.93), m(0), m(29.38))
    j014 = Point(m(3.93), m(0), m(29.38))
    j015 = Point(m(-5.9), m(0), m(29.01))
    j016 = Point(m(5.9), m(0), m(29.01))
    j017 = Point(m(-1.51), m(0), m(28.07))
    j018 = Point(m(1.51), m(0), m(28.07))
    j019 = Point(m(-0.01), m(0), m(27.28))
    j020 = Point(m(-4.02), m(0), m(27.22))
    j021 = Point(m(4.02), m(0), m(27.22))
    j022 = Point(m(-1.51), m(0), m(25.19))
    j023 = Point(m(1.51), m(0), m(25.19))
    j024 = Point(m(-6.4), m(0), m(24.09))
    j025 = Point(m(6.4), m(0), m(24.09))
    j026 = Point(m(-8.53), m(0), m(23.62))
    j027 = Point(m(8.52), m(0), m(23.62))
    j028 = Point(m(-1.59), m(0), m(23.59))
    j029 = Point(m(1.59), m(0), m(23.59))
    j030 = Point(m(-4.04), m(0), m(23.54))
    j031 = Point(m(4.04), m(0), m(23.54))
    j032 = Point(m(-12.08), m(0), m(22.83))
    j033 = Point(m(12.07), m(0), m(22.83))
    j034 = Point(m(-12.94), m(0), m(22.64))
    j035 = Point(m(12.91), m(0), m(22.64))
    j036 = Point(m(-10.74), m(0), m(22.02))
    j037 = Point(m(10.74), m(0), m(22.02))
    j038 = Point(m(-12.94), m(0), m(22))
    j039 = Point(m(-12.08), m(0), m(22))
    j040 = Point(m(-10.66), m(0), m(22))
    j041 = Point(m(-8.52), m(0), m(22))
    j042 = Point(m(-6.39), m(0), m(22))
    j043 = Point(m(-4.03), m(0), m(22))
    j044 = Point(m(-1.66), m(0), m(22))
    j045 = Point(m(1.66), m(0), m(22))
    j046 = Point(m(4.03), m(0), m(22))
    j047 = Point(m(6.39), m(0), m(22))
    j048 = Point(m(8.52), m(0), m(22))
    j049 = Point(m(10.65), m(0), m(22))
    j050 = Point(m(12.07), m(0), m(22))
    j051 = Point(m(12.91), m(0), m(22))
    j052 = Point(m(-12.5), m(0), m(22))
    j053 = Point(m(12.5), m(0), m(22))
    j054 = Point(m(-1.76), m(0), m(20))
    j055 = Point(m(1.76), m(0), m(20))
    j056 = Point(m(-1.87), m(0), m(18.01))
    j057 = Point(m(1.86), m(0), m(18.01))
    j058 = Point(m(-1.97), m(0), m(16))
    j059 = Point(m(1.97), m(0), m(16))
    j060 = Point(m(-9.51), m(0), m(14.61))
    j061 = Point(m(9.49), m(0), m(14.61))
    j062 = Point(m(-5.72), m(0), m(14))
    j063 = Point(m(-2.07), m(0), m(14))
    j064 = Point(m(2.07), m(0), m(14))
    j065 = Point(m(5.71), m(0), m(14))
    j066 = Point(m(-11.8), m(0), m(13.94))
    j067 = Point(m(11.78), m(0), m(13.94))
    j068 = Point(m(-15.68), m(0), m(12.79))
    j069 = Point(m(15.67), m(0), m(12.79))
    j070 = Point(m(-16.33), m(0), m(12.6))
    j071 = Point(m(16.32), m(0), m(12.6))
    j072 = Point(m(-16.33), m(0), m(12))
    j073 = Point(m(-16), m(0), m(12))
    j074 = Point(m(-15.68), m(0), m(12))
    j075 = Point(m(-14.6), m(0), m(12))
    j076 = Point(m(-11.8), m(0), m(12))
    j077 = Point(m(-9.5), m(0), m(12))
    j078 = Point(m(-5.69), m(0), m(12))
    j079 = Point(m(-2.17), m(0), m(12))
    j080 = Point(m(2.17), m(0), m(12))
    j081 = Point(m(5.69), m(0), m(12))
    j082 = Point(m(9.5), m(0), m(12))
    j083 = Point(m(11.78), m(0), m(12))
    j084 = Point(m(14.59), m(0), m(12))
    j085 = Point(m(15.67), m(0), m(12))
    j086 = Point(m(16), m(0), m(12))
    j087 = Point(m(16.32), m(0), m(12))
    j088 = Point(m(-2.3), m(0), m(9.51))
    j089 = Point(m(2.3), m(0), m(9.51))
    j090 = Point(m(-2.43), m(0), m(6.93))
    j091 = Point(m(2.43), m(0), m(6.93))
    j092 = Point(m(-2.58), m(0), m(4.05))
    j093 = Point(m(2.58), m(0), m(4.05))
    j094 = Point(m(-7.21), m(0), m(3.04))
    j095 = Point(m(7.19), m(0), m(3.04))
    j096 = Point(m(-4.9), m(0), m(2.03))
    j097 = Point(m(4.9), m(0), m(2.03))
    j098 = Point(m(-12.11), m(0), m(1.83))
    j099 = Point(m(12.09), m(0), m(1.83))
    j100 = Point(m(-9.66), m(0), m(1.53))
    j101 = Point(m(9.66), m(0), m(1.53))
    j102 = Point(m(-2.71), m(0), m(1.33))
    j103 = Point(m(2.71), m(0), m(1.33))
    j104 = Point(m(-14.58), m(0), m(1.21))
    j105 = Point(m(14.56), m(0), m(1.21))
    j106 = Point(m(-17.15), m(0), m(0.57))
    j107 = Point(m(17.14), m(0), m(0.57))
    j108 = Point(m(-17.15), m(0), m(0))
    j109 = Point(m(-14.58), m(0), m(0))
    j110 = Point(m(-12.1), m(0), m(0))
    j111 = Point(m(-7.2), m(0), m(0))
    j112 = Point(m(-2.78), m(0), m(0))
    j113 = Point(m(2.78), m(0), m(0))
    j114 = Point(m(7.2), m(0), m(0))
    j115 = Point(m(12.1), m(0), m(0))
    j116 = Point(m(14.56), m(0), m(0))
    j117 = Point(m(17.14), m(0), m(0))
    j118 = Point(m(-17), m(0), m(0))
    j119 = Point(m(0), m(0), m(0))
    j120 = Point(m(17), m(0), m(0))
    j121 = Point(m(-2.89), m(0), m(-2.13))
    j122 = Point(m(2.89), m(0), m(-2.13))
    j123 = Point(m(-3.07), m(0), m(-3.62))
    j124 = Point(m(-1.45), m(0), m(-3.62))
    j125 = Point(m(1.45), m(0), m(-3.62))
    j126 = Point(m(3.07), m(0), m(-3.62))
    j127 = Point(m(-3.25), m(0), m(-5.12))
    j128 = Point(m(-0.01), m(0), m(-5.12))
    j129 = Point(m(3.25), m(0), m(-5.12))
    j130 = Point(m(-3.48), m(0), m(-6.98))
    j131 = Point(m(-1.8), m(0), m(-6.98))
    j132 = Point(m(1.8), m(0), m(-6.98))
    j133 = Point(m(3.48), m(0), m(-6.98))
    j134 = Point(m(-3.61), m(0), m(-8.83))
    j135 = Point(m(3.61), m(0), m(-8.83))
    j136 = Point(m(-4.01), m(0), m(-11.33))
    j137 = Point(m(-1.8), m(0), m(-11.33))
    j138 = Point(m(1.8), m(0), m(-11.33))
    j139 = Point(m(4.01), m(0), m(-11.33))
    j140 = Point(m(-4.3), m(0), m(-13.73))
    j141 = Point(m(4.3), m(0), m(-13.73))
    j142 = Point(m(-4.58), m(0), m(-16.02))
    j143 = Point(m(-1.59), m(0), m(-16.02))
    j144 = Point(m(1.59), m(0), m(-16.02))
    j145 = Point(m(4.58), m(0), m(-16.02))
    j146 = Point(m(-4.82), m(0), m(-17.94))
    j147 = Point(m(-2.98), m(0), m(-17.94))
    j148 = Point(m(2.98), m(0), m(-17.94))
    j149 = Point(m(4.82), m(0), m(-17.94))
    j150 = Point(m(-5.19), m(0), m(-21))
    j151 = Point(m(5.19), m(0), m(-21))
    return Tower(
        name="DA-4-DE-2018.1 WE WAdiff 140",
        datum=LowestCrossarm((m(21), m(27), m(30))),
        voltages=(kv(380),),
        line_angles=(),
        attachments=(
            Mount(Wire.SHIELD, Point(m(-8.6), m(0), m(32.5)), Hold.CLAMP),
            Mount(Wire.SHIELD, Point(m(8.6), m(0), m(32.5)), Hold.CLAMP),
            Mount(Wire.PHASE, Point(m(-12.5), m(0), m(22)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(12.5), m(0), m(22)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-16), m(0), m(12)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-9.5), m(0), m(12)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(9.5), m(0), m(12)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(16), m(0), m(12)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-17), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-12.1), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(-7.2), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.SHIELD, Point(m(0), m(0), m(0)), Hold.CLAMP),
            Mount(Wire.PHASE, Point(m(7.2), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(12.1), m(0), m(0)), Hold.STRAIN),
            Mount(Wire.PHASE, Point(m(17), m(0), m(0)), Hold.STRAIN),
        ),
        bases=(),
        body=(
            Body(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j143, j138, role=Role.DIAGONAL_BRACE),
                        Bar(j144, j137, role=Role.DIAGONAL_BRACE),
                        Bar(j141, j140, role=Role.TRANSVERSE_BRACE),
                        Bar(j022, j023, role=Role.TRANSVERSE_BRACE),
                        Bar(j044, j045, role=Role.TRANSVERSE_BRACE),
                        Bar(j079, j080, role=Role.TRANSVERSE_BRACE),
                        Bar(j058, j059, role=Role.TRANSVERSE_BRACE),
                        Bar(j080, j088, role=Role.DIAGONAL_BRACE),
                        Bar(j088, j091, role=Role.DIAGONAL_BRACE),
                        Bar(j091, j092, role=Role.DIAGONAL_BRACE),
                        Bar(j093, j090, role=Role.DIAGONAL_BRACE),
                        Bar(j090, j089, role=Role.DIAGONAL_BRACE),
                        Bar(j089, j079, role=Role.DIAGONAL_BRACE),
                        Bar(j122, j119, role=Role.DIAGONAL_BRACE),
                        Bar(j119, j102, role=Role.DIAGONAL_BRACE),
                        Bar(j121, j119, role=Role.DIAGONAL_BRACE),
                        Bar(j119, j103, role=Role.DIAGONAL_BRACE),
                        Bar(j103, j092, role=Role.DIAGONAL_BRACE),
                        Bar(j102, j093, role=Role.DIAGONAL_BRACE),
                        Bar(j132, j128, role=Role.DIAGONAL_BRACE),
                        Bar(j128, j125, role=Role.DIAGONAL_BRACE),
                        Bar(j129, j128, role=Role.TRANSVERSE_BRACE),
                        Bar(j121, j112, role=Role.CHORD),
                        Bar(j112, j102, role=Role.CHORD),
                        Bar(j102, j092, role=Role.CHORD),
                        Bar(j092, j090, role=Role.CHORD),
                        Bar(j090, j088, role=Role.CHORD),
                        Bar(j088, j079, role=Role.CHORD),
                        Bar(j079, j063, role=Role.CHORD),
                        Bar(j063, j058, role=Role.CHORD),
                        Bar(j059, j063, role=Role.DIAGONAL_BRACE),
                        Bar(j063, j080, role=Role.DIAGONAL_BRACE),
                        Bar(j080, j089, role=Role.CHORD),
                        Bar(j089, j091, role=Role.CHORD),
                        Bar(j091, j093, role=Role.CHORD),
                        Bar(j093, j103, role=Role.CHORD),
                        Bar(j103, j113, role=Role.CHORD),
                        Bar(j113, j122, role=Role.CHORD),
                        Bar(j058, j064, role=Role.DIAGONAL_BRACE),
                        Bar(j064, j079, role=Role.DIAGONAL_BRACE),
                        Bar(j058, j056, role=Role.CHORD),
                        Bar(j056, j054, role=Role.CHORD),
                        Bar(j054, j044, role=Role.CHORD),
                        Bar(j044, j028, role=Role.CHORD),
                        Bar(j028, j022, role=Role.CHORD),
                        Bar(j045, j028, role=Role.DIAGONAL_BRACE),
                        Bar(j028, j023, role=Role.DIAGONAL_BRACE),
                        Bar(j023, j029, role=Role.CHORD),
                        Bar(j029, j045, role=Role.CHORD),
                        Bar(j045, j055, role=Role.CHORD),
                        Bar(j055, j057, role=Role.CHORD),
                        Bar(j057, j059, role=Role.CHORD),
                        Bar(j059, j064, role=Role.CHORD),
                        Bar(j064, j080, role=Role.CHORD),
                        Bar(j044, j029, role=Role.DIAGONAL_BRACE),
                        Bar(j029, j022, role=Role.DIAGONAL_BRACE),
                        Bar(j044, j055, role=Role.DIAGONAL_BRACE),
                        Bar(j055, j056, role=Role.DIAGONAL_BRACE),
                        Bar(j056, j059, role=Role.DIAGONAL_BRACE),
                        Bar(j058, j057, role=Role.DIAGONAL_BRACE),
                        Bar(j057, j054, role=Role.DIAGONAL_BRACE),
                        Bar(j054, j045, role=Role.DIAGONAL_BRACE),
                        Bar(j112, j119, role=Role.TRANSVERSE_BRACE),
                        Bar(j119, j113, role=Role.TRANSVERSE_BRACE),
                        Bar(j092, j093, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        legs=(
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j150, j146, role=Role.CHORD),
                        Bar(j146, j142, role=Role.CHORD),
                        Bar(j142, j140, role=Role.CHORD),
                        Bar(j140, j136, role=Role.CHORD),
                        Bar(j136, j130, role=Role.CHORD),
                        Bar(j130, j127, role=Role.CHORD),
                        Bar(j127, j123, role=Role.CHORD),
                        Bar(j123, j121, role=Role.CHORD),
                        Bar(j150, j147, role=Role.DIAGONAL_BRACE),
                        Bar(j147, j143, role=Role.DIAGONAL_BRACE),
                        Bar(j137, j134, role=Role.DIAGONAL_BRACE),
                        Bar(j143, j142, role=Role.TRANSVERSE_BRACE),
                        Bar(j147, j146, role=Role.TRANSVERSE_BRACE),
                        Bar(j137, j136, role=Role.TRANSVERSE_BRACE),
                        Bar(j147, j142, role=Role.DIAGONAL_BRACE),
                        Bar(j143, j140, role=Role.DIAGONAL_BRACE),
                        Bar(j140, j137, role=Role.DIAGONAL_BRACE),
                        Bar(j128, j124, role=Role.DIAGONAL_BRACE),
                        Bar(j124, j121, role=Role.DIAGONAL_BRACE),
                        Bar(j134, j131, role=Role.DIAGONAL_BRACE),
                        Bar(j131, j128, role=Role.DIAGONAL_BRACE),
                        Bar(j128, j127, role=Role.TRANSVERSE_BRACE),
                        Bar(j127, j124, role=Role.DIAGONAL_BRACE),
                        Bar(j127, j131, role=Role.DIAGONAL_BRACE),
                        Bar(j130, j131, role=Role.TRANSVERSE_BRACE),
                        Bar(j123, j124, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Leg(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j122, j126, role=Role.CHORD),
                        Bar(j126, j129, role=Role.CHORD),
                        Bar(j129, j133, role=Role.CHORD),
                        Bar(j133, j139, role=Role.CHORD),
                        Bar(j139, j141, role=Role.CHORD),
                        Bar(j141, j145, role=Role.CHORD),
                        Bar(j145, j149, role=Role.CHORD),
                        Bar(j149, j151, role=Role.CHORD),
                        Bar(j138, j135, role=Role.DIAGONAL_BRACE),
                        Bar(j151, j148, role=Role.DIAGONAL_BRACE),
                        Bar(j148, j144, role=Role.DIAGONAL_BRACE),
                        Bar(j144, j145, role=Role.TRANSVERSE_BRACE),
                        Bar(j148, j149, role=Role.TRANSVERSE_BRACE),
                        Bar(j138, j139, role=Role.TRANSVERSE_BRACE),
                        Bar(j148, j145, role=Role.DIAGONAL_BRACE),
                        Bar(j144, j141, role=Role.DIAGONAL_BRACE),
                        Bar(j141, j138, role=Role.DIAGONAL_BRACE),
                        Bar(j135, j132, role=Role.DIAGONAL_BRACE),
                        Bar(j125, j122, role=Role.DIAGONAL_BRACE),
                        Bar(j125, j129, role=Role.DIAGONAL_BRACE),
                        Bar(j129, j132, role=Role.DIAGONAL_BRACE),
                        Bar(j125, j126, role=Role.TRANSVERSE_BRACE),
                        Bar(j132, j133, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
        ),
        head=(
            Head(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j018, j023, role=Role.CHORD),
                        Bar(j023, j019, role=Role.DIAGONAL_BRACE),
                        Bar(j019, j022, role=Role.DIAGONAL_BRACE),
                        Bar(j018, j019, role=Role.DIAGONAL_BRACE),
                        Bar(j019, j017, role=Role.DIAGONAL_BRACE),
                        Bar(j022, j017, role=Role.CHORD),
                    ),
                )
            ),
        ),
        crossarms=(
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j038, j052, role=Role.CHORD),
                        Bar(j052, j039, role=Role.CHORD),
                        Bar(j039, j036, role=Role.CHORD),
                        Bar(j036, j040, role=Role.CHORD),
                        Bar(j040, j041, role=Role.CHORD),
                        Bar(j041, j042, role=Role.CHORD),
                        Bar(j042, j043, role=Role.CHORD),
                        Bar(j043, j044, role=Role.CHORD),
                        Bar(j034, j032, role=Role.CHORD),
                        Bar(j032, j026, role=Role.CHORD),
                        Bar(j026, j024, role=Role.CHORD),
                        Bar(j024, j022, role=Role.CHORD),
                        Bar(j034, j038, role=Role.CHORD),
                        Bar(j044, j030, role=Role.DIAGONAL_BRACE),
                        Bar(j030, j043, role=Role.TRANSVERSE_BRACE),
                        Bar(j024, j042, role=Role.TRANSVERSE_BRACE),
                        Bar(j042, j030, role=Role.DIAGONAL_BRACE),
                        Bar(j030, j022, role=Role.DIAGONAL_BRACE),
                        Bar(j041, j026, role=Role.TRANSVERSE_BRACE),
                        Bar(j026, j042, role=Role.DIAGONAL_BRACE),
                        Bar(j026, j036, role=Role.DIAGONAL_BRACE),
                        Bar(j039, j032, role=Role.TRANSVERSE_BRACE),
                        Bar(j032, j036, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j045, j046, role=Role.CHORD),
                        Bar(j046, j047, role=Role.CHORD),
                        Bar(j047, j048, role=Role.CHORD),
                        Bar(j048, j049, role=Role.CHORD),
                        Bar(j049, j037, role=Role.CHORD),
                        Bar(j037, j050, role=Role.CHORD),
                        Bar(j050, j053, role=Role.CHORD),
                        Bar(j053, j051, role=Role.CHORD),
                        Bar(j051, j035, role=Role.CHORD),
                        Bar(j035, j033, role=Role.CHORD),
                        Bar(j033, j027, role=Role.CHORD),
                        Bar(j027, j025, role=Role.CHORD),
                        Bar(j025, j023, role=Role.CHORD),
                        Bar(j033, j050, role=Role.TRANSVERSE_BRACE),
                        Bar(j033, j037, role=Role.DIAGONAL_BRACE),
                        Bar(j048, j027, role=Role.TRANSVERSE_BRACE),
                        Bar(j027, j047, role=Role.DIAGONAL_BRACE),
                        Bar(j027, j037, role=Role.DIAGONAL_BRACE),
                        Bar(j025, j047, role=Role.TRANSVERSE_BRACE),
                        Bar(j047, j031, role=Role.DIAGONAL_BRACE),
                        Bar(j031, j023, role=Role.DIAGONAL_BRACE),
                        Bar(j045, j031, role=Role.DIAGONAL_BRACE),
                        Bar(j031, j046, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j072, j073, role=Role.CHORD),
                        Bar(j073, j074, role=Role.CHORD),
                        Bar(j074, j075, role=Role.CHORD),
                        Bar(j075, j076, role=Role.CHORD),
                        Bar(j076, j077, role=Role.CHORD),
                        Bar(j077, j078, role=Role.CHORD),
                        Bar(j078, j079, role=Role.CHORD),
                        Bar(j072, j070, role=Role.CHORD),
                        Bar(j070, j068, role=Role.CHORD),
                        Bar(j068, j066, role=Role.CHORD),
                        Bar(j066, j060, role=Role.CHORD),
                        Bar(j060, j058, role=Role.CHORD),
                        Bar(j068, j074, role=Role.TRANSVERSE_BRACE),
                        Bar(j058, j062, role=Role.DIAGONAL_BRACE),
                        Bar(j062, j077, role=Role.DIAGONAL_BRACE),
                        Bar(j077, j060, role=Role.TRANSVERSE_BRACE),
                        Bar(j068, j075, role=Role.DIAGONAL_BRACE),
                        Bar(j075, j066, role=Role.DIAGONAL_BRACE),
                        Bar(j066, j077, role=Role.DIAGONAL_BRACE),
                        Bar(j076, j066, role=Role.TRANSVERSE_BRACE),
                        Bar(j079, j062, role=Role.DIAGONAL_BRACE),
                        Bar(j062, j078, role=Role.TRANSVERSE_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j080, j081, role=Role.CHORD),
                        Bar(j081, j082, role=Role.CHORD),
                        Bar(j082, j083, role=Role.CHORD),
                        Bar(j083, j084, role=Role.CHORD),
                        Bar(j084, j085, role=Role.CHORD),
                        Bar(j085, j086, role=Role.CHORD),
                        Bar(j086, j087, role=Role.CHORD),
                        Bar(j087, j071, role=Role.CHORD),
                        Bar(j071, j069, role=Role.CHORD),
                        Bar(j069, j067, role=Role.CHORD),
                        Bar(j067, j061, role=Role.CHORD),
                        Bar(j061, j059, role=Role.CHORD),
                        Bar(j069, j085, role=Role.TRANSVERSE_BRACE),
                        Bar(j069, j084, role=Role.DIAGONAL_BRACE),
                        Bar(j084, j067, role=Role.DIAGONAL_BRACE),
                        Bar(j067, j082, role=Role.DIAGONAL_BRACE),
                        Bar(j082, j061, role=Role.TRANSVERSE_BRACE),
                        Bar(j083, j067, role=Role.TRANSVERSE_BRACE),
                        Bar(j080, j065, role=Role.DIAGONAL_BRACE),
                        Bar(j065, j081, role=Role.TRANSVERSE_BRACE),
                        Bar(j059, j065, role=Role.DIAGONAL_BRACE),
                        Bar(j065, j082, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j092, j094, role=Role.CHORD),
                        Bar(j094, j098, role=Role.CHORD),
                        Bar(j098, j104, role=Role.CHORD),
                        Bar(j104, j106, role=Role.CHORD),
                        Bar(j106, j108, role=Role.CHORD),
                        Bar(j108, j118, role=Role.CHORD),
                        Bar(j118, j109, role=Role.CHORD),
                        Bar(j109, j110, role=Role.CHORD),
                        Bar(j110, j111, role=Role.CHORD),
                        Bar(j111, j112, role=Role.CHORD),
                        Bar(j094, j100, role=Role.DIAGONAL_BRACE),
                        Bar(j100, j110, role=Role.DIAGONAL_BRACE),
                        Bar(j110, j104, role=Role.DIAGONAL_BRACE),
                        Bar(j111, j096, role=Role.DIAGONAL_BRACE),
                        Bar(j096, j092, role=Role.DIAGONAL_BRACE),
                        Bar(j096, j112, role=Role.DIAGONAL_BRACE),
                        Bar(j104, j109, role=Role.TRANSVERSE_BRACE),
                        Bar(j094, j111, role=Role.TRANSVERSE_BRACE),
                        Bar(j098, j110, role=Role.TRANSVERSE_BRACE),
                        Bar(j111, j100, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Crossarm(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j113, j114, role=Role.CHORD),
                        Bar(j114, j115, role=Role.CHORD),
                        Bar(j115, j116, role=Role.CHORD),
                        Bar(j116, j120, role=Role.CHORD),
                        Bar(j120, j117, role=Role.CHORD),
                        Bar(j117, j107, role=Role.CHORD),
                        Bar(j107, j105, role=Role.CHORD),
                        Bar(j105, j099, role=Role.CHORD),
                        Bar(j099, j095, role=Role.CHORD),
                        Bar(j095, j093, role=Role.CHORD),
                        Bar(j095, j101, role=Role.DIAGONAL_BRACE),
                        Bar(j101, j115, role=Role.DIAGONAL_BRACE),
                        Bar(j115, j105, role=Role.DIAGONAL_BRACE),
                        Bar(j114, j097, role=Role.DIAGONAL_BRACE),
                        Bar(j097, j093, role=Role.DIAGONAL_BRACE),
                        Bar(j097, j113, role=Role.DIAGONAL_BRACE),
                        Bar(j105, j116, role=Role.TRANSVERSE_BRACE),
                        Bar(j095, j114, role=Role.TRANSVERSE_BRACE),
                        Bar(j099, j115, role=Role.TRANSVERSE_BRACE),
                        Bar(j114, j101, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
        peaks=(
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j017, j013, role=Role.CHORD),
                        Bar(j013, j010, role=Role.CHORD),
                        Bar(j010, j007, role=Role.CHORD),
                        Bar(j007, j003, role=Role.CHORD),
                        Bar(j003, j001, role=Role.CHORD),
                        Bar(j001, j005, role=Role.CHORD),
                        Bar(j005, j009, role=Role.CHORD),
                        Bar(j009, j015, role=Role.CHORD),
                        Bar(j015, j020, role=Role.CHORD),
                        Bar(j020, j022, role=Role.CHORD),
                        Bar(j017, j020, role=Role.DIAGONAL_BRACE),
                        Bar(j020, j013, role=Role.DIAGONAL_BRACE),
                        Bar(j013, j015, role=Role.DIAGONAL_BRACE),
                        Bar(j015, j010, role=Role.DIAGONAL_BRACE),
                        Bar(j010, j009, role=Role.TRANSVERSE_BRACE),
                        Bar(j009, j007, role=Role.DIAGONAL_BRACE),
                        Bar(j007, j005, role=Role.DIAGONAL_BRACE),
                        Bar(j005, j003, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
            Peak(
                construction=Truss(
                    material=Steel,
                    bars=(
                        Bar(j008, j012, role=Role.DIAGONAL_BRACE),
                        Bar(j012, j011, role=Role.TRANSVERSE_BRACE),
                        Bar(j011, j016, role=Role.DIAGONAL_BRACE),
                        Bar(j016, j014, role=Role.DIAGONAL_BRACE),
                        Bar(j014, j021, role=Role.DIAGONAL_BRACE),
                        Bar(j021, j018, role=Role.DIAGONAL_BRACE),
                        Bar(j023, j021, role=Role.CHORD),
                        Bar(j021, j016, role=Role.CHORD),
                        Bar(j016, j012, role=Role.CHORD),
                        Bar(j012, j006, role=Role.CHORD),
                        Bar(j006, j002, role=Role.CHORD),
                        Bar(j002, j004, role=Role.CHORD),
                        Bar(j004, j008, role=Role.CHORD),
                        Bar(j008, j011, role=Role.CHORD),
                        Bar(j011, j014, role=Role.CHORD),
                        Bar(j014, j018, role=Role.CHORD),
                        Bar(j008, j006, role=Role.DIAGONAL_BRACE),
                        Bar(j006, j004, role=Role.DIAGONAL_BRACE),
                    ),
                )
            ),
        ),
    )


DA_4_DE_2018_1_WE_WADIFF_140 = _da_4_de_2018_1_we_wadiff_140()

MT_008_001 = Tower(
    name="MT-008-001",
    datum=Ground((m(0),)),
    voltages=(kv(400),),
    line_angles=(),
    attachments=(),
    bases=(),
    body=(
        Body(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-4100), mm(0), mm(9500)), Point(mm(4100), mm(0), mm(9500))),
                panels=(
                    Panel(
                        Edge(Point(mm(-2810), mm(0), mm(17500)), Point(mm(2810), mm(0), mm(17500))),
                        Bracing.DIAMOND,
                        1,
                    ),
                    Panel(
                        Edge(Point(mm(-2250), mm(0), mm(21000)), Point(mm(2250), mm(0), mm(21000))),
                        Bracing.DIAMOND,
                        1,
                    ),
                ),
            )
        ),
        Body(
            construction=PanelRun(
                face=Face.LONGITUDINAL,
                start=Edge(Point(mm(0), mm(-4100), mm(9500)), Point(mm(0), mm(4100), mm(9500))),
                panels=(
                    Panel(
                        Edge(Point(mm(0), mm(-2810), mm(17500)), Point(mm(0), mm(2810), mm(17500))),
                        Bracing.DIAMOND,
                        1,
                    ),
                    Panel(
                        Edge(Point(mm(0), mm(-2250), mm(21000)), Point(mm(0), mm(2250), mm(21000))),
                        Bracing.DIAMOND,
                        1,
                    ),
                    Panel(
                        Edge(Point(mm(0), mm(-920), mm(34500)), Point(mm(0), mm(920), mm(34500))),
                        Bracing.CROSS,
                        7,
                    ),
                ),
            )
        ),
    ),
    legs=(
        Leg(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-5630), mm(0), mm(0)), Point(mm(-5630), mm(0), mm(0))),
                panels=(
                    Panel(
                        Edge(Point(mm(-4100), mm(0), mm(9500)), Point(mm(0), mm(0), mm(9500))),
                        Bracing.PRATT,
                        5,
                    ),
                ),
            )
        ),
        Leg(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(5630), mm(0), mm(0)), Point(mm(5630), mm(0), mm(0))),
                panels=(
                    Panel(
                        Edge(Point(mm(4100), mm(0), mm(9500)), Point(mm(0), mm(0), mm(9500))),
                        Bracing.PRATT,
                        5,
                    ),
                ),
            )
        ),
        Leg(
            construction=PanelRun(
                face=Face.LONGITUDINAL,
                start=Edge(Point(mm(0), mm(-5630), mm(0)), Point(mm(0), mm(-5630), mm(0))),
                panels=(
                    Panel(
                        Edge(Point(mm(0), mm(-4100), mm(9500)), Point(mm(0), mm(0), mm(9500))),
                        Bracing.PRATT,
                        5,
                    ),
                ),
            )
        ),
        Leg(
            construction=PanelRun(
                face=Face.LONGITUDINAL,
                start=Edge(Point(mm(0), mm(5630), mm(0)), Point(mm(0), mm(5630), mm(0))),
                panels=(
                    Panel(
                        Edge(Point(mm(0), mm(4100), mm(9500)), Point(mm(0), mm(0), mm(9500))),
                        Bracing.PRATT,
                        5,
                    ),
                ),
            )
        ),
    ),
    head=(
        Head(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-2250), mm(0), mm(21000)), Point(mm(0), mm(0), mm(22750))),
                panels=(
                    Panel(
                        Edge(
                            Point(mm(-5910), mm(0), mm(29500)), Point(mm(-4650), mm(0), mm(29500))
                        ),
                        Bracing.PRATT,
                        4,
                    ),
                    Panel(
                        Edge(
                            Point(mm(-4800), mm(0), mm(33250)), Point(mm(-3550), mm(0), mm(33250))
                        ),
                        Bracing.WARREN,
                        3,
                    ),
                ),
            )
        ),
        Head(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(2250), mm(0), mm(21000)), Point(mm(0), mm(0), mm(22750))),
                panels=(
                    Panel(
                        Edge(Point(mm(5910), mm(0), mm(29500)), Point(mm(4650), mm(0), mm(29500))),
                        Bracing.PRATT,
                        4,
                    ),
                    Panel(
                        Edge(Point(mm(4800), mm(0), mm(33250)), Point(mm(3550), mm(0), mm(33250))),
                        Bracing.WARREN,
                        3,
                    ),
                ),
            )
        ),
        Head(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-4350), mm(0), mm(34500)), Point(mm(-4800), mm(0), mm(33250))),
                panels=(
                    Panel(
                        Edge(Point(mm(4350), mm(0), mm(34500)), Point(mm(4800), mm(0), mm(33250))),
                        Bracing.WARREN,
                        8,
                    ),
                ),
            )
        ),
    ),
    crossarms=(
        Crossarm(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-5910), mm(0), mm(29500)), Point(mm(-5440), mm(0), mm(27950))),
                panels=(
                    Panel(
                        Edge(
                            Point(mm(-9500), mm(0), mm(28700)), Point(mm(-9500), mm(0), mm(28700))
                        ),
                        Bracing.PRATT,
                        3,
                    ),
                ),
            )
        ),
        Crossarm(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(5910), mm(0), mm(29500)), Point(mm(5440), mm(0), mm(27950))),
                panels=(
                    Panel(
                        Edge(Point(mm(9500), mm(0), mm(28700)), Point(mm(9500), mm(0), mm(28700))),
                        Bracing.PRATT,
                        3,
                    ),
                ),
            )
        ),
    ),
    peaks=(
        Peak(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-4800), mm(0), mm(33250)), Point(mm(-3550), mm(0), mm(33250))),
                panels=(
                    Panel(
                        Edge(
                            Point(mm(-7280), mm(0), mm(36200)), Point(mm(-7280), mm(0), mm(36200))
                        ),
                        Bracing.PRATT,
                        3,
                    ),
                ),
            )
        ),
        Peak(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(4800), mm(0), mm(33250)), Point(mm(3550), mm(0), mm(33250))),
                panels=(
                    Panel(
                        Edge(Point(mm(7280), mm(0), mm(36200)), Point(mm(7280), mm(0), mm(36200))),
                        Bracing.PRATT,
                        3,
                    ),
                ),
            )
        ),
    ),
)

# EirGrid, p. 1: drawn to MT-008-001's outline.
MT_008_002 = replace(MT_008_001, name="MT-008-002")

# EirGrid, p. 1: drawn to MT-008-001's outline.
MT_008_003 = replace(MT_008_001, name="MT-008-003")

MT_008_004 = Tower(
    name="MT-008-004",
    datum=Ground((m(0),)),
    voltages=(kv(400),),
    line_angles=(),
    attachments=(),
    bases=(),
    body=(
        Body(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-4030), mm(0), mm(9000)), Point(mm(4030), mm(0), mm(9000))),
                panels=(
                    Panel(
                        Edge(Point(mm(-3090), mm(0), mm(17000)), Point(mm(3090), mm(0), mm(17000))),
                        Bracing.DIAMOND,
                        1,
                    ),
                    Panel(
                        Edge(Point(mm(-1450), mm(0), mm(30990)), Point(mm(1450), mm(0), mm(30990))),
                        Bracing.DIAMOND,
                        2,
                    ),
                ),
            )
        ),
        Body(
            construction=PanelRun(
                face=Face.LONGITUDINAL,
                start=Edge(Point(mm(0), mm(-4030), mm(9000)), Point(mm(0), mm(4030), mm(9000))),
                panels=(
                    Panel(
                        Edge(Point(mm(0), mm(-3090), mm(17000)), Point(mm(0), mm(3090), mm(17000))),
                        Bracing.DIAMOND,
                        1,
                    ),
                    Panel(
                        Edge(Point(mm(0), mm(-1450), mm(30990)), Point(mm(0), mm(1450), mm(30990))),
                        Bracing.DIAMOND,
                        2,
                    ),
                    Panel(
                        Edge(Point(mm(0), mm(-510), mm(42590)), Point(mm(0), mm(510), mm(42590))),
                        Bracing.CROSS,
                        8,
                    ),
                ),
            )
        ),
    ),
    legs=(
        Leg(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-5090), mm(0), mm(0)), Point(mm(-5090), mm(0), mm(0))),
                panels=(
                    Panel(
                        Edge(Point(mm(-4030), mm(0), mm(9000)), Point(mm(0), mm(0), mm(9000))),
                        Bracing.PRATT,
                        5,
                    ),
                ),
            )
        ),
        Leg(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(5090), mm(0), mm(0)), Point(mm(5090), mm(0), mm(0))),
                panels=(
                    Panel(
                        Edge(Point(mm(4030), mm(0), mm(9000)), Point(mm(0), mm(0), mm(9000))),
                        Bracing.PRATT,
                        5,
                    ),
                ),
            )
        ),
        Leg(
            construction=PanelRun(
                face=Face.LONGITUDINAL,
                start=Edge(Point(mm(0), mm(-5090), mm(0)), Point(mm(0), mm(-5090), mm(0))),
                panels=(
                    Panel(
                        Edge(Point(mm(0), mm(-4030), mm(9000)), Point(mm(0), mm(0), mm(9000))),
                        Bracing.PRATT,
                        5,
                    ),
                ),
            )
        ),
        Leg(
            construction=PanelRun(
                face=Face.LONGITUDINAL,
                start=Edge(Point(mm(0), mm(5090), mm(0)), Point(mm(0), mm(5090), mm(0))),
                panels=(
                    Panel(
                        Edge(Point(mm(0), mm(4030), mm(9000)), Point(mm(0), mm(0), mm(9000))),
                        Bracing.PRATT,
                        5,
                    ),
                ),
            )
        ),
    ),
    head=(
        Head(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-1450), mm(0), mm(30990)), Point(mm(0), mm(0), mm(32690))),
                panels=(
                    Panel(
                        Edge(
                            Point(mm(-6400), mm(0), mm(38540)), Point(mm(-5200), mm(0), mm(38540))
                        ),
                        Bracing.PRATT,
                        4,
                    ),
                    Panel(
                        Edge(
                            Point(mm(-4470), mm(0), mm(41540)), Point(mm(-3450), mm(0), mm(41540))
                        ),
                        Bracing.PRATT,
                        2,
                    ),
                ),
            )
        ),
        Head(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(1450), mm(0), mm(30990)), Point(mm(0), mm(0), mm(32690))),
                panels=(
                    Panel(
                        Edge(Point(mm(6400), mm(0), mm(38540)), Point(mm(5200), mm(0), mm(38540))),
                        Bracing.PRATT,
                        4,
                    ),
                    Panel(
                        Edge(Point(mm(4470), mm(0), mm(41540)), Point(mm(3450), mm(0), mm(41540))),
                        Bracing.PRATT,
                        2,
                    ),
                ),
            )
        ),
    ),
    crossarms=(
        Crossarm(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-6400), mm(0), mm(38540)), Point(mm(-5200), mm(0), mm(36990))),
                panels=(
                    Panel(
                        Edge(
                            Point(mm(-9500), mm(0), mm(37000)), Point(mm(-9500), mm(0), mm(37000))
                        ),
                        Bracing.PRATT,
                        3,
                    ),
                ),
            )
        ),
        Crossarm(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(6400), mm(0), mm(38540)), Point(mm(5200), mm(0), mm(36990))),
                panels=(
                    Panel(
                        Edge(Point(mm(9500), mm(0), mm(37000)), Point(mm(9500), mm(0), mm(37000))),
                        Bracing.PRATT,
                        3,
                    ),
                ),
            )
        ),
    ),
    peaks=(
        Peak(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(-4470), mm(0), mm(41540)), Point(mm(-3450), mm(0), mm(41540))),
                panels=(
                    Panel(
                        Edge(Point(mm(0), mm(0), mm(43000)), Point(mm(-6750), mm(0), mm(42590))),
                        Bracing.WARREN,
                        4,
                    ),
                ),
            )
        ),
        Peak(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(Point(mm(4470), mm(0), mm(41540)), Point(mm(3450), mm(0), mm(41540))),
                panels=(
                    Panel(
                        Edge(Point(mm(0), mm(0), mm(43000)), Point(mm(6750), mm(0), mm(42590))),
                        Bracing.WARREN,
                        4,
                    ),
                ),
            )
        ),
    ),
)

TYPICAL_765KV_TANGENT_TOWER = Tower(
    name="TYPICAL 765KV TANGENT TOWER",
    datum=LowestCrossarm(()),
    voltages=(kv(765),),
    line_angles=(),
    attachments=(
        Mount(Wire.SHIELD, Point(-ft_in(47, 6), ft_in(0, 0), ft_in(13, 0)), Hold.CLAMP),
        Mount(Wire.SHIELD, Point(ft_in(47, 6), ft_in(0, 0), ft_in(13, 0)), Hold.CLAMP),
        WirePosition(
            Wire.PHASE,
            Point(-ft_in(47, 6), ft_in(0, 0), -ft_in(19, 6)),
            Hold.V_STRING,
            strings=(
                DiscString(
                    mount=Point(-ft_in(70, 10), ft_in(0, 0), ft_in(0, 0)),
                    discs=34,
                    diameter=ft_in(0, 8),
                    length=ft_in(15, 4),
                ),
                DiscString(
                    mount=Point(-ft_in(31, 7), ft_in(0, 0), -ft_in(5, 11)),
                    discs=34,
                    diameter=ft_in(0, 8),
                    length=ft_in(15, 4),
                ),
            ),
        ),
        WirePosition(
            Wire.PHASE,
            Point(ft_in(0, 0), ft_in(0, 0), -ft_in(19, 6)),
            Hold.V_STRING,
            strings=(
                DiscString(
                    mount=Point(-ft_in(23, 8), ft_in(0, 0), ft_in(0, 0)),
                    discs=34,
                    diameter=ft_in(0, 8),
                    length=ft_in(15, 4),
                ),
                DiscString(
                    mount=Point(ft_in(23, 8), ft_in(0, 0), ft_in(0, 0)),
                    discs=34,
                    diameter=ft_in(0, 8),
                    length=ft_in(15, 4),
                ),
            ),
        ),
        WirePosition(
            Wire.PHASE,
            Point(ft_in(47, 6), ft_in(0, 0), -ft_in(19, 6)),
            Hold.V_STRING,
            strings=(
                DiscString(
                    mount=Point(ft_in(31, 7), ft_in(0, 0), -ft_in(5, 11)),
                    discs=34,
                    diameter=ft_in(0, 8),
                    length=ft_in(15, 4),
                ),
                DiscString(
                    mount=Point(ft_in(70, 10), ft_in(0, 0), ft_in(0, 0)),
                    discs=34,
                    diameter=ft_in(0, 8),
                    length=ft_in(15, 4),
                ),
            ),
        ),
    ),
    bases=(),
    body=(
        Body(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(
                    Point(-ft_in(16, 0), ft_in(0, 0), -ft_in(89, 5)),
                    Point(-ft_in(16, 0), ft_in(0, 0), -ft_in(89, 5)),
                ),
                panels=(
                    Panel(
                        Edge(
                            Point(-ft_in(11, 9), ft_in(0, 0), -ft_in(60, 4)),
                            Point(ft_in(0, 0), ft_in(0, 0), -ft_in(60, 4)),
                        ),
                        Bracing.PRATT,
                        3,
                    ),
                ),
            )
        ),
        Body(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(
                    Point(ft_in(16, 0), ft_in(0, 0), -ft_in(89, 5)),
                    Point(ft_in(16, 0), ft_in(0, 0), -ft_in(89, 5)),
                ),
                panels=(
                    Panel(
                        Edge(
                            Point(ft_in(11, 9), ft_in(0, 0), -ft_in(60, 4)),
                            Point(ft_in(0, 0), ft_in(0, 0), -ft_in(60, 4)),
                        ),
                        Bracing.PRATT,
                        3,
                    ),
                ),
            )
        ),
        Body(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(
                    Point(-ft_in(17, 8), ft_in(0, 0), -ft_in(100, 6)),
                    Point(ft_in(17, 8), ft_in(0, 0), -ft_in(100, 6)),
                ),
                panels=(
                    Panel(
                        Edge(
                            Point(-ft_in(16, 0), ft_in(0, 0), -ft_in(89, 5)),
                            Point(ft_in(16, 0), ft_in(0, 0), -ft_in(89, 5)),
                        ),
                        Bracing.DIAMOND,
                        1,
                    ),
                ),
            )
        ),
        Body(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(
                    Point(-ft_in(11, 9), ft_in(0, 0), -ft_in(60, 4)),
                    Point(ft_in(11, 9), ft_in(0, 0), -ft_in(60, 4)),
                ),
                panels=(
                    Panel(
                        Edge(
                            Point(-ft_in(10, 11), ft_in(0, 0), -ft_in(54, 3)),
                            Point(ft_in(10, 11), ft_in(0, 0), -ft_in(54, 3)),
                        ),
                        Bracing.DIAMOND,
                        1,
                    ),
                ),
            )
        ),
    ),
    legs=(
        Leg(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(
                    Point(-ft_in(25, 7), ft_in(0, 0), -ft_in(154, 9)),
                    Point(-ft_in(25, 7), ft_in(0, 0), -ft_in(154, 9)),
                ),
                panels=(
                    Panel(
                        Edge(
                            Point(-ft_in(16, 0), ft_in(0, 0), -ft_in(89, 5)),
                            Point(ft_in(0, 0), ft_in(0, 0), -ft_in(89, 5)),
                        ),
                        Bracing.PRATT,
                        7,
                    ),
                ),
            )
        ),
        Leg(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(
                    Point(ft_in(25, 7), ft_in(0, 0), -ft_in(154, 9)),
                    Point(ft_in(25, 7), ft_in(0, 0), -ft_in(154, 9)),
                ),
                panels=(
                    Panel(
                        Edge(
                            Point(ft_in(16, 0), ft_in(0, 0), -ft_in(89, 5)),
                            Point(ft_in(0, 0), ft_in(0, 0), -ft_in(89, 5)),
                        ),
                        Bracing.PRATT,
                        7,
                    ),
                ),
            )
        ),
    ),
    head=(
        Head(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(
                    Point(-ft_in(10, 11), ft_in(0, 0), -ft_in(54, 3)),
                    Point(ft_in(0, 0), ft_in(0, 0), -ft_in(54, 3)),
                ),
                panels=(
                    Panel(
                        Edge(
                            Point(-ft_in(14, 9), ft_in(0, 0), -ft_in(45, 3)),
                            Point(-ft_in(7, 2), ft_in(0, 0), -ft_in(45, 3)),
                        ),
                        Bracing.WARREN,
                        1,
                    ),
                    Panel(
                        Edge(
                            Point(-ft_in(23, 8), ft_in(0, 0), -ft_in(23, 11)),
                            Point(-ft_in(23, 8), ft_in(0, 0), -ft_in(23, 11)),
                        ),
                        Bracing.PRATT,
                        2,
                    ),
                    Panel(
                        Edge(
                            Point(-ft_in(34, 2), ft_in(0, 0), ft_in(0, 0)),
                            Point(-ft_in(23, 8), ft_in(0, 0), ft_in(0, 0)),
                        ),
                        Bracing.PRATT,
                        3,
                    ),
                ),
            )
        ),
        Head(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(
                    Point(ft_in(10, 11), ft_in(0, 0), -ft_in(54, 3)),
                    Point(ft_in(0, 0), ft_in(0, 0), -ft_in(54, 3)),
                ),
                panels=(
                    Panel(
                        Edge(
                            Point(ft_in(14, 9), ft_in(0, 0), -ft_in(45, 3)),
                            Point(ft_in(7, 2), ft_in(0, 0), -ft_in(45, 3)),
                        ),
                        Bracing.WARREN,
                        1,
                    ),
                    Panel(
                        Edge(
                            Point(ft_in(23, 8), ft_in(0, 0), -ft_in(23, 11)),
                            Point(ft_in(23, 8), ft_in(0, 0), -ft_in(23, 11)),
                        ),
                        Bracing.PRATT,
                        2,
                    ),
                    Panel(
                        Edge(
                            Point(ft_in(34, 2), ft_in(0, 0), ft_in(0, 0)),
                            Point(ft_in(23, 8), ft_in(0, 0), ft_in(0, 0)),
                        ),
                        Bracing.PRATT,
                        3,
                    ),
                ),
            )
        ),
        Head(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(
                    Point(-ft_in(28, 5), ft_in(0, 0), ft_in(6, 0)),
                    Point(-ft_in(23, 8), ft_in(0, 0), ft_in(0, 0)),
                ),
                panels=(
                    Panel(
                        Edge(
                            Point(ft_in(28, 5), ft_in(0, 0), ft_in(6, 0)),
                            Point(ft_in(23, 8), ft_in(0, 0), ft_in(0, 0)),
                        ),
                        Bracing.WARREN,
                        12,
                    ),
                ),
            )
        ),
    ),
    crossarms=(
        Crossarm(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(
                    Point(-ft_in(28, 5), ft_in(0, 0), ft_in(6, 0)),
                    Point(-ft_in(23, 8), ft_in(0, 0), ft_in(0, 0)),
                ),
                panels=(
                    Panel(
                        Edge(
                            Point(-ft_in(35, 1), ft_in(0, 0), ft_in(8, 0)),
                            Point(-ft_in(34, 2), ft_in(0, 0), ft_in(0, 0)),
                        ),
                        Bracing.WARREN,
                        2,
                    ),
                    Panel(
                        Edge(
                            Point(-ft_in(43, 0), ft_in(0, 0), ft_in(6, 1)),
                            Point(-ft_in(43, 0), ft_in(0, 0), ft_in(0, 0)),
                        ),
                        Bracing.WARREN,
                        1,
                    ),
                    Panel(
                        Edge(
                            Point(-ft_in(70, 10), ft_in(0, 0), ft_in(0, 0)),
                            Point(-ft_in(70, 10), ft_in(0, 0), ft_in(0, 0)),
                        ),
                        Bracing.PRATT,
                        5,
                    ),
                ),
            )
        ),
        Crossarm(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(
                    Point(ft_in(28, 5), ft_in(0, 0), ft_in(6, 0)),
                    Point(ft_in(23, 8), ft_in(0, 0), ft_in(0, 0)),
                ),
                panels=(
                    Panel(
                        Edge(
                            Point(ft_in(35, 1), ft_in(0, 0), ft_in(8, 0)),
                            Point(ft_in(34, 2), ft_in(0, 0), ft_in(0, 0)),
                        ),
                        Bracing.WARREN,
                        2,
                    ),
                    Panel(
                        Edge(
                            Point(ft_in(43, 0), ft_in(0, 0), ft_in(6, 1)),
                            Point(ft_in(43, 0), ft_in(0, 0), ft_in(0, 0)),
                        ),
                        Bracing.WARREN,
                        1,
                    ),
                    Panel(
                        Edge(
                            Point(ft_in(70, 10), ft_in(0, 0), ft_in(0, 0)),
                            Point(ft_in(70, 10), ft_in(0, 0), ft_in(0, 0)),
                        ),
                        Bracing.PRATT,
                        5,
                    ),
                ),
            )
        ),
    ),
    peaks=(
        Peak(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(
                    Point(-ft_in(43, 0), ft_in(0, 0), ft_in(6, 1)),
                    Point(-ft_in(35, 1), ft_in(0, 0), ft_in(8, 0)),
                ),
                panels=(
                    Panel(
                        Edge(
                            Point(-ft_in(47, 6), ft_in(0, 0), ft_in(13, 0)),
                            Point(-ft_in(47, 6), ft_in(0, 0), ft_in(13, 0)),
                        ),
                        Bracing.PRATT,
                        3,
                    ),
                ),
            )
        ),
        Peak(
            construction=PanelRun(
                face=Face.TRANSVERSE,
                start=Edge(
                    Point(ft_in(43, 0), ft_in(0, 0), ft_in(6, 1)),
                    Point(ft_in(35, 1), ft_in(0, 0), ft_in(8, 0)),
                ),
                panels=(
                    Panel(
                        Edge(
                            Point(ft_in(47, 6), ft_in(0, 0), ft_in(13, 0)),
                            Point(ft_in(47, 6), ft_in(0, 0), ft_in(13, 0)),
                        ),
                        Bracing.PRATT,
                        3,
                    ),
                ),
            )
        ),
    ),
)
