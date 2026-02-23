# ==========================================
# RC BEAM FLEXURAL DESIGN CHECKER
# Units:
# mm, MPa, mm², kN-m
# ==========================================

print("RC BEAM FLEXURAL DESIGN CHECKER")
print("--------------------------------")

# INPUT SECTION
b = float(input("Beam width b (mm): "))
d = float(input("Effective depth d (mm): "))
fc = float(input("Concrete strength f'c (MPa): "))
fy = float(input("Steel yield strength fy (MPa): "))
As = float(input("Steel area As (mm^2): "))
Mu = float(input("Factored moment demand Mu (kN-m): "))

# CONSTANTS
phi = 0.90
beta1 = 0.85

# CALCULATIONS
a = (As * fy) / (0.85 * fc * b)
Mn = As * fy * (d - a / 2)      # N-mm
phi_Mn = phi * Mn              # N-mm

# CONVERT TO kN-m
Mn_kNm = Mn / 1e6
phi_Mn_kNm = phi_Mn / 1e6

# RESULTS
print("\n===== RESULTS =====")
print("Compression block depth a =", round(a, 2), "mm")
print("Nominal Moment Mn =", round(Mn_kNm, 2), "kN-m")
print("Design Capacity φMn =", round(phi_Mn_kNm, 2), "kN-m")

# CHECK
if phi_Mn_kNm >= Mu:
    print("\nSTATUS: SAFE (φMn ≥ Mu)")
else:
    print("\nSTATUS: NOT SAFE (Increase steel or section)")

input("\nPress Enter to exit...")