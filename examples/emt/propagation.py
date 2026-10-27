"""Propagation and characteristic admittance

Calculate the three current modes of a 100 km, untransposed 230 kV line from 1 Hz to 100 MHz.
Plot modal characteristic admittance and propagation, removing each mode's phase delay at
the first magnitude below 1e-5, or at 100 MHz if it stays above the cutoff.
"""

import matplotlib.pyplot as plt
import numpy as np

from openline import Circuit, Earth, Line, Strung, conductors, electrical, structures
from openline import units as u

# %% Setup
frame = structures.frame.TH_230
line = Line(
    structure=frame,
    height=u.m(22),
    span=u.m(300),
    circuits=(
        Circuit.uniform(
            conductors.astm.b232.DRAKE,
            at=dict(zip("ABC", frame.phases, strict=True)),
            strung=Strung(u.kn(28), u.celsius(15)),
            insulator_drop=u.m(2.5),
        ),
    ),
    shields=(),
    earth=Earth(u.ohm_m(100), 10),
)

# %% Calculation
frequencies = np.geomspace(1, 1e8, 121)
sweep = electrical.propagation_sweep(
    line, temperature=u.celsius(50), frequencies=map(u.hz, frequencies), length=u.km(100)
)
h = np.array([[mode.function for mode in sample.modes] for sample in sweep])
yc = np.array(
    [[mode.characteristic_admittance.to(u.siemens) for mode in sample.modes] for sample in sweep]
)
phase_delays = np.array([[mode.phase_delay.si for mode in sample.modes] for sample in sweep])

cutoff = 1e-5
stops = []
delays = []
print("Mode  Cutoff frequency (Hz)  Phase delay (µs)")
for mode in range(h.shape[1]):
    below = np.flatnonzero(abs(h[:, mode]) <= cutoff)
    stop = int(below[0]) if below.size else len(sweep) - 1
    delay = phase_delays[stop, mode]
    stops.append(stop)
    delays.append(delay)
    print(f"{mode + 1:4}  {frequencies[stop]:21.3g}  {delay * 1e6:16.2f}")

# %% Plot
fig, axes = plt.subplots(1, 2, sharex=True, num="Modal characteristic admittance")
for mode in range(yc.shape[1]):
    axes[0].semilogx(frequencies, yc[:, mode].real * 1e3, label=f"Mode {mode + 1}")
    axes[1].semilogx(frequencies, yc[:, mode].imag * 1e3)
axes[0].set(ylabel="Re $Y_c$ (mS)", title="Real part")
axes[1].set(ylabel="Im $Y_c$ (mS)", title="Imaginary part")
for ax in axes:
    ax.set(xlabel="Frequency (Hz)", xlim=(frequencies[0], frequencies[-1]))
fig.legend(loc="outside upper center", ncols=3)

fig, axes = plt.subplots(3, 1, sharex=True, figsize=(7.2, 6.6), num="Modal current propagation")
for mode, (stop, delay) in enumerate(zip(stops, delays, strict=True)):
    f = frequencies[: stop + 1]
    tau = phase_delays[: stop + 1, mode]
    axes[0].loglog(f, abs(h[: stop + 1, mode]), label=f"Mode {mode + 1}")
    # Use the propagation constant's phase delay; sparse complex samples cannot be unwrapped.
    axes[1].semilogx(f, -360 * f * tau)
    axes[2].semilogx(f, 360 * f * (delay - tau), marker="o", markevery=[-1])
axes[0].set(ylabel="$|H|$", ylim=(cutoff, 1.2), title="Propagation magnitude")
axes[1].set(ylabel="Phase (°)", title="Before delay removal")
axes[2].set(ylabel="Phase (°)", title="After delay removal", xlabel="Frequency (Hz)")
axes[2].set_xlim(frequencies[0], frequencies[-1])
fig.legend(loc="outside upper center", ncols=3)
plt.show()
