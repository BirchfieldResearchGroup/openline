# Validation

## Catalog

```{openline:validation}
:view: summary
```

## By standard

```{openline:validation}
:view: standards
```

## Line parameters

```{list-table}
:header-rows: 1
:class: openline-table

* - Check
  - Against
  - Where
* - Earth return: [Carson's integral](https://doi.org/10.3311/PPee.7894), homogeneous soil
  - Quadrature; 80-digit reference values
  - `tests/openline/test_earth.py`
* - PSRC line: mutual impedance and capacitance
  - ATP
  - [PSRC example](../examples/emt/psrc.md)
* - IEEE 738 rating
  - The standard's three benchmark results
  - [IEEE 738 example](../examples/ratings/ieee738.md)
```
